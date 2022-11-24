"""final class needs df to be indexed,
users must leave a new line"""

class Bins():
    def bin_commit(self, df):
        import tkinter as tk
        from math import ceil
        root=tk.Tk()
        textBox=tk.Text(root, height=10, width=20)
        textBox.pack()
        label = tk.Label(root, text=f'Enter {ceil(df/96)} Bins').pack()
        buttonCommit=tk.Button(root, height=1, width=10, text="Commit", 
                            command=lambda: retrieve_input(textBox, root))
        buttonCommit.pack()
        tk.mainloop()
        res = self.check_values(inputValue, df)
        return res

    def check_values(self, inputValue, df):
        from math import ceil
        if len(inputValue) >= ceil(df/96):
            if all(len(bin) == 9 for bin in inputValue):
                return inputValue
            else:
                print('Improper bin was typed, please reinput')
                self.bin_commit(df)
        else:
            print('Insufficient number of bins, please re-enter')
            self.bin_commit(df)

def retrieve_input(textBox, root):
    """ add in a check to make sure the list is the correct length of bins,
    and then check to make sure the bins are accurate, or call bin commit again."""
    global inputValue
    inputValue=textBox.get("1.0","end-2c").split('\n')
    root.destroy()

