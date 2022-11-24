from .bins import Bins
from .working_folder import Working_folder
from .query import Query
from .interface import Interface
from .lot import Lot

class Operator(Bins, Working_folder, Query, Interface, Lot):
    def get_items(file) -> Dataframe:
        import pandas as pd
        df = pd.read_csv(file, usecols=[1], header=None, index_col=None)
        item_list = df.values.tolist()
        query = Query(item_list=item_list)
        df = query.item_query()
        return df

    def sort_write(df:Dataframe) -> Dataframe:
        df.drop_duplicates(subset=['Item'], keep='first')
        df.sort_values(by=['Bin code'])
        bins = Bins()
        bin_codes = bins.bin_commit(df)
        upload = df.insert(loc=3,column="tobincode", values=serialize(df, bin_codes))
        return upload

    def serialize(df, bin_codes):
    """df.index also needs to be added to this function to work in production"""
    letters = ['A','B','C','D','E','F','G','H']
    data = []
    i=0
    while i <= df:
        for bin_code in bin_codes:  
            for num in range(1,13):
                for let in letters:
                    data.append(f"{bin_code}-{let}{num}")
                    i+=1
    return data

    def combine(files):
        import pandas as pd
        df_list = []
        for file in files:
            df = pd.read_csv(file, usecols=[1], header=None, index_col=None)
            df_list.append(df)
        df = pd.concatf(df_list, axis=0, ignore_index=True).drop_duplicates().reset_index(drop=True)
        return df.values.tolist()
        
    def export(upload, file_loc, file): 
        upload.to_csv(f"{file_loc}/upload{file}", index=False, header=False)
        
   def lowvsorder(low_df, order_list):
        items = low_df[0].values.tolist()
        drop_items = List(map(Lambda x: x if x in order_list, items))
                
    def upcoming_orders(order_list, vol_df):
        import pandas as pd
        query = Query()
        item_list = vol_df["Item"].values.tolist()
        overlap = [item for item in item_list if item in order_list]
        drop_list = []
        for item in overlap:
            res = query.altlot_query(item)
            if len(res) > 1:
                continue
            else:
                drop_list.append(item)
        return drop_list
