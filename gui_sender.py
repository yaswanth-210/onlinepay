import tkinter as tk
import qrcode
import uuid

def open_sender():

    win = tk.Toplevel()
    win.title("Send Payment")
    win.geometry("400x450")

    tk.Label(win,text="Sender Wallet").pack(pady=5)
    sender_entry = tk.Entry(win,width=30)
    sender_entry.pack()

    tk.Label(win,text="Receiver Wallet").pack(pady=5)
    receiver_entry = tk.Entry(win,width=30)
    receiver_entry.pack()

    tk.Label(win,text="Amount").pack(pady=5)
    amount_entry = tk.Entry(win,width=30)
    amount_entry.pack()

    status = tk.Label(win,text="",fg="green")
    status.pack(pady=10)

    qr_label = tk.Label(win)
    qr_label.pack()

    def generate_qr():

        sender = sender_entry.get()
        receiver = receiver_entry.get()
        amount = amount_entry.get()

        if sender == "" or receiver == "" or amount == "":
            status.config(text="Please fill all fields",fg="red")
            return

        token = str(uuid.uuid4())

        qr_data = f"{token},{sender},{receiver},{amount}"

        qr = qrcode.make(qr_data)
        qr.save("payment_qr.png")

        img = tk.PhotoImage(file="payment_qr.png")
        qr_label.config(image=img)
        qr_label.image = img

        status.config(text="QR Generated Successfully",fg="green")

    tk.Button(win,
              text="Generate QR",
              command=generate_qr,
              width=20,
              height=2).pack(pady=20)