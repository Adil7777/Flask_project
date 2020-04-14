import smtplib
from config import EMAIL, PASSWORD
from logins import EMAILS


def send_email(send_to_email):
    password = EMAILS[send_to_email]
    mes = "Forget your password?\nIt is {}\nDon't forget again".format(str(password.split(':')[1]))
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    server.ehlo()
    server.login(EMAIL, PASSWORD)

    server.sendmail(EMAIL, send_to_email, mes)
    server.quit()

