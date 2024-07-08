from flask import Flask, render_template, request


app = Flask(__name__)

@app.route('/', methods = ['GET', 'POST'])
def index():
    if request.method == 'POST':
        data = request.form
        temperaturaC = data.get('temperaturaC')
        temperaturaC = float(temperaturaC)
        temperaturaF = 1.8 * temperaturaC + 32
        return render_template('index.html', temperaturaF = temperaturaF)
    else:
        return render_template('index.html')
        

if __name__  == '__main__':
    app.run(debug=True)