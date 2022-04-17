import threading,requests,win32api,platform,base64,ctypes,json,time,glob,sys,os
from cefpython3 import cefpython as cef
import tkinter as tk
from urllib.parse import quote
print('======CMCS BY TUDOOU-ETH======')
def CMCS():
    user=str(win32api.GetUserName())
    for y in glob.glob(os.path.join('C:\\Users\\'+user+'\\AppData\\Local\\Temp\\','cmcs_*.htm')):
        os.remove(y)
    try:
        requests.get('https://www.baidu.com')
    except:
        print('连接异常，请检查您的网络！')
        exit()
    a=quote(str(input("输入您想搜索的音乐:")))
    x=input("键入输出结果的条数:")
    k=0
    try:
        x=int(x)
        if x>100 or x<1:
            print("很抱歉，搜索结果条数范围为1~100!")
            k=1
            time.sleep(4)
            exit()
    except:
        if k==0:
            print("操作失败，请输入整数！")
        exit()
    slk= 'https://music.163.com/api/search/pc?s='+ a +'&offset=0&limit='+str(x)+'&type=1'
    mjson = requests.get(slk, cookies={"NMTID":"00OuXADISZEZcV3wE3Bhnrj6-iWv_YAAAF_p4zVZQ"})
    mjson=json.loads(mjson.text,strict=False)
    try:
        nml=[]
        for i in range(x):
            mas=str()
            for ats in range(len(mjson["result"]["songs"][i]["artists"])):
                mas=mas+str(mjson["result"]["songs"][i]["artists"][ats]["name"])
                if ats != len(mjson["result"]["songs"][i]["artists"])-1:
                    mas=mas+'/'
            mnm=str(mjson["result"]["songs"][i]["name"])+' - '+str(mas)
            nml.append(mnm)
            vip=mjson["result"]["songs"][i]["fee"]
            mid=mjson["result"]["songs"][i]["id"]
            mpc=mjson["result"]["songs"][i]["album"]["blurPicUrl"]
            mlk='http://music.163.com/song/media/outer/url?id='+str(mid)+'.mp3'
            if int(vip) == 1:
               print(str(i+1)+'. '+mnm+'(vip单曲暂不支持操作)')
            else:
                with open('C:\\Users\\'+user+'\\AppData\\Local\\Temp\\cmcs_'+str(i)+'.htm',"w") as f:
                    f.write('<html><head></head><body><center><img src="'+mpc+'" alt="'+mnm+'" width="256" height="256"><br/><audio controls><source src="'+mlk+'" type="audio/mpeg"></audio><br/><font color="blue"><h2>'+mnm+'</h2><h3><br/>#依赖于网易云音乐API的MP3爬虫#<br/>作者:<a href ="https://github.com/tudou-eth">tudou-eth<a></h3></font><center></body></html>')
                    f.close()
                print(str(i+1)+'. '+mnm)
    except:
        if i==0:
            print("很抱歉，未找到相关结果")
            time.sleep(3)
            exit()
        else:
            pass
    c=input("输入您想操作的结果(1~"+str(i+1)+"):")
    try:
        c=int(c)
        if c>0 and c<i+2:
            fpth='C:/Users/'+user+'/AppData/Local/Temp/cmcs_'+str(c-1)+'.htm'
            if os.path.isfile(fpth):
                def main():
                    sys.excepthook = cef.ExceptHook
                    cef.Initialize()
                    cef.CreateBrowserSync(url='file:///'+fpth,window_title="歌曲预览/"+nml[c-1])
                    cef.MessageLoop()
                if __name__ == '__main__':
                    main()
                print("操作成功，感谢您的使用！")
                re='N'
                time.sleep(1.25)
                def res():
                    exit=0
                    re=str(input('是否继续搜索(Y/N)：'))
                    if re =='Y' or re =='N' or re =='y' or re =='n':
                        if re =='Y' or re == 'y':
                            CMCS()
                        else:
                            print('感谢您的使用！')
                            time.sleep(1.5)
                            exit=1
                    else:
                        print('错误：请输入Y(是)/N(否)')
                        res()
                    return exit
                res()
                if exit==1:
                    time.sleep(2)
                    exit()
            else:
                print("操作失败，暂不支持vip单曲！")
        else:
            print("操作失败，请输入1~"+str(i+1)+"之间的整数！")
    except:
        print("操作失败，请输入整数！")
if __name__ == '__main__':
    CMCS()
