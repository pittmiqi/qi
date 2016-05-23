import pandas as pd
import tushare as ts
import pickle
import numpy as np
import qi.utility.util as ut
import pyprind

def get_hist_all(filename, codes, names, start_date,end_date, ktype:str) :
    '''
    Download the history data for all the stock from tushare from start_date to end_date.
    The data will be saved in a pickle file
    Example: get_hist_all('output.p', ['600848','600066'],start='2015-01-05',end='2015-01-09')
    '''
    all = []
    bar = pyprind.ProgBar(len(codes))
    for i in np.arange(len(codes)):
        temp = ts.get_hist_data(code = codes[i], start = start_date, end= end_date, ktype = ktype)
        if temp is not None:
            temp['date'] = temp.index
            temp['code']= codes[i]
            temp['name']= names[i] # names and codes should be the same length
            all.append(temp)
        bar.update()
    all = pd.concat(all, ignore_index = True)
    #pickle.dump(all, open(filename, "wb"))
    if filename:
        write_pickle(all, filename)
    return all

def get_codes_names(filename):
    '''
    Get the latest codes which includes stock and index

    '''
    zs = ts.get_index()
    stock = ts.get_today_all()
    codes = np.concatenate( (zs['code'].unique(), stock['code'].unique()))
    names = np.concatenate( (zs['name'].unique(), stock['name'].unique()))
    out = (codes, names)
    if filename:
        write_pickle(out, filename)
    return out

def load_pickle(filename):
    data = pickle.load(open(filename,"rb"))
    return data

def write_pickle(data,filename):
	'''
	Write data to pickle filename
	'''
	pickle.dump(data, open(filename, "wb"))
