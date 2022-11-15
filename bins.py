class Bins():
  from tkinter import *
  root = Tk()
  root.title("Enter Bin Codes")
  root.geometry("850x900")
  root.iconbitmap('/icon.ico')
  entry = Entry(root)
  bin_entries = []
    
  def create_entry_widget(df):
    for bin in range(len(df.index/96))
      Bins.entry.grid(row=0, column=bin, pady=20, padx=5)
      self.bin_entries.append(entry)
    self.bin_entries.sort()
    
  @classmethod 
  def get_bins(cls):
    return [x for x in Bin.bin_entries]
