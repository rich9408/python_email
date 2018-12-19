import smtplib 
from email.message import EmailMessage

# import getpass
# password = getpass.getpass('비밀번호뭐니?')

email_list = ['fun3440@naver.com', 'yud02150@gmail.com']

for email in email_list:
    msg = EmailMessage()
    msg['Subject'] = "안녕하세요 저는 서희수입니다!!"
    msg['From'] = "seoheesu81@naver.com"
    msg['To'] = email 
    msg.set_content(email + '에게 메일을 보냈습니다!!')

smtp_url = 'smtp.naver.com'
smtp_port = 465

s = smtplib.SMTP_SSL(smtp_url, smtp_port)

s.login('seoheesu81','GMLTN6257')
s.send_message(msg)