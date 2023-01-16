from flask import Flask
app = Flask(__name__)

@app.route("/", methods= ['POST'])
def home():
    # TODO : render a html page 
    pass

if __name__ == '__main__':
    app.run(debug=True)