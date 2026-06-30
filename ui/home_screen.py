import tkinter as tk

from ui.binary_search_screen import show_binary_search_screen


def show_home_screen(root):
    # Remove everything currently on the screen
    for widget in root.winfo_children():
        widget.destroy()

    title = tk.Label(
        root,
        text="Choose an Algorithm",
        font=("Arial", 24, "bold"),
        bg="white"
    )

    title.pack(pady=30)

    binary_button = tk.Button(
        root,
        text="Binary Search",
        width=25,
        height=2,
        command=lambda: show_binary_search_screen(root)
    )

    binary_button.pack(pady=10)

    bubble_button = tk.Button(
        root,
        text="Bubble Sort",
        width=25,
        height=2
    )

    bubble_button.pack(pady=10)

    selection_button = tk.Button(
        root,
        text="Selection Sort",
        width=25,
        height=2
    )

    selection_button.pack(pady=10)