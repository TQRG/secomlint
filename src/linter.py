import parser
import rules 

def secom(message):
    header = parser.parse(message)
    results = rules.engine(header)
    return results

    