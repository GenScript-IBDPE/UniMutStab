import matplotlib.pyplot as plt
import numpy as np

methods = [
    "ProSTAGE", "MAESTRO", "ThermoMPNN", "Model_single", "ACDC-NN",
    "INPS-Seq", "PROST", "INPS3D", "Mutate_everthing", "ProteinMPNN",
    "DDGun", "ESM2_15B", "ESM2_3B"
]
S462_direct = [
    0.52, 0.43, 0.42, 0.41, 0.38, 0.37, 0.37, 0.35, 0.35, 0.35, 0.3, 0.008, 0.01
]
S462_inverse = [
    0.5, 0.18, 0.43, 0.4, 0.37, 0.36, 0.38, 0.31, 0.25, 0.35, 0.29, 0.008, 0.01
]

x = np.arange(len(methods))
width = 0.35

fig, ax = plt.subplots(figsize=(16, 10))
bars1 = ax.bar(x - width/2, S462_direct, width, label='S462_direct', edgecolor='black', linewidth=1.5)
bars2 = ax.bar(x + width/2, S462_inverse, width, label='S462_inverse', edgecolor='black', linewidth=1.5)


plt.rc('axes', titlesize=25)
plt.rc('axes', labelsize=18)
plt.rc('xtick', labelsize=14)
plt.rc('ytick', labelsize=16)
plt.rc('legend', fontsize=18) 


ax.set_xlabel('Methods')
ax.set_ylabel('Pearson correlation coefficient')
ax.set_title('S462 dataset')
ax.set_xticks(x)
ax.set_xticklabels(methods, rotation=45, ha='right')
ax.legend()


def add_labels(bars, fontsize=10):
    for bar in bars:
        height = bar.get_height()
        ax.annotate(f'{height:.2f}', xy=(bar.get_x() + bar.get_width() / 2, height),
                    xytext=(0, 3), textcoords="offset points", ha='center', va='bottom', fontsize=fontsize)

add_labels(bars1, fontsize=12)
add_labels(bars2, fontsize=12)


for spine in ['top', 'right']:
    ax.spines[spine].set_visible(False)
for spine in ['left', 'bottom']:
    ax.spines[spine].set_linewidth(1.5)

fig.tight_layout()
plt.show()