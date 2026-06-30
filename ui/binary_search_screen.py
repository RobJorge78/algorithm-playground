import tkinter as tk


def show_binary_search_screen(root):
    # Remove everything currently on the screen
    for widget in root.winfo_children():
        widget.destroy()

    title = tk.Label(
        root,
        text="Binary Search Visualization",
        font=("Arial", 24, "bold"),
        bg="white"
    )

    title.pack(pady=25)

    info = tk.Label(
        root,
        text="Today's goal: build the Binary Search visualizer.",
        font=("Arial", 14),
        bg="white"
    )

    info.pack(pady=10)

    numbers = [2, 5, 8, 11, 15, 20, 27]

    numbers_label = tk.Label(
        root,
        text="   ".join(str(num) for num in numbers),
        font=("Consolas", 20),
        bg="white"
    )

    numbers_label.pack(pady=40)

    def go_back():
        from ui.home_screen import show_home_screen
        show_home_screen(root)

    back_button = tk.Button(
        root,
        text="Back",
        width=15,
        command=go_back
    )

    back_button.pack(pady=20)