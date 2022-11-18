class Extract():
  def '__init__'(self, files):
    self.files = files
  
  def extract(self):
    import pandas as pd
    df = pd.read_csv(self.files, usecols=[1],header=None,index_col=None)
    item_list = df.values.tolist()
    return item_list
