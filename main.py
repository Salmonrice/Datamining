from flask import Flask , render_template
from forms import InputForm
from flask import request

app = Flask(__name__)
app.config['SECRET_KEY'] = 'you-will-never-guess'


@app.route('/')
def index():
    return render_template('base.html')


@app.route('/input', methods = ['GET','POST'])
def input():
    if request.method == 'POST':
        output = Output(request.form.get('friend'),
                        request.form.get('utilization'),
                        request.form.get('exclusive'),
                        request.form.get('cheaper'),
                        request.form.get('anticheat'),
                        request.form.get('problem'),
                        request.form.get('longterm'),
                        request.form.get('service'),
                        request.form.get('spend'),
                        request.form.get('gender')),
        output.pred()
        return render_template('inputform.html' , output=output)
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

'''
class Output():
    def __init__(self):

    def setup(self, friend , utilization , exclusive , cheaper , anticheat , problem , longterm , service , spend , gender):
        self.friend = friend
        self.utilization = utilization
        self.exclusive = exclusive
        self.cheaper = cheaper
        self.anticheat = anticheat
        self.problem = problem
        self.longterm = longterm
        self.service = service
        self.spend = spend
        self.gender = gender


'''
