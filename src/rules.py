import re

hrules = {
    'header_max_length': [1, 0, 50],
    'header_is_not_empty': [1, 1, 0],
    'header_starts_with_type': [1, 1, 'vuln-fix'],
    'header_ends_with_vuln_id': [1, 0, '(GHSA|CVE|OSV)-.*']
}

brules = {
    'body_max_length': [1, 0, 75],
    'body_is_not_empty': [1, 1, 75],
    'body_section_max_length': [1, 0, 25],
    'body_section_is_not_empty': [1, 1, 0]
}

def header_max_length(header, value, rtype):
    if len(header) > 0 and len(header) <= value:
        return ['header_max_length', 0, f'✅\tHeader size is within the max length ({value} chars)']
    return ['header_max_length', 1, f'{rtype}\tHeader has more than {value} chars']

def header_is_not_empty(header, rtype):
    if len(header) == 0:
        return ['header_is_not_empty', 1, f'{rtype}\tHeader is empty']
    return ['header_is_not_empty', 0, f'✅\tHeader is not empty']

def header_starts_with_type(ctype, value, rtype):
    if len(ctype) > 0:
        if ctype == value:
            return ['header_starts_with_type', 0, f'✅\tHeader includes the {value} type']
        else:
            return ['header_starts_with_type', 1, f'{rtype}\tHeader includes the wrong type']
    return ['header_starts_with_type', 1, f'{rtype}\tHeader is missing the {value} type at the start']

def header_ends_with_vuln_id(vuln_id, value, rtype):
    if len(vuln_id) > 0:
        pattern = re.compile(value)
        if bool(pattern.match(vuln_id)):
            return ['header_ends_with_vuln_id', 0, f'✅\tHeader includes the vulnerability ID']
    return ['header_ends_with_vuln_id', 1, f'{rtype}\tHeader is missing the vulnerability ID at the end']

def body_max_length(body, value, rtype):
    if len(body) > 0:
        body = ' '.join(body)
        if len(body.split(' ')) <= value:
            return ['body_max_length', 0, f'✅\tBody size is within the max length ({value} words)']
    return ['body_max_length', 1, f'{rtype}\tBody has more than {value} words']

def body_is_not_empty(body, rtype):
    if len(''.join(body)) > 0:
        return ['body_is_not_empty', 0, f'✅\tBody is not empty'], False
    return ['body_is_not_empty', 1, f'{rtype}\tBody is empty'], True

def body_section_max_length(sec, name, value, rtype):
    if len(sec) > 0 and len(sec.split(' ')) <= value:
        return ['body_section_max_length', 0, f'✅\tSection {name} size is within the max length ({value} words)']
    return ['body_section_max_length', 1, f'{rtype}\tSection {name} has more than {value} words']

def body_section_is_not_empty(sec, name, rtype):
    if len(sec) > 0:
        return ['body_section_max_length', 0, f'✅\tSection {name} is not empty']
    return ['body_section_max_length', 1, f'{rtype}\tSection {name} is empty']
  
def check_body(body):
    
    arr_body, results = [body[sec] for sec in body], []      
    renable, rtype, rvalue = brules['body_is_not_empty']
    if renable == 1:
        rtype = '⚠️' if rtype == 0 else '🚩'
        out, violates = body_is_not_empty(arr_body, rtype)
        results.append(out)
        if violates:
            return results
        
    renable, rtype, rvalue = brules['body_max_length']
    if renable == 1:
        rtype = '⚠️' if rtype == 0 else '🚩'
        results.append(body_max_length(arr_body, rvalue, rtype))

    renable, rtype, rvalue = brules['body_section_is_not_empty']
    if renable == 1:
        rtype = '⚠️' if rtype == 0 else '🚩'
        for key in body:
            results.append(body_section_is_not_empty(body[key], key, rtype))       

    renable, rtype, rvalue = brules['body_section_max_length']
    if renable == 1:
        rtype = '⚠️' if rtype == 0 else '🚩'
        for key in body:
            results.append(body_section_max_length(body[key], key, rvalue, rtype))       
        
    return results

def check_header(header):
    results = []
    renable, rtype, rvalue = hrules['header_max_length']
    if renable == 1:
        rtype = '⚠️' if rtype == 0 else '🚩'
        results.append(header_max_length(header, rvalue, rtype))
    
    renable, rtype, rvalue = hrules['header_is_not_empty']
    if renable == 1:
        rtype = '⚠️' if rtype == 0 else '🚩'
        results.append(header_is_not_empty(header, rtype))
    return results

def check_vuln_id(vuln_id):
    results = []
    renable, rtype, rvalue = hrules['header_ends_with_vuln_id']
    if renable == 1:
        rtype = '⚠️' if rtype == 0 else '🚩'
        results.append(header_ends_with_vuln_id(vuln_id, rvalue, rtype))
    return results 

def check_type(ctype):
    results = []
    renable, rtype, rvalue = hrules['header_starts_with_type']
    if renable == 1:
        rtype = '⚠️' if rtype == 0 else '🚩'
        results.append(header_starts_with_type(ctype, rvalue, rtype))
    return results