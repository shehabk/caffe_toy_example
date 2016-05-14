import numpy as np
import matplotlib.pyplot as plt
import cv2
import os
# codebase: http://pjreddie.com/projects/mnist-in-csv/
def convert(imgf, labelf, prefix, n):

    if not os.path.exists(os.path.join("mnist",  prefix)):
        os.makedirs(os.path.join("mnist",  prefix ) )

    root  = os.path.dirname(os.path.realpath('__file__'))

    # folder = os.path.join(root, "mnist", prefix )
    folder = os.path.join("mnist", prefix )
    f = open(os.path.join(root,imgf), "rb")
    l = open(os.path.join(root,labelf), "rb")
    o = open(os.path.join(root,prefix)  + ".txt", "w")

    f.read(16)
    l.read(8)


    for i in range(n):
        image = [ord(l.read(1))]
        for j in range(28*28):
            image.append(ord(f.read(1)))
        reshpaedImage = np.reshape( image[1:] , (28 , 28))
        reshapedImageName =  prefix + str(i) + ".png"
        o.write(os.path.join(folder,reshapedImageName) + " " + str(image[0]) + "\n")
        cv2.imwrite(os.path.join(folder,reshapedImageName), reshpaedImage)


    f.close()
    o.close()
    l.close()



if not os.path.exists("mnist"):
    os.makedirs("mnist")
convert("train-images-idx3-ubyte", "train-labels-idx1-ubyte",
        "train", 60000)
convert("t10k-images-idx3-ubyte", "t10k-labels-idx1-ubyte",
        "val", 10000)