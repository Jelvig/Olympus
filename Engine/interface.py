


class Interface(PRC,LVR):
  def window():
    import tkinter as tk

    win= tk.Tk()
    win.geometry("600x250")
    win.resizable(False, False)

    tk.Button(win, text= "Pre-Rack Condenstation",fg='black',height=5, width=30, command=quit).pack()
    tk.Button(win, text= "Low-Volume Removal", fg='black',height=5, width=30, command=write_text).pack()
    win.mainloop()

