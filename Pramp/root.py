import math
def root(x, n):
  if x == 0:
    return 0
  lower = 0
  upper = max(1, x)
  appRoot = (upper + lower) / 2
  while abs(appRoot - lower) >= 0.001:
    if math.pow(appRoot, n) > x:
      upper = appRoot
    elif math.pow(appRoot, n) < x:
      lower = appRoot
    else:
      break 
    appRoot = (upper + lower) / 2
    
  return appRoot

print(root(10, 3))