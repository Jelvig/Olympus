from Engine import interface
from Engine import operator
from Engine import working_folder
from Engine import lot

def PRC():
  import pandas as pd
  prc = Operator()
  file_loc, files = prc.file_list()
  for file in files:
    item_list = prc.get_item(file)
    upload = prc.sort_write(item_list)
    prc.export(upload, file_loc, file)
  
def LVR():
  import pandas as pd
  lvr = Operator()
  file_loc, files = lvr.file_list()
  if len(files) > 1:
    order_list = lvr.combine(files)
  else:
    order_list = pd.read_csv(files, usecols=[1,2], header=None, index_col=None).values.tolist()
  lot_list = lvr.lot_commit()
  vol_df = lvr.lowvol_query(lot_list=lot_list)
  drop_list = lvr.upcoming_orders(order_list, vol_df)
  tmp_df = vol_df[vol_df['Item'] is in drop_list].index
  upload = vol_df.drop(tmp_df, inplace=True)
  lvr.export(upload, file_loc, file=1)
