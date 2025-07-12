import smtplib
from email.message import EmailMessage

#https://docs.python.org/3/library/email.examples.html
class MyMailerClass:
    def __init__(self, Host, Port):
        self.Host = Host
        self.Port = Port
        self.RecipientList = []
        self.CCList = []
        self.BCCList = []
        self.AttachmentList = []

    def setFrom(self, FromEmail):
        self.FromEmail = FromEmail

    def setTo(self, ToEmail):
        self.ToEmail = ToEmail

    def setUser(self, User, Password):
        self.User = User
        self.Password = Password

    def addRecipient(self, email):
        self.RecipientList.append(email)

    def addCC(self, email):
        self.CCList.append(email)

    def addBCC(self, email):
        self.BCCList.append(email)

    def setSubject(self, Subject):
        self.Subject = Subject

    def setBody(self, Body):
        self.Body = Body

    def addAttachment(self, filename, maintype, subtype):
        attachment = {"filename": filename,
                      "maintype": maintype, "subtype": subtype}
        self.AttachmentList.append(attachment)

    def sendMail(self):
        msg = EmailMessage()
        msg['Subject'] = self.Subject
        msg['From'] = self.FromEmail
        msg['To'] = ', '.join(self.RecipientList)
        msg['cc'] = ', '.join(self.CCList)
        msg['Bcc'] = ', '.join(self.BCCList)
        msg.set_content(self.Body, subtype='html')

        for attachment in self.AttachmentList:
            with open(attachment['filename'], 'rb') as file:
                data = file.read()
                file_name = file.name
            msg.add_attachment(
                data, maintype=attachment['maintype'], subtype=attachment['subtype'], filename=file_name)

        with smtplib.SMTP(self.Host, self.Port) as s:
            s.starttls()
            s.ehlo()
            s.login(self.User, self.Password)

            s.send_message(msg)
            s.quit()
