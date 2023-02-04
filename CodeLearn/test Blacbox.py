# send email to khoi0941@gmail.com?
server = smtplib.SMTP('smtp.gmail.com:587')
server.ehlo()
server.starttls()


msg = "\r\n".join([
  "From: user_me@gmail.com",
  "To: user_you@gmail.com",
  "Subject: Just a message",
  "",
  "Why, oh why"
  ])




#Source: https://stackoverflow.com/questions/10147455


