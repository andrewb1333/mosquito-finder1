'''imports'''

import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
'''import geopandas as gp'''

import dask.dataframe as dd
import dask.array as da
import dask.bag as db

from sklearn.multioutput import MultiOutputClassifier
from sklearn.svm import LinearSVC
from sklearn.model_selection import train_test_split
from sklearn.metrics import multilabel_confusion_matrix, ConfusionMatrixDisplay



'''data management'''
bothcols=['agency_collection_num','collection_id','code','longitude','latitude','collection_date','aedes_dorsalis_males','aedes_dorsalis_females-mixed',
            'aedes_melanimon_males','aedes_melanimon_females-mixed','aedes_nigromaculis_males',
            'aedes_nigromaculis_females-mixed','aedes_sierrensis_males','aedes_sierrensis_females-mixed',
            'aedes_squamiger_males','aedes_squamiger_females-mixed','aedes_vexans_males','aedes_vexans_females-mixed',
            'aedes_washinoi_males','aedes_washinoi_females-mixed','anopheles_franciscanus_males',
            'anopheles_franciscanus_females-mixed','anopheles_freeborni_males','anopheles_freeborni_females-mixed',
            'anopheles_occidentalis_males','anopheles_occidentalis_females-mixed','anopheles_punctipennis_males',
            'anopheles_punctipennis_females-mixed','culex_apicalis_males','culex_apicalis_females-mixed',
            'culex_erythrothorax_males','culex_erythrothorax_females-mixed','culex_pipiens_males',
            'culex_pipiens_females-mixed','culex_restuans_males','culex_restuans_females-mixed','culex_stigmatosoma_males',
            'culex_stigmatosoma_females-mixed','culex_tarsalis_males','culex_tarsalis_females-mixed','culiseta_incidens_males',
            'culiseta_incidens_females-mixed','culiseta_inornata_males','culiseta_inornata_females-mixed',
            'culiseta_particeps_males','culiseta_particeps_females-mixed']

femalecols =['agency_collection_num','collection_id','code','longitude','latitude','collection_date','aedes_dorsalis_females-mixed',
          'aedes_melanimon_females-mixed','aedes_nigromaculis_females-mixed','aedes_sierrensis_females-mixed',
          'aedes_squamiger_females-mixed','aedes_vexans_females-mixed','aedes_washinoi_females-mixed',
          'anopheles_franciscanus_females-mixed','anopheles_freeborni_females-mixed',
          'anopheles_occidentalis_females-mixed','anopheles_punctipennis_females-mixed','culex_apicalis_females-mixed',
          'culex_erythrothorax_females-mixed','culex_pipiens_females-mixed','culex_restuans_females-mixed',
          'culex_stigmatosoma_females-mixed','culex_tarsalis_females-mixed','culiseta_incidens_females-mixed',
          'culiseta_inornata_females-mixed','culiseta_particeps_females-mixed']

rawdata = dd.read_csv (r'C:\Users\AndrewBurns\Documents\abundance1622.csv', usecols = femalecols)


procols = ['indexed', 'trapid', 'siteid', 'long', 'lat', 'date','dorsalis', 'melanimon', 'nigromaculis', 'sierrensis', 'squamiger',
           'vexans', 'washinoi', 'franciscanus', 'freeborni', 'occidentalis', 'punctipennis', 'apicalis', 'erythrothorax',
           'pipiens','restuans', 'stigmatosoma', 'tarsalis', 'incidens', 'inornata', 'particeps']

'''Genera lists'''
aedes = ['dorsalis', 'melanimon', 'nigromaculis', 'sierrensis', 'squamiger', 'vexans', 'washinoi']
anopheles = ['franciscanus', 'freeborni', 'occidentalis', 'punctipennis']
culex = ['apicalis', 'erythrothorax', 'pipiens', 'restuans', 'stigmatosoma', 'tarsalis']
culiseta = ['incidens', 'inornata', 'particeps']

'''pdata = rawdata.copy()'''
'''for x in femalecols:
    pdata.rename(columns={x: procols[femalecols.index(x)]})'''
rawdata.fillna(0)






