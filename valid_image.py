import os

file = 10000
max_file = 2000

for i in range(file, file + max_file, 1):
    size = os.stat(f"img/{file}.jpg")
    print(f"{file}.jpg - {size.st_size} Bytes")
    if size.st_size == 0:
        os.remove(f"img/{file}.jpg")
    file += 1