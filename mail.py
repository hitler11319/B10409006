import smtplib
import mimetypes
from email.mime.multipart import MIMEMultipart
from email import encoders
from email.message import Message
from email.mime.audio import MIMEAudio
from email.mime.base import MIMEBase
from email.mime.image import MIMEImage
from email.mime.text import MIMEText

# --- Email 的收件人與寄件人address ---
emailfrom = "someone@company.com" 
emailto = "someone@company.com" 
# # --- Email 附件檔案 Attachment ----------- 
fileToSend = "test.csv" 
username = "user" # --- 寄信的SMTP的帳號---- 
password = "pass" # --- 寄信的SMTP的密碼---- 

msg = MIMEMultipart() 
msg["From"] = emailfrom 
msg["To"] = emailto 
# --- Email 的主旨 Subject ---
msg["Subject"] = "Test for Python" 
msg["preamble"] = 'You will not see this in a MIME-aware mail reader.\n' 

#----- Email 的信件內容 Message ----- 
part = MIMEText(u"body text including an Euro char \u20ac\n 中文測試\n ", _charset="UTF-8") 

msg.attach(part) 
#----- Test for Text Message ----- 

ctype, encoding = mimetypes.guess_type(fileToSend)
if ctype is None or encoding is not None:
    ctype = "application/octet-stream"
maintype, subtype = ctype.split("/", 1)

if maintype == "text":
    fp = open(fileToSend)
    attachment = MIMEText(fp.read(), _subtype=subtype)
    fp.close()
elif maintype == "image":
    fp = open(fileToSend, "rb")
    attachment = MIMEImage(fp.read(), _subtype=subtype)
    fp.close()
elif maintype == "audio":
    fp = open(fileToSend, "rb")
    attachment = MIMEAudio(fp.read(), _subtype=subtype)
    fp.close()
else:
    fp = open(fileToSend, "rb")
    attachment = MIMEBase(maintype, subtype)
    attachment.set_payload(fp.read())
    fp.close()
    encoders.encode_base64(attachment)
    attachment.add_header("Content-Disposition", "attachment", filename=fileToSend)
    msg.attach(attachment)


# --- 寄件的 SMTP mail server --- 
server = smtplib.SMTP('smtp.company.com', 25) 
# --- 如果是 Gmail 可使用這行 ---
# server = smtplib.SMTP('smtp.gmail.com', 587) 
server.ehlo()
server.starttls()
# --- 如果SMTP server 不需要登入則可把 server.login 用 # mark 掉
server.login(username,password)
server.sendmail(emailfrom, emailto, msg.as_string())
server.quit()