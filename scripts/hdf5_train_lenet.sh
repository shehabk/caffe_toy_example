#!/usr/bin/env sh

CAFFE_ROOT=/media/shehab/D_DRIVE/Codes/CodeCollection/Caffe/caffe-master_18_APR_2016

$CAFFE_ROOT/build/tools/caffe train --solver=models/hdf5_lenet_solver.prototxt
