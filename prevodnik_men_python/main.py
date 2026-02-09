import tkinter as tk
from tkinter import messagebox
import requests


def get_exchange_rate():
    # URL with current exchange rates in JSON format
    url = "https://api.exchangerate-api.com/v4/latest/CZK"

    try:
        response = requests.get(url)
        data = response.json()

        # Extract rates for EUR and GBP
        rate_eur = data["rates"]["EUR"]
        rate_gbp = data["rates"]["GBP"]

        return rate_eur, rate_gbp

    except:
        print("Error while fetching data.")
        return None, None


def calculate():
    try:
        amount_czk = float(entry_czk.get())
        rate_eur, rate_gbp = get_exchange_rate()

        if rate_eur and rate_gbp:
            amount_eur = amount_czk * rate_eur
            amount_gbp = amount_czk * rate_gbp

            # Update results in the labels
            label_res_eur.config(text=f"{amount_eur:.2f} EUR")
            label_res_gbp.config(text=f"{amount_gbp:.2f} GBP")

            # Show both exchange rates in the info label
            label_info.config(
                text=f"Rates: 1 EUR = {1/rate_eur:.2f} CZK | 1 GBP = {1/rate_gbp:.2f} CZK",
                fg="#555",
            )
        else:
            messagebox.showerror("Error", "Could not fetch exchange rates.")

    except ValueError:
        messagebox.showwarning("Input Error", "Please enter a valid number.")


# Main window setup
root = tk.Tk()
root.title("Currency Converter")
root.geometry("350x420")
root.config(bg="#f0f0f0")

# Heading
tk.Label(
    root, text="Currency Converter", font=("Arial", 16, "bold"), bg="#f0f0f0"
).pack(pady=10)

# Input for CZK
tk.Label(root, text="Amount in CZK:", bg="#f0f0f0").pack()
entry_czk = tk.Entry(root, font=("Arial", 12), justify="center")
entry_czk.pack(pady=10)

# Conversion button
btn_calc = tk.Button(
    root,
    text="Convert",
    command=calculate,
    bg="#27ae60",
    fg="white",
    font=("Arial", 10, "bold"),
    padx=20,
)
btn_calc.pack(pady=10)

# Results Frame
frame_results = tk.Frame(root, bg="white", bd=2, relief="groove")
frame_results.pack(pady=20, padx=20, fill="x", ipady=10)

label_res_eur = tk.Label(
    frame_results, text="0.00 EUR", font=("Arial", 14, "bold"), bg="white", fg="#2c3e50"
)
label_res_eur.pack(pady=5)

label_res_gbp = tk.Label(
    frame_results, text="0.00 GBP", font=("Arial", 14, "bold"), bg="white", fg="#2c3e50"
)
label_res_gbp.pack(pady=5)

# Exchange rate info label
label_info = tk.Label(root, text="", font=("Arial", 8), bg="#f0f0f0")
label_info.pack(pady=10)

root.mainloop()
