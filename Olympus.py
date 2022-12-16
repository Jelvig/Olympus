from Engine import Operator

def main():
    import tkinter as tk

    win= tk.Tk()
    win.geometry("250x250")
    win.resizable(False, False)

    b1 = tk.Button(win, text= "Pre-Rack Condenstation",fg='black',height=5, width=30, command=lambda: PRC(win))
    b2 = tk.Button(win, text= "Low-Volume Removal", fg='black',height=5, width=30, command=lambda: LVR(win))
    b1.grid(row=1,column=1)
    b2.grid(row=2,column=1)
    
    win.mainloop()
   
def PRC(win):
    import pandas as pd
    win.destroy()
    prc = Operator()
    file_loc, files = prc.file_list()  #Get the files and location of the working folders
    probe = 'RP'
    next_bin=None
    for file in files:
        df = prc.get_items(file)  # Retrieve data frame of any available items from master
        upload, next_bin = prc.sort_write(df, next_bin)  # sort, drop duplicates and add bins
        upload.to_csv(f"{file_loc}/upload{probe}.csv", index=False, header=False)
        probe = 'GP'
        
def LVR(win):
    import pandas as pd
    win.destroy()
    lvr = Operator()
    file_loc, files = lvr.file_list()
    if len(files) > 1:
        order_list = lvr.combine(files) 
    else:
        order_list = pd.read_csv(files, usecols=[1], header=None, index_col=None).values.tolist()
    lot_list = lvr.get_lots()  # automatically retrieve lots from the garbage wall
    vol_df = lvr.lowvol_query(lot_list=lot_list)  # query for low volume probes and lots
    drop_list = lvr.upcoming_orders(order_list, vol_df)  # Compare query return to upcoming orders return items to drop
    df = vol_df[~vol_df['Item'].isin(drop_list)]
    df = df.sort_values(by='Bin code')
    bin_codes, next_bin = lvr.serialize(df)
    df.insert(loc=3, column="tobincode", value=bin_codes)
    df.to_csv(f'{file_loc}/upload.csv',index=False, header=False)


 

if __name__ == "__main__":
    main()
