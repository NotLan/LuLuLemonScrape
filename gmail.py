import smtplib
import ssl


def send_mail():
    ctx = ssl.create_default_context()
    password = "tjpzeyccwnwhpdum"    # Your app password goes here
    sender = "alertslulu@gmail.com"    # Your e-mail address
    receiver = "ian.allheim@gmail.com"  # Recipient's address
    message = """
    The Lulu lemon bags are back in stock!!!!!! 
    \n https://shop.lululemon.com/p/bags/Everywhere-Belt-Bag/_/prod8900747?color=23315&sz=ONESIZE
    """

    with smtplib.SMTP_SSL("smtp.gmail.com", port=465, context=ctx) as server:
        server.login(sender, password)
        server.sendmail(sender, receiver, message)