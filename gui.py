import tkinter as tk
from tkinter import messagebox
from calendar_logic import CalendarLogic


class CalendarApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Calendar App")

        self.month_label = tk.Label(root, text="Month (MM):")
        self.month_label.grid(row=0, column=0)

        self.month_entry = tk.Entry(root)
        self.month_entry.grid(row=0, column=1)

        self.year_label = tk.Label(root, text="Year (YYYY):")
        self.year_label.grid(row=1, column=0)

        self.year_entry = tk.Entry(root)
        self.year_entry.grid(row=1, column=1)

        self.show_button = tk.Button(root, text="Show Calendar", command=self.show_calendar)
        self.show_button.grid(row=2, columnspan=2)

        self.calendar_text = tk.Text(root, width=20, height=8)
        self.calendar_text.grid(row=3, columnspan=2)

    def show_calendar(self):
        try:
            month = int(self.month_entry.get())
            year = int(self.year_entry.get())
            if month < 1 or month > 12:
                raise ValueError

            calendar_logic = CalendarLogic(month, year)
            calendar_str = calendar_logic.get_calendar()
            self.calendar_text.delete(1.0, tk.END)
            self.calendar_text.insert(tk.END, calendar_str)
        except ValueError:
            messagebox.showerror("Invalid input", "Please enter a valid month (MM) and year (YYYY).")


if __name__ == "__main__":
    root = tk.Tk()
    app = CalendarApp(root)
    root.mainloop()
