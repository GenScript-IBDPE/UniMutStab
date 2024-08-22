import matplotlib.pyplot as plt
import numpy as np


methods = ["UniMutStab", "DDGun-3D", "DDGun", "MAESTRO", "FoldX", "ESM2_3B", "ESM2_15B"]
M28 = [0.58, 0.44, 0.42, 0.28, 0.38, -0.08, 0.04]
M38 = [0.60, 0.44, 0.41, 0.58, 0.44, 0.08, 0.10]


x = np.arange(len(methods))
width = 0.25

fig, ax = plt.subplots(figsize=(16, 10))

bars1 = ax.bar(x - width/2, M28, width, label='M28', edgecolor='black', linewidth=1.5)
bars2 = ax.bar(x + width/2, M38, width, label='M38', edgecolor='black', linewidth=1.5)


plt.rc('axes', titlesize=36)
plt.rc('axes', labelsize=36)
plt.rc('xtick', labelsize=36)
plt.rc('ytick', labelsize=36) 
plt.rc('legend', fontsize=30) 


ax.set_xlabel('Methods', fontsize=36)
ax.set_ylabel('Pearson correlation coefficient', fontsize=36)
ax.set_title('Performance on Multiple point Datasets', fontsize=36)
ax.set_xticks(x)
ax.set_xticklabels(methods, rotation=30, ha='right', fontsize=36)
ax.legend(fontsize=30)

'''
def add_labels(bars, fontsize=36):
    for bar in bars:
        height = bar.get_height()
        if not np.isnan(height):
            if height < 0:
                ax.annotate(f'{height:.2f}', xy=(bar.get_x() + bar.get_width() / 2, height),
                            xytext=(0, -10), textcoords="offset points", ha='center', va='center', fontsize=fontsize)
            else:
                ax.annotate(f'{height:.2f}', xy=(bar.get_x() + bar.get_width() / 2, height),
                            xytext=(0, 3), textcoords="offset points", ha='center', va='bottom', fontsize=fontsize)

add_labels(bars1, fontsize=36)
add_labels(bars2, fontsize=36)
'''
for spine in ['top', 'right']:
    ax.spines[spine].set_visible(False)
for spine in ['left', 'bottom']:
    ax.spines[spine].set_linewidth(1.5)

fig.tight_layout()
plt.savefig("m28.pdf")
# plt.show()
