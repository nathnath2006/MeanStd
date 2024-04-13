import numpy as np

def conform(list):
    if len(list) != 9:
       raise ValueError


def calculate(list):
    try:
      conform(list)
      tlist = [list[0:3], list[3:6], list[6:9]]
      narray = np.array(tlist)
      narray.reshape((3,3))
      trnarray = np.transpose(narray)
      calculations ={'mean': [[np.mean(trnarray[i]) for i in range(3)], [np.mean(narray[i]) for i in range(3)], np.mean(narray)],
                     'variance': [[np.var(trnarray[i]) for i in range(3)], [np.var(narray[i]) for i in range(3)], np.var(narray)],
                     'standard deviation': [[np.std(trnarray[i]) for i in range(3)], [np.std(narray[i]) for i in range(3)], np.std(narray)],
                     'max': [[np.max(trnarray[i]) for i in range(3)], [np.max(narray[i]) for i in range(3)], np.max(narray)],
                     'min': [[np.min(trnarray[i]) for i in range(3)], [np.min(narray[i]) for i in range(3)], np.min(narray)],
                     'sum': [[np.sum(trnarray[i]) for i in range(3)], [np.sum(narray[i]) for i in range(3)], np.sum(narray)]}
      return calculations
    except ValueError as ve:
       return "List must have nine numbers"




