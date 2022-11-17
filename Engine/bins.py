class Bins():
  from tkinter import *
  root = Tk()
  root.title("Enter Bin Codes")
  root.geometry("850x900")
  root.iconbitmap('/icon.ico')
  entry = Entry(root)
  bin_entries = []
  
  def '__init__'(self, df)
  self.df = df
  
  def create_entry_widget():
    from math import ceil
    bin = ceil(self.df.index/96)
    Bins.entry.grid(row=0, column=bin, pady=20, padx=5)
    Bins.bin_entries.append(entry)
    
    Bins.bin_entries.sort()
    
