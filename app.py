import json
from flask import Flask, render_template, request, jsonify   

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("InputOutput.html")        

@app.route("/submitJSON", methods=["POST"])
def processJSON(): 
	jsonStr = request.get_json()
	jsonObj = json.loads(jsonStr)

	l=eval(jsonObj['a'])

	m = max(l)
	

	d={}
	for i in range (1,m+1):
		d[i]=0
		
		
  
	for k in l:
		for j in range(1,m+1):
			if k%j==0:
				d[j]=d[j]+1
				
				
	response="<b> Output: "+str(d)+".</b><br>"
	return response

if __name__ == "__main__":
	app.run()
    
