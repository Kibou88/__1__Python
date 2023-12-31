import scipy.special


cube_root = scipy.special.cbrt(27)
print('The cube root of 27 is {cube_root} because {cube_root} * {cube_root} * {cube_root} is 27'
      .format(**{'cube_root': cube_root}))
