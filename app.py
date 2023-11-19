from flask import Flask, render_template, request
from text_summary import summarizer

app=Flask(__name__)

@app.route('/')
def index():
    return render_template("index.html")


@app.route('/analyze', methods=['GET','POST'])
def new():
    if request.method=='POST':
        rawtext=request.form['rawtext']
        summary,originaltext,len_o,len_s=summarizer(rawtext)

        return render_template('summary.html',summary=summary,originaltext=originaltext,len_o=len_o,len_s=len_s)

if __name__ == '__main__':
    app.run(debug=False,host='0.0.0.0')