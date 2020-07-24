import numpy as np
import tkinter.filedialog as dialog
import tkinter as tk

def get_path():
    tk.Tk().withdraw()
    return dialog.askopenfilename()

def parse_hng(fp):
    f = open(fp, 'r')
    s = f.read()
    vals = s.split('\n')
    hinges = np.empty((0, 4))
    for i in range(int(len(vals) // 4)):
        h = [float(vals[4 * i]), float(vals[4 * i + 1]), float(vals[4 * i + 2]), float(vals[4 * i + 3])]
        hinges = np.append(hinges, [h], axis=0)
    return hinges

def parse_vtx(fp):
    f = open(fp, 'r')
    s = f.read()
    vals = s.split('\n')
    vectors = np.empty((0, 9, 3))
    for i in range(int(len(vals) // 9)):
        v = []
        for j in range(9):
            l = vals[9 * i + j][1:-1].split(', ')
            v0 = [float(l[0]), float(l[1]), float(l[2])]
            v.append(v0)
        v = np.array(v)
        v_mean = np.mean(v, axis=0)
        vectors = np.append(vectors, [v - v_mean], axis=0)
    return vectors