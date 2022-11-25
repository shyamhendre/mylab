import subprocess
import sys

from flask import Flask, jsonify,request


# run flask --app test1 run
#https://auth0.com/blog/developing-restful-apis-with-python-and-flask/


app = Flask(__name__)

@app.route('/')
def index():
    return "hello"
@app.route('/admin',methods=['POST','GET','PUT'])
def checkAccess():

    #http://127.0.0.1:5000/admin?username=test&sharepath=\\DESKTOP-JF1BDNA\shyam

    #Invoke-RestMethod -Uri "http://127.0.0.1:5000/admin?username='test'&sharepath='\\DESKTOP-JF1BDNA\shyam'"

    p = subprocess.Popen(["powershell.exe","Get-NTFSEffectiveAccess",request.args.get('sharepath'),request.args.get('username'),"| Select-object accessrights | ForEach-Object {$_.accessrights} | out-file c:\\temp\\result.txt -Encoding ascii"])
    #p.communicate()
    p.wait()
    log = open("c:\\temp\\result.txt", "r").read()
    return log

if __name__=="__main__":
    app.run(port=5000,debug=True)



