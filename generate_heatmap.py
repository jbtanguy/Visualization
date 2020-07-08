import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

df = pd.DataFrame({
	'n_min': [1,1,1,1,1,2,2,2,2,3,3,3,4,4,5], 
	'n_max': [1,2,3,4,5,2,3,4,5,3,4,5,4,5,5], 
	'F-m': [0.8373,0.5696,0.45,0.413,0.3945,0.6359,0.5978,0.578,0.5715,0.6849,0.6922,0.6929,0.6958,0.6917,0.5631]})
result = df.pivot(index='n_min', columns='n_max', values='F-m')
heatmap = sns.heatmap(result, annot=True, cmap='gray_r', vmin=0.5, vmax=0.9)
heatmap.xaxis.tick_top()
heatmap.set_xlabel('n_max')    
heatmap.xaxis.set_label_position('top')

plt.show()
