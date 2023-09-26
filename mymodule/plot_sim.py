#! /usr/bin/env python
'''
Code to create plot showing right ascension and declination coordinates of a star catalogue
'''
import matplotlib.pyplot as plt
import pandas as pd

path = '/Users/Ryan/Software/ADACS_Workshop/sky_catalogue'

coordinates = pd.read_csv(path+'/data/output/catalogue.csv')

plt.scatter(coordinates['ra'],coordinates['dec'],s=10)
plt.xlabel('Right Ascension (deg)')
plt.ylabel('Declination (deg)')

plt.show()
