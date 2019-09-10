finalList = str(JobList)
sender = 'lwardle@unca.edu'
receivers = 'lwardle@unca.edu'
body_of_email = 'Heres your message homie:'+finalList+''
msg = MIMEText(body_of_email, 'html')
msg['Subject'] = 'New Job Updates'
msg['From'] = sender
msg['To'] = receivers

s = smtplib.SMTP_SSL(host = 'smtp.gmail.com', port = 465)
s.login(user = 'lwardle@unca.edu', password = 'Evaricky0')
s.sendmail(sender, receivers, msg.as_string())
s.quit()
