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
                            command=lambda: retrieve_input(textBox, root))
        buttonCommit.pack()
        tk.mainloop()
        res = check_values(inputValue)
        return res

    def check_values(inputValue):
        from math import ceil
        if len(inputValue) == ceil(self.df.index):
            if all(len(bin) == 9 for bin in inputValue):
                return inputValue
            else:
                print('Improper bin was typed, please reinput')
                self.bin_commit()
        else:
            print('Insufficient number of bins, please re-enter')
            self.bin_commit()

def retrieve_input(textBox, root):
    """ add in a check to make sure the list is the correct length of bins,
    and then check to make sure the bins are accurate, or call bin commit again."""
    global inputValue
    inputValue=textBox.get("1.0","end-2c").split('\n')
    root.destroy()
