import matplotlib.pyplot
from numpy.core.multiarray import datetime_as_string
import matplotlib.pyplot as plt
import matplotlib.image as mpimg
from mpl_toolkits.axes_grid1 import make_axes_locatable
import numpy as np
import scipy
from scipy import stats
import collections

img = mpimg.imread('Tartan_Ribbon.jpg')


fig, ax = plt.subplots(2, 2, figsize=(13, 13))
my_img = ax[0, 0].imshow(img)
ax[0, 0].set_title('original image')
divider = make_axes_locatable(ax[0, 0])
cax1 = divider.append_axes("right", size="5%", pad=0.05)
plt.colorbar(my_img, ax=ax[0, 0], cax=cax1)

my_img_red = ax[0, 1].imshow(img[:, :, 0], cmap='Reds') #default colormap is viridis
ax[0, 1].set_title('Red is being plotted')
divider = make_axes_locatable(ax[0, 1])
cax2 = divider.append_axes("right", size="5%", pad=0.05)
plt.colorbar(my_img_red, ax=ax[0, 1], cax=cax2)

my_img_green = ax[1, 0].imshow(img[:, :, 1], cmap='Greens')
ax[1, 0].set_title('Green is being plotted')
divider = make_axes_locatable(ax[1, 0])
cax3 = divider.append_axes("right", size="5%", pad=0.05)
plt.colorbar(my_img_green, ax=ax[1, 0], cax=cax3)

my_img_blue = ax[1, 1].imshow(img[:, :, 0], cmap='Blues')
ax[1, 1].set_title('Blue is being plotted')
divider = make_axes_locatable(ax[1, 1])
cax4 = divider.append_axes("right", size="5%", pad=0.05)
plt.colorbar(my_img_blue, ax=ax[1, 1], cax=cax4)

plt.tight_layout()
fig.suptitle('4 panel plot')
fig.show()



fig_1 , ax_1 = plt.subplots(1, 3, figsize=(40, 20))

#red band
value_red = img[:, :, 0]
data_red = value_red.ravel()
hist_R = ax_1[0].hist(data_red, bins=500)
ax_1[0].annotate('min(24, 1)', xy=(24, 1), xycoords='data',xytext=(6, 16) , textcoords='offset points' , arrowprops=dict(arrowstyle='->', connectionstyle='angle, angleA=-90, angleB=180, rad=5'))
ax_1[0].plot(24, 1, marker='o', markersize=5, markerfacecolor='black',markeredgecolor='black')
ax_1[0].annotate('max(255,7)', xy=(255, 7), xycoords='data', xytext=(6, 16), textcoords='offset points', arrowprops=dict(arrowstyle='->', connectionstyle='angle, angleA=-90, angleB=180, rad=5'))
ax_1[0].plot(255, 7, marker='o', markersize=5, markerfacecolor='black',markeredgecolor='black')
ax_1[0].annotate('mode(81,20156)', xy=(81,20156), xycoords='data', xytext=(6, 16), textcoords='offset points', arrowprops=dict(arrowstyle='->', connectionstyle='angle, angleA=-90, angleB=180, rad=5'))
ax_1[0].plot(81, 20156, marker='o', markersize=5, markerfacecolor='black',markeredgecolor='black')
ax_1[0].annotate('median(83,19960)', xy=(81,19960), xycoords='data', xytext=(20, 60), textcoords='offset points', arrowprops=dict(arrowstyle='->', connectionstyle='angle, angleA=-90, angleB=180, rad=5'))
ax_1[0].plot(83, 19960, marker='o', markersize=5, markerfacecolor='black',markeredgecolor='black')
ax_1[0].axvline(93.78289191919193, color='r', linestyle='-.', linewidth=1)
ax_1[0].text(100, 60000, 'Mean: {:.2f}'.format(93.78289191919193), c='r')
ax_1[0].set_title('red band')
red_mode = scipy.stats.mode(data_red)
print(red_mode)
std_Red = np.std(value_red)
mask_array_red_ub = np.ma.masked_where(data_red > 93.78289191919193 + std_Red, data_red)
mask_array_red_lb = np.ma.masked_where(mask_array_red_ub < 93.78289191919193 - std_Red, mask_array_red_ub)
ax_1[0].hist(mask_array_red_lb, bins=100)


#green band
value_green = img[:, :, 1]
data_green = value_green.ravel()
hist_G = ax_1[1].hist(data_green, bins=500)
ax_1[1].annotate('min(19, 2)', xy=(19, 2), xycoords='data',xytext=(6, 16) , textcoords='offset points' , arrowprops=dict(arrowstyle='->', connectionstyle='angle, angleA=-90, angleB=180, rad=5'))
ax_1[1].plot(19, 2, marker='o', markersize=5, markerfacecolor='black',markeredgecolor='black')
ax_1[1].annotate('max(243,2)', xy=(243, 2), xycoords='data', xytext=(6, 16), textcoords='offset points', arrowprops=dict(arrowstyle='->', connectionstyle='angle, angleA=-90, angleB=180, rad=5'))
ax_1[1].plot(243, 2, marker='o', markersize=5, markerfacecolor='black',markeredgecolor='black')
ax_1[1].annotate('mode(79,21332)', xy=(79,21332), xycoords='data', xytext=(6, 16), textcoords='offset points', arrowprops=dict(arrowstyle='->', connectionstyle='angle, angleA=-90, angleB=180, rad=5'))
ax_1[1].plot(79, 21332, marker='o', markersize=5, markerfacecolor='black',markeredgecolor='black')
ax_1[1].annotate('median(78,21109)', xy=(78,21109), xycoords='data', xytext=(20, 60), textcoords='offset points', arrowprops=dict(arrowstyle='->', connectionstyle='angle, angleA=-90, angleB=180, rad=5'))
ax_1[1].plot(78, 21109, marker='o', markersize=5, markerfacecolor='black',markeredgecolor='black')
min_green = np.amin(data_green)
max_green = np.amax(data_green)
mode_green = scipy.stats.mode(data_green)
print(mode_green)
median_green = np.median(data_green)
mean_green = np.mean(data_green)
green_element = collections.Counter(data_green)
green_element[min_green]
ax_1[1].axvline(86.23330505050505, color='r', linestyle='-.', linewidth=1)
ax_1[1].text(95, 60000, 'Mean: {:.2f}'.format(86.23330505050505), c='r')
ax_1[1].set_title('green band')

std_Green = np.std(value_green)
mask_array_green_ub = np.ma.masked_where(data_green > 86.23330505050505 + std_Green, data_green)
mask_array_green_lb = np.ma.masked_where(mask_array_green_ub < 86.23330505050505 - std_Green, mask_array_green_ub)
ax_1[1].hist(mask_array_green_lb, bins=100)


#blue band
value_blue = img[:, :, 2]
data_blue = value_blue.ravel()
hist_B = ax_1[2].hist(data_blue, bins=500)
#blue band min, max, mean, mode, median plot and arrow
ax_1[2].annotate('min(6, 1)', xy=(6, 1), xycoords='data',xytext=(6, 16) , textcoords='offset points' , arrowprops=dict(arrowstyle='->', connectionstyle='angle, angleA=-90, angleB=180, rad=5'))
ax_1[2].plot(6, 1, marker='o', markersize=5, markerfacecolor='black',markeredgecolor='black')
ax_1[2].annotate('max(250,2)', xy=(250, 2), xycoords='data', xytext=(6, 16), textcoords='offset points', arrowprops=dict(arrowstyle='->', connectionstyle='angle, angleA=-90, angleB=180, rad=5'))
ax_1[2].plot(250, 2, marker='o', markersize=5, markerfacecolor='black',markeredgecolor='black')
ax_1[2].annotate('mode(57,24254)', xy=(57,24254), xycoords='data', xytext=(6, 16), textcoords='offset points', arrowprops=dict(arrowstyle='->', connectionstyle='angle, angleA=-90, angleB=180, rad=5'))
ax_1[2].plot(57, 24254, marker='o', markersize=5, markerfacecolor='black',markeredgecolor='black')
ax_1[2].annotate('median(78,5754)', xy=(78,5754), xycoords='data', xytext=(6, 40), textcoords='offset points', arrowprops=dict(arrowstyle='->', connectionstyle='angle, angleA=-90, angleB=180, rad=5'))
ax_1[2].plot(78, 5754, marker='o', markersize=5, markerfacecolor='black',markeredgecolor='black')

min_blue = np.amin(data_blue)
max_blue = np.amax(data_blue)
mode_blue = scipy.stats.mode(data_blue)
median_blue = np.median(data_blue)
mean_blue = np.mean(data_blue)
blue_element = collections.Counter(data_blue)
#line that indicate mean on the graph
ax_1[2].axvline(69.10403737373737, color='r', linestyle='-.', linewidth=1)
ax_1[2].text(75, 70000, 'Mean: {:.2f}'.format(69.10403737373737), c='r')
ax_1[2].set_title('blue band')
print(median_blue)
# 1 sd from mean
std_Blue = np.std(data_blue)
mask_array_blue_ub = np.ma.masked_where(data_blue > 69.10403737373737 + std_Blue, data_blue)
mask_array_blue_lb = np.ma.masked_where(mask_array_blue_ub < 69.10403737373737 - std_Blue, mask_array_blue_ub)
ax_1[2].hist(mask_array_blue_lb, bins=100)

fig_1.suptitle('color values for different color band')
#matplotlib.pyplot.savefig('../week14.jpg')
#matplotlib.pyplot.close(fig_1)


#please use variable name!!!

red_cutoff_ind = np.where((red > np.mean(red) - np.std(red)) & (red < np.mean(red) + np.std(red)))