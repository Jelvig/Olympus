class Bins():
  from tkinter import *
  def '__init__'(self, df)
    self.df = df
    self.root = Tk()
    self.root.title("Enter Bin Codes")
    self.root.geometry("850x900")
    self.root.iconbitmap('/icon.ico')
    self.entry = Entry(root)
    self.bin_entries = []
  
  def create_entry_widget():
    from math import ceil
    bin = ceil(self.df.index/96)
    self.entry.grid(row=0, column=bin, pady=20, padx=5)
    my_button = Button(self.root, text='Append Bin', command=add_button)
    my_button.grid(row=1,column=0,pady=20)
    my_label = Label(root, text='Bin Selection')
    my_label.grid(row=2, column=0, pady=20)
    root.mainloop()
                  
  def add_button(self):
    self.bin_entries.append(self.entry)
