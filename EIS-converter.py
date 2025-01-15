# -*- coding: utf-8 -*-
"""
Created on Wed Jan 15 15:30:44 2025

@author: VX47TT
"""

import os
import pandas as pd

if not 'Neware Data' in os.listdir():
    os.mkdir('Neware Data')
    
if not 'EC-lab Data' in os.listdir():
    os.mkdir('EC-lab Data')

neware_files = os.listdir('Neware Data')

for file in neware_files:
    neware_file = pd.read_csv('Neware Data/' + file, header=10)
    neware_file = neware_file[neware_file['Status']=='EIS']
    
    EC_file = pd.DataFrame()
    EC_file['Freq/Hz'] = neware_file['SetFreq'].to_numpy(dtype=float)
    EC_file['Re(Z)/Ohm'] = neware_file['Zreal1'].to_numpy(dtype=float)
    EC_file['-Im(Z)/Ohm'] = -neware_file['Zimg1'].to_numpy(dtype=float)
    EC_file.to_csv('EC-lab Data/' + file, index=False)
