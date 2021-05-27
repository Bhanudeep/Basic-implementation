from flask import Flask, request, render_template , Response,url_for
import os,math, random,smtplib, ssl
from datetime import datetime,date
app = Flask(__name__)   
def mail():
   string = '0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'
   OTP = ""
   length = len(string)
   for i in range(6) :
      OTP += string[math.floor(random.random() * length)]
   now = datetime.now()
   time=str(now.strftime("%I:%M %p"))
   content = '\nHello, otp for verification is '+OTP 
   username = "email_id"
   password = "password"
   sender = "name"
   recipient = "recvr email"
   mail = smtplib.SMTP("smtp.gmail.com",587)
   mail.ehlo() 
   mail.starttls() 
   mail.ehlo()
   mail.login(username,password)
   header = 'To:' + recipient + '\n' + 'From:' + sender + '\n' + 'Subject: Verification code \n'
   content = header+content
   mail.sendmail(sender,recipient,content)
   mail.close
@app.route('/', methods =["GET", "POST"])
def index():
   return render_template("main.html")

@app.route('/autlog')
def autlog():
   if request.method == 'POST':
      return redirect(url_for('main'))
   return render_template('autlog.html')

@app.route('/log')
def log():
   if request.method == 'POST':
      return redirect(url_for('main'))
   return render_template('login.html')

@app.route('/loginfu')
def loginfu():
   if request.method == 'POST':
      return redirect(url_for('login'))
   return render_template('home.html')

@app.route('/logoutfu')
def logoutfu():
   if request.method == 'POST':
      return redirect(url_for('home'))
   return render_template('login.html')

@app.route('/signin')
def signin():
   if request.method == 'POST':
      return redirect(url_for('login'))
   return render_template('signup.html')

@app.route('/goback')
def goback():
   if request.method == 'POST':
      return redirect(url_for('signup'))
   return render_template('main.html')

@app.route('/report')
def report():
   mail()
   if request.method == 'POST':
      return redirect(url_for('autlog'))
   return render_template('report.html')

@app.route('/crime')
def crime():
   if request.method == 'POST':
      return redirect(url_for('report'))
   return render_template('crime.html')

@app.route('/submit', methods =["GET", "POST"])
def submit():
   if request.method == "POST":
      content = request.form.get("content")
      print(content)
      file1 = open("contents.txt","w")
      file1.write(content)
      file1.close()
      # getting input with name = lname in HTML form 
      #last_name = request.form.get("lname") 
      #return redirect(url_for('home'))
   return render_template("home.html")

@app.route('/gg')
def gg():
   
   f = open("contents.txt", "r")
   message=f.read()
   if request.method == 'POST':
      return redirect(url_for('crime'))
   return render_template('crime.html',mes=message)

if __name__=='__main__':
   app.run(host="your network ip",port="8000",use_reloader=True,debug=True)