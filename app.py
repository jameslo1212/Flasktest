from flask import Flask, render_template

app = Flask(__name__)


@app.route('/', methods=['GET'])
def index():
    return render_template('index.html')


@app.route('/hello')
@app.route('/hello/<name>')
def hello(name='Nobody'):
    return f'hello:{name} '

@app.route('/hi')
@app.route('/hi/<name>')
def hi(name='Nobody'):
    list=['python','java','C++']
    return render_template('hi.html',name=name,list=list)


if __name__ == "__main__":
    app.run()
