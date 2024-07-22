from collections import Counter
import io
import datetime

date_time = datetime.datetime.now()
year = datetime.datetime.now()

print(f"date_time = {date_time}")
print(f"year = {year.year}")


alpha = ['a', 'b', 'c', 'd', 'a', 'a', 'c']
data_count = Counter(alpha)
print(f"counter = {data_count}")
print(f"jumlah a = {data_count["a"]}")
print(f"jumlah d = {data_count["d"]}")


file = io.open('file.txt', 'r')
print(file.read())
