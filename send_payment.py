import qrcode
import uuid

sender = input("Enter Sender Wallet ID: ")
receiver = input("Enter Receiver Wallet ID: ")
amount = input("Enter Amount: ")

token = str(uuid.uuid4())

data = f"{token},{sender},{receiver},{amount}"

img = qrcode.make(data)
img.save("payment_qr.png")

print("QR Code Generated")
print("Token:", token)