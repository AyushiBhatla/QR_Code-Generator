# QR Code Generator Web App

A simple Flask-based web application to generate QR codes from user-provided URLs. Users can enter a URL, and the app generates a downloadable QR code with custom colors.

## Features
- Generates QR codes based on user input (URL)
- Customizable QR code colors
- Downloadable QR code image in PNG format

## Technologies Used
- **Python**: Core programming language
- **Flask**: Web framework to build the backend
- **QRCode**: Python library for generating QR codes
- **Pillow**: Python Imaging Library to handle image processing

## Installation

### Prerequisites
- **Python 3.13** (Ensure Python is installed and added to PATH)
- **pip** (comes with Python)

### Steps
1. **Clone the repository**:
   ```bash
   git clone https://github.com/your-username/qr-code-generator.git
   cd qr-code-generator
   ```

2. **Install dependencies**:
   Use pip to install required packages:
   ```bash
   pip install Flask qrcode[pil]
   ```

3. **Run the application**:
   Start the Flask server:
   ```bash
   python app.py
   ```

4. **Access the Web App**:
   Open a web browser and go to `http://127.0.0.1:5000`.

## Usage

1. Open the web application in your browser.
2. Enter the URL you wish to generate a QR code for.
3. Click the **Generate QR Code** button.
4. The app will generate and download a QR code image as `qr_code.png`.

## File Structure

- `app.py`: Main application file containing Flask routes and QR code generation logic.
- `templates/index.html`: HTML template for the frontend user interface.
- `static/`: Directory for CSS or JavaScript files if needed.

## Troubleshooting
If you encounter an `HTTP ERROR 405`, ensure that:
- The route in `app.py` allows `POST` requests.
- The form in `index.html` is set to `method="POST"`.
  
