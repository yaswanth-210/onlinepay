import tkinter as tk
import gui_sender
import gui_receiver

window = tk.Tk()
window.title("Secure Offline Payment System")
window.geometry("400x350")

tk.Label(window,
         text="Secure Offline Payment",
         font=("Arial",18,"bold")).pack(pady=20)

tk.Button(window,
          text="Send Payment",
          width=25,
          height=2,
          command=gui_sender.open_sender).pack(pady=10)

tk.Button(window,
          text="Receive Payment",
          width=25,
          height=2,
          command=gui_receiver.open_receiver).pack(pady=10)

window.mainloop()