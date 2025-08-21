import tkinter as tk

class Calculator:
    def __init__(self, root):
        self.root = root
        self.root.title("Calculator")

        # Center the window
        w, h = 350, 500
        sw, sh = root.winfo_screenwidth(), root.winfo_screenheight()
        x, y = (sw - w) // 2, (sh - h) // 2
        root.geometry(f"{w}x{h}+{x}+{y}")
        root.resizable(False, False)

        # Entry field
        self.entry = tk.Entry(root, font=("Arial", 24), borderwidth=5, relief="ridge", justify="right")
        self.entry.grid(row=0, column=0, columnspan=4, ipadx=8, ipady=15, sticky="nsew")

        # Buttons layout
        buttons = [
            ("AC", 1, 0, "lightgrey"), ("+/-", 1, 1, "lightgrey"), ("%", 1, 2, "lightgrey"), ("/", 1, 3, "orange"),
            ("7", 2, 0, "grey"), ("8", 2, 1, "grey"), ("9", 2, 2, "grey"), ("*", 2, 3, "orange"),
            ("4", 3, 0, "grey"), ("5", 3, 1, "grey"), ("6", 3, 2, "grey"), ("-", 3, 3, "orange"),
            ("1", 4, 0, "grey"), ("2", 4, 1, "grey"), ("3", 4, 2, "grey"), ("+", 4, 3, "orange"),
            ("0", 5, 0, "grey"), (".", 5, 1, "grey"), ("√", 5, 2, "grey"), ("=", 5, 3, "orange")
        ]

        for (text, r, c, color) in buttons:
            tk.Button(root, text=text, bg=color, fg="black", font=("Arial", 18, "bold"),
                      command=lambda t=text: self.on_click(t)).grid(row=r, column=c, sticky="nsew", padx=3, pady=3)

        # Grid config
        for i in range(6):
            root.grid_rowconfigure(i, weight=1)
        for j in range(4):
            root.grid_columnconfigure(j, weight=1)

    def on_click(self, char):
        if char == "AC":
            self.entry.delete(0, tk.END)
        elif char == "=":
            try:
                expr = self.entry.get().replace("√", "**0.5")
                self.entry.delete(0, tk.END)
                self.entry.insert(tk.END, str(eval(expr)))
            except:
                self.entry.delete(0, tk.END)
                self.entry.insert(tk.END, "Error")
        elif char == "+/-":
            try:
                value = float(self.entry.get())
                self.entry.delete(0, tk.END)
                self.entry.insert(tk.END, str(-value))
            except:
                pass
        else:
            self.entry.insert(tk.END, char)

# Run App
root = tk.Tk()
Calculator(root)
root.mainloop()
