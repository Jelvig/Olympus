from Engine import interface
from Engine import Operator

def PRC():
  prc = Operator()
  file_loc, files = prc.file_list()
  for file in files:
    prc.extract()
  
