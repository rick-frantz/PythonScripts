import os
from os import listdir, walk
from os.path import isfile, join
import csv
# import glob

mypath = "N:\Engineering\Development Group\Water\Water Tap Cards\Tap Cards"
# mypath = "N:\Engineering\Development Group\Water\Water Tap Cards\Tap Cards\E\Edinburgh Road"
exclude = set(['W'])

f = []
for (dirpath, dirnames, filenames) in walk(mypath, topdown=True):
    dirnames[:]= [d for d in dirnames if d not in exclude]
    f.extend(os.path.splitext(name)[0] for name in filenames)

print("Found " + str(len(f)) + " addresses")

csvout = 'G:\\GIS Data\\Users Engineering\\Projects\\Utility Editing\\Water Tap Cards\\Addresses.csv'

header = ['Address']
with open(csvout, 'w') as file:
    writer = csv.DictWriter(file, fieldnames=header, lineterminator='\n')
    writer.writeheader()

    for i in f:
        writer.writerow({'Address':i})

print("All done.")