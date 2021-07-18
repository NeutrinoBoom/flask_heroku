from flask import Flask

app=Flask(__name__)

@app.route('/',methods=["GET","POST"])
def index():
    return"<h1> This is a flask application </h1>"

# <h1> and </h1> is the header1

if __name__ == "__main__" :
    app.run()
