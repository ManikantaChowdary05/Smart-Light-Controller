from flask import Flask, render_template, request

app = Flask(__name__)
light_status = {'on': False}

@app.route('/')
def home():
    return render_template('light.html', status=light_status['on'])

@app.route('/toggle', methods=['POST'])
def toggle():
    light_status['on'] = not light_status['on']
    return ('', 204)  # No content

@app.route('/status')
def status():
    return {'status': light_status['on']}

if __name__ == '__main__':
    app.run(debug=True)
