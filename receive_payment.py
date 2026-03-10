import cv2
import sqlite3

detector = cv2.QRCodeDetector()

img = cv2.imread("payment_qr.png")

data, bbox, _ = detector.detectAndDecode(img)

if data:
    token, sender, receiver, amount = data.split(",")

    conn = sqlite3.connect("transactions.db")
    cursor = conn.cursor()

    cursor.execute("SELECT * FROM transactions WHERE token=?", (token,))
    result = cursor.fetchone()

    if result:
        print("Double Spending Detected! Payment Rejected")
    else:
        cursor.execute(
            "INSERT INTO transactions VALUES (?,?,?,?,?)",
            (token, token, sender, receiver, amount)
        )
        conn.commit()
        print("Payment Accepted")

    conn.close()

else:
    print("QR not detected")