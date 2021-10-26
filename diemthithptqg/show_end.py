import json

def to_txt(text,sbd):

    data = ",".join(text)
    data = data.replace("None,","")
    if data == "":
        data = str(sbd) + ",-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1 "
    with open("test.txt","a+",encoding = 'utf-8') as F:
        F.write(data)
        F.write("\n")
        F.close()
    print(data)
    
def show_end_def(data,sbd):
    score = []
    start_mid = data.find("ListGroup")
    end_mid = data.find("NgoaiNgu")
    start_mid = data[:start_mid]
    end_mid = data[end_mid:]
    done_data = start_mid + end_mid
    done_data = done_data.split()
    for i in range(0,len(done_data)):
        if i % 2 != 0:
            score.append(done_data[i])
    to_txt(score,sbd)
