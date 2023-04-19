from secomlint.rule import Rule

from secomlint.section import Header, Body, Metadata, Contact, Bugtracker

class Ruler:
    def __init__(self, config) -> None:
        self.rules = []
        for rule in config.default_rules:
            section_name = rule.split('_')[0]
            section = globals()[section_name.capitalize()]
            default_rule = config.default_rules[rule]
            self.rules.append(Rule(rule,
                                   default_rule['active'],
                                   default_rule['type'],
                                   default_rule['value']
                                   if 'value' in default_rule.keys() else 'entity',
                                   section(),
                                   tag='_'.join(rule.split('_')[2::])
                                   if section_name in ('metadata', 'contact', 'bugtracker')
                                   else None
                                   ))

    def get_section_rules(self, section, tag=None):
        return [rule for rule in self.rules
                if type(rule.section) == type(section)
                and rule.tag == tag]
