import re
# Задача 11: Замена слов короче 3 символов на "***"
text11 = "A cat is on the bed"
print("Задача 11:", re.sub(r'\b\w{1,2}\b', '***', text11))