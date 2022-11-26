import re

from secomlint.section import Header
from secomlint.section import Body
from secomlint.section import Metadata
from secomlint.section import Contact
from secomlint.section import Bugtracker
from secomlint.extractor import Extractor

from secomlint.utils import extend_tags

TAGS_METADATA = ['weakness', 'severity', 'detection',
                 'report', 'cvss', 'introduced in']

TAGS_CONTACT = ['reported-by', 'signed-off-by', 'co-authored-by']
TAGS_CONTACT_NEW = ['reported-by', 'signed-off-by', 'co-authored-by']

TAGS_CONTACT_EXT = extend_tags(TAGS_CONTACT)

TAGS_BUG_TRACKER = extend_tags(['bug-tracker', 'resolves', 'see also'])

ALL_TAGS = TAGS_METADATA + TAGS_CONTACT_EXT + TAGS_BUG_TRACKER


class Parser:
    def __init__(self) -> None:
        pass

    def run(self, message):
        """separates message in different 
        bulks of info

        Args:
            message (list): array of lines

        Returns:
            _type_: _description_
        """
        section = []
        for idx, line in enumerate(message):
            if line == '\n' or line == '':
                break
            else:
                section += [line.strip()]
        return section, message[idx+1::]

    def is_body(self, lines):
        is_body = []
        for line in lines:
            regex = rf"^(?!{'|'.join(ALL_TAGS)}(:)?.*$).*"
            is_body += [1] if re.search(regex, line) else [0]
        return len(lines) >= 1 and sum(is_body) > 0

    def is_metadata(self, line):
        return re.search(rf"^({'|'.join(TAGS_METADATA)}):", line)

    def is_contact(self, line):
        return re.search(rf"^({'|'.join(TAGS_CONTACT_EXT)}):", line)

    def is_bugtracker(self, line):
        return re.search(rf"^({'|'.join(TAGS_BUG_TRACKER)}):", line)

    def collect_sections(self, message):
        sections=[]
        message_tail, idx = message, 0
        ruler = Extractor()
        bugtracker = None
        while message_tail:
            lines, message_tail = self.run(message_tail)
            # header (1 first line)
            if len(lines) == 1 and idx == 0:
                sections.append(
                    Header(
                        lines=lines,
                        entities=ruler.extract_entities(lines)
                    )
                )
            # body
            elif idx > 0 and self.is_body(lines):
                sections.append(
                    Body(
                        lines=lines,
                        entities=ruler.extract_entities(lines)
                    )
                )
            else:
                for line in lines:
                    if self.is_metadata(line):
                        tag = self.is_metadata(line)[0].replace(
                            ':', '').replace(' ', '_')
                        sections.append(
                            Metadata(
                                lines=line,
                                tag=tag,
                                entities=ruler.extract_entities([line])
                            ))
                    elif self.is_contact(line):
                        tag = self.is_contact(line)[0].replace(
                            ':', '').replace('-', '_')
                        sections.append(
                            Contact(
                                lines=line,
                                tag=tag,
                                entities=ruler.extract_entities([line])
                            ))
                    elif self.is_bugtracker(line):
                        if bugtracker:
                            bugtracker.append_line(line)
                        else:
                            bugtracker = Bugtracker(
                                lines=[line],
                                tag='reference',
                                entities=ruler.extract_entities([line])
                            )
            if bugtracker:
                sections.append(bugtracker)
            idx += 1

        metadata_tags = []
        for section in sections:
            if type(section) == Metadata:
                metadata_tags += [section.tag.replace('_', ' ')]
        
        for tag in TAGS_METADATA:
            if tag not in metadata_tags:
                sections.append(
                    Metadata(
                        lines=None,
                        tag=tag,
                        entities=None
                    ))
                
        contact_tags = []
        for section in sections:
            if type(section) == Contact:
                contact_tags += [section.tag.replace('_', '-')]
        
        for tag in TAGS_CONTACT_NEW:
            if tag not in contact_tags:
                sections.append(
                    Contact(
                        lines=None,
                        tag=tag.replace('-', '_'),
                        entities=None
                    ))

        return sections
