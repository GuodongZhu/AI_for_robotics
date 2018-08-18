# -----------
# User Instructions
#
# Define a function smooth that takes a path as its input
# (with optional parameters for weight_data, weight_smooth,
# and tolerance) and returns a smooth path. The first and
# last points should remain unchanged.
#
# Smoothing should be implemented by iteratively updating
# each entry in newpath until some desired level of accuracy
# is reached. The update should be done according to the
# gradient descent equations given in the instructor's note
# below (the equations given in the video are not quite
# correct).
# -----------

from copy import deepcopy
import numpy as np

# thank you to EnTerr for posting this on our discussion forum
def printpaths(path, newpath):
    for old, new in zip(path, newpath):
        print '[' + ', '.join('%.3f' % x for x in old) + \
              '] -> [' + ', '.join('%.3f' % x for x in new) + ']'


# Don't modify path inside your function.
path = [[0, 0],
        [0, 1],
        [0, 2],
        [1, 2],
        [2, 2],
        [3, 2],
        [4, 2],
        [4, 3],
        [4, 4]]


def path_diff( newpath, path ):
    score  = 0

    for new_waypoint, waypoint in zip( newpath, path ):
        score += (new_waypoint[0] - waypoint[0])**2 + (new_waypoint[1] - waypoint[1])**2

    return score

def smooth(path, weight_data=0.5, weight_smooth=0.1, tolerance=0.000001):
    # Make a deep copy of path into newpath
    newpath = deepcopy(path)
    tol     = 1
    #######################
    while tol > tolerance:

        last_path = deepcopy( newpath )

        for idx, new_waypoint in enumerate(newpath):
            if idx!= 0 and idx != len( newpath ) -1:
                for i in range(2):
                    new_waypoint[i] += weight_data * ( path[idx][i] - new_waypoint[i]  ) +\
                                       weight_smooth * ( newpath[idx+1][i] + newpath[idx-1][i] - 2*new_waypoint[i] )
        tol = path_diff( newpath, last_path )
    #######################

    return newpath  # Leave this line for the grader!


printpaths(path, smooth(path))
