# CaffeToyExampleMnist
A full caffe experiment using MNIST dataset. It includes organizing the data into ImageList, lmdb, and hdf5 format. Training the lenet network with data and finally test the network with a single image.

Prerequisites:

	1) Install caffe, with python layers, and pycaffe.
	2) Anaconda for python (https://docs.continuum.io/anaconda/install ).



Data Preparation:

	1) Download the code ( There should be a folder named 'CaffeToyExampleMnist' )
	2) Open terminal and then 'cd' to the the directory 'data'
	3) From the directory data run the script get_mnist.sh
	    sample command: 
	    	shehab@CSE-TONG-R2:~home/DeepLearningGroup/CaffeToyExampleMnist/data$ ./get_mnist.sh

	   This script will download mnist dataset in some compressed files.

	4) From the same directory run the python script  'ImageListAndImage.py'. This script will
	   extract the the images from the compressed files and organize them inside a folder 'mnist'.
	   It will also generate two text files named train.txt , and val.txt which can be used by caffe
	   for training and validation of the network.

	   sample command: 
	    	shehab@CSE-TONG-R2:~home/DeepLearningGroup/CaffeToyExampleMnist/data$ python ImageListAndImage.py

	5) Open the script 'create_mnist_lmdb.sh' in a text editor and make necessary changes to CAFFE_ROOT , TRAIN_DATA_ROOT, VAL_DATA_ROOT. Run the script create_mnist_lmdb.sh, it will create lmdb databases using the train.txt and test.txt files. lmdb is another way to feed data to caffe. This script uses the utility provided by caffe to create lmdb dataset.

		sample command: 
	    	shehab@CSE-TONG-R2:~home/DeepLearningGroup/CaffeToyExampleMnist/data$ python ./create_mnsit_lmdb.sh

	6) Run the python script 'hdf5fromImgList.py', this will create hdf5 database from the Images, which is another way of to feed data to
	   caffe.

Train and Validataion: 

	1) With a text editor modify all the files inside 'CaffeToyExampleMnist/scripts', ie change the CAFFE_ROOT to your own caffe root.
	2) In terminal move back to the directory 'CaffeToyExampleMnist', using 'cd ..'
	3) Now from here run any scripts to train the corresponding network.  
	sample command: 
	    	shehab@CSE-TONG-R2:~home/DeepLearningGroup/CaffeToyExampleMnist$ ./scripts/hdf5_train_lenet.sh

	It will use the hdf5_lenet_solver.prototxt hdf5_lenet_train_test.prototxt present in the 'CaffeToyExampleMnist/models' to run the 
	training and validation. It uses the hdf5 database which was generated in the data generation step.

Test:

	1) Modify the python script testSample.py  and run the script to see the result of a specific image. The variables to change are
	caffe_root , model_def, model_weights,sampleImgPath. 


