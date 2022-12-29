# -*- coding: utf-8 -*-
from hackcqooc.core import Core
import requests
import time
import json
import datetime
import pyperclip
import threading
import sys
import webbrowser
sys.coinit_flags = 2

from tkinter import END 
import tkinter as tk
# import ttkbootstrap as ttk
# from tkinter import ttk
from tkinter import messagebox


from ttkbootstrap import Style
from tkinter import ttk
 
style = Style(theme='darkly')
import re
from fake_useragent import UserAgent



root = style.master

root.title("小鱼学习通签到小助手")
root.geometry("650x530+400+300")
root.resizable(False, False) # 窗口大小不可变
global usaen 
global cqoocuser 
global cqoocpassword 
global beisu
beisu = 25
usaen = "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:104.0) Gecko/20100101 Firefox/104.0"
# 左边布局
left_frame = tk.Frame(root)

# 激活登录
left_frame.pack(side=tk.LEFT,anchor=tk.N,padx=5,pady=5,fill=tk.X)
net_frame = tk.LabelFrame(left_frame,text="公告",padx=5,pady=5)
net_frame.pack()
tk.Label(net_frame,text="本软件现已免费开源，入群获取密码").pack(anchor=tk.W)
entry_port = ttk.Entry(net_frame,show = '*',width=10)
entry_port.pack(fill=tk.X)
# 按钮
button_frame = tk.Frame(net_frame)
button_frame.pack()
open_button = ttk.Button(button_frame,text="确定",command=lambda:thread_it( click_determine), bootstyle="success",width=8)
open_button.pack(side=tk.RIGHT,pady=10)
get_button = ttk.Button(button_frame,text="交流群" ,command=lambda:click_goto(),bootstyle="info",width=8)
get_button.pack(side=tk.RIGHT,pady=10,padx=9)

# 信息
# 左边布局  激活信息
recv_frame = tk.LabelFrame(left_frame,text="版本信息",padx=5,pady=5)
recv_frame.pack(side=tk.TOP,anchor= tk.N,fill=tk.X)
endbox1_frame = tk.LabelFrame(recv_frame)
endbox1_frame.pack(side=tk.TOP,anchor= tk.N,fill=tk.X)

endbox2_frame = tk.Frame(recv_frame)
endbox2_frame.pack(side=tk.TOP,anchor= tk.N,fill=tk.X,pady=3)
tk.Label(endbox2_frame,text="版本：V1.0-2022/12/25").pack(anchor=tk.W)
label_endtime = tk.Label(endbox2_frame,text="源码：github.com/Mrkk1/xxtqd")
label_endtime.pack(anchor=tk.W)

#左边布局 课程选择
chose_frame = tk.LabelFrame(left_frame,text="学习通登录",padx=5,pady=8)
chose_frame.pack(side=tk.TOP,anchor= tk.N,fill=tk.X)

label_frame = tk.Frame(chose_frame)
label_frame.pack(side=tk.TOP,anchor= tk.N,fill=tk.X ,pady=5)

# xsid_lable = tk.Label(label_frame,text="xsid")
# xsid_lable.pack(side=tk.LEFT)

cqoocuser_lable = tk.Label(label_frame,text="手机号")
cqoocuser_lable.pack(side=tk.LEFT)
cqoocuser_port = ttk.Entry(label_frame )
cqoocuser_port.pack(fill=tk.X)

# button_help = ttk.Button(label_frame,text= '?',bootstyle="secondary-outline",command=lambda:gotohelp())
# button_help.pack(side=tk.RIGHT)




label_frame2 = tk.Frame(chose_frame)
label_frame2.pack(side=tk.TOP,anchor= tk.N,fill=tk.X ,pady=5)
cqoocpassword_lable = tk.Label(label_frame2,text="密码")
cqoocpassword_lable.pack(side=tk.LEFT)
cqoocpassword_port = ttk.Entry(label_frame2,show='*' )
cqoocpassword_port.pack(fill=tk.X)

label_frame3 = tk.Frame(chose_frame)
label_frame3.pack(side=tk.TOP,anchor= tk.N,fill=tk.X ,pady=5)
sendkey_lable = tk.Label(label_frame3,text="sendkey")
sendkey_lable.pack(side=tk.LEFT)
sendkey_port = ttk.Entry(label_frame3,show='*' )
sendkey_port.pack(fill=tk.X)


label_frame4 = tk.Frame(chose_frame)
label_frame4.pack(side=tk.TOP,anchor= tk.N,fill=tk.X ,pady=5)
qdname_lable = tk.Label(label_frame4,text="签到昵称")
qdname_lable.pack(side=tk.LEFT)
qdname_port = ttk.Entry(label_frame4 )
qdname_port.pack(fill=tk.X)

label_frame5 = tk.Frame(chose_frame)
label_frame5.pack(side=tk.TOP,anchor= tk.N,fill=tk.X ,pady=5)
address_lable = tk.Label(label_frame5,text="签到地址")
address_lable.pack(side=tk.LEFT)
address_port = ttk.Entry(label_frame5 )
address_port.pack(fill=tk.X)

#按钮
button_login = tk.Frame(chose_frame)
button_login.pack()
login_button = ttk.Button(button_login,text="开始",command=lambda:thread_it(starts))
login_button.pack(side=tk.LEFT,pady=6,ipadx=10)


# bottomday=tk.Label(left_frame,text="本软件由小鱼开发，开源协议为MIT")


# bottomday.pack(anchor=tk.W)


#右边布局
right_frame = tk.Frame(root)
right_frame.pack(side=tk.TOP,padx=5,pady=4)

info_frame= tk.Frame(right_frame)
info_frame.pack()









tk.Label(info_frame,text="数据日志").pack(anchor=tk.W)
text_pad = tk.Text(info_frame,width=60,height=26)
text_pad.pack(side=tk.LEFT,fill=tk.X)

send_text_bar = tk.Scrollbar(info_frame)
send_text_bar.pack(side=tk.RIGHT,fill=tk.Y)
text_pad.insert(END,'用户需知：\n')
text_pad.insert(END,'请准确的填写您学习通的相关信息\n')
text_pad.insert(END,'目前只能使用手机号和密码登录学习通，无法使用学号登录\n')
text_pad.insert(END,'sendkey用于将签到信息推送到您的微信，你可以不填写。如有需要可以前往：https://sct.ftqq.com/sendkey 获取\n')
text_pad.insert(END,'当您填写一次信息之后将会保存在confg.js文件中，下一次打开时会自行填写完成\n')
text_pad.insert(END,'\n')

#DIBVU
bottom_frame = tk.Frame(root)
bottom_frame.pack(side=tk.LEFT,anchor=tk.N,padx=0,pady=0,fill=tk.X)
tk.Label(bottom_frame,text="本软件由小鱼开发，开源协议为MIT").pack(anchor=tk.E)

################### Config #############################

global cookie_xsid 
global capassword 
global luck 
global quanxian
global jhres
global courseData
global CompleteCourse

quanxian = False

########################################################
#获取代理ip

    
   

################################
def thread_it(func, *args):
    '''将函数打包进线程'''
    # 创建
    t = threading.Thread(target=func, args=args) 
    # 守护 !!!
    t.setDaemon(True) 
    # 启动
    t.start()
    # 阻塞--卡死界面！
    # t.join()
# 点击确定激活码
def click_determine():
    global cami 
    cami = entry_port.get()
    jiaoyankami()

def click_goto():
    pyperclip.copy('264135853')
    messagebox.showinfo("成功","群号264135853已复制到您的剪贴板")
    # webbrowser.open_new("https://qm.qq.com/cgi-bin/qm/qr?k=5r-TsnUKjoZbeKIqOMaxX2kMHxTqGM3W&jump_from=webapi")

# 校验卡密
def jiaoyankami():

    global quanxian
    now_time = datetime.datetime.now().strftime('%Y-%m-%d')
    headers={ "User-Agent": "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/51.0.2704.103 Safari/537.36"}

    if(cami=='gxpt2022'):

        if(cami=='gxpt2022'):
            print('')
            quanxian = True
            messagebox.showinfo("成功","密码正确您将可以直接使用")
    else:
        messagebox.showerror("错误","密码有误，请五秒后再次尝试")
        open_button.config(state='disabled')
        time.sleep(5)
        open_button.config(state='common')





def getTs():
    return int(time.time() * 1000)

import requests,json
import urllib.parse
from random import choices
import datetime,os,time
session = requests.session()
requests.packages.urllib3.disable_warnings()

with open('./confg.json', 'r', encoding='utf-8') as f:
    setting = json.loads(f.read())
f.close

if setting["account"]:

    cqoocuser_port.insert ('0',setting["account"])

if setting["password"]:
    cqoocpassword_port.insert ('0',setting["password"])

if setting["sendkey"]:
    sendkey_port.insert ('0',setting["sendkey"])

if setting["sign"]["name"]:
    qdname_port.insert ('0',setting["sign"]["name"])

if setting["sign"]["address"]:
    address_port.insert ('0',setting["sign"]["address"])



#乱七八糟的变量 不要动我
mycookie=""
myuid=""
courselist=[]

#登录
def login(uname,code):
    global mycookie,myuid
    url="https://passport2-api.chaoxing.com/v11/loginregister?code="+code+"&cx_xxt_passport=json&uname="+uname+"&loginType=1&roleSelect=true"
    res=session.get(url)
    data = requests.utils.dict_from_cookiejar(session.cookies)
    mycookie=""
    for key in data:
        mycookie+=key+"="+data[key]+";"
    d=json.loads(res.text)
    if(d['mes']=="验证通过"):
        print(uname+"登录成功")
        messagebox.showinfo("成功","登录成功")


        url="https://sso.chaoxing.com/apis/login/userLogin4Uname.do"
        res=session.get(url)
        a=json.loads(res.text)
        if(a['result']==1):
            myuid=str(a['msg']['puid'])
            #save_cookies(myuid,2)
            return 1
        else:
            print("获取uid失败")
    return 0
#获取同意请求头 包含Cookie
def getheaders():
    headers={"Accept-Encoding": "gzip",
    "Accept-Language": "zh-Hans-CN;q=1, zh-Hant-CN;q=0.9",
    "Cookie": mycookie,
    "User-Agent": "Mozilla/5.0 (iPhone; CPU iPhone OS 14_2_1 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Mobile/15E148 com.ssreader.ChaoXingStudy/ChaoXingStudy_3_4.8_ios_phone_202012052220_56 (@Kalimdor)_12787186548451577248",
    "X-Requested-With": "com.chaoxing.mobile",

             }
    # "User-Agent": "Mozilla/5.0 (iPhone; CPU iPhone OS 14_2_1 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Mobile/15E148 com.ssreader.ChaoXingStudy/ChaoXingStudy_3_4.8_ios_phone_202012052220_56 (@Kalimdor)_12787186548451577248"
    return headers
def getheaders2():
    headers={"Accept": "*/*",
             "Accept-Encoding": "gzip,deflate",
             "Accept-Language": "zh-CN,zh;q=0.9,en-US;q=0.8,en;q=0.7",

             "User-Agent": "Mozilla/5.0 (Linux; Android 7.1.2; M2007J22C Build/QP1A.190711.020; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/92.0.4515.131 Mobile Safari/537.36 com.chaoxing.mobile/ChaoXingStudy_3_4.3.4_android_phone_494_27 (@Kalimdor)_d0037b51d800439894388df2d41ec6ef",
             "X-Requested-With": "XMLHttpRequest",
             'Referer':'',
             'Host': 'mobilelearn.chaoxing.com',
             "Cookie": mycookie,
             'Sec-Fetch-Site': 'same-origin',
             'Sec-Fetch-Mode': 'cors',
             'Sec-Fetch-Dest': 'empty',
             'Connection': 'keep-alive'
             }
    # "User-Agent": "Mozilla/5.0 (iPhone; CPU iPhone OS 14_2_1 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Mobile/15E148 com.ssreader.ChaoXingStudy/ChaoXingStudy_3_4.8_ios_phone_202012052220_56 (@Kalimdor)_12787186548451577248"
    return headers
#获取课程列表
def getcourse():
    global courselist
    url="http://mooc1-api.chaoxing.com/mycourse/backclazzdata?view=json&rss=1"
    headers=getheaders()
    if(headers==0):
        return 0
    res=session.get(url,headers=headers)
    print(res)
    if('请重新登录' in res.text):
        print("Cookie已过期")

    else:
        d=json.loads(res.text)
        courselist=d['channelList']

#普通签到
def sign1(referer,aid,uid,name):
    print(referer,aid,uid,name)
    t=get_time()
    snow_time = datetime.datetime.now().strftime('%Y-%m-%d   %H:%M:%S')

    print("发现普通签到" +'\t'+ str(snow_time)+'\n')
    # text_pad.insert("发现普通签到" +'\t'+ str(snow_time)+'\n')
    name=urllib.parse.quote(name)
    url="https://mobilelearn.chaoxing.com/pptSign/stuSignajax?activeId="+aid+"&uid="+uid+"&clientip=&latitude=-1&longitude=-1&appType=15&fid=0&name="+name
    headers = getheaders2()
    headers['Referer'] = referer
    ani_spider=session.get(referer,headers=headers)
    time.sleep(2)
    if(headers==0):
        return 0
    res=requests.get(url,headers=headers)
    print(res.text)

    if(res.text=="success"):

        if setting["sendkey"]:
            api = 'https://sctapi.ftqq.com/' + setting["sendkey"] + '.send'
            title = u"已为您成功签到"
            content = "签到类型:"+'普通签到'+'\n\n用户:' + setting["account"]
            data = {
                "text": title,
                "desp": content
            }
            requests.post(api, data=data)
            text_pad.insert("签到成功，已尝试推送消息到微信" +'\t'+ str(snow_time)+'\n')
            messagebox.showinfo("成功","签到成功，已推送消息到微信")

        time.sleep(60) 
        return 1
        
    else:
        return 0
#照片签到/手势签到
def sign2(referer,aid,uid,oid,name):
    t=get_time()
    snow_time = datetime.datetime.now().strftime('%Y-%m-%d   %H:%M:%S')

    print("发现照片签到/手势签到" +'\t'+ str(snow_time)+'\n')

    # text_pad.insert("发现照片签到/手势签到" +'\t'+ str(snow_time)+'\n')
    name=urllib.parse.quote(name)
    url="https://mobilelearn.chaoxing.com/pptSign/stuSignajax?activeId="+aid+"&uid="+uid+"&clientip=&useragent=&latitude=-1&longitude=-1&appType=15&fid=0&objectId="+oid+"&name="+name
    headers = getheaders2()
    headers['Referer'] = referer
    requests.get(referer,headers=headers)
    time.sleep(2)
    if(headers==0):
        return 0
    res=requests.get(url,headers=getheaders2())
    print(res.text)
    if(res.text=="success"):

        if setting["sendkey"]:

            api = 'https://sctapi.ftqq.com/' + setting["sendkey"] + '.send'
            title = u"已为您成功签到"
            content = "签到类型:"+'照片签到/手势签到'+'\n\n用户:' + setting["account"]
            data = {
                "text": title,
                "desp": content
            }
            requests.post(api, data=data)
            print("签到成功，已尝试推送消息到微信" +'\t'+ str(snow_time)+'\n')
            messagebox.showinfo("成功","签到成功，已尝试推送消息到微信")

            # text_pad.insert("签到成功，已尝试推送消息到微信" +'\t'+ str(snow_time)+'\n')

        time.sleep(60)
        return 1
    else:
        return 0
#定位签到
def sign3(referer,aid,uid,lat,long,name,address):
    t=get_time()
    snow_time = datetime.datetime.now().strftime('%Y-%m-%d   %H:%M:%S')


    print("发现定位签到" +'\t'+ str(snow_time)+'\n')
    # text_pad.insert("发现定位签到" +'\t'+ str(snow_time)+'\n')
    name=urllib.parse.quote(name)
    address=urllib.parse.quote(address)
    ani_spider=session.get(referer,headers=getheaders2())
    url="https://mobilelearn.chaoxing.com/pptSign/stuSignajax?name="+name+"&address="+address+"&activeId="+aid+"&uid="+uid+"&clientip=&latitude="+lat+"&longitude="+long+"&latitude_gd="+lat+"&longitude_gd"+long+"&fid=0&appType=15&ifTiJiao=1"
    #url="https://mobilelearn.chaoxing.com/newsign/preSign?courseId=228288159&classId=62734634&activePrimaryId=8000039303851&general=1&sys=1&ls=1&appType=15&uid=150862179&isTeacherViewOpen=0"
    #print('----------------------')
    #print(url)
    headers=getheaders2()
    headers['Referer']=referer
   # print(headers)
    if(headers==0):
        return 0
    time.sleep(2)
    res=requests.get(url,headers=headers)
    #print(headers)
    print(res.text)
    if(res.text=="success"):

        if setting["sendkey"]:

            api = 'https://sctapi.ftqq.com/' + setting["sendkey"] + '.send'
            title = u"已为您成功签到"
            content = "签到类型:"+'定位签到'+'\n\n用户:' + setting["account"]
            data = {
                "text": title,
                "desp": content
            }
            requests.post(api, data=data)
            messagebox.showinfo("成功","签到成功，已尝试推送消息到微信")
            
            # text_pad.insert("签到成功，已尝试推送消息到微信" +'\t'+ str(snow_time)+'\n')
            print("签到成功，已尝试推送消息到微信" +'\t'+ str(snow_time)+'\n')
        time.sleep(60)
        return 1
       
    else:
        return 0
#获取签到类型
def get_sign_type(aid):

    url="https://mobilelearn.chaoxing.com/newsign/signDetail?activePrimaryId="+aid+"&type=1&"
    headers={
      "User-Agent": "Mozilla/5.0 (iPad; CPU OS 13_3_1 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Mobile/15E148 ChaoXingStudy/ChaoXingStudy_3_4.3.2_ios_phone_201911291130_27 (@Kalimdor)_11391565702936108810"
    }
    res=requests.get(url,verify=False)
    d=json.loads(res.text)
    #print(res.text)

    if(d['otherId']==0):
        if(d['ifPhoto']==1):
            return 1
        else:
            return 2
    elif(d['otherId']==2):
        if(d['ifRefreshEwm']==1):
            return 3
        else:
            return 4
    elif(d['otherId']==3):
        return 6
    elif(d['otherId']==4):
        return 5
    elif(d['otherId']==5):
        return 5
    else:
        return 0
#统一签到入口
def sign(referer,aid,uid,name):
    #拍照签到 1 普通签到 2 定位签到 5 手势签到 6 
    activeType=get_sign_type(aid)
    if(activeType==1):#拍照签到
        images=setting['sign']['img']
        #未配置图片
        if(len(images)==0):
            signres=sign2(referer,aid,uid,"",name)
        else:
            nowimg=choices(images)[0]
            signres=sign2(referer,aid,uid,nowimg,name)
    elif(activeType==2):#普通签到
        signres=sign1(referer,aid,uid,name)
    elif(activeType==5):#位置签到
        signres=sign3(referer,aid,uid,setting['sign']['lat'],setting['sign']['long'],name,setting['sign']['address'])
    elif(activeType==6):#手势签到
        signres=sign2(referer,aid,uid,"",name)
    else:
        return -1
    print("签到结果"+str(signres))
    return signres
#获取用户活动列表
def gettask(courseId,classId,uid,cpi,name,sign_common,sign_pic,sign_hand,sign_local):
    time.sleep(2)
    snow_time = datetime.datetime.now().strftime('%Y-%m-%d   %H:%M:%S')

    print()
    text_pad.insert(END,"正在探测" +'\t'+ str(snow_time)+'\n')

    try:
        #url="https://mobilelearn.chaoxing.com/ppt/activeAPI/taskactivelist?courseId="+courseId+"&classId="+classId+"&uid="+uid+"&cpi="+cpi
        url="https://mobilelearn.chaoxing.com/v2/apis/active/student/activelist?fid=0&courseId="+courseId+"&classId="+classId+"&showNotStartedActive=0&_=1663752482576"

        headers=getheaders()
        if(headers==0):
            return 0
        res=requests.get(url,headers=headers)
        #print(f"{name}:{res.text}")
        d=json.loads(res.text)


        if(d['result']==1):
            #data去掉
            activeList=d['data']['activeList']
            # print(activeList)

            count=0
            for active in activeList:
                status=active['status']
                activeType=active['activeType']
                aid=str(active['id'])
                #referer=active['url']
                referer="https://mobilelearn.chaoxing.com/newsign/preSign?courseId="+courseId+"&classId="+classId+"&activePrimaryId="+aid+"&general=1&sys=1&ls=1&appType=15&tid=&uid="+uid+"&ut=s"
                if(status!=1):
                    return 0
                if(activeType==1 and sign_pic=="True"):
                    sign(referer,aid,uid,name)
                if(activeType==2 and sign_common=="True"):
                    sign(referer,aid,uid,name)
                if(activeType==5 and sign_local=="True"):
                    sign(referer,aid,uid,name)
                if(activeType==6 and sign_hand=="True"):
                    sign(referer,aid,uid,name)
                count+=1
                if(count>=setting['other']['count']):
                    break
    except Exception as e:
        print(e)
#获取时间
def get_time():
    today = datetime.datetime.today()
    year = today.year
    month = today.month
    day= today.day
    hour= today.hour
    minute= today.minute
    second= today.second
    if(month<10):
        month="0"+str(month)
    if(day<10):
        day="0"+str(day)   
    date="["+str(year)+"."+str(month)+"."+str(day)+" "+str(hour)+":"+str(minute)+":"+str(second)+"]"
    return date
#初始化Cookies
def init_cookies():
    try:
        with open('cookies.txt','r') as f:
            data=f.read()
            f.close()
            if(len(data)<100):
                return 0
            return data
    except Exception as e:
        return 0
#初始化uid
def init_uid():
    try:
        with open('uid.txt','r') as f:
            data=f.read()
            f.close()
            if(len(data)<5):
                return 0
            return data
    except Exception as e:
        return 0
#初始化img
def init_img():
    print('你没有看错，我不想写了，时间紧迫，完了再更新图片上传')
#保存Cookies文件
def save_cookies(data,type):
    if(type==1):
        with open('cookies.txt','w') as f:
            f.write(data)
            f.close()
    else:
        with open('uid.txt','w') as f:
            f.write(str(data))
            f.close()
#初始化函数
def init2():
    global mycookie,myuid
    if(setting['account']=="" or setting['password']==""):
        print("未进行账号配置")
        return 0
    cookies=init_cookies()
    uid=init_uid()
    if(cookies==0 or uid==0):
        res=login(setting['account'],setting['password'])
        if(res==0):
            print("登录失败，请检查账号密码")
            messagebox.showerror("错误","登录失败，请检查账号密码")

        else:
            save_cookies(mycookie,1)
            getcourse()


    return 1

#初始化函数
def init():
    global mycookie,myuid
    print(setting['account'])
    res=login(setting['account'],setting['password'])
    if(res==0):
            print("登录失败，请检查账号密码")
            messagebox.showerror("错误","登录失败，请检查账号密码")

    else:
        #    save_cookies(mycookie,1)
            getcourse()



    return 1
#检测函数    
def check():
    print(courselist)
    for course in courselist:

        if('roletype' in course['content']):
            roletype=course['content']['roletype']
        else:
            continue
        if(roletype!=3):
            continue

        classId=str(course['content']['id'])
        courseId=str(course['content']['course']['data'][0]['id'])
        cpi=str(course['content']['cpi'])
        
        gettask(courseId,classId,myuid,cpi,setting['sign']['name'],setting['sign']['sign_common'],setting['sign']['sign_pic'],setting['sign']['sign_hand'],setting['sign']['sign_local'])
def starts():



    global quanxian


    print(quanxian)
    if quanxian == True:
        global phone
        global passwordN
        global sendkey
        global passwordN
        global qdname
        global address


        phone =cqoocuser_port.get()
        passwordN = cqoocpassword_port.get()
        sendkey = sendkey_port.get()
        qdname = qdname_port.get()
        address = address_port.get()
        if phone:
            if passwordN:
                if qdname:
                    if address:
                        messagebox.showinfo("提醒","探测程序已启动")
                        with open('./confg.json', 'r', encoding='utf-8') as f:
                            json_data = json.loads(f.read())
                        f.close   
                        json_data["account"] =  str(phone) 
                        json_data["password"] =  str(passwordN)                   
                        json_data["sendkey"] =  str(sendkey)                   
                        json_data["sign"]["name"] = str(qdname)                    
                        json_data["sign"]["address"] =str(address)                     

                        with open('./confg.json', 'w', encoding='utf-8') as f:
                            json.dump(json_data,f)
                        f.close
                        res=init()
                        datetime1=datetime.datetime
                        if(res==1):
                        
                            # text_pad.insert('初始化完成 \n')
                            #课程开始时间 自行修改
                            startTime=datetime1.strptime("00:00", "%H:%M")- datetime1.strptime('0:0', "%H:%M")
                            #课程结束时间 自行修改
                            endTime=datetime1.strptime("22:30", "%H:%M")- datetime1.strptime('0:0', "%H:%M")
                            while True:

                                now = datetime1.now()
                                Time = now.strftime("%H:%M")
                                Time = datetime1.strptime(Time, "%H:%M") - datetime1.strptime('0:0', "%H:%M")
                                if(endTime>Time>startTime):
                                    check()

                                #print(f"{endTime>Time>startTime}")
                                    time.sleep(setting['other']['sleep'])
                                else:
                                    time.sleep(15)
                    else:
                        messagebox.showerror("错误","签到时的地址")

                else:
                    messagebox.showerror("错误","签到时的昵称")

            else:
                messagebox.showerror("错误","请填写密码")


        else:
            messagebox.showerror("错误","请填写手机号")        

    else:
        messagebox.showerror("错误","请填写秘钥")

# def thread_it(func,*atgs):
#     t = threading.Thread(target = func , args =args)
#     t.setDaemon(True)
#     t.start()

root.mainloop()




