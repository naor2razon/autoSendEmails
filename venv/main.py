import smtplib


def send_mail():
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    server.ehlo()

    # with open('password.txt', 'r') as x:
    #   password = x.read()
    server.login('dailen.ronel@extraale.com', 'wuyaa7S&')

    subject = "Good morning Bek Brace!"
    #with open('body.txt', 'r') as n:
    #    body = n.read()
    body = " Let us recreate Tanks shooter game with Pygame!"
    msg = f"subject: {subject} \n\n\n {body}"

    server.sendmail(
        'dailen.ronel@extraale.com',
        'dailen.ronel@extraale.com',
        msg
    )
    print('Message is sent succesfully!')


if __name__ == "__main__":
    send_mail()
