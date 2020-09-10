import pandas as pd
from PIL import Image, ImageDraw,ImageFont
import smtplib
import imghdr
from email.message import EmailMessage

def create_certificate(name):
    im = Image.open("certificate.jpg")
    draw = ImageDraw.Draw(im)
    draw.text((170,150),name,"blue",font=ImageFont.truetype("arial.ttf",35))
    im.save('certi\\'+name+'.jpg')


def send(to,name):
    email_user = 'vendu.doll@gmail.com'
    message = EmailMessage()
    message['subject']='IEEE XYZ Webinar'
    message['from'] = email_user
    message['to']= to
    html_message =open('message.html').read()
    message.add_alternative(html_message, subtype='html')

    with open('certi\\'+name+'.jpg','rb') as attach_file:
        image_name = attach_file.name
        image_type = imghdr.what(attach_file)
        image_data = attach_file.read()
    message.add_attachment(image_data, maintype='image', subtype=image_type, filename =name+'.png')
    with smtplib.SMTP_SSL("smtp.gmail.com",465) as smtp:
        smtp.login(email_user,"*passward")
        smtp.send_message(message)


def n_c_c():
    df = pd.read_csv("cont.csv",header=None)
    for i  in range(len(df)):
        name = df.iloc[i,0]
        email = df.iloc[i,1]
        create_certificate(name)
        send(email,name)



n_c_c()