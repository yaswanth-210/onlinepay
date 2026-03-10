import tkinter as tk
import receive_payment_camera
import threading

def open_receiver():

    win = tk.Toplevel()
    win.title("Receive Payment")
    win.geometry("300x200")

    label = tk.Label(win, text="Scan QR using Camera")
    label.pack(pady=20)

    def start_scan():
        # run scanner in separate thread
        threading.Thread(target=receive_payment_camera.scan_qr).start()

    btn = tk.Button(win,
                    text="Start Camera Scan",
                    command=start_scan)

    btn.pack(pady=20)