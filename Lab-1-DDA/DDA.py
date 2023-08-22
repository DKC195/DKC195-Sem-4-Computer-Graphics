import matplotlib.pyplot as plt
from time import sleep


def DDA(x0, x1, y0, y1):
  dx = abs(x0 - x1)
  dy = abs(y0 - y1)

  steps = max(dx, dy)

  xinc = dx/steps
  yinc = dy/steps
  x = float(x0)
  y = float(y0)

  x_coordinates = []
  y_coordinates = []

  for i in range(steps):
    x_coordinates.append(x)
    y_coordinates.append(y)

    x = x + xinc
    y = y + yinc

  plt.plot(x_coordinates, y_coordinates)
  plt.show()


DDA(1, 5, 1, 5)
