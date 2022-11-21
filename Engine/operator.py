from .bins import Bins
from .working_folder import Working_folder
from .extract import Extract
from .query import Query
from .interface import Interface

class Operator(Bins, Working_folder, Extract, Query, Interface):
    def '__init__'(self, file_loc)
        self.file_loc = file_loc
    
    def get_items(file):
        import pandas as pd
        df = pd.read_csv(file, usecols=[1], header=None, index_col=None)
        item_list = df.values.tolist()
        query = Query(item_list=item_list)
        df = query.item_query()
        return df

    def sort_write(df):
        df.drop_duplicates(subset=['Item'], keep='first')
        df.sort_values(by=['Bin code'])
        bins = Bins(df)
        bin_codes = bins.bin.commit()
        upload = df.insert(loc=3,column="tobincode", values=serialize(df, bin_codes))
        return upload

    def serialize(df, bin_codes):
        letters = ['A','B','C','D','E','F','G','H']
        data = []
        i=0
        while i <= len(df.index):
            for bin_code in bin_codes:  
                for num in range(13):
                    for let in letters:
                        data.append(f"{bin_code}-{let}{num}")
        return data

    def main():
        item_list = file_list()
        df = query_items(item_list)
        upload = sort_write(df)
        upload.to_csv(file_loc'/upload', index=False, header = False)
