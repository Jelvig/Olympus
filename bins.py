class Bins():
  def create_entry_widget(df):
    # Import the Tkinter Library
    import tkinter as tk
    root = tk.Tk()
    root.title("Enter Bin Codes")
    root.geometry("850x500")
    root.iconbitmap('/icon.ico')
    entry = tk.Entry(root)
    entry.grid(row=len(df.index), column=0, pady=20, padx=9)
