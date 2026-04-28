🔳 Advanced QR Code Generator
A fully interactive, command-line based Python script to generate highly customizable QR codes.

🌟 Features
  Interactive CLI: Step-by-step user-friendly command-line interface
  Customizable Dimensions: Control version, box size, and border
  Custom Colors: Use color names (e.g., red, blue) or Hex codes (e.g., #FF5733)
  High Error Correction: Uses ERROR_CORRECT_H for better scannability
  
Auto-Fallbacks:
  Default link if none provided
  Automatically adds .png if missing
  Error Handling: Prevents crashes from invalid inputs
  
⚙️ Prerequisites
    Make sure you have:
    Python 3.x installed
    Required libraries installed:
    pip install qrcode[pil]
    
▶️ How to Run
  Open Terminal / Command Prompt / PowerShell
  Navigate to your project folder:
  cd path\to\your\project
Run the script:
  python qr_code.py
Follow the prompts:
  Enter URL or text
  (Optional) Set Version, Box Size, Border
  (Optional) Choose colors
  Enter filename to save QR code  
  Type exit at the first prompt to safely close the program.

📄 License (MIT)
This project is licensed under the MIT License.
