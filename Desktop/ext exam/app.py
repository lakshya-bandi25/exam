from flask import Flask,render_template,request
app=Flask(__name__)
@app.route('/')
def index():
    return render_template("form.html")
@app.route('/submit',methods=['POST'])
def submit():
    name=request.form['username']
    roll=request.form['rollno']
    mail=request.form['email']
    yr=request.form['year']
    return render_template("result.html,name=username,mail=email,roll=rollno,yr=year")
if __name__=="__main__" :
    app.run(debug=True)
    