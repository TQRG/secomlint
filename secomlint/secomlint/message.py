import re

from secomlint.section import Header, Body, Metadata, Contact, Bugtracker
from secomlint.extractor import Extractor
from secomlint.tags import TAGS, CONTACT, METADATA, BUG_TRACKER


class Message:
    def __init__(self, lines) -> None:
        self.raw_text = lines
        self.text = lines
        self.sections = []

    def parse(self):
        
        def is_body(lines):
            is_body = []
            for line in lines:
                regex = rf"^(?!{'|'.join(TAGS)}(:)?.*$).*"
                is_body += [1] if re.search(regex, line) else [0]
            return len(lines) >= 1 and sum(is_body) > 0

        def is_metadata(line):
            return re.search(rf"^({'|'.join(METADATA)}):", line)

        def is_contact(line):
            return re.search(rf"^({'|'.join(CONTACT)}):", line)

        def is_bugtracker(line):
            return re.search(rf"^({'|'.join(BUG_TRACKER)})(:)?", line)
        
        def parse_section(message):
            section=[]
            for idx, line in enumerate(message):
                if line in ('\n',''):
                    break
                else:
                    section.append(line.strip())
            return section, message[idx+1::]
        
        message_tail, idx, bugtracker = self.text, 0, None
        extractor = Extractor()

        while message_tail:
            lines, message_tail = parse_section(message_tail)
            # first line with size 1 (header)
            if idx == 0:
                if len(lines) == 1:
                    self.sections.append(
                        Header(
                            lines=lines,
                            entities=extractor.entities(lines)
                        )
                    )
            else:
                # body
                if is_body(lines):
                    self.sections.append(
                        Body(
                            lines=lines,
                            entities=extractor.entities(lines)
                        )
                    )
                else:
                    for line in lines:
                        if is_metadata(line):
                            tag = is_metadata(line)[0].replace(
                                ':', '').replace(' ', '_')
                            self.sections.append(
                                Metadata(
                                    lines=line,
                                    tag=tag,
                                    entities=extractor.entities([line])
                                ))
                        elif is_contact(line):
                            tag = is_contact(line)[0].replace(
                                ':', '').replace('-', '_')
                            self.sections.append(
                                Contact(
                                    lines=line,
                                    tag=tag,
                                    entities=extractor.entities([line])
                                ))
                        elif is_bugtracker(line):
                            if bugtracker:
                                bugtracker.append_line(line)
                            else:
                                bugtracker = Bugtracker(
                                    lines=[line],
                                    tag='reference',
                                    entities=extractor.entities([line])
                                )
                if bugtracker:
                    self.sections.append(bugtracker)
            idx += 1

        metadata_tags = []
        for section in self.sections:
            if type(section) == Metadata:
                metadata_tags += [section.tag.replace('_', ' ')]

        for tag in METADATA:
            if tag not in metadata_tags:
                self.sections.append(
                    Metadata(
                        lines=None,
                        tag=tag.replace(' ', '_'),
                        entities=None
                    ))

        contact_tags = []
        for section in self.sections:
            if type(section) == Contact:
                contact_tags += [section.tag.replace('_', '-')]

        for tag in CONTACT:
            if tag not in contact_tags:
                self.sections.append(
                    Contact(
                        lines=None,
                        tag=tag.replace('-', '_'),
                        entities=None
                    ))

    def get_sections(self):
        return self.sections

    def get_text(self):
        return self.text
