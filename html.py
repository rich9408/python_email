import smtplib 
from email.message import EmailMessage

import getpass
password = getpass.getpass('비밀번호뭐니?')

msg = EmailMessage()
msg['Subject'] = "안녕하세요 저는 서희수입니다!!"
msg['From'] = "seoheesu81@naver.com"
msg['To'] = "seoheesu81@naver.com" 
# msg.set_content('에게 메일을 보냈습니다!!')
msg.add_alternative('''
<h1>안녕하세요!!</h1>
<p>저는 서희수입니다.</p>
''', subtype="html")

smtp_url = 'smtp.naver.com'
smtp_port = 465

s = smtplib.SMTP_SSL(smtp_url, smtp_port)

s.login('seoheesu81',password)
s.send_message(msg)