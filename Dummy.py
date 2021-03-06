from flask import Flask, request, jsonify
import matplotlib.pyplot as plt
import sqlite3, pandas, json
import pandas as pd
import numpy as np

app = Flask(__name__)
@app.route('/ip', methods=['GET'])

class cache:
    def convertip(ip):
        ip = request.environ.get('HTTP_X_REAL_IP', request.remote_addr)
        df = pd.read_json(ip)
        
        df.get()

    def get(columns):
        num = 0
        dict = {}

        for value in columns:
            dict[num] = value
            num += 1

        data = list(dict.items())
        file = np.array(data)
        file.plot()
    
    def plot(file):
        plt.plot(file)
        plt.show()

        
def connect():
    path = sqlite3.connect("/Users/naumanakbani/Downloads/portal_mammals.sqlite")

    cursor = path.cursor()
    cursor.execute("SELECT * from species;")

    data = cursor.fetchall()

    json.dumps(data)
    path.close()

a = cache()
a.convertip()

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=80)
