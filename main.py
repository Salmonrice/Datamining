from flask import Flask , render_template
from flask import request
from Class import Output

app = Flask(__name__)
app.config['SECRET_KEY'] = 'you-will-never-guess'


@app.route('/')
def index():
    return render_template('base.html')

@app.route('/input', methods = ['GET','POST'])
def input():
    if request.method == 'POST':
        output = Output(request.form.get('friend'),
                        request.form.get('price'),
                        request.form.get('utilization'),
                        request.form.get('exclusive'),
                        request.form.get('cheaper'),
                        request.form.get('anticheat'),
                        request.form.get('problem'),
                        request.form.get('longterm'),
                        request.form.get('service'),
                        request.form.get('spend'),
                        request.form.get('gender'),
                        request.form.get('year'))
        output.train()
        output.pred()
        print('output')
        return render_template('output.html' , output=output)
    return render_template('inputform.html')


if __name__ == '__main__':
    app.debug = True
    app.run(host='0.0.0.0',port=8000)

'''
request.form.get('friend')
request.form.get('utilization')
request.form.get('exclusive')
request.form.get('cheaper')
request.form.get('anticheat')
request.form.get('problem')
request.form.get('longterm')
request.form.get('service')
request.form.get('spend')
request.form.get('gender')

'''
