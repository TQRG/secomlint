import parser
import rules 

def secom(message):
    results = []
    ftype, header, vuln_id, body = parser.parse(message)
    results += rules.check_header(header)
    results += rules.check_vuln_id(vuln_id)
    results += rules.check_type(ftype)
    results += rules.check_body(body)
    return results

    