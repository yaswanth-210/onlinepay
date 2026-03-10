from tkinter import messagebox
import cv2
from pyzbar.pyzbar import decode
import sqlite3


def scan_qr():

    cap = cv2.VideoCapture(0)

    if not cap.isOpened():
        messagebox.showerror("Camera Error", "Camera not detected")
        return

    print("Scanner started...")

    while True:

        ret, frame = cap.read()

        if not ret:
            break

        barcodes = decode(frame)

        for barcode in barcodes:

            qr_data = barcode.data.decode("utf-8")

            try:
                token, sender, receiver, amount = qr_data.split(",")
            except:
                messagebox.showerror("QR Error", "Invalid QR format")
                continue

            print("Scanned Token:", token)

            conn = sqlite3.connect("transactions.db")
            cursor = conn.cursor()

            # Check if token already exists
            cursor.execute(
                "SELECT token FROM transactions WHERE token=?",
                (token,)
            )

            result = cursor.fetchone()

            if result:

                messagebox.showerror(
                    "Fraud Alert 🚨",
                    "Double Spending Detected!\nTransaction Blocked."
                )

                print("Fraud detected: token already used")

            else:

                cursor.execute(
                    """
                    INSERT INTO transactions
                    (token, sender, receiver, amount, timestamp)
                    VALUES (?, ?, ?, ?, datetime('now'))
                    """,
                    (token, sender, receiver, amount)
                )

                conn.commit()

                messagebox.showinfo(
                    "Payment Successful ✅",
                    f"Sender: {sender}\nReceiver: {receiver}\nAmount: ₹{amount}"
                )

                print("Transaction stored successfully")

            conn.close()

            cap.release()
            cv2.destroyAllWindows()
            return

        # Display instructions on camera screen
        cv2.putText(
            frame,
            "Show QR Code to Camera",
            (30, 40),
            cv2.FONT_HERSHEY_SIMPLEX,
            0.8,
            (0, 255, 0),
            2
        )

        cv2.putText(
            frame,
            "Press Q or ESC to exit",
            (30, 80),
            cv2.FONT_HERSHEY_SIMPLEX,
            0.7,
            (255, 255, 255),
            2
        )

        cv2.imshow("QR Scanner", frame)

        key = cv2.waitKey(1) & 0xFF

        if key == ord('q') or key == 27:
            break

        # Detect window close button
        if cv2.getWindowProperty("QR Scanner", cv2.WND_PROP_VISIBLE) < 1:
            break

    cap.release()
    cv2.destroyAllWindows()


if __name__ == "__main__":
    scan_qr()