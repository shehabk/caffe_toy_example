import h5py
import numpy as np
import cv2
import os

import numpy as np
import matplotlib.pyplot as plt
import cv2
import os
# codebase: http://pjreddie.com/projects/mnist-in-csv/
def convert( imgListFileName, phase , sizedata , sizelabel ):

    hdfFileName =  os.path.join("hdf5",phase) + '.hdf5'
    txtFileName = os.path.join('hdf5', phase) + '.txt'


    hdfFile  =  h5py.File( hdfFileName, "w")
    data  = hdfFile.create_dataset('data', sizedata , dtype='f')
    label = hdfFile.create_dataset('label', sizelabel, dtype='f')

    with open(imgListFileName) as f:
        lines = f.readlines()

    for idx, line in enumerate(lines):
        imPath, imLabel =  line.split()
        img = cv2.imread( imPath )
        img = img.transpose(2,0,1)
        data[idx,...] = img/256.0
        label[idx] = int(imLabel)

    hdfFile.close()

    with open( txtFileName , "w") as txtfile:
        folderpath = os.path.dirname(os.path.realpath('__file__'))
        txtfile.write(os.path.join(folderpath,'hdf5',phase) + '.hdf5\n')







if not os.path.exists("hdf5"):
    os.makedirs("hdf5")

convert('train.txt', 'train' , (60000,3,28,28), (60000,1) )
convert('val.txt', 'val' , (10000,3,28,28), (10000,1) )