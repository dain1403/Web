from flask import Flask, render_template, request
app = Flask(__name__)

@app.route('/')
def index():
    menu = {'home':True, 'rgrs':False, 'stmt':False, 'clsf':False, 'clst':False, 'user':False}
    return render_template('home.html', menu=menu)

@app.route('/regression', methods=['GET', 'POST'])
def regression():
    menu = {'home':False, 'rgrs':True, 'stmt':False, 'clsf':False, 'clst':False, 'user':False}
    if request.method == 'GET':
        return render_template('regression1.html', menu=menu)
    else:
        slen = float(request.form['slen'])
        plen = float(request.form['plen'])
        pwid = float(request.form['pwid'])
        swid = float(request.form['swid'])
        #species = int(request.form['species'])
        #swid = 0.637 * slen - 0.535 * plen + 0.558 * pwid - 0.126 * species + 0.783
        species = 1.18650 + slen*(-0.11191) + swid*(-0.04008) + plen*0.22865 + pwid*0.60925
        #names = ['Setosa', 'Versicolor', 'Virginica']
        #species = names[species]
        iris = {'slen':slen, 'plen':plen, 'pwid':pwid, 'swid':swid, 'species':species}
        return render_template('reg_result1.html', menu=menu, iris=iris)


@app.route('/sentiment')
def sentiment():
    pass

@app.route('/classification')    ### 품종맞추기   회귀식으로 구하기 regression으로 
def classification():
    pass

@app.route('/clustering')
def clustering():
    pass

if __name__ == '__main__':
    app.run(debug=True) ## deburg = true : 개발모드