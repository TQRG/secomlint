from secomlint.utils import extend_tags

METADATA = ['weakness', 'severity', 'detection', 'report', 'cvss', 'introduced in']

CONTACT = ['reported-by', 'signed-off-by', 'co-authored-by']

CONTACT_EXT = extend_tags(CONTACT)

BUG_TRACKER = extend_tags(['bug-tracker', 'resolves', 'see also', 'fixes'])

TAGS = METADATA + CONTACT_EXT + BUG_TRACKER
