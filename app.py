from flask import Flask
from datetime import datetime
from time import sleep
app = Flask(__name__)

@app.route('/')
def homepage():
    the_time = datetime.now().strftime("%A, %d %b %Y %l:%M %p")

    sleep_time = 10
    sleep(sleep_time)

    return """
    <h1>Hello heroku</h1>
    <p>I waited {0}[s].</p>

    <img src="http://loremflickr.com/600/400">
    """.format(str(sleep_time))

if __name__ == '__main__':
    app.run(debug=True, use_reloader=True)
