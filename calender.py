import tkinter as tk
from tkinter import ttk
from tkcalendar import Calendar


def select_date():
    selected_date = cal.get_date()
    label.config(text="Selected Date: " + selected_date)


app = tk.Tk()
app.title("Calendar Date Picker")

cal = Calendar(app, selectmode="day", date_pattern="y-mm-dd")
cal.pack(pady=20)

button = ttk.Button(app, text="Select Date", command=select_date)
button.pack(pady=10)

label = ttk.Label(app, text="")
label.pack(pady=5)

app.mainloop()


# made with ❤️ by Aman
# Name = Amandeep singh
# Batch = Cap04
# cap_id = cap04_027
