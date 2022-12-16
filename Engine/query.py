class Query:
  def __init__(self, item_list=None, lot_list=None):
    import pyodbc
    self.item_list = item_list
    self.lot_list = lot_list
    self.res = []
    self.conn = pyodbc.connect(r'Driver={Microsoft Access Driver (*.mdb, *.accdb)};DBQ=C:\Users\jelvig\Desktop\Poseidon_Test.accdb;')
    self.cursor = self.conn.cursor()
    self.conn.autocommit = True
    
  def item_query(self):
    """ This query breaks the items into lists of 150 for easy return, appends the dataframe into a list,
        and then concatenates them all together for the final dataframe. for PRC"""
    import pandas as pd
    sublists = [self.item_list[ i : i + 150] for i in range(0, len(self.item_list), 150)]
    df_list = []
    for sublist in sublists:
      placeholder = '?'
      placeholder = ', '.join(placeholder for unused in sublist)
      data = """
              SELECT [dbo_NanoString$Warehouse Entry].[Item No_], [dbo_NanoString$Warehouse Entry].[Lot No_], [dbo_NanoString$Warehouse Entry].[Bin Code], SUM([dbo_NanoString$Warehouse Entry].Quantity),
                      [dbo_NanoString$Warehouse Entry].[Location Code], LEN([dbo_NanoString$Warehouse Entry].[Lot No_])
              FROM [dbo_NanoString$Warehouse Entry]
              GROUP BY [dbo_NanoString$Warehouse Entry].[Item No_], [dbo_NanoString$Warehouse Entry].[Lot No_], [dbo_NanoString$Warehouse Entry].[Location Code],
                      [dbo_NanoString$Warehouse Entry].[Bin Code]
              HAVING (SUM([dbo_NanoString$Warehouse Entry].Quantity)>1) AND (LEN([dbo_NanoString$Warehouse Entry].[Lot No_]) = 10) AND
                      [dbo_NanoString$Warehouse Entry].[Location Code] = 'BOTHELL' AND ([dbo_NanoString$Warehouse Entry].[Item No_]  IN (%s))
              ORDER BY [dbo_NanoString$Warehouse Entry].[Lot No_];""" % placeholder

      self.cursor.execute(data, sublist)
      items = self.cursor.fetchall()
      info = {'Item': [i[0] for i in items], 'Lot': [i[1] for i in items],
      'Bin code': [i[2] for i in items], 'Qty': [i[3] for i in items], 'UL': [i[4] for i in items]}
      df_tmp = pd.DataFrame(info, index=None)
      df_list.append(df_tmp)
    df = pd.concat(df_list)
    
    return df
  
  def altlot_query(self, overlap):
    """ This query collects the items that are apart of upcoming orders and retrieves all data for those items,
        Then counts how many of those items are returned, if only 1 is, then it will be removed"""
    import pyodbc
    from pandas import DataFrame
    from collections import Counter
    overlap = [str(x) for x in overlap]
    placeholder = '?'
    placeholder = ', '.join(placeholder for unused in overlap)
    data = """
            SELECT [dbo_NanoString$Warehouse Entry].[Item No_], [dbo_NanoString$Warehouse Entry].[Lot No_], [dbo_NanoString$Warehouse Entry].[Bin Code], SUM([dbo_NanoString$Warehouse Entry].Quantity),
                    [dbo_NanoString$Warehouse Entry].[Location Code], LEN([dbo_NanoString$Warehouse Entry].[Lot No_])
            FROM [dbo_NanoString$Warehouse Entry]
            GROUP BY [dbo_NanoString$Warehouse Entry].[Item No_], [dbo_NanoString$Warehouse Entry].[Lot No_], [dbo_NanoString$Warehouse Entry].[Location Code],
                    [dbo_NanoString$Warehouse Entry].[Bin Code]
            HAVING (SUM([dbo_NanoString$Warehouse Entry].Quantity)>1) AND (LEN([dbo_NanoString$Warehouse Entry].[Lot No_]) = 10) AND
                    [dbo_NanoString$Warehouse Entry].[Location Code] = 'BOTHELL' AND ([dbo_NanoString$Warehouse Entry].[Item No_]  IN (%s));""" % placeholder
    self.cursor.execute(data, overlap)
    drop_list = [i[0] for i in self.cursor.fetchall()]
    drop_list = Counter(drop_list)
    drop_list = [i for i in drop_list if drop_list[i]==1]
    return drop_list
  
  def lowvol_query(self, lot_list):
    """This collects all probes of RP and GP that are under 41uL and returns the lots,
        these are added to the lot list from garbage wall, and all queried at once,
        dataframe is created and returned."""
    from pandas import DataFrame
    low_lots = """
    SELECT [dbo_NanoString$Warehouse Entry].[Item No_], [dbo_NanoString$Warehouse Entry].[Lot No_], SUM([dbo_NanoString$Warehouse Entry].Quantity),
            [dbo_NanoString$Warehouse Entry].[Location Code], LEN([dbo_NanoString$Warehouse Entry].[Lot No_])
    FROM [dbo_NanoString$Warehouse Entry]
    WHERE  [dbo_NanoString$Warehouse Entry].[Location Code] = 'BOTHELL'
    GROUP BY [dbo_NanoString$Warehouse Entry].[Item No_], [dbo_NanoString$Warehouse Entry].[Lot No_], [dbo_NanoString$Warehouse Entry].[Location Code]
    HAVING (SUM([dbo_NanoString$Warehouse Entry].Quantity) BETWEEN 0.001 AND 41) AND
              (LEFT([dbo_NanoString$Warehouse Entry].[Item No_], 1) = '2' OR LEFT([dbo_NanoString$Warehouse Entry].[Item No_], 1) = '3') AND
              (LEN([dbo_NanoString$Warehouse Entry].[Lot No_]) = 10);"""

    self.cursor.execute(low_lots)
    lowvol_list = [i[1] for i in self.cursor.fetchall()]
    lot_list.extend(lowvol_list)

    placeholder = '?'
    placeholder = ', '.join(placeholder for unused in lot_list)
    data = """
    SELECT qy_oligos_containers.[Item No_], qy_oligos_containers.[Lot No_], qy_oligos_containers.[Bin Code],qy_oligos_containers.lotQty AS Qty, 'UL' AS UOMC
    FROM ((qy_oligos_containers INNER JOIN [dbo_NanoString$Bin Content] ON qy_oligos_containers.[Bin Code] = [dbo_NanoString$Bin Content].[Bin Code]) INNER JOIN qy_rack_contents ON qy_oligos_containers.shelfCode = qy_rack_contents.shelfCode) INNER JOIN [dbo_NanoString$Item] ON [dbo_NanoString$Bin Content].[Item No_] = [dbo_NanoString$Item].No_
    WHERE (qy_oligos_containers.[Lot No_] IN (%s))
    ORDER BY qy_oligos_containers.[Lot No_];""" % placeholder

    self.cursor.execute(data, lot_list)
    lowvol_info = self.cursor.fetchall()
    info = {'Item': [i[0] for i in lowvol_info], 'Lot': [i[1] for i in lowvol_info],
              'Bin code': [i[2] for i in lowvol_info], 'Qty': [i[3] for i in lowvol_info], 'UL': [i[4] for i in lowvol_info]}

    df = DataFrame(info, index=None)
    return df

  def bin_query(self):
    """ This is to check if C02-12 is empty, if it is then it is returned, if not, then C02-13 is returned"""
    from pandas import DataFrame
    data = """
    SELECT TOP 5, qy_oligos_containers.[Item No_], qy_oligos_containers.[Lot No_], qy_oligos_containers.[Bin Code], qy_oligos_containers.shelfCode, qy_oligos_containers.type, qy_oligos_containers.caneNo
    FROM (qy_oligos_containers)
    WHERE ((Left(qy_oligos_containers.[Bin Code],3)='C02') And (qy_oligos_containers.caneNo)='12') And (qy_oligos_containers.type='2')
    ORDER BY (qy_oligos_containers.[Bin Code]);"""

    self.cursor.execute(data)
    items = self.cursor.fetchall()
    df = DataFrame(items)
    if df.values.tolist():
      return 'C02-13'
    else:
      return 'C02-12'
