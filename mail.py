import os
import sys
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.mime.application import MIMEApplication

# to_from
to_email = sys.argv [1]
from_email = sys.argv [2]

# message
subject = sys.argv [3]
body = sys.argv [4]

args = sys.argv
filepath = ""

# file
if len(args) == 6:
        filepath = sys.argv [5]
        filename = os.path.basename(filepath)

pre_list = sys.argv[1]
list = pre_list.split(',')

for user in list:
        msg = MIMEMultipart()
        msg["Subject"] = subject
        msg["To"] = user
        msg["From"] = from_email
        msg.attach(MIMEText(body))

        if filepath != "":
                with open(filepath, "rb") as f:
                        atfile = MIMEApplication(f.read())
                atfile.add_header("Content-Disposition", "attachment", filename=filename)
                msg.attach(atfile)
        else:
                pass

        # mail_server
        server = smtplib.SMTP("localhost", 25)

        # sent
        server.send_message(msg)

# close
server.quit()
