from flask import Flask, render_template, request
app = Flask(__name__)

@app.route('/')
def index():
    return render_template('01_bootstrap.html')

@app.route('/typo')  ## localhost:5000/typo   ## 크롬에 http://127.0.0.1:5000/typo 입력하면 03_typography.html가 나오게 됨
def typo():
    return render_template('03_typography.html')

@app.route('/iris', methods = ['GET','POST'])
def iris():
    if request.method == 'GET':
        return render_template('iris.html')
    else:
        slen = float(request.form['slen']) * 2  # 입력된 값의 두배  # 타입은 스트링으로 들어옴 -> 바꿔줘야함
        plen = float(request.form['plen']) * 2
        pwid = float(request.form['pwid']) * 2
        species = int(request.form['species'])
        comment = request.form['comment']
        return render_template('12_iris_result.html', slen = slen, plen = plen, pwid = pwid,  species = species, comment = comment)

@app.route('/project')
def project():
    return render_template('iris.html')

@app.route('/hello')
@app.route('/hello/<name>')
def hello(name = None):
    return render_template('hello.html', name = name)


if __name__ == '__main__':
    app.run(debug=True)    ## debug=True는 개발모드라는 것/