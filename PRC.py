def query_items(items_list):
    import pyodbc
    from pandas import DataFrame

    conn = pyodbc.connect(r'Driver={Microsoft Access Driver (*.mdb, *.accdb)};DBQ=C:\Users\jelvig\Desktop\Poseidon_Test.accdb;')
    cursor = conn.cursor()

    #current query used to find raw data: work in progress
    placeholder = '?'
    placeholder = ', '.join(placeholder for unused in items_list)

    data = """
    SELECT qy_oligos_containers.[Item No_], qy_oligos_containers.[Lot No_], qy_oligos_containers.[Bin Code], '' AS toBinCode, qy_oligos_containers.lotQty AS Qty, 'UL' AS UOMC, qy_oligos_containers.type
    FROM ((qy_oligos_containers INNER JOIN [dbo_NanoString$Bin Content] ON qy_oligos_containers.[Bin Code] = [dbo_NanoString$Bin Content].[Bin Code]) INNER JOIN qy_rack_contents ON qy_oligos_containers.shelfCode = qy_rack_contents.shelfCode) INNER JOIN [dbo_NanoString$Item] ON [dbo_NanoString$Bin Content].[Item No_] = [dbo_NanoString$Item].No_
    WHERE qy_oligos_containers.type=2 AND (qy_oligos_containers.[Item No_] IN (%s))
    ORDER BY qy_oligos_containers.[Lot No_];""" % placeholder

    cursor.execute(data, items_list)
    items = cursor.fetchall()
    df = DataFrame(items, columns=['Item', 'Lot', 'Bin code', 'Qty', 'UL'])
    
    
    return df

def csv_write(data_list):
    from pandas import DataFrame

    df = df.drop_duplicates(subset=['Item'], keep='first')
    df.sort_values(by=['Bin code'])
    df.insert(3, ) # insert column to be serialized with bin code input

def file_list():
    from tkinter import filedialog
    from pandas import read_csv

    file = filedialog.askopenfilename(title="Choose master file", initialdir=r'W:\Production\Probe Oligos\REMP Files\_Re-Rack Files')
    items_df = read_csv(file, header=None, index_col=None)
    items_list = items_df[1].tolist()
    return items_list

def main():
    item_list = file_list()
    data_list = list(map(lambda x: query_items(x), item_list))
    csv_write(data_list)
        
# if "__name__" == main():
#     main()
query_items()

"""New plan, query for all RP probes into a dataframe,
 then search dataframe for items and return the row. this would be much faster"""
