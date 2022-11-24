from .bins import Bins
from .working_folder import Working_folder
from .extract import Extract
from .query import Query
from .interface import Interface
from .lot import Lot
class Operator(Bins, Working_folder, Extract, Query, Interface, Lot):
    
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
        bin_codes = bins.bin.commit(df)
        upload = df.insert(loc=3,column="tobincode", values=serialize(df, bin_codes))
        return upload

    def serialize(df:Dataframe, bin_codes:List[str]) -> List[str]:
        letters = ['A','B','C','D','E','F','G','H']
        data = []
        i=0
        while i <= len(df.index):
            for bin_code in bin_codes:  
                for num in range(13):
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
        df = pd.concatf(df_list, axis=0, ignore_index=True)
        return df.values.tolist()
        
    def export(upload, file_loc, file): 
        upload.to_csv(f"{file_loc}/upload{file}", index=False, header=False)
        
   def lowvsorder(low_df, order_list):
        items = low_df[0].values.tolist()
        drop_items = List(map(Lambda x: x if x in order_list, items))
                

