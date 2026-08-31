from flask import Flask
app = Flask(__name__)
memory_hog = []
@app.route('/')
def hello():
    return "Memory Leak App is Running!"
@app.route('/leak')
def leak():
    memory_hog.append("A" * 10000000)
    return "Memory leaked! Check your pod metrics."
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080)

