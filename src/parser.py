
def parse_header(header):
    ftype, fheader, vuln_id = '', header, ''
    if ':' in header:
        ftype, fheader = header.split(':')
    if '(' in header:
        header, vuln_id = header.split('(')
        fheader = header.strip()
        vuln_id = vuln_id.replace(')','').strip()
    return ftype, fheader, vuln_id

def parse_body(body):
    what, why, how = '', '', ''
    if len(body) > 0:
        body_sentences = body.split('\n')
        if len(body_sentences) > 0:
            for sentence in body_sentences:
                if '(what)' in sentence:
                    what = sentence.replace('(what)', '').lstrip()
                elif '(why)' in sentence:
                    why = sentence
                elif '(how)' in sentence:
                    how = sentence
        if len(body_sentences) == 3:
            what, why, how = body_sentences[0].replace('(what)', '').lstrip(), \
                            body_sentences[1].replace('(why)', '').lstrip(), \
                            body_sentences[2].replace('(how)', '').lstrip()

    return what, why, how

def split(message):       
    smsg = message.split("\n\n")
    header, body, metadata, contacts, tracker = '', '', '', '', ''
    for idx, info in enumerate(smsg):
        info_split = info.split('\n')
        if idx == 0 and len(info_split) == 1:
            header = info
        elif 'weakness:' in info.lower() or \
            'severity:' in info.lower() or \
            'cvss:' in info.lower() or \
            'detection:' in info.lower() or \
            'introduced in:' in info.lower():
            metadata = info 
        elif 'reported-by:' in info.lower() or \
            'signed-off-by:' in info.lower() or \
                'reported by:' in info.lower() or \
                'signed off by:' in info.lower():
            contacts = info
        elif 'resolves:' in info.lower() or \
            'bug-tracker:' in info.lower():
            tracker = info   
        else:
            body = info 
    return header, body, metadata, contacts, tracker

def parse(message):
    header, body, metadata, contacts, tracker = split(message)
    ftype, header, vuln_id = parse_header(header)
    what, why, how = parse_body(body)
    return ftype, header, vuln_id, {'what': what, 'why': why, 'how': how}#, body, metadata, contacts, tracker
    