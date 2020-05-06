#
import re
def de_fang(modified_ip_address):
    pattern = '^\d\d[\D]*\d\d\d[\D]*\d[\D]*\d\d\d'
    ret = re.match(pattern, modified_ip_address)
    if ret:
        return True
    else:
        return False


ip = "18.233.0.222"
print(de_fang(ip))

