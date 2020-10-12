import numpy

import matplotlib.pyplot

a = numpy.zeros( [3,2] )

a[1,1] = 1
a[0,1] = 2
a[1,0] = 9
a[2,1] = 12

#print(a[2,1])

matplotlib.pyplot.imshow(a, interpolation="nearest")

#x = np.linspace(0, 20, 100)
#plt.plot(x, np.sin(x))
#plt.show(block=False)

input('press <ENTER> to continue')