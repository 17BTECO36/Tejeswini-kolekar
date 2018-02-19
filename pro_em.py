import smtplib
 
# creates SMTP session
s = smtplib.SMTP('smtp.gmail.com', 587)
 
# start TLS for security
s.starttls()
 
# Authentication
s.login("tejeswini13kolekar@gmail.com", "7769766")
 
# message to be sent
message = "hi"
 
# sending the mail
s.sendmail("tejeswini13kolekar@gmail.com", "tejeswini13kolekar@gmail.com", message)
 
# terminating the session
s.quit()
