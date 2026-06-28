import tkinter as tk


def main():
    root = tk.Tk()

    root.title("Algorithm Playground")

    root.geometry("900x600")

    welcome_label = tk.Label(
        root,
        text="Welcome to Algorithm Playground!",
        font=("Arial", 18)
    )

    welcome_label.pack(pady=40)

    root.mainloop()


if __name__ == "__main__":
    main()