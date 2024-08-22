import matplotlib.pyplot as plt
import numpy as np
 
methods = ["Ours", "DDGun-3D", "DDGun", "MAESTRO", "FoldX", "ESM2_3B", "ESM2_15B"]
S98 = [0.46, 0.33, 0.32, 0.19, 0.35, -0.07, 0.18]
M218 = [0.56, 0.55, 0.46, 0.15, 0.41, -0.02, -0.13]
 

x = np.arange(len(methods)) 
width = 0.35
 
fig, ax = plt.subplots(figsize=(16, 10))
 
bars1 = ax.bar(x - width/2, S98, width, label='S98', edgecolor='black', linewidth=1.5)
bars2 = ax.bar(x + width/2, M218, width, label='M218', edgecolor='black', linewidth=1.5)
 

plt.rc('axes', titlesize=36)
plt.rc('axes', labelsize=36) 
plt.rc('xtick', labelsize=36) 
plt.rc('ytick', labelsize=36)
plt.rc('legend', fontsize=30) 
 

#ax.set_xlabel('Methods')
ax.set_ylabel('Pearson correlation coefficient', fontsize=36)
ax.set_title('Performance on "Variant to variant" Datasets', fontsize=36)
ax.set_xticks(x)
ax.set_xticklabels(methods, rotation=30, ha='right', fontsize=36)
ax.legend()
 

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
'''
for spine in ['top', 'right']:
    ax.spines[spine].set_visible(False)
for spine in ['left', 'bottom']:
    ax.spines[spine].set_linewidth(1.5)
 
fig.tight_layout()
plt.savefig('Figure2d.pdf', dpi=600)
#plt.show()