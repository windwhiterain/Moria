from dataclasses import dataclass
from scipy.spatial.transform import Rotation
from backend import Concept, concept
from type import *
class Plain():
    @property
    def normal(self)->f3:
        pass
    def dist(self,pos:f3)->float:
        pass
class Quad(Plain):
    @property
    def bound(self)->bound2:
        pass
class Ray():
    def dist(self,pos:f3)->float:
        pass
    def flow_field(self,pos:f3)->float:
        pass
    @property
    def dir(self)->f3:
        pass
    @property
    def origin(self)->f3:
        pass
class Segment(Ray):
    @property
    def len()->float:
        pass
    @property
    def pair()->l[2,'f3']:
        pass
@dataclass
class rot:
    data:Rotation
    def __mul__(self,other:f3)->f3:
        return self.data.apply(other)
    @property
    def inv(self)->'rot':
        return rot(self.data.inv())
    @staticmethod
    def from_euler(euler:f3)->'rot':
        return rot(Rotation.from_euler('xyz',euler,False))
@dataclass
class RotPos:
    rot:rot
    pos:f3
    def to(self,_:f3)->f3:
        return self.rot.inv*(_-self.pos)
    def back(self,_:f3)->f3:
        return self.rot*_+self.pos
    def dist(self,pos:f3)->float:
        return (self.rot*pos)[2]
    @property
    def normal(self)->f3:
        return self.rot*[0,0,1]
    @property
    def plain(self)->Plain:
        return Concept(self)

@dataclass
class OrthBound2(RotPos):
    bound:bound2
    @property
    def quad(self)->Quad:
        return Concept(self)
    
@dataclass
class PosDir:
    origin:f3
    dir:f3
    def flow_field(self,_:f3)->float:
        (_-self.origin).dot(self.dir)
    def distance(self,_:f3)->float:
        pos=_-self.origin
        pos.dot(self.dir.cross(pos).cross(self.dir).normalize)
