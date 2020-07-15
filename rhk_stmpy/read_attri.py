import numpy as np


## Wan-Ting borrow this function from io from stmpy folder.
def _make_attr(self, attr, names, data):
    '''
    Trys to give object an attribute from self.data by looking through
    each key in names.  It will add only the fist match, so the order of
    names dictates the preferences.

    Inputs:
        attr    - Required : Name of new attribute
        names   - Required : List of names to search for
        data    - Required : Name of a current attribute in which the new
                             attribute is stored.

    Returns:
        1   - If successfully added the attribute
        0   - If name is not found.

    History:
        2017-08-11  - HP : Initial commit.
        2017-08-24  - HP : Now uses grid z value for Z attribute.
    '''
    dat = getattr(self, data)
    for name in names:
       if name in dat.keys():
            setattr(self, attr, dat[name])
            return 1
    return 0








def loadsm4(filePath):
    '''
    The load_sm4 can now output several attributes: including I, iv, LIY, didv, didvStd, Z, en

    Inputs:
        filePath- Required : Name of the file
        
    Returns:
        self.info     - information of the pages
        self.header   - details of the pages
        self.data     - all the data from all of the pages
        self.en       - x axis for the spectropscopy data
        self.Z        - Topography of the data
        self.I        - Spectropscopy of the current data
        self.iv       - Average of the current spectroscopy data
        self.LIY      - Spectropscopy of the didv data
        self.didv     - Average of the didv spectroscopy data
        self.didvStd  - Standard deviation of all the didv spectropscopy data
   
    History:
        2020-07-15  - WT : Initial commit.
      
    '''
    import rhk_stmpy.rhk_sm4 as sm4
    f = sm4.load_sm4(filePath)
    self = Spy()
    self.info = {}
    self.info = f.print_info()
        
    name = f.print_info().iloc[:, 0].to_numpy()
    it = f.print_info().iloc[:, 1].to_numpy()
    namef = np.char.strip(it.astype(str), 'DATA_')
    names = namef + name
        
        
    label = {}
    for ix, item in zip(range(0,len(names)), names):
        label[ix] = item
        
    self.data = {}
    for ix, line in enumerate(f):
        self.data[ix] = f[ix].data  
        
    self.header = {}
    for ix, line in enumerate(f):
        self.header[ix] = f[ix].attrs
         
        
    def getf(channel):
        res = 100
        for key in label:
            if(label[key] == channel):
                res = list(label.values()).index(channel) 
        return(res)
            
                    
    liy = getf('LINELIA Current')
    i = getf('LINECurrent')
    z = getf('IMAGETopography')
        
    self.en = {}
    if liy < 100:
        self.en = f[liy].coords[1][1]
    else:
        self.en = f[0].coords[1][1]
  
        
    if _make_attr(self, 'LIY', [liy], 'data'):
        self.didv = np.mean(self.LIY, axis=0)
        self.didvStd = np.std(self.LIY, axis=0)
    else:
        print('ERR: LIY channel not found')
        
    if _make_attr(self, 'I',  [i], 'data'):
        self.iv = np.mean(self.I,  axis=0)
    else:
        print('ERR: Current not found')
                  
    if _make_attr(self, 'Z',  [z], 'data'):
        self.Z = self.Z
    else:
        print('ERR: Z channel not found')
    return self
        
        
        
class Spy(object):
    def __init__(self):
        pass