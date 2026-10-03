import qrcode
file_name = input("\nEnter the file name to save the QR Code(EX- image.png): ")
data = input("\nEnter the text or URL to generate the QR Code: ")
qr = qrcode.make(data)
qr.save(f"{file_name}.png")
print(f"\nQR Code generated successfully and saved as {file_name}.png")