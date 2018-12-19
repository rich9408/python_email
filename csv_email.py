import csv
import smtplib 
from email.message import EmailMessage

f = open('pygj.csv', 'r', encoding='utf-8')
read_csv = csv.reader(f)
smtp_url = 'smtp.naver.com'
smtp_port = 465
s = smtplib.SMTP_SSL(smtp_url, smtp_port)
s.login('seoheesu81@naver.com','GMLTN6257')

for line in read_csv:
    email = line[1]
    msg = EmailMessage()
    msg['Subject'] = "안녕하세요 저는 서희수입니다!!"
    msg['From'] = 'seoheesu81@naver.com'
    msg['To'] = email
    msg.set_content(line[0] + '에게 메일을 보냈습니다!!')
    print(line[0]+ email)
    s.send_message(msg)
    

f.close()