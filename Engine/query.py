class Query:
  def __init__(self, item_list=None, lot_list=None):
    self.item_list = item_list
    self.lot_list = lot_list
    self.res = []
    self.conn = pyodbc.connect(r'Driver={Microsoft Access Driver (*.mdb, *.accdb)};DBQ=C:\Users\jelvig\Desktop\Poseidon_Test.accdb;')
    self.cursor = conn.cursor()
    
  def item_query(self):
    import pyodbc
    from pandas import DataFrame
    
    placeholder = '?'
    placeholder = ', '.join(placeholder for unused in self.items_list)
    data = """
    SELECT qy_oligos_containers.[Item No_], qy_oligos_containers.[Lot No_], qy_oligos_containers.[Bin Code], '' AS toBinCode, qy_oligos_containers.lotQty AS Qty, 'UL' AS UOMC, qy_oligos_containers.type
    FROM ((qy_oligos_containers INNER JOIN [dbo_NanoString$Bin Content] ON qy_oligos_containers.[Bin Code] = [dbo_NanoString$Bin Content].[Bin Code]) INNER JOIN qy_rack_contents ON qy_oligos_containers.shelfCode = qy_rack_contents.shelfCode) INNER JOIN [dbo_NanoString$Item] ON [dbo_NanoString$Bin Content].[Item No_] = [dbo_NanoString$Item].No_
    WHERE qy_oligos_containers.type=2 AND (qy_oligos_containers.[Item No_] IN (%s))
    ORDER BY qy_oligos_containers.[Lot No_];""" % placeholder

    self.cursor.execute(data, self.items_list)
    items = self.cursor.fetchall()
    df = DataFrame(items, columns=['Item', 'Lot', 'Bin code', 'Qty', 'UL'])
    return df
