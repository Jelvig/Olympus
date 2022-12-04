from Engine import interface
from Engine import operator
from Engine import working_folder
from Engine import lot

def PRC():
  import pandas as pd
  prc = Operator()
  file_loc, files = prc.file_list()  #Get the files and location of the working folders
  for file in files:
    item_list = prc.get_item(file)  # Retrieve data frame of any available items from master
    upload = prc.sort_write(item_list)  # sort, drop duplicates and add bins
    prc.export(upload, file_loc, file)
  
def LVR():
  import pandas as pd
  lvr = Operator()
  file_loc, files = lvr.file_list()
  if len(files) > 1:
    order_list = lvr.combine(files)  # Concatenate all masterfiles
  else:
    order_list = pd.read_csv(files, usecols=[1], header=None, index_col=None).values.tolist()
  lot_list = lvr.get_lots()  # automatically retrieve lots from the garbage wall
  vol_df = lvr.lowvol_query(lot_list=lot_list)  # query for low volume probes and lots
  drop_list = lvr.upcoming_orders(order_list, vol_df)  # Compare query return to upcoming orders return items to drop
  upload = vol_df[~vol_df['Item'].isin(drop_list)]
  lvr.export(upload, file_loc, file=1)  # export final product

def main():
  wind = Interface(PRC(), LVR())
  wind.window()
 

if '__name__' == '__main__':
  main()
