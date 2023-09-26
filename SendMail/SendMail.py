import smtplib
from email.mime.text import MIMEText


def send_mail(host, port, user, password, from_email, to_email, emails, subject, body, htmltype = False,files = None):
    mailServer = smtplib.SMTP(host, port)
    mailServer.starttls()
    mailServer.ehlo()
    mailServer.login(user, password)
    msg = MIMEMultipart()
    msg['From'] = from_email
    msg['To'] = to_email
    msg['Date'] = formatdate(localtime=True)
    msg['Subject'] = subject
        
    if htmltype:
        msg.attach(MIMEText(body, 'html'))
    else:
        msg.attach(MIMEText(body, 'plain'))
    #msg.attach(MIMEText(text, 'plain'))
    
    #msg.attach(MIMEText(body))
    for f in files or []:
        with open(f, "rb") as fil:
            part = MIMEApplication(
                fil.read(),
                Name=basename(f)
            )
        # After the file is closed
        part['Content-Disposition'] = 'attachment; filename="%s"' % basename(f)
        msg.attach(part)
    mailServer.sendmail(msg['From'], emails, msg.as_string())
    mailServer.quit()
