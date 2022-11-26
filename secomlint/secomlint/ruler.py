from secomlint.rule import Rule
from secomlint.section import Header
from secomlint.section import Body
from secomlint.section import Metadata
from secomlint.section import Contact
from secomlint.section import Bugtracker


class Ruler:
    def __init__(self, config) -> None:
        self.rules = []
        for rule in config.default_rules:
            section_name = rule.split('_')[0]
            section = globals()[section_name.capitalize()]
            self.rules.append(Rule(rule,
                                   config.default_rules[rule]['active'],
                                   config.default_rules[rule]['type'],
                                   config.default_rules[rule]['value']
                                   if 'value' in config.default_rules[rule].keys() else 'entity',
                                   section(),
                                   tag='_'.join(rule.split('_')[2::])
                                   if section_name in ('metadata', 'contact', 'bugtracker')
                                   else None
                                   ))

    def get_section_rules(self, section, tag=None):
        return [rule for rule in self.rules
                if type(rule.section) == type(section)
                and rule.tag == tag]

    def compliance(self, section):
        warnings = []
        section_rules = self.get_section_rules(
            section,
            tag=section.tag
        )
        for rule in section_rules:
            if rule.active:
                func_rule = getattr(Rule, rule.name)
                warning = func_rule(rule, section)
                warnings.append(warning)
        
        return warnings
