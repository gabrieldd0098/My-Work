import smtplib
import datetime as dt

SENDER_EMAIL = "gabrieldd98@yahoo.com"
SENDER_PASS = "freakiii"

with smtplib.SMTP(host="smtp.mail.yahoo.com", port=587) as connection: #or 465
    connection.starttls()
    connection.login(user=SENDER_EMAIL, password=SENDER_PASS)
    connection.sendmail(from_addr=SENDER_EMAIL,
                        to_addrs=SENDER_EMAIL,
                        msg="Subject: IDLB\n\nI dont love boosters")

when = dt.datetime.now()
print(when)
print(when.weekday())
