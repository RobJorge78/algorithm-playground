import tkinter as tk


numbers = [2, 5, 8, 11, 15, 20, 27]


def binary_search(arr, target):
    left = 0
    right = len(arr) - 1

    while left <= right:
        middle = (left + right) // 2

        if arr[middle] == target:
            return middle

        elif arr[middle] < target:
            left = middle + 1

        else:
            right = middle - 1

    return -1


def show_binary_search_screen(root):
    for widget in root.winfo_children():
        widget.destroy()

    title = tk.Label(
        root,
        text="Binary Search Visualization",
        font=("Arial", 24, "bold"),
        bg="white"
    )

    title.pack(pady=20)

    instruction = tk.Label(
        root,
        text="Enter a number to search for:",
        font=("Arial", 14),
        bg="white"
    )

    instruction.pack()

    entry = tk.Entry(
        root,
        font=("Arial", 14),
        justify="center",
        width=10
    )

    entry.pack(pady=10)

    numbers_label = tk.Label(
        root,
        text="   ".join(str(num) for num in numbers),
        font=("Consolas", 20),
        bg="white"
    )

    numbers_label.pack(pady=25)

    result_label = tk.Label(
        root,
        text="",
        font=("Arial", 14),
        bg="white"
    )

    result_label.pack(pady=15)

    def start_search():
        value = entry.get()

        try:
            target = int(value)

        except ValueError:
            result_label.config(text="Please enter a valid integer.")
            return

        index = binary_search(numbers, target)

        if index == -1:
            result_label.config(
                text=f"{target} was not found."
            )
        else:
            result_label.config(
                text=f"{target} found at index {index}."
            )

    search_button = tk.Button(
        root,
        text="Start Search",
        width=20,
        command=start_search
    )

    search_button.pack(pady=10)

    def go_back():
        from ui.home_screen import show_home_screen
        show_home_screen(root)

    back_button = tk.Button(
        root,
        text="Back",
        width=20,
        command=go_back
    )

    back_button.pack(pady=20)