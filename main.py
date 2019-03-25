import yagmail
import os
import json

user = 'your email here'
password = 'your password here'

yag = yagmail.SMTP(user, password)
subject = 'Subject'

with open('template.txt') as f:
    template = f.read()

with open('email_list.json') as f:
    email_list = json.load(f)

for name in email_list:
    email = email_list[name]
    txt = template.format(name, email)
    yag.send(email, subject, txt)
