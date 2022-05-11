import numpy as np 
import seaborn as sns 

class viz:
    '''Define the default visualize configure
    '''
    Blue    = .95 * np.array([ 46, 107, 149]) / 255
    Green   = .95 * np.array([  0, 135, 149]) / 255
    Red     = .95 * np.array([199, 111, 132]) / 255
    Yellow  = .95 * np.array([220, 175, 106]) / 255
    Purple  = .95 * np.array([108,  92, 231]) / 255
    Palette = [Blue, Red, Green, Yellow, Purple]
    Greens  = [np.array([8,154,133]) / 255, np.array([118,193,202]) / 255] 
    dpi     = 200
    sfz, mfz, lfz = 11, 13, 16
    lw, mz  = 2.5, 6.5

    @staticmethod
    def get_style(): 
        sns.set_context('talk')
        sns.set_style("ticks", {'axes.grid': False})
        
viz.get_style()