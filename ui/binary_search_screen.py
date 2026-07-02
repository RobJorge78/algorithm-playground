import tkinter as tk


numbers = [2, 5, 8, 11, 15, 20, 27]


def generate_binary_search_steps(arr, target):
    steps = []
    left = 0
    right = len(arr) - 1

    while left <= right:
        middle = (left + right) // 2
        middle_value = arr[middle]

        if middle_value == target:
            steps.append(
                f"Middle index is {middle}. Value {middle_value} equals target {target}. Target found!"
            )
            return steps

        elif middle_value < target:
            steps.append(
                f"Middle index is {middle}. Value {middle_value} is less than {target}. Search the right half."
            )
            left = middle + 1

        else:
            steps.append(
                f"Middle index is {middle}. Value {middle_value} is greater than {target}. Search the left half."
            )
            right = middle - 1

    steps.append(f"Target {target} was not found.")
    return steps


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
        text="Numbers: " + "   ".join(str(num) for num in numbers),
        font=("Consolas", 18),
        bg="white"
    )
    numbers_label.pack(pady=25)

    step_label = tk.Label(
        root,
        text="",
        font=("Arial", 14),
        bg="white",
        wraplength=700,
        justify="center"
    )
    step_label.pack(pady=20)

    state = {
        "steps": [],
        "current_step": 0
    }

    def start_search():
        value = entry.get()

        try:
            target = int(value)
        except ValueError:
            step_label.config(text="Please enter a valid integer.")
            return

        state["steps"] = generate_binary_search_steps(numbers, target)
        state["current_step"] = 0

        step_label.config(text=state["steps"][0])

    def next_step():
        if not state["steps"]:
            step_label.config(text="Start a search first.")
            return

        if state["current_step"] < len(state["steps"]) - 1:
            state["current_step"] += 1
            step_label.config(text=state["steps"][state["current_step"]])
        else:
            step_label.config(text="Search complete.")

    search_button = tk.Button(
        root,
        text="Start Search",
        width=20,
        command=start_search
    )
    search_button.pack(pady=5)

    next_button = tk.Button(
        root,
        text="Next Step",
        width=20,
        command=next_step
    )
    next_button.pack(pady=5)

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