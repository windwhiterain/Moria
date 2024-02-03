from definition import *
a=OrthBound2(rot.from_euler([0,0,0]),np.zeros(3),[[-1,1],[-1,1]]).quad
print(a.normal)
