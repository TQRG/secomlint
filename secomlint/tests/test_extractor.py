from secomlint import extractor

def get_entities(ext, lines):
    return len(ext.extract_entities(lines))

def test_ents_extraction():
    ext = extractor.Extractor()
    lines = ['fix vulnerability']
    assert ext.extract_entities(lines) == \
        [('fix', 'ACTION', ''), ('vulnerability', 'SECWORD', '')]

def test_ents_extraction_len():
    ext = extractor.Extractor()
    lines = ['fix vulnerability']
    assert len(ext.extract_entities(lines)) == 2
    
def test_ents_extraction_action():
    ext = extractor.Extractor()
    lines = ['fix vulnerability']
    action_ents = sum([1 if list(ent)[1] == 'ACTION' else 0 for ent in ext.extract_entities(lines)])
    assert action_ents > 0