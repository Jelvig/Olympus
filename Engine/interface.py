


class Interface():
  def __init__(self, PRC, LVR):
    self.PRC = PRC
    self.LVR = LVR
  def window():
    import tkinter as tk

    win= tk.Tk()
    win.geometry("600x250")
    win.resizable(False, False)

    tk.Button(win, text= "Pre-Rack Condenstation",fg='black',height=5, width=30, command=self.PRC).pack()
    tk.Button(win, text= "Low-Volume Removal", fg='black',height=5, width=30, command=self.LVR).pack()
    win.mainloop()

