from .working_folder import Files
from .query import Query
from .lots import Lots

class Operator(Files, Query, Lots):

    def get_items(self,file):
        """ Will read the csv, gather item numbers and query them and return a dataframe"""
        import pandas as pd
        df = pd.read_csv(file, usecols=[1], header=None, index_col=None, names=['Items'])
        item_list= df['Items'].values.tolist()
        query = Query(item_list=item_list)
        df = query.item_query()

        return df

    def sort_write(self,df, next_bin):
        """Dataframe manipulation of droping duplicates, sorting and applying the 'tobincodes' """
        df = df.drop_duplicates(subset=['Item'], keep='first')
        df = df.sort_values(by='Bin code')
        query = Query()
        bin_code = query.bin_query()
        data, next_bin = self.serialize(df, bin_code=bin_code, next_bin=next_bin)
        df.insert(loc=3,column="tobincode", value=data)
        return df, next_bin

    def serialize(self,df, bin_code='F02-80', next_bin=None):
        """creates 'tobincode' location for the same amount of lines as the dataframe"""
        letters = ['A','B','C','D','E','F','G','H']
        data = []
        i=0
        cane = 0
        if not next_bin:
            while i <= len(df.index):
                cane += 1
                for num in range(1,13):
                    for let in letters:
                        data.append(f"{bin_code}-{str(cane).zfill(2)}-{let}{str(num).zfill(2)}")
                        i+=1
                        if i == len(df.index):
                            next_bin = f"{bin_code}-{str(cane).zfill(2)}"
                            return data, next_bin
        elif next_bin:
            cane = int(next_bin[7:9])
            while i <= len(df.index):
                cane += 1
                for num in range(1,13):
                    for let in letters:
                        data.append(f"{bin_code}-{str(cane).zfill(2)}-{let}{str(num).zfill(2)}")
                        i+=1
                        if i == len(df.index):
                            next_bin = f"{bin_code}-{str(cane).zfill(2)}"
                            return data, next_bin

    def combine(self,files):
        """Creates a list of all the items that are on upcoming orders or potential reworks, chain is used
            to create one big list"""
        import pandas as pd
        import itertools
        df_list = []
        for file in files:
            df = pd.read_csv(file, usecols=[1], header=None, index_col=None)
            df_list.append(df)
        df = pd.concat(df_list, axis=0, ignore_index=True).drop_duplicates().reset_index(drop=True)
        return list(itertools.chain(*df.values.tolist()))
        
    def lowvsorder(self, low_df, order_list):
        """Compares low volume items to items on upcoming orders and returns the overlap"""
        items = low_df[0].values.tolist()
        drop_items = [x for x in items if x in order_list]
        return drop_items
                
    def upcoming_orders(self,order_list, vol_df):
        """Finds the overlap between the low volumes probes and upcoming orders and 
            tests the overlap for alt-lots"""
        import pandas as pd
        query = Query()
        item_list = vol_df["Item"].values.tolist()
        item_list = [int(x) for x in item_list]
        overlap = [item for item in item_list if item in order_list]
        drop_list = query.altlot_query(overlap)
        
        return drop_list
