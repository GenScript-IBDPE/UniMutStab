#!/usr/bin/env python3
# -*- coding: utf-8 -*-=

import seaborn as sns
import matplotlib.pyplot as plt
from matplotlib.colors import LinearSegmentedColormap
import pandas as pd
import math
import numpy as np

alphabet = 'AGVLISTCMDENQKFYWPHR'
seq = 'TETYKYDDKREAEKAAEEFRRRGITVTVEERNGTWVLESK'
aas = []
for i in range(40):
    loc = i+1
    aa_pre = seq[i]
    aa_after = [aa_pre+str(loc)+j for j in alphabet]
    aas.append(aa_after)

df = pd.read_csv('/path/results.csv')
dict_mut_pred = dict(zip(df['mut_type'], df['pred']))

pred1 = [dict_mut_pred[j] if j in list(dict_mut_pred.keys()) else math.nan for i in aas for j in i]
pred1 = np.array(pred1).reshape(40,20)

plt.figure(figsize=(22, 8), dpi=600)
data = pred1.T
x = [i for i in range(len(seq))]
y = [i for i in alphabet]
ax = sns.heatmap(data, annot=False, cmap='coolwarm', linewidths=0,
                 xticklabels = x, yticklabels = y, vmin=-1, vmax=1)

plt.xticks(fontsize=30)
plt.yticks(fontsize=22)
labels = ax.get_xticklabels()
for i, label in enumerate(labels):
    if i % 4 != 0:  
        label.set_visible(False)
    else:
        label.set_rotation(0) 
        label.set_fontsize(40)  
        label.set_ha('right') 
        label.set_va('top') 
        label.set_text(label.get_text() + ' →') 
        
colorbar = ax.collections[0].colorbar
colorbar.set_ticks([-1, 0, 1])
colorbar.ax.tick_params(labelsize=35)
colorbar.set_ticklabels(['-1', '0', '1'])
plt.savefig('/path/heatmap.pdf', format='pdf')
plt.show()
