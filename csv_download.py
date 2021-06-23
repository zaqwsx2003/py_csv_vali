import os
import csv
import requests

f = open(r'C:\Users\응용프로그램\Desktop\csv\face-dataset.csv') #디폴트 인코딩 cp949
#f = open(r'D:\토닥토닥파이썬\소스\CSV파일읽고쓰기(csv모듈)\예제\output\naver_blog.csv',encoding='cp949') 
#f = open(r'D:\토닥토닥파이썬\소스\CSV파일읽고쓰기(csv모듈)\예제\output\naver_blog.csv',encoding='utf8')
r = csv.reader(f)

mask = 0 # 0: no_mask, 1: with_mask

idx = 20000
count = 0 
max_file = 2000

headers = next(r)
for row in r:
    if os.path.isfile(f"img/{idx + count}.jpg") == True:
        count += 1
        continue

    with open(f"img/{idx + count}.jpg", "wb") as handle:
        responses = requests.get(row[5], stream=True)
        if responses.ok:
            for block in responses.iter_content(4096):
                if block:
                    handle.write(block)

    size = os.stat(f"img/{idx + count}.jpg")
    if size.st_size == 0:
        os.remove(f"img/{idx + count}.jpg")
        idx += 1
        continue

    print(f"[{count}/{max_file}] {row[5]}")

    count += 1
    
    if count > max_file:
        break

print("<== END ===>")

f.close()