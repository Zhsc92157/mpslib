# mpslib_example.py
# example of using mpslib.py

#%%
import mpslib as mps;
import matplotlib.pyplot as plt;
import numpy as np;
from scipy import squeeze


O1 = mps.mpslib(method='mps_snesim_tree', n_real = 1)
O2 = mps.mpslib(method='mps_snesim_tree', n_real = 1)

#%%  Load and set training image
ti = mps.trainingimages.strebelle()[0]
ti2=np.transpose(ti)

O1.ti=ti
O2.ti=np.swapaxes(ti,2,1)

#%% SIMULATE
O1.run()
O2.run()

#%% plot the TI's and simulation results
plt.set_cmap('hot')
fig1 = plt.figure(1)
plt.subplot(2,2,1)
plt.title('TI')
plt.imshow(squeeze(O1.ti))
plt.subplot(2,2,2)
plt.imshow(squeeze(O2.ti))
plt.title('TI 2')

plt.subplot(2,2,3)
plt.imshow(squeeze(O1.sim[0]), interpolation='none')
plt.subplot(2,2,4)
plt.imshow(squeeze(O2.sim[0]), interpolation='none')

fig1.suptitle(O1.method, fontsize=16)
plt.savefig('mpslib_example_2_'+O1.method+'.png', dpi=600)
plt.show();

