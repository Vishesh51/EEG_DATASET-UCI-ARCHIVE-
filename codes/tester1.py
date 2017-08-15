import os                   #box plot
from scipy.stats import *
import pickle as pl
from nltk.tokenize import word_tokenize
import pandas as pd
import numpy as np
from pandas import plotting
import plotly.figure_factory as ff
import plotly.plotly as py
import plotly.graph_objs as go
import matplotlib.pyplot as plt
from scipy.stats import norm
import ast
import seaborn
import pandas as pd
import scipy

dir_name='C:\\Users\\Saumya\\Desktop\\smni_eeg_data'

i = 0
os.chdir(dir_name)


mean= [[ 2.10562009 , 2.29609704 , 0.32164538 , 1.04972613 ,-0.19978566 , 0.5747783,
 -1.99107771 , 1.16958567 ,-3.21792801 , 0.61148176],
 [-6.68528718 , 0.18572024 ,-2.01833169 , -2.31188654 , -2.6887746 , -2.65099137,
 -0.95367141 ,-4.19052523, -5.24838027 ,-4.42598224],
 [ 2.00887359 ,-1.32247118 ,-2.84299939 ,-2.26290119 ,-3.40233236 ,-2.66604208,
 -3.27599544, -3.87930433, -4.43998796, -2.0551646 ],
[-2.23398006, -1.55343536, -1.00424328 , 0.75614508 , 2.74500261, -1.66698498,
  3.53602341 , 2.31842582 , 3.82492448 , 2.10852554],
[ 0.10376833 ,-4.01058726 ,-5.17869981, -6.91027253, -1.32858634, -7.17423945,
 -4.24552815, -0.86084939, -1.23227484 ,-6.93129655],
[-3.7931981,  -8.32937243 ,-2.4994021 , -7.11710495, -0.70963085, -4.59666308,
 -4.35177052, -5.25894582, -5.35001709, -6.28746534]]

twosample_results = scipy.stats.ttest_ind(mean[2], mean[5])

matrix_twosample = [
    ['', 'Test Statistic', 'p-value'],
    ['Sample Data', twosample_results[0], twosample_results[1]]
]

twosample_table = ff.create_table(matrix_twosample, index=True)
print(twosample_table)
py.plot(twosample_table, filename='twosample-table')

for i in range(3):
    plt.subplot(2,2,i+1)
    plt.boxplot(mean[i],mean[i+3],'gD')
    
plt.show()
