# QR Generator

A simple and user-friendly QR code generator built with Python and Tkinter. This application allows you to create QR codes from URLs or text and save them as PNG images with custom filenames.

## Features

- **Easy-to-use GUI**: Clean and intuitive interface built with Tkinter
- **Custom naming**: Save QR codes with personalized filenames
- **Real-time preview**: View generated QR codes directly in the application
- **PNG output**: High-quality PNG format for generated QR codes
- **Organized storage**: Automatically saves QR codes in a dedicated folder

## Requirements

- Python 3.x
- Required Python packages:
  - `tkinter` (usually comes with Python)
  - `qrcode`
  - `Pillow` (PIL)

## Installation

1. **Clone or download** this repository
2. **Install required dependencies**:
   ```bash
   pip install qrcode[pil]
   ```
   
3. **Create necessary folders**:
   - Create a `QR Codes/` folder in the same directory as the script
   - Add an `icon.png` file for the application icon (optional)

## Usage

1. **Run the application**:
   ```bash
   python qr_generator.py
   ```

2. **Generate a QR code**:
   - Enter a **title** for your QR code (this will be the filename)
   - Enter the **URL or text** you want to encode
   - Click the **"Generate"** button
   - The QR code will appear in the preview area and be saved to the `QR Codes/` folder

## File Structure

```
qr-generator/
│
├── qr_generator.py          # Main application file
├── icon.png                 # Application icon (optional)
├── QR Codes/               # Output folder for generated QR codes
│   └── [generated_qr_codes].png
└── README.md               # This file
```

## Application Interface

- **Title Field**: Enter a name for your QR code file
- **URL Field**: Enter the URL or text to be encoded
- **Generate Button**: Creates and displays the QR code
- **Preview Area**: Shows the generated QR code with a raised border effect

## Customization

### Colors
- Background color: `#AE2321` (dark red)
- Text color: White
- Button: Black background with white text

### Window Settings
- Size: 1000x550 pixels
- Non-resizable window
- Custom application icon support

## Notes

- Ensure the `QR Codes/` directory exists before running the application
- The application will overwrite existing files with the same name
- Generated QR codes are saved as PNG files
- The preview updates each time you generate a new QR code

## Troubleshooting

**Common Issues:**

1. **"No module named 'qrcode'" error**:
   ```bash
   pip install qrcode[pil]
   ```

2. **"No such file or directory: 'icon.png'" error**:
   - Add an icon.png file to the project directory, or
   - Comment out the icon-related lines in the code

3. **"No such file or directory: 'QR Codes/'" error**:
   - Create a `QR Codes` folder in the same directory as the script

## License

This project is open source and available under the [MIT License](LICENSE).

## Contributing

Feel free to fork this project and submit pull requests for any improvements or bug fixes.

---

**Enjoy generating QR codes!** 🔲
