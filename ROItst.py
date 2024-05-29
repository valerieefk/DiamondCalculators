import cv2
import numpy as np
  
# im = ("/Users/benjaminmartin/Documents/MILKTECH/AHS_logo.png") 
# # Read image
# image = cv2.imread(im)
  
# # Select ROI
# r = cv2.selectROI("select the area", image)
  
# # Crop image
# cropped_image = image[int(r[1]):int(r[1]+r[3]), 
#                       int(r[0]):int(r[0]+r[2])]
# print(r)  
# # Display cropped image
# cv2.imshow("Cropped image", cropped_image)
# cv2.waitKey(0)



# Matplotlib provides its own RectangleSelector. There is an example on the matplotlib page, which you may adapt to your needs.

# # A simplified version would look something like this:

# import matplotlib.pyplot as plt
# import numpy as np
# from matplotlib.widgets  import RectangleSelector

# xdata = np.linspace(0,9*np.pi, num=301)
# ydata = np.sin(xdata)

# fig, ax = plt.subplots()
# line, = ax.plot(xdata, ydata)


# def line_select_callback(eclick, erelease):
#     x1, y1 = eclick.xdata, eclick.ydata
#     x2, y2 = erelease.xdata, erelease.ydata

#     rect = plt.Rectangle( (min(x1,x2),min(y1,y2)), np.abs(x1-x2), np.abs(y1-y2) )
#     ax.add_patch(rect)


# # rs = RectangleSelector(ax, line_select_callback,
# #                        drawtype='box', useblit=False, button=[1], 
# #                        minspanx=5, minspany=5, spancoords='pixels', 
# #                        interactive=True)
# rs = RectangleSelector(ax, line_select_callback,
#                         useblit=False, button=[1], 
#                        minspanx=5, minspany=5, spancoords='pixels', 
#                        interactive=True)
# plt.show()


# from roipoly import RoiPoly
# from matplotlib import pyplot as plt
# im = cv2.imread("/Users/benjaminmartin/Documents/MILKTECH/AHS_logo.png")
# # plt.imshow(im)

# r = cv2.selectROI("select the area", im)

# print(r)

# my_roi = RoiPoly(color='r') # draw new ROI in red color

# mask = my_roi.get_mask()

# mask = my_roi.get_mask(im)

# plt.imshow(mask) # show the binary signal mask

# mean = plt.mean(im[mask])
# for r in [my_roi1, my_roi2, my_roi3]
#     r.display_roi()


