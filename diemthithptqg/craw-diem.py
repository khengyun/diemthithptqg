from unicodedata import normalize
import json,requests,csv
from bs4 import BeautifulSoup
from tkinter import *
from show_end import show_end_def

print(" Lưu ý: Số báo danh có tổng là 8 kí tự")
start = int(input("Nhập sbd bắt đầu : "))
end = int(input("Nhập sbd kết thúc : "))
with open("test.txt","a+",encoding = 'utf-8') as F:
        F.write("Số báo danh , Địa Lí,GDCD,Hoá Học,KHTN,KHXH, Lịch Sử,Ngoại Ngữ, Ngữ văn,Sinh Học,Toán,Vật Lí")
        F.write("\n")
        F.close()
for i in range(start,end):
    list_rm  = ["'g'","'p'","[","]","{","}",",","",":","Result None "]
    diem = []
    response = requests.get("https://hoctap.coccoc.com/composer/proxyapi2/graduation_grades/score_search?code="+str(i)+"&nam=2021&fbclid=IwAR33j_UYrRsKhMf-GrjzoAzN_r9U5ktxn3eRIXBIoAmG_kJEluNfjuVbw9k%22)%20data%20=%20r.json()") 
    data = response.json()
    data = (f'{data["proxyapi2"]}')
    for pos in list_rm:
        if pos in list_rm:
            data = data.replace(pos,"")
    if data == []:
        data = str(i) + " -1 -1 -1 -1 -1 -1 -1 -1 -1 -1 -1 "
    data = data.replace("''","-1")
    data = data.replace("'","")
    data = data.replace("Code","SBD")
    data = str(data)
    data = data.split()
    data = " ".join(data)
    print(show_end_def(data,i))
