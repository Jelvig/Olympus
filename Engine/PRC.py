from Engine import bins
from Engine import working_folder

class PRC():
    def '__init__'(self, file_loc, files)
        self.file_loc = file_loc
        self.files = files
        
    def query_items(items_list:list):
        import pyodbc
        import pandas as pd

        conn = pyodbc.connect(r'Driver={Microsoft Access Driver (*.mdb, *.accdb)};DBQ=C:\Users\jelvig\Desktop\Poseidon_Test.accdb;')
        cursor = conn.cursor()

        # will insert values as list to find
        placeholder = '?'
        placeholder = ', '.join(placeholder for unused in items_list)

        data = """
        SELECT qy_oligos_containers.[Item No_], qy_oligos_containers.[Lot No_], qy_oligos_containers.[Bin Code], '' AS toBinCode, qy_oligos_containers.lotQty AS Qty, 'UL' AS UOMC, qy_oligos_containers.type
        FROM ((qy_oligos_containers INNER JOIN [dbo_NanoString$Bin Content] ON qy_oligos_containers.[Bin Code] = [dbo_NanoString$Bin Content].[Bin Code]) INNER JOIN qy_rack_contents ON qy_oligos_containers.shelfCode = qy_rack_contents.shelfCode) INNER JOIN [dbo_NanoString$Item] ON [dbo_NanoString$Bin Content].[Item No_] = [dbo_NanoString$Item].No_
        WHERE (qy_oligos_containers.[Item No_] IN (%s))
        ORDER BY qy_oligos_containers.[Lot No_];""" % placeholder

        cursor.execute(data, items_list)
        items = cursor.fetchall()
        df = pd.DataFrame(items, columns=['Item', 'Lot', 'Bin code', 'Qty', 'UL'])
        return df

    def sort_write(df):
        df.drop_duplicates(subset=['Item'], keep='first')
        df.sort_values(by=['Bin code'])
        bin_codes = get_bins(df)
        upload = df.insert(loc=3,column="tobincode", values=serialize(df, bin_codes))
        return upload

        # def get_bins(df):
        #   from math import ceil
        #   rows = len(df.index)
        #   bin_count = ceil(rows/96)
        #   bincodes = []
        #   i=0
        #   while i <= bin_count:
        #     bin_code = input(f"Enter bin code {i}/{bin_count}:")
        #     if len(bin_code) == 9:
        #       bincodes.append(bin_code) 
        #       i += 1
        #     else:
        #       print("This is an invalid bin code, try again")
        #   return bincodes

        # def file_list():
        #     from tkinter import filedialog
        #     from pandas import read_csv

        #     file = filedialog.askopenfilename(title="Choose master file", initialdir=r'W:\Production\Probe Oligos\REMP Files\_Re-Rack Files')
        #     item_df = read_csv(file, header=None, index_col=None)
        #     item_list = item_df[1].tolist()
        #     return item_list

    def serialize(df, bin_codes):
        letters = ['A','B','C','D','E','F','G','H']
        i=0
        while i <= len(df.index):
        for bin_code in bin_codes:  
        for num in range(13):
        for let in letters:
        f"{bin_code}-{let}{num}"

    def main():
        item_list = file_list()
        df = query_items(item_list)
        upload = sort_write(df)
        upload.to_csv('location', index=False, header = False)
