######################################
#             make images            #
#           black and white          #
#                V0.01               #
######################################
import matplotlib.pyplot as plt
import matplotlib.image as mpimg
import numpy as np

# enter image name and path here
filename = 'pixels3.png'

#img = mpimg.imread(filename)
img_array = np.array(mpimg.imread(filename))
height, width , z= img_array.shape

# show image before any change
plt.imshow(img_array)
plt.show()

# change values of pixels
for i in range(0,height):
    for j in range(0,width):
        for k in range(0,3):
            # you can use min(), max() or average() functions here
            img_array[i,j,k] = max(img_array[i,j,0], img_array[i,j,1], img_array[i,j,2])

# show image after changes
plt.imshow(img_array)
plt.show()
