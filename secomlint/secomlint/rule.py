import re


class Warning:
    def __init__(self, rule_name, result, wtype, wmessage) -> None:
        self.rule_name = rule_name
        self.result = result
        self.type = wtype
        self.message = wmessage
        self.link = f"[\u001b]8;;https://tqrg.github.io/secomlint/#/secomlint-rules?id={self.rule_name.replace('_', '-')}\u001b\\{self.rule_name}\u001b]8;;\u001b\\]"


class Rule:
    def __init__(self, name, active, wtype, value, section, tag=None) -> None:
        self.name = name
        self.active = active
        self.wtype = wtype
        self.value = value
        self.section = section
        self.tag = tag

    def header_max_length(self, section):
        section_text = ''.join(section.lines)
        if section.lines and len(section_text) <= self.value:
            return Warning('header_max_length', 0, self.wtype,
                           f'Header size is within the max length ({self.value} chars).')
        return Warning('header_max_length', 1, self.wtype,
                       f'Header has more than {self.value} chars.')

    def header_is_not_empty(self, section):
        section_text = ''.join(section.lines)
        if len(section_text) > self.value:
            return Warning('header_is_not_empty', 0, self.wtype,
                           'Header is not empty.')
        return Warning('header_is_not_empty', 1, self.wtype,
                       'Header is empty.')

    def header_starts_with_type(self, section):
        section_text = ''.join(section.lines)
        if re.search(rf"^{self.value}.*", section_text):
            return Warning('header_starts_with_type', 0, self.wtype,
                           f'Header starts with {self.value} type')
        return Warning('header_starts_with_type', 1, self.wtype,
                       f'Header is missing the {self.value} type at the start.')

    def header_ends_with_vuln_id(self, section):
        def vuln_id_at_the_end(value, text):
            return re.search(rf".*{value}(\))?$", text)
        section_text = ''.join(section.lines)
        if self.value == 'entity':
            entities = section.entities
            if entities:
                vuln_id = [list(entity)[0]
                           for entity in entities if list(entity)[1] == 'VULNID']
                if vuln_id:
                    if vuln_id_at_the_end(vuln_id[0].lower(), section_text):
                        return Warning('header_ends_with_vuln_id', 0, self.wtype,
                                       'Header ends with vulnerability ID.')
        else:
            if vuln_id_at_the_end(self.value.lower(), section_text):
                return Warning('header_ends_with_vuln_id', 0, self.wtype,
                               'Header ends with vulnerability ID')
        return Warning('header_ends_with_vuln_id', 1, self.wtype,
                       'Header is missing the vulnerability ID at the end.')

    def body_max_length(self, section):
        if section.lines:
            body = ''.join(section.lines)
            if len(body) <= self.value:
                return Warning('body_max_length', 0, self.wtype,
                               f'Body size is within the max length ({self.value} words).')
        return Warning('body_max_length', 1, self.wtype,
                       f'Body has more than {self.value} words.')

    def body_is_not_empty(self, section):
        body = ''.join(section.lines)
        if len(body) > self.value:
            return Warning('body_is_not_empty', 0, self.wtype,
                           'Body is not empty.')
        return Warning('body_is_not_empty', 1, self.wtype,
                       'Body is empty.')

    def body_has_three_paragraphs(self, section):
        if len(section.lines) == 3:
            return Warning('body_has_three_paragraphs', 0, self.wtype,
                           'Body follows the what, why and how structure (three paragraphs).')
        return Warning('body_has_three_paragraphs', 1, self.wtype,
                       'Body doesn\'t follow the what, why and how structure (three paragraphs).')

    def metadata_has_weakness(self, section):
        if 'weakness' == section.tag:
            entities = section.entities
            if entities:
                weakness = [list(entity)[0]
                            for entity in entities if list(entity)[1] == 'CWEID']
                if weakness:
                    return Warning('metadata_has_weakness', 0, self.wtype,
                                   'Metadata mentions a weakness (CWE) id.')
                return Warning('metadata_has_weakness', 1, self.wtype,
                               'Metadata has tag weakness but a weakness (CWE) id was not mentioned.')
        return Warning('metadata_has_weakness', 1, self.wtype,
                       'Metadata section is missing weakness tag/mention.')

    def metadata_has_severity(self, section):
        if 'severity' == section.tag:
            entities = section.entities
            if entities:
                severity = [list(entity)[0] for entity in entities if list(
                    entity)[1] == 'SEVERITY']
                if severity:
                    return Warning('metadata_has_severity', 0, self.wtype,
                                   f'Metadata mentions severity.')
                return Warning('metadata_has_severity', 1, self.wtype,
                               f'Metadata section has severity tag but is missing vulnerability severity /mention.')
        return Warning('metadata_has_severity', 1, self.wtype,
                       f'Metadata section is missing vulnerability severity tag/mention.')

    def metadata_has_detection(self, section):
        if 'detection' == section.tag:
            entities = section.entities
            if entities:
                detection = [list(entity)[0] for entity in entities if list(
                    entity)[1] == 'DETECTION']
                if detection:
                    return Warning('metadata_has_detection', 0, self.wtype,
                                   f'Metadata mentions detection method.')
                Warning('metadata_has_detection', 1, self.wtype,
                        f'Metadata section has detection tag but is missing detection method mention.')
        return Warning('metadata_has_detection', 1, self.wtype,
                       f'Metadata section is missing detection method tag/mention.')

    def metadata_has_report(self, section):
        if 'report' == section.tag:
            entities = section.entities
            if entities:
                url = [list(entity)[0]
                       for entity in entities if list(entity)[1] == 'URL']
                if url:
                    return Warning('metadata_has_report', 0, self.wtype,
                                   f'Metadata mentions report.')
            return Warning('metadata_has_report', 1, self.wtype,
                           f'Metadata has report tag but does not have link to it.')
        return Warning('metadata_has_report', 1, self.wtype,
                       f'Metadata section is missing report tag/mention.')

    def metadata_has_cvss(self, section):
        if 'cvss' == section.tag and section.lines:
            return Warning('metadata_has_cvss', 0, self.wtype,
                           f'Metadata mentions cvss score.')
        return Warning('metadata_has_cvss', 1, self.wtype,
                       f'Metadata section is missing cvss tag/mention.')

    def metadata_has_introduced_in(self, section):
        if 'introduced_in' == section.tag:
            entities = section.entities
            if entities:
                sha = [list(entity)[0]
                       for entity in entities if list(entity)[1] == 'SHA']
                if sha:
                    return Warning('metadata_has_introduced_in', 0, self.wtype,
                                   f'Metadata mentions sha where vulnerability was introduced in.')
            return Warning('metadata_has_introduced_in', 1, self.wtype,
                           f'Metadata mentions introduced in tag but no sha was found.')
        return Warning('metadata_has_introduced_in', 1, self.wtype,
                       f'Metadata section is missing introduced in tag/mention.')

    def contact_has_reported_by(self, section):
        if 'reported_by' == section.tag and section.lines:
            entities = section.entities
            email = [list(entity)[0]
                     for entity in entities if list(entity)[1] == 'EMAIL']
            if email:
                return Warning('contacts_has_reported_by', 0, self.wtype,
                               f'Contacts section includes {self.value} info.')
            return Warning('contacts_has_reported_by', 1, 0,
                           f'Contacts section includes tag for {self.value} but email is missing.')
        return Warning('contacts_has_reported_by', 1, self.wtype,
                       f'Contacts section is missing {self.value} info.')

    def contact_has_signed_off_by(self, section):
        if 'signed_off_by' == section.tag and section.lines:
            entities = section.entities
            email = [list(entity)[0]
                     for entity in entities if list(entity)[1] == 'EMAIL']
            if email:
                return Warning('contact_has_signed_off_by', 0, self.wtype,
                               f'Contacts section includes {self.value} info.')
            return Warning('contact_has_signed_off_by', 1, 0,
                           f'Contacts section includes tag or mention for {self.value} but email is missing.')
        return Warning('contact_has_signed_off_by', 1, self.wtype,
                       f'Contacts section is missing {self.value} info.')

    def contact_has_co_authored_by(self, section):
        if 'co_authored_by' == section.tag and section.lines:
            entities = section.entities
            email = [list(entity)[0]
                     for entity in entities if list(entity)[1] == 'EMAIL']
            if email:
                return Warning('contacts_has_co_authored_by', 0, self.wtype,
                               f'Contacts section includes {self.value} info.')
            return Warning('contacts_has_co_authored_by', 1, 0,
                           f'Contacts section includes tag or mention for {self.value} but email is missing.')
        return Warning('contacts_has_co_authored_by', 1, self.wtype,
                       f'Contacts section is missing {self.value} info.')

    def bugtracker_has_reference(self, section):
        if 'reference' == section.tag and section.lines:
            line = ''.join(section.lines)
            if 'bug-tracker' in line:
                entities = section.entities
                url = [list(entity)[0]
                       for entity in entities if list(entity)[1] == 'URL']
                if url:
                    return Warning('bugtracker_has_reference', 0, self.wtype,
                                   f'Bug tracker section includes url.')
                return Warning('bugtracker_has_reference', 1, self.wtype,
                               f'Bug tracker section mentions bug tracker but is missing url to it.')

            if 'resolves' in line or 'see also' in line:
                entities = section.entities
                issue = [list(entity)[0]
                         for entity in entities if list(entity)[1] == 'ISSUE']
                if issue:
                    return Warning('bugtracker_has_reference', 0, self.wtype,
                                   f'Bug tracker section includes references to issues.')

        return Warning('bugtracker_has_reference', 1, self.wtype,
                       f'Bug tracker section is missing bug-tracker info.')
