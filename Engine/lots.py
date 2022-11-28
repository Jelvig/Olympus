class Lots():
    """needs updates
    This class is purely for gathering lots that are located
    on the garabge wall, without manuelling entering them"""
    def get_lots():
        import pandas as pd
        garbage_wall = pd.read_excel('path')
        lots = garbage_wall[garbage_wall['removed?'] != False]
        lots = lots["lot number?"].values.tolist()
        return lots
