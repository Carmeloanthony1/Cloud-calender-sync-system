import tkinter as tk

def task_cardbox(parent, time, text):
    card = tk.Frame(
        parent,
        bg="#4c7273",
        bd=1,
        relief="ridge"
    )
    card.pack(fill="x", padx=10, pady=6)

    time_label = tk.Label(
        card,
        text=time,
        bg="#4c7273",
        fg="white",
        font=("Arial", 10, "bold")
    )
    time_label.pack(anchor="w", padx=10, pady=(6, 0))

    text_label = tk.Label(
        card,
        text=text,
        bg="#4c7273",
        fg="white",
        font=("Arial", 12),
        wraplength=280,
        justify="left"
    )
    text_label.pack(anchor="w", padx=10, pady=(2, 6))


def start_app():
    window = tk.Tk()
    window.title("CCSS")
    window.geometry("800x600")
    window.configure(bg="white")

    header = tk.Frame(window, bg="#4c7273", height=70)
    header.pack(fill="x")

    title = tk.Label(
        header,
        text="CCSS (Cloud Calendar Sync Systems)",
        bg="#4c7273",
        fg="white",
        font=("Arial", 18, "bold")
    )
    title.pack(pady=20)

    task_frame = tk.Frame(window, bg="white")
    task_frame.pack(fill="both", expand=True)

    left_panel = tk.Frame(task_frame, bg="#cfd6d6", width=350)
    left_panel.pack(side="left", fill="y", padx=10, pady=10)
    left_panel.pack_propagate(False)

    today_label = tk.Label(
        left_panel,
        text="Today Task",
        bg="#d0d6d6",
        font=("Arial", 18, "bold")
    )
    today_label.pack(anchor="w", padx=10, pady=10)

    today_task = [
        ("09.00", "Berak"),
        ("12.00", "Berak lagi"),
        ("13.00", "Berak berkali-kali"),
        ("21.00", "berak lagi")
    ]

    task_container = tk.Frame(left_panel, bg="#cfd6d6")
    task_container.pack(fill="x")

    for time, task in today_task:
        task_cardbox(task_container, time, task)

    window.mainloop()


start_app()