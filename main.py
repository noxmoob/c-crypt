from flask import Flask, render_template, request
import pyaes
import hashlib

app = Flask(__name__)

def encrypt_data(passphrase):
    key = hashlib.sha256(passphrase.encode('utf-8')).digest()
    aes = pyaes.AESModeOfOperationCTR(key)
    plaintext = b'test'
    result = aes.encrypt(plaintext)
    return result

@app.route('/', methods=['GET', 'POST'])
def index():
    encrypted_result = None

    if request.method == 'POST':
        passphrase = request.form['passphrase']
        encrypted_result = encrypt_data(passphrase)

    return render_template('index.html', encrypted_result=encrypted_result)

if __name__ == '__main__':
    app.run(debug=True)
