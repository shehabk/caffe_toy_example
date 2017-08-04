#!/usr/bin/env sh

CAFFE_ROOT=/home/shehabk/codes/caffe/caffe-sc-histogram
$CAFFE_ROOT/build/tools/caffe train --solver=models/imageData_lenet_solver.prototxt
