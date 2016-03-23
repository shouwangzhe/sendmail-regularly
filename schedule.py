#coding:utf8
import sys
reload(sys)
sys.setdefaultencoding('utf-8')
import time
import os
from datetime import datetime, timedelta
from sendmail import SendMail
SECONDS_PER_DAY = 24 * 60 * 60
def func_to_do():
    print "do Function..."
    #os.system("python d:/auto_test_multithread.py")
    SendMail('mymail@eversec.cn','password',['mymail@qq.com','mymail@eversec.cn'],'smtp.263.net','25','This is the title','<b><i>我的</i>测试</b>邮件',['H:\\test.txt','H:\\test.txt'],['111.txt','222.txt'])

def Schedule(deshour,desminute,sleepseconds=SECONDS_PER_DAY):
    curTime = datetime.now()
    desTime = curTime.replace(hour=deshour, minute=desminute, second=00, microsecond=0)
    delta = curTime - desTime
    skipSeconds = (sleepseconds - delta.total_seconds())%sleepseconds
    print "Must sleep %d seconds" % skipSeconds
    time.sleep(skipSeconds)
    func_to_do()
    time.sleep(1)
    
if __name__=='__main__':
    print datetime.now()
    while True:
        Schedule(22,4)
