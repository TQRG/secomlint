import re

hrules = {
    'header_max_length': [1, 0, 50],
    'header_is_not_empty': [1, 1, 0],
    'header_starts_with_type': [1, 1, 'vuln-fix'],
    'header_ends_with_vuln_id': [1, 0, '(GHSA|CVE|OSV)-.*']
}

def header_max_length(header, value, rtype):
    if len(header) > 0:
        if ':' in header:
            header = header.split(':')[1].split('(')[0].strip()
        else:
            header = header.split('(')[0].strip()
        if len(header) <= value:
            return ['header_max_length', 0, f'✅\tHeader size is within the max length ({value} chars)']
    return ['header_max_length', 1, f'{rtype}\tHeader has more than {value} chars']


def header_is_not_empty(header, value, rtype):
    if len(header) == value:
        return ['header_is_not_empty', 1, f'{rtype}\tHeader is empty']
    return ['header_is_not_empty', 0, f'✅\tHeader is not empty']

def header_starts_with_type(header, value, rtype):
    if len(header) > 0:
        isvuln = header.split(':')[0].strip()
        if isvuln == value:
            return ['header_starts_with_type', 0, f'✅\tHeader includes the {value} type']
    return ['header_starts_with_type', 1, f'{rtype}\tHeader is missing the {value} type at the start']

    
def header_ends_with_vuln_id(header, value, rtype):
    if len(header) > 0:
        vulnid = header.split('(')[-1].replace(')', '')
        pattern = re.compile(value)
        if bool(pattern.match(vulnid)):
            return ['header_ends_with_vuln_id', 0, f'✅\tHeader includes the vulnerability ID']
    return ['header_ends_with_vuln_id', 1, f'{rtype}\tHeader is missing the vulnerability ID at the end']
 

def engine(header):
    results = []
    for rule in hrules:
        renable, rtype, rvalue = hrules[rule]
        rtype = '⚠️' if rtype == 0 else '🚩'
        if renable == 1:
            if rule == 'header_max_length':
                results.append(header_max_length(header, rvalue, rtype))
            elif rule == 'header_is_not_empty':
                results.append(header_is_not_empty(header, rvalue, rtype))
            elif rule == 'header_starts_with_type':
                results.append(header_starts_with_type(header, rvalue, rtype))
            elif rule == 'header_ends_with_vuln_id':
                results.append(header_ends_with_vuln_id(header, rvalue, rtype))
    return results