from flask import Flask, render_template
import pandas as pd

app = Flask(__name__)

@app.route("/")
def home():
    # Load CSV
    data = pd.read_csv("universities.csv")
    
    # Remove extra spaces in headers
    data.columns = data.columns.str.strip()
    
    # Convert to list of dictionaries for Jinja
    universities = data.to_dict(orient="records")
    
    # Debug: show first 5 records in console
    print(universities[:5])
    
    return render_template("index.html", universities=universities)

# Optional test route to check rendering
from flask import render_template_string
@app.route("/test")
def test():
    data = pd.read_csv("universities.csv")
    data.columns = data.columns.str.strip()
    universities = data.to_dict(orient="records")
    return render_template_string(
        "<h1>First University: {{ universities[0].get('University Name', 'N/A') }}</h1>",
        universities=universities
    )

if __name__ == "__main__":
    app.run(debug=True)