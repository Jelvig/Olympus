class Bins():
    def __init__(self, df):
        self.df = df

    def bin_commit(self):
        import tkinter as tk
        from math import ceil
        root=tk.Tk()
        textBox=tk.Text(root, height=10, width=20)
        textBox.pack()
        label = tk.Label(root, text=f'Enter {ceil(self.df/96)} Bins').pack()
        buttonCommit=tk.Button(root, height=1, width=10, text="Commit", 
                            command=lambda: retrieve_input(textBox))
        buttonCommit.pack()
        tk.mainloop()

def retrieve_input(textBox):
    """ add in a check to make sure the list is the correct length of bins,
    and then check to make sure the bins are accurate, or call bin commit again."""
    inputValue=textBox.get("1.0","end-2c").split('\n')
    print(inputValue)

df = 1500
bin = Bins(df)
bin.bin_commit()
