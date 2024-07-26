
from matplotlib import image
from matplotlib import pyplot
import os

path = os.path.dirname(os.path.abspath(__file__))
filename = path + '/' + 'lenna copy.bmp'
country = path+'/' + 'usa.png'
data = image.imread(filename)
country_data = image.imread(country)
country_dimensions = country_data.shape


plot_data = data.copy()
for width in range(country_dimensions[1]):
    for height in range(country_dimensions[0]):
        plot_data[height][width+12][0]= country_data[height][width][0]*255
        plot_data[height][width+12][1] =country_data[height][width][1]*255
        plot_data[height][width+12][2] =country_data[height][width][2]*255


image.imsave(path+'/'+'lenna-mod.jpg', plot_data)


pyplot.imshow(plot_data)
pyplot.show()