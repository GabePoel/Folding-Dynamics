#!/usr/bin/python3

# Find relation between vertex and index

import numpy as np

def reshape_curve(v, vtx_pick=0, vertex=0):
    x = np.transpose(v[vtx_pick][...,0])[vertex]
    y = np.transpose(v[vtx_pick][...,1])[vertex]
    z = np.transpose(v[vtx_pick][...,2])[vertex]
    curve = np.array([x, y, z])
    return np.transpose(curve)

def length_of_curve(curve):
    l = 0
    for i in range(1, len(curve)):
        l += np.linalg.norm(curve[i] - curve[i - 1])
    return l
    
def point_on_curve(curve, distance):
    if distance <= 0:
        return curve[0]
    elif distance >= length_of_curve(curve):
        return curve[len(curve) - 1]
    else:
        i = 0
        while distance > 0:
            i += 1
            distance -= np.linalg.norm(curve[i] - curve[i - 1])
        extension = curve[i] - curve[i - 1]
        l = np.linalg.norm(extension)
        d = (l - distance) / l
        extension = d * extension
        return curve[i - 1] + extension

def unit_time_curve(curve, final_time):
    normalized_curve = np.empty((0, 3))
    length = length_of_curve(curve)
    for i in range(final_time):
        distance = i / final_time * length
        extension = point_on_curve(curve, distance)
        normalized_curve = np.append(normalized_curve, [extension], axis=0)
    return normalized_curve
    
def distance_function(curve_1, curve_2):
    distances = []
    for i in range(len(curve_1)):
        distances.append(np.linalg.norm(curve_1[i] - curve_2[i]))
    return np.array(distances)
