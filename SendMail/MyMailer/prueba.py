from MyMailer import MyMailerClass
from SecretKey import email_user, email_password, from_address, to_address, Host, Port

mailer = MyMailerClass(Host, Port)

mailer.setFrom(from_address)


mailer.addRecipient(to_address)

mailer.setSubject(f"Prueba de envío Python")
mailer.setUser(email_user, email_password)

mailer.setBody(
    f"<html><body><p><strong>La prueba ha sido satisfactoria</strong></p></body></html>")

mailer.sendMail()
