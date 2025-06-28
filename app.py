from flask import Flask, render_template, request
import requests

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    subdomains = []
    domain = ""
    if request.method == 'POST':
        domain = request.form['domain']
        url = f"https://crt.sh/?q=%25.{domain}&output=json"
        try:
            response = requests.get(url)
            if response.ok:
                data = response.json()
                subdomains = sorted(set(entry['name_value'] for entry in data))
        except Exception as e:
            subdomains = [f"Error occurred: {e}"]
    return render_template('index.html', subdomains=subdomains, domain=domain)

if __name__ == '__main__':
    app.run(debug=True)
