import pandas as pd
import tkinter as tk
from tkinter import ttk, messagebox
import sv_ttk
import os
from datetime import datetime
import dotenv



class Application:
    """
    Donation Tracker application class.
    """

    def __init__(self, master):
        """
        Initialize the Donation Tracker application.

        Args:
            master (tk.Tk): The root Tkinter window.
        """

        dotenv.load_dotenv()

        if os.getenv("CURRENCY") is not None:
            self.CURRENCY: str = os.getenv("CURRENCY")
        else:
            self.CURRENCY: str = "€"

        

        try:
            if not files_initialized():
                init_files()

            self.dataframe = pd.read_csv("data/donations.csv")
            self.current_date = str(datetime.now().date())
            self.update_counters()
        except Exception as e:
            print(e)
            messagebox.showerror("Startup Error", "An error occurred while initializing the file structure.")
            return

        self.master = master
        self.master.title("Donation Tracker")

        self.window_width = 300
        self.window_height = 200

        self.center_window()

        self.master.resizable(False, False)

        self.frame = ttk.Frame(self.master, padding="20")
        self.frame.pack(expand=True)

        self.create_widgets()

        sv_ttk.set_theme("light")

    def center_window(self):
        """
        Center the application window on the screen.
        """

        screen_width = self.master.winfo_screenwidth()
        screen_height = self.master.winfo_screenheight()

        x = (screen_width - self.window_width) // 2
        y = (screen_height - self.window_height) // 2

        self.master.geometry(f"{self.window_width}x{self.window_height}+{x}+{y}")

    def create_widgets(self):
        """
        Create the widgets for the application.
        """

        donate_button = ttk.Button(self.frame, text="Donate", command=self.donate)

        monthly_total_label = ttk.Label(self.frame, text="Monthly Total: ")
        alltime_total_label = ttk.Label(self.frame, text="All-time Total: ")

        self.monthly_total_display = ttk.Label(self.frame, text=self.monthly_total_value)
        self.alltime_total_display = ttk.Label(self.frame, text=self.alltime_total_value)

        donate_button.grid(row=0, column=0, columnspan=4, padx=5, pady=5)

        monthly_total_label.grid(row=1, column=0, padx=5, pady=5)
        alltime_total_label.grid(row=1, column=1, padx=5, pady=5)

        self.monthly_total_display.grid(row=2, column=0, padx=5, pady=5)
        self.alltime_total_display.grid(row=2, column=1, padx=5, pady=5)

    def donate(self) -> None:
        """
        Process a donation.
        """

        if self.current_date in self.dataframe["date"].values:
            self.dataframe.loc[self.dataframe["date"] == self.current_date, "amount"] += 1
        else:
            new_entry = pd.DataFrame({"date": [self.current_date], "amount": [1]})
            self.dataframe = pd.concat([self.dataframe, new_entry], ignore_index=True)

        self.update_counters()

        self.monthly_total_display.config(text=self.monthly_total_value)
        self.alltime_total_display.config(text=self.alltime_total_value)

        self.dataframe.to_csv("data/donations.csv", index=False)

    def update_counters(self):
        """
        Update the monthly and all-time donation counters.
        """

        self.monthly_total_value = f"{self.dataframe[
            self.dataframe["date"].str.startswith(f"{self.current_date[:-3]}")
        ]["amount"].sum()} {self.CURRENCY}"

        self.alltime_total_value = f"{self.dataframe["amount"].sum()} {self.CURRENCY}"


def init_files():
    """
    Initialize the file structure for the application.
    """

    if not os.path.exists("data"):
        os.mkdir("data")

    donations_data = pd.DataFrame({'date': [], 'amount': []})
    donations_data.to_csv("data/donations.csv", index=False)


def files_initialized() -> bool:
    """
    Check if the file structure has been initialized.

    Returns:
        bool: True if the file structure exists, False otherwise.
    """

    return os.path.exists("data/donations.csv")
