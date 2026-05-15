import datetime
with open('log.txt', 'a', encoding='utf-8') as f:
    f.write(f"{datetime.datetime.now()} - Log message\n")