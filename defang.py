#
import re
def de_fang(modified_ip_address):
    pattern = "^\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}$"
    ret = re.match(pattern, modified_ip_address)
    if ret:
        return True
    else:
        return False


ip = "18.233.0.222"
print(de_fang(ip))

