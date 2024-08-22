import matplotlib.pyplot as plt
import numpy as np


methods = ["UniMutStab", "FoldX", "ESM2_3B", "ESM2_15B"]
PrP = [0.79, 0.06, -0.21, -0.20]
Endolysin = [0.52, -0.22, -0.38, -0.05]
Thermonuclease = [0.55, 0.55, 0.33, 0.55]
Indels732 = [0.51, np.nan, 0.005, 0.000] 


x = np.arange(len(methods))
width = 0.2

fig, ax = plt.subplots(figsize=(16, 10))

bars1 = ax.bar(x - 1.5 * width, PrP, width, label='PrP', edgecolor='black', linewidth=1.5)
bars2 = ax.bar(x - 0.5 * width, Endolysin, width, label='Endolysin', edgecolor='black', linewidth=1.5)
bars3 = ax.bar(x + 0.5 * width, Thermonuclease, width, label='Thermonuclease', edgecolor='black', linewidth=1.5)
bars4 = ax.bar(x + 1.5 * width, Indels732, width, label='Indels732', edgecolor='black', linewidth=1.5)

plt.rc('axes', titlesize=36)
plt.rc('axes', labelsize=36) 
plt.rc('xtick', labelsize=36)  
plt.rc('ytick', labelsize=36) 
plt.rc('legend', fontsize=30) 


#ax.set_xlabel('Methods')
ax.set_ylabel('Pearson correlation coefficient', fontsize=36)
ax.set_title('Performance on Indels Datasets', fontsize=36)
ax.set_xticks(x)
ax.set_xticklabels(methods, ha='center')


ax.legend(bbox_to_anchor=(0.85, 1), loc='upper right')

'''

def add_labels(bars, fontsize=36):
    for bar in bars:
        height = bar.get_height()
        if not np.isnan(height):
            if height < 0:
                ax.annotate(f'{height:.2f}', xy=(bar.get_x() + bar.get_width() / 2, height),
                            xytext=(0, -3), textcoords="offset points", ha='center', va='top', fontsize=fontsize)
            else:
                ax.annotate(f'{height:.2f}', xy=(bar.get_x() + bar.get_width() / 2, height),
                            xytext=(0, 3), textcoords="offset points", ha='center', va='bottom', fontsize=fontsize)

add_labels(bars1, fontsize=36)
add_labels(bars2, fontsize=36)
add_labels(bars3, fontsize=36)
add_labels(bars4, fontsize=36)
'''
for spine in ['top', 'right']:
    ax.spines[spine].set_visible(False)
for spine in ['left', 'bottom']:
    ax.spines[spine].set_linewidth(1.5)

fig.tight_layout()
plt.savefig('indels.pdf')
#plt.show()
