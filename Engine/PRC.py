from .bins import Bins
from .working_folder import Working_folder
from .extract import Extract

class PRC(Bins, Working_folder, Extract):
    def '__init__'(self, file_loc, files)
        self.file_loc = file_loc
        self.files = files
       

    def sort_write(df):
        df.drop_duplicates(subset=['Item'], keep='first')
        df.sort_values(by=['Bin code'])
        #bin_codes = get_bins(df) changed to a class to be used
        upload = df.insert(loc=3,column="tobincode", values=serialize(df, bin_codes))
        return upload

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
        upload.to_csv(file_loc'/upload', index=False, header = False)
