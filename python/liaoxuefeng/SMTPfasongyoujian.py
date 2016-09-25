from email.mime.text import MIMEText
#第一个参数是邮件正文，第二个参数是MIME的subtype，传‘plain’表示纯文本最终就是‘text/plain’，最后是编码方式

msg=MIMEText('hello,send by Python...','plain','utf-8')
#输入Email地址和口令：
from_addr=input('From:')
password=input('Password:')
#输入收件人地址：
to_addr=input('To:')
#输入SMTP服务器地址：
smtp_server=input('SMTP server:')

import smtplib
server=smtplib.SMTP(smtp_server,25)#STMP协议默认端口是25
server.set_debuglevel(1)
server.login(from_addr,password)
server.sendmail(from_addr,[to_addr],msg.as_string())
server.quit()
