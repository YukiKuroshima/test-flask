from flask import Flask
from datetime import datetime
from time import sleep

app = Flask(__name__)

@app.route('/')
def homepage():
    the_time = datetime.now().strftime("%A, %d %b %Y %l:%M %p")

    sleep_time = randint(1, 7)
    sleep(sleep_time)

    return """
    <p>I waited {0}[s].</p>
    """.format(str(sleep_time))

if __name__ == '__main__':
    app.run(debug=True, use_reloader=True)
