import qrcode
import sys

def generate_qr():
    print("========================================")
    print("   🚀 ADVANCED QR CODE GENERATOR 🚀   ")
    print("========================================\n")
    
    while True:
        # 1. Get the link or data from the user
        website_link = input("🔗 Enter the link or text (or type 'exit' to quit): ").strip()
        
        if website_link.lower() == 'exit':
            print("\nExiting... Happy scanning! 👋")
            break
            
        if not website_link:
            website_link = 'https://www.youtube.com/watch?v=dQw4w9WgXcQ'
            print(f"   (No link entered. Using default: {website_link})")

        # 2. Customization Parameters
        print("\n🛠️  Customization Settings (Press Enter for defaults):")
        try:
            # Version: 1 is 21x21, 40 is 177x177. 'None' allows auto-sizing.
            v_input = input("   - Version (1-40, default 1): ").strip()
            version = int(v_input) if v_input else 1
            
            # Box Size: Pixels per square
            bs_input = input("   - Box Size (default 5): ").strip()
            box_size = int(bs_input) if bs_input else 5
            
            # Border: Thickness in squares
            b_input = input("   - Border Size (default 5): ").strip()
            border = int(b_input) if b_input else 5

            # 3. Create QR Code Object
            qr = qrcode.QRCode(
                version=version,
                error_correction=qrcode.constants.ERROR_CORRECT_H, # Higher error correction
                box_size=box_size,
                border=border
            )

            # 4. Process Data
            qr.add_data(website_link)
            qr.make(fit=True)

            # 5. Visual Styling
            print("\n🎨 Color Options (e.g., 'red', 'blue', '#FF5733'):")
            fill = input("   - Fill color (default 'black'): ").strip() or 'black'
            back = input("   - Background color (default 'white'): ").strip() or 'white'
            
            img = qr.make_image(fill_color=fill, back_color=back)

            # 6. Saving
            filename = input("\n💾 Enter filename (default 'my_qr_code.png'): ").strip() or 'my_qr_code.png'
            if not filename.lower().endswith('.png'):
                filename += '.png'
            
            img.save(filename)
            print(f"\n✅ SUCCESS: QR code saved as '{filename}'\n")
            print("-" * 40 + "\n")

        except ValueError as e:
            if "unknown color specifier" in str(e).lower():
                print(f"\n❌ ERROR: Invalid color name. Please try common color names (like 'gold' instead of 'golden') or use hex codes.\n")
            else:
                print("\n❌ ERROR: Please enter valid numbers for version/size.\n")
        except Exception as e:
            print(f"\n❌ ERROR: An unexpected error occurred: {e}\n")

if __name__ == "__main__":
    generate_qr()
