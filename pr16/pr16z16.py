import re
# Задача 16: 

text16 = "192.168.1.1"
ipv4_pattern = r'^(?:(?:25[0-5]|2[0-4]\d|[01]?\d\d?)\.){3}(?:25[0-5]|2[0-4]\d|[01]?\d\d?)$'
print("Задача 16:", bool(re.fullmatch(ipv4_pattern, text16)))