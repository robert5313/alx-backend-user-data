import re

def filter_datum(fields, redaction, message, separator):
    pattern = '|'.join(fields)
    return re.sub(pattern + r'=[^{0}]*'.format(separator), redaction, message)
