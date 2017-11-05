import numpy as np
import matplotlib as mpl
# mpl.use Must come after importing mpl, but before importing plt

#mpl.use("Agg")   # Does nothing on JF Linux Mint
mpl.use('TkAgg') # JF Required on my Linux Mint for windowed ouput
#mpl.use('PDF')   # PDF file generation
# mpl.use('WXAgg')  # ImportError: No module named 'wx'
import matplotlib.pyplot as plt

from mpl_toolkits.mplot3d import Axes3D
from matplotlib import cm

def gen_plot():
    print('Generating...')

    # Silly example data
    X = np.arange(-5, 5, 0.25)
    Y = np.arange(-5, 5, 0.25)
    X, Y = np.meshgrid(X, Y)
    R = np.sqrt(X**2 + Y**2)
    Z = np.sin(R)

    # Make the plot
    fig  = plt.figure()
    ax   = fig.gca(projection="3d")
    surf = ax.plot_surface(X, Y, Z, rstride=1, cstride=1, cmap=cm.coolwarm,
                           linewidth=0, antialiased=False)
    ax.set_zlim(-1.01, 1.01)
    fig.colorbar(surf, shrink=0.5, aspect=5)

def pltfile(ext):
    fn = 'pltjf.' + ext
    print('Plotting to file : "{0}"'.format(fn))
    plt.savefig(fn)
    
def use_plot():    
    gen_plot()    
    print('Close plot window to continue.')
    plt.show()  # Blocking-Interactive plot) 

def view_plot():    
    gen_plot()    
    plt.show(block=False)  # Non blocking (but non-Interactive plot)

def save_plot():  
    gen_plot() 
    pltfile('png')  
    pltfile('svg')
    pltfile('pdf')

save_plot()
view_plot()
 
# Note that the inteactive mode ends up clearing the file?

import time
time.sleep(10)

print('- All done')


