class Lots():
    """ This class is purely for gathering lots that are located
        on the garabge wall, without manualling entering them"""
    def get_lots(self):
            import pandas as pd
            import openpyxl
            
            garbage_wall = pd.read_excel(r"W:\Production\Probe Oligos\REMP Files\_Re-Rack Files\Garbage Wall.xlsx", sheet_name='Garbage Wall', engine='openpyxl')
            lots = garbage_wall[(garbage_wall['Removed From NAV'].isnull())]
            lots = lots["Lot #"].values.tolist()
            lots = [int(x) for x in lots]
            return lots
