import tkinter as tk

from ui.home_screen import show_home_screen


def main():
    root = tk.Tk()

    root.title("Algorithm Playground")
    root.geometry("900x600")
    root.configure(bg="white")

    title_label = tk.Label(
        root,
        text="Algorithm Playground",
        font=("Arial", 28, "bold"),
        bg="white"
    )

    title_label.pack(pady=(50, 15))

    description_label = tk.Label(
        root,
        text="Learn algorithms through interactive visualizations.",
        font=("Arial", 14),
        bg="white"
    )

    description_label.pack()

    start_button = tk.Button(
        root,
        text="Start Exploring",
        font=("Arial", 14),
        width=20,
        command=lambda: show_home_screen(root)
    )

    start_button.pack(pady=40)

    root.mainloop()


if __name__ == "__main__":
    main()