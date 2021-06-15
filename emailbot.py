import smtplib
import sys
import subprocess
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email import encoders
from email.mime.application import MIMEApplication #Used for attachments

# sys.path.append('C:\Users\win 10\PycharmProjects\gtp-2-fine-tuned\gpt-2-finetuning\src')
proc = subprocess.Popen('python generate_unconditional_samples.py',
                        cwd="C:/Users/win 10/PycharmProjects/gtp-2-fine-tuned/gpt-2-finetuning/src", shell=True,
                        stdout=subprocess.PIPE, )
output = proc.communicate()[0]

print(output)
msg = output.decode("utf-8")
message = MIMEMultipart()
#message = message.as_string()

#messagedone = 'Subject: {}\n\n{}'.format("Attention", msg + "\n" + message)


part1 = MIMEText(msg, 'plain')
part2 = MIMEText(u'<br> <p>To take action: </p><a href="https://www.hackoff.nl/">Clik here</a>', 'html')

message.attach(part1)
message.attach(part2)
message['Subject'] = 'Attention'
receivers = ['steen380@gmail.com']
#'steen380@gmail.com'
server = smtplib.SMTP('smtp.gmail.com', 587)
server.starttls()
server.login('emailbot014@gmail.com', 'Emailbot14!')
for receiver in receivers:
    #email = EmailMessage()
    #email['From'] = 'emailbot014@gmail.com'
    #email['To'] = receiver
    #email['Subject'] = 'Attention'
    #email.set_content(msg)
    #server.send_message(email)
    server.sendmail('emailbot014@gmail.com', receiver, message.as_string())
