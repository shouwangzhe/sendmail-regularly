#coding:utf8
import sys
reload(sys)
sys.setdefaultencoding('utf-8')
import time
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

def make_attachment(file,name):
    att = MIMEText(open(file, 'rb').read(), 'base64', 'gb2312')
    att["Content-Type"] = 'application/octet-stream'
    att["Content-Disposition"] = 'attachment; filename="%s"' %name
    return att
def SendMail(mymail,mypassword,sendlist,mailhost,hostport,mail_title,mail_body,attachment_list,attachment_name):
    try:
        mail_from=mymail
        mail_to=sendlist

        msg = MIMEMultipart()
        msg['Subject']=mail_title #mail title
        msg['From']=mail_from
        msg['To']=';'.join(mail_to)
        msg['date']=time.strftime('%a, %d %b %Y %H:%M:%S %z')

        msgContent = MIMEText(mail_body,'html','utf-8')#mail body
        msg.attach(msgContent)
        attachment_len=len(attachment_list)
        for i in range(attachment_len):
            att=make_attachment(attachment_list[i],attachment_name[i]) #构造附件
            msg.attach(att) #添加附件到邮件

        smtp=smtplib.SMTP()


        smtp.connect(mailhost,hostport)
        smtp.login(mymail,mypassword)
        smtp.sendmail(mail_from,mail_to,msg.as_string())
        smtp.quit()
        print 'You have send it!'
    except:
        print 'failed to send email'
if __name__=='__main__':
    #example
    SendMail('lvpengbin@163.com','mypassword',['mymail@qq.com','mymail@163.com'],'smtp.263.net','25','This is my title','<b><i>我的</i>测试</b>邮件',['H:\\test.txt','H:\\test.txt'],['111.txt','222.txt'])