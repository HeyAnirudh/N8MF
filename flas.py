# clean_api.py
from flask import Flask, request, jsonify
import pandas as pd
from io import BytesIO
import json

app = Flask(__name__)

@app.route('/clean-mf', methods=['POST'])
def clean_mutual_fund():
    file = request.files['file']
    df = pd.read_excel(BytesIO(file.read()))
    df_clean = df.dropna()

    data = {}
    for i in range(len(df_clean.columns)):
        data[df_clean.iloc[0, i]] = []

    for i in df_clean.columns:
        column = [i for i in df_clean[i]]
        if column[0] in data:
            data[column[0]] = column[1:]

    return json.dumps(data)

if __name__ == "__main__":
    app.run(debug=True)
