from flask import Flask
import os
app == Flask(__name__)
memory_hog = []
@app.route('/')
def home():
    return "SRE App is running. Visit /leak to consume memory.", 200
@app.route('/leak')
def cause_leak():
    large_chunk_of_data = "A" * 10 * 1024 * 1024
    memory_hog.append(large_chunk_of_data)
    return f"Memory leaked! The list now holds {len(memory_hog)} chunks of data.", 200
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080)