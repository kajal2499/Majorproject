import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
file= open("/ml/accuracy.txt", "r")
acc=float(file.read())
acc*=100
file.close()
host_address = "kajalgayakwad99@gmail.com"
host_pass = "ycdqqcrztgfnbdid"
guest_address = "clanofking001@gmail.com"
subject = "Regarding Success of your model "
content = '''Dear Admin, 
				Your trained model has given best accuracy .
				Check your OS your accuracy is: '''+str(acc)+ '''
			-Jenkins'''
message = MIMEMultipart()
message['From'] = host_address
message['To'] = guest_address
message['Subject'] = subject
message.attach(MIMEText(content, 'plain'))
session = smtplib.SMTP('smtp.gmail.com', 587)
session.starttls()
session.login(host_address, host_pass)
text = message.as_string()
session.sendmail(host_address, guest_address  , text)
session.quit()
print('Successfully sent your mail')
