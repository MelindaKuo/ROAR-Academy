from matplotlib import image
from matplotlib import pyplot
import os


path = os.path.dirname(os.path.abspath(__file__))
filename = path + '/' + 'lenna copy.bmp'
country_photo = path+ '/' + 'usa.png'
lenna = image.imread(filename)
country = image.imread(country_photo)


country_dimensions = country.shape

plot_data = lenna.copy()
for width in range(country_dimensions[1]):
    for height in range(country_dimensions[0]):
        plot_data[height][width+12][0] = country[height][width][0]  * 255
        plot_data[height][width+12][1] = country[height][width][1]  *255
        plot_data[height][width+12][2] = country[height][width][2]  *255


image.imsave(path+'/'+'lenna-mod.jpg', plot_data)

# use pyplot to plot the image
pyplot.imshow(plot_data)
pyplot.show()