import re
def printer_error(s):
    pattern = re.compile(r'[^abcdefghijklm]')
    result = pattern.findall(s)
    return f'{len(result)}/{len(s)}'

print(printer_error('kkkwwwaaaaaaaaaaaaaabbbbbbbbbbbbbbbbbbmmmmmmmmmmmmmmmmmmmxyzuuuuu'))