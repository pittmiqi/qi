import pandas as pd
import tushare as ts
import pickle 
import numpy as np


def get_hist_all(filename,codes,start_date,end_date, ktype:str):
    '''
    Download the history data for all the stock from tushare from start_date to end_date. 
    The data will be saved in a pickle file 
    Example: get_hist_all('output.p', ['600848','600066'],start='2015-01-05',end='2015-01-09')
    '''
    all = []
    for code in codes:
        temp = ts.get_hist_data(code = code, start = start_date, end= end_date, ktype = ktype)
        all.append(temp)
    all = pd.concat(all, ignore_index = True)
    pickle.dump(all, open(filename, "rb"))





