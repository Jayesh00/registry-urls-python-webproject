from flask import Flask,render_template
import socket

app = Flask(__name__)

@app.route('/')
def home():
    try:
        hostname = socket.gethostname()
        ip_address = socket.gethostbyname(hostname)
        return render_template('index.html', hostname=hostname, ip_address=ip_address)
    except :
        return render_template('error.html', message="Unable to fetch hostname or IP address.")
    
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=9090)
