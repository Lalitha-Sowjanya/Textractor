from flask import Flask, render_template,request,jsonify     
import pytesseract
from PIL import Image
app = Flask(__name__)

@app.route("/")
def home():
    return render_template("/index.html")
    
@app.route("/upload",methods=['POST'])
def upload():
    if 'image' not in request.files:
        return jsonify({'error': 'No image uploaded'})

    image = request.files['image']
    image = Image.open(image)
    pytesseract.pytesseract.tesseract_cmd=r'C:/Program Files/Tesseract-OCR/tesseract.exe'
    extracted_text = pytesseract.image_to_string(image)

    return jsonify({'text': extracted_text})

    
if __name__ == "__main__":
    app.run(debug=True)
