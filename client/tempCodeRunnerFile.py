import tkinter as tk
from tkinter import messagebox

def start_app():
    window = tk.Tk()
    window.title("CCSS")
    window.geometry("800x600")
    window.configure(bg="white")

    header = tk.Frame(
        window, 
        bg = "#4c7273",
        height = 70
    )
    header.pack(fill = "x")

    title = tk.Label(
        header, 
        text = "CCSS (Cloud Calender sync Systems)",
        bg = "#4c7273",
        fg = "white", 
        font = ("Arial", 18, "bold")
    )
    title.pack(pady=20)

    task_frame = tk.Frame(window, bg = "white")
    task_frame.pack(fill = "both", expand = True)

    left_panel = tk.Frame(task_frame, bg = "#cfd6d6", width = 350)
    left_panel.pack(side = "left", fill = "y", padx = 10, pady = 10)
    left_panel.pack_propagate(False)
    today_label = tk.Label (
        left_panel,
        text = "Today task",
        bg = "#d0d6d6",
        font = ("Arial", 18, "bold")
    )
    today_label.pack(anchor="w", padx=10,pady=10)

    task_box = tk.Frame(
        left_panel,
        bg = "#4c7273",
        height = 80

        task_text = tk.Label(
            task_box,
            text = "No task",
            bg = "#4c7273",
            fg = "white",
            font =("Arial", 18)
        )
        task_text.pack(anchor = "w", padx = 10, pady = 10)
    )
    task_box.pack(fill = "x", padx = 10, pady = 10)
    task_box.pack_propagate(False)
    window.mainloop()



start_app()