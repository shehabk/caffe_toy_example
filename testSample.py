# set up Python environment: numpy for numerical routines, and matplotlib for plotting
import cv2
import numpy as np
import matplotlib.pyplot as plt

# display plots in this notebook

import os

# set display defaults
plt.rcParams['figure.figsize'] = (5, 5)        # large images
plt.rcParams['image.interpolation'] = 'nearest'  # don't interpolate: show square pixels
plt.rcParams['image.cmap'] = 'gray'  # use grayscale output rather than a (potentially misleading) color heatmap


# The caffe module needs to be on the Python path;
#  we'll add it here explicitly.
import sys
caffe_root = '/home/shehabk/codes/caffe/caffe-sc-histogram'
sys.path.insert(0, caffe_root + 'python')
import caffe
# If you get "No module named _caffe", either you have not built pycaffe or you have the wrong path.


caffe.set_mode_cpu()

model_def = 'models/deploy.prototxt'
model_weights = 'models/snapshot/imageData_lenet_iter_10000.caffemodel'
sampleImgPath = 'data/sample/val111.png'

net = caffe.Net(model_def,      # defines the structure of the model
                model_weights,  # contains the trained weights
                caffe.TEST)     # use test mode (e.g., don't perform dropout)

sampleImg = cv2.imread(sampleImgPath);
plt.imshow(sampleImg)
plt.show()

transformedImg = sampleImg.transpose(2,0,1) # to bring the channel as the first dimension of the img
transformedImg = transformedImg/256.0 ;


net.blobs['data'].data[...] = transformedImg ;

### perform classification
output = net.forward()
output_prob = output['prob'][0]  # the output probability vector for the first image in the batch
top_inds = output_prob.argsort()[::-1][:10]  # reverse sort and take five largest items

for idx in top_inds:
    print 'Probability of %d is %lf' % (idx, output_prob[idx])