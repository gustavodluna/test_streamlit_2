from flask import Flask, jsonify
import pandas as pd

app = Flask(__name__)

# Cargar los datos
data = pd.read_csv("data/df_conf.csv")

@app.route('/get_data')
def get_data():
    # Convertir los datos a formato JSON y devolverlos
    return jsonify(data.to_dict(orient='records'))

if __name__ == '__main__':
    app.run(debug=True)
