#!/usr/bin/env python3.9
import time
import os
import datetime
import requests
import sqlite3

last_update_id = 0

with sqlite3.connect('/var/.secret.db3') as conn:
    cursor = conn.cursor()
    cursor.execute("SELECT secret FROM pass WHERE app LIKE 'ASHONOFF'")
    t_bot = cursor.fetchone()[0]
    cursor.execute("SELECT secret FROM pass WHERE app LIKE 't_elena'")
    t_elena =  int(cursor.fetchone()[0])
    cursor.execute("SELECT secret FROM pass WHERE app LIKE 't_andrey'")
    t_andrey =  int(cursor.fetchone()[0])
    print(t_bot, t_elena, t_andrey)
    t_url = 'https://api.telegram.org/bot{}/getUpdates'.format(t_bot)

while True:
    a = 65537
    result = requests.get(t_url, params={'offset': last_update_id + 1})
    print(last_update_id)
    print(result.json())
    data = result.json()
    time.sleep(3)
    for txt in data["result"]:
        last_update_id = txt['update_id']
        if 'message' not in txt: break 
        print(txt['message']['from']['id'])
        #print(txt['message']['from']['first_name'])
        #print(txt['message']['from']['last_name'])
        #print(txt['message']['from']['username'])
         
        if txt['message']['from']['id']==t_andrey or txt['message']['from']['id']==t_elena:
            print(txt['message']['text'])
            #last_update_id = txt['update_id']
            if txt['message']['text']=='/on':
                text = "successfully"
                print ("\nOn {}".format(datetime.datetime.today()))
                for i in range(10):
                    a = os.system("ssh admin@10.248.0.6 '/interface ethernet poe set  poe-out=force ether5'")
                    if a == 0:
                        break 
                    else:
                        text = "unsuccessfuly"
                print ("On gone {} {}".format(text, datetime.datetime.today()))
                print (a)

            if txt['message']['text']=='/off':
                text = "successfully"
                print ("\nOff {}".format(datetime.datetime.today()))
                for i in range(10):
                    a = os.system("ssh admin@10.248.0.6 '/interface ethernet poe set  poe-out=off ether5'")
                if a == 0:
                    break 
                else:
                    text = "unsuccessfuly"
                print ("Off gone {} {}".format(text, datetime.datetime.today()))
                print (a)
    if 'update_id' in data: last_update_id = txt['update_id']

