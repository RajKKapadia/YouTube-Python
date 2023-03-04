from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/contactus')
def contact_us():
    return 'OK', 200

if __name__ == '__main__':
    app.run(debug=True)
