import pandas as pd
import os
from typing import cast
from pandas import Series
from flask import Flask, request

app = Flask(__name__)

UPLOAD_FOLDER = 'uploads'
os.makedirs(UPLOAD_FOLDER, exist_ok=True)


@app.route("/")
def home():
    return """
    <h1>Radiology Quality Assurance Prototype</h1>
    <form action="/upload" method="post" enctype="multipart/form-data">
        <input type="file" name="file">
        <button type="submit">Upload</button>
    </form>
    """


@app.route("/upload", methods=["POST"])
def upload():
    file = request.files["file"]
    filepath = os.path.join(UPLOAD_FOLDER, file.filename)
    file.save(filepath)

    df = pd.read_csv(filepath) # type: ignore

    duration_series = cast(Series, df["Duration"])
    tat = pd.to_numeric(duration_series, errors="coerce").dropna()

    mean_tat = tat.mean()
    max_tat = tat.max()
    delayed = (tat > 60).sum()

    return f"""
    <h2>Radiology QA Metrics</h2>
    <p><strong>Mean TAT:</strong> {mean_tat:.2f} minutes</p>
    <p><strong>Max TAT:</strong> {max_tat:.2f} minutes</p>
    <p><strong>Delayed cases (&gt;60 min):</strong> {delayed}</p>
    <a href="/">Upload another file</a>
    """


if __name__ == "__main__":
    app.run(debug=True)