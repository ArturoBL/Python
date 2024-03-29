import smtplib
from email.message import EmailMessage

emails = ['email1@hotmail.com','email2@gmail.com']

msg = EmailMessage()
msg['Subject'] = 'prueba multi mail'
msg['From'] = 'emailfrom@gmail.com'
msg['To'] = ', '.join(emails)
#msg.preamble = 'You will not see this in a MIME-aware mail reader.\n'
body = '''
<!DOCTYPE html>
    <html>
    <head>
        <link rel="stylesheet" type="text/css" hs-webfonts="true" href="https://fonts.googleapis.com/css?family=Lato|Lato:i,b,bi">
        <meta http-equiv="Content-Type" content="text/html; charset=UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <style type="text/css">
          h1{font-size:56px}
          h2{font-size:28px;font-weight:900}
          p{font-weight:100}
          td{vertical-align:top}
          #email{margin:auto;width:600px;background-color:#fff}
        </style>
    </head>
    <body bgcolor="#F5F8FA" style="width: 100%; font-family:Lato, sans-serif; font-size:18px;">
    <div id="email">
        <table role="presentation" width="100%">
            <tr>
                <td bgcolor="#00A4BD" align="center" style="color: white;">
                    <h1> Welcome!</h1>
                </td>
        </table>
        <table role="presentation" border="0" cellpadding="0" cellspacing="10px" style="padding: 30px 30px 30px 60px;">
            <tr>
                <td>
                    <h2>Custom stylized email</h2>
                    <p>
                        You can add HTML/CSS code here to stylize your emails.
                    </p>
                </td>
            </tr>
        </table>
    </div>
    </body>
    </html>
'''
msg.set_content(body, subtype='html')


with open('python.jpg', 'rb') as file:
   imgjpg = file.read()
msg.add_attachment(imgjpg, maintype='image',
                       subtype='jpeg')


with smtplib.SMTP('smtphost', 587) as s:
    s.starttls()    
    s.ehlo()
    s.login("emailuser", "emailpassword")

    s.send_message(msg)
    s.quit()