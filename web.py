# This Python file uses the following encoding: utf-8
import pycurl
from urllib import urlencode
import random
from random import randint
import time
import json
import urllib2
import re
import certifi

random.seed(time.time())
def MakeCurl(Token , method , data):
    c = pycurl.Curl()
    c.setopt(pycurl.CAINFO , certifi.where())
    c.setopt(pycurl.URL, "https://api.telegram.org/bot" + Token + "/" + method)
    postfields =  urlencode(data)
    c.setopt(c.POSTFIELDS, postfields)
    #c.setopt(pycurl.POST,1)
    #c.setopt(pycurl.transfer)
    out = c.perform()
    c.close()
    return out
def GetUpdates():
    post_data = {'offset': last_id}
    j = MakeCurl(Token=Token , method="getUpdates" , data=post_data)
    req = urllib2.Request("https://api.telegram.org/bot" + Token + "/getUpdates")
    response = urllib2.urlopen(req)
    data = response.read().decode('utf-8')
    json_data = json.loads(data)
    return json_data

def ContainsRamin(text):
    pattern = '^'+b'رامین '.decode('utf-8')
    #
    rex = re.compile(pattern)
    if rex.search(text) is not None:
        return GetRamin()
    if text == b'رامین'.decode('utf-8'):
        return GetRamin()
    pattern = b' رامین'.decode('utf-8')+'$'
    #
    rex = re.compile(pattern)
    if rex.search(text) is not None:
        return GetRamin()
    pattern =b' رامین '.decode('utf-8')
    #
    rex = re.compile(pattern)
    if rex.search(text) is not None:
        return GetRamin()
    return None

def ContainsRudeTextRamin(text):
    pattern = b'کیری'.decode('utf-8')
    rex = re.compile(pattern)
    if rex.search(text) is not None:
        return GetKiriTextForRamin()
    pattern = b'کیر'.decode('utf-8')
    rex = re.compile(pattern)
    if rex.search(text) is not None:
        return 'از داشته هات حرف بزن. آخه کیر؟؟؟'
    pattern = b' بات '.decode('utf-8')
    rex = re.compile(pattern)
    if rex.search(text) is not None:
        return 'با بات جماعت در نیفت کونت پاره س'
    pattern = b'جون'.decode('utf-8')
    rex = re.compile(pattern)
    if rex.search(text) is not None:
        return 'جوووووون'
    return None


    #print re.match('*'+pattern+'*' , text)


def GetTextForRamin():
    x = randint(0,len(RaminText)-1)
    print x
    return RaminText[x]
def GetEditTextForRamin():
    x = randint(0,len(RaminEditText)-1)
    print x
    return RaminEditText[x]
def GetKiriTextForRamin():
    x = randint(0,len(RaminKiriText)-1)
    print x
    return RaminKiriText[x]
def GetRamin():
    x = randint(0,len(Ramin)-1)
    print x
    return Ramin[x]

def GetText():
    x = randint(0,len(Text)-1)
    print x
    return Text[x]

RaminText = []
RaminText.append("کس نگو")
RaminText.append("کیر نداشتم دهنت کسکش")
RaminText.append("شهرکی ... بسه دیگه خندیدیم")
RaminText.append("عن آقا")
RaminText.append("آخه آدم کیری")
RaminText.append("کیییییییییر")

RaminEditText = []
RaminEditText.append("جقی کمتر بزن")
RaminEditText.append("ادیت میکنی برا من")
RaminEditText.append("ادیت عنه؟؟؟")
RaminEditText.append("عن تیلیت کتمر بکن ادیت")
RaminEditText.append("وجود داری یه بار بنویس")

RaminKiriText = []
RaminKiriText.append("کیری مقام")
RaminKiriText.append("خودتی")
RaminKiriText.append("صفات خودت رو نگو لطفا اینجا")

Ramin = []
Ramin.append('باز اسمش رو اورد')
Ramin.append('یه چی بهت میگما')
Ramin.append('اسمش رو نیار جلوم')


Text = []
Text.append("کس نگو")
Text.append("جوووون")
Text.append("بامزه")
Text.append("عن آقا")
Text.append("لا اله الا الله . نذار باز شه دهنم")
Text.append("کیییییییییر")


Token = "283050839:AAHcI-fUt9vWMgvsj40BUvB6Ym43r068Ftk"
#post_data = {'text': 'Kos Nagu Momen' , 'chat_id':'-155288122'}
#post_data = {'text': 'ehsan ziadi var naro ba man' , 'chat_id':'107997967'}
#numpy.rand(23)
ticks = time.time()
#print MakeCurl(Token=Token , method="sendMessage" , data=post_data)

#print "\n\n\n" , len(msg['result'])
last_id = 0
while (True):
    if time.time() - ticks > 15:
        print "---------------------------------------------------"
        #print GetTextForRamin()
        msg =  GetUpdates()
        print  "\nupdated"
        print(json.dumps(msg['result'], sort_keys=True, indent=4))
        for key in msg['result']:
            if key.has_key('message') :
                chat_id =  key['message']['chat']['id']
                first_name =  key['message']['from']['first_name']
                message_id = key['message']['message_id']
                last_id =  key['update_id'] + 1
                if key['message'].has_key('text'):
                    text = key['message']['text']
                else:
                    text = ''
                edited = False
                if key['message'].has_key('forward_from_chat'):
                    forwarded = True
                else:
                    forwarded = False
            else:
                chat_id =  key['edited_message']['chat']['id']
                first_name =  key['edited_message']['from']['first_name']
                message_id = key['edited_message']['message_id']
                last_id =  key['update_id'] + 1
                text = key['edited_message']['text']
                edited = True
                forwarded = False
            #print "---------------------------------------------------"
            #print text

            if chat_id == 106698568 and first_name == "Soheil" :
                if ContainsRudeTextRamin ( text) is not None:
                    MakeCurl(Token=Token , method="sendMessage" , data={'chat_id': chat_id , 'reply_to_message_id': message_id , 'text':ContainsRudeTextRamin ( text)})
                #elif edited:
                #    MakeCurl(Token=Token , method="sendMessage" , data={'chat_id': chat_id , 'reply_to_message_id': message_id , 'text':'++++'+GetEditTextForRamin()})
                #else:
                #    MakeCurl(Token=Token , method="sendMessage" , data={'chat_id': chat_id , 'reply_to_message_id': message_id , 'text':'------'+GetTextForRamin()})
            #if chat_id == -155288122 and first_name == "Soheil" :
            #    MakeCurl(Token=Token , method="sendMessage" , data={'chat_id': chat_id , 'reply_to_message_id': message_id , 'text':'Mokhles e Dach Soheil'})
            #if chat_id == -155288122 and first_name == "Ramin" :
            rand = random.random()
            if ContainsRamin(text) is not None:
                MakeCurl(Token=Token , method="sendMessage" , data={'chat_id': chat_id , 'reply_to_message_id': message_id , 'text':ContainsRamin ( text)})
            elif ContainsRudeTextRamin ( text) is not None:
                MakeCurl(Token=Token , method="sendMessage" , data={'chat_id': chat_id , 'reply_to_message_id': message_id , 'text':ContainsRudeTextRamin ( text)})

            elif edited:
                    MakeCurl(Token=Token , method="sendMessage" , data={'chat_id': chat_id , 'reply_to_message_id': message_id , 'text':GetEditTextForRamin()})
            elif forwarded:
                username = key['message']['forward_from_chat']['username']
                if username == 'sharif_counseling_center':
                    MakeCurl(Token=Token , method="sendMessage" , data={'chat_id': chat_id , 'reply_to_message_id': message_id , 'text':'باز ازین کانال کسشر فرستادی'})
                if username == 'youtwitte':
                    MakeCurl(Token=Token , method="sendMessage" , data={'chat_id': chat_id , 'reply_to_message_id': message_id , 'text':'کانال خوبیه خوشم اومد'})
            if rand> 0.75 and first_name != "Ali":
                MakeCurl(Token=Token , method="sendMessage" , data={'chat_id': chat_id , 'reply_to_message_id': message_id , 'text':GetText()})
            elif rand > 0.75:
                MakeCurl(Token=Token , method="sendMessage" , data={'chat_id': chat_id , 'reply_to_message_id': message_id , 'text':'با متاهلا کاری ندارم.مخلصیم'})

				
				
            if first_name == "Ramin" :
                if edited:
                    MakeCurl(Token=Token , method="sendMessage" , data={'chat_id': chat_id , 'reply_to_message_id': message_id , 'text':GetEditTextForRamin()})
                else:
                    MakeCurl(Token=Token , method="sendMessage" , data={'chat_id': chat_id , 'reply_to_message_id': message_id , 'text':GetTextForRamin()})


        ticks = time.time()
