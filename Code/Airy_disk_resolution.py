#!/usr/bin/env python
# -*- coding: utf8 -*-

'''
Copyright (C) 2008 Wikimedia Foundation

This program is free software; you can redistribute it and/or modify
it under the terms of the GNU General Public License as published by
the Free Software Foundation; either version 2 of the License, or
(at your option) any later version.

This program is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
GNU General Public License for more details.

You should have received a copy of the GNU General Public License
along with this program; if not, write to the Free Software
Foundation, Inc., 59 Temple Place - Suite 330, Boston, MA 02111-1307, USA.
'''
##########
# Modified by R. Todd Lines
# June 10 2026
##########
# Included more coments and directions on changing the spacing 
#  between the two Airy patterns

import matplotlib.pyplot as plt
import math as m
import numpy as np
import scipy as sp
import scipy.special
from PIL import Image

w = 400
h = 400
image = np.zeros((h, w))

# Distance between the two diffraction patterns
#
# rayleigh criterion is to put the peak of on on the first zero of the other:
#  Calculate the zeros of a Bessel funciton of the first kind, the first 
#  arguement is the order number of the Bessel function and the second
#  is the number of zeros to compute. The spacing , r0, in this case will be 
#  the zero of the bessel function
r0 = scipy.special.jn_zeros(1, 1)
#
#  chosing spacing, r0, yourself (Maybe start close to 3.8 which is the 
#  Rayleigh criteria distance) Just about 3.0 gives the Sparrow criterial
#r0=6.00
#r0=3
#r0=.5

# Calculate the first two zeros of the Bessel fuction of the first kind, order
#  1 and retrn the second zero [-1] and add to it half lf the first zero
scalex = sp.special.jn_zeros(1, 2)[-1] + r0 / 2.
scaley = h * scalex / w

# make dark areas better visible
color_func = m.sqrt

# Now go pixel by pixel through the image and fill in the data
#  We need to calculate the Bessel functions and add them togeter 
#  with our chosen spacing.
for y in range(h):
	for x in range(w):
		xx = ((x + .5) / w - .5) * 2. * scalex
		yy = ((y + .5) / h - .5) * 2. * scaley
        # Distance measurment
		r1 = m.hypot(xx + r0 / 2., yy)
		r2 = m.hypot(xx - r0 / 2., + yy)
        # calculate the Bessel functions
		v1 = v2 = .5
		if r1 != 0.: v1 = (sp.special.j1(r1) / r1) ** 2
		if r2 != 0.: v2 = (sp.special.j1(r2) / r2) ** 2
		image[y, x] = color_func(v1 + v2)

max_val = image.max()

# write image to file
image_file = Image.new('L', (w, h))
# Scale image pixes so they fall within the vale range for image pixel values
for y in range(h):
	for x in range(w):
		c = int(2**8 * image[y, x] / max_val)
		image_file.putpixel((x, y), c)
# Save the image to a file        
image_file.save('Airydisks_rayleigh_sqrt.png', 'PNG')
# Plot the image on the screen
plt.imshow(image,cmap='gray')
plt.show()
# Plot the middle row so we can see a side view of the combined Airy patterns
middle_row = image[image.shape[0] // 2, :]
plt.plot(middle_row)
plt.show()
###############################################################################
