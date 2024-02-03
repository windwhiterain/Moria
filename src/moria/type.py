from typing import Any, Generic, Literal, NewType,TypeVar,ParamSpec,Callable, override,Self,Any,Annotated
from dataclasses import dataclass

l=Literal
T=TypeVar("T")
class OperatorTable:
    @staticmethod
    def from_array(_:Any)->Any:
        pass
    @staticmethod
    def dot(a:T,b:T)->float:
        pass
    @staticmethod
    def pow2(array:T)->T:
        pass
    @staticmethod
    def pow05(_:T)->T:
        pass
    @staticmethod
    def sum(_:T)->float:
        pass
    @staticmethod
    def cross(a:T,b:T)->Any:
        pass
class NumpyOperatorTable:
    @staticmethod
    def from_array(_:Any)->Any:
        return np.array(_)
    @staticmethod
    def dot(a:T,b:T)->float:
        return np.dot(a,b)
    @staticmethod
    def pow2(_:T)->T:
        return np.square(_)
    @staticmethod
    def sum(_:T)->float:
        return np.sum(_)
    @staticmethod
    def cross(a:T,b:T)->Any:
        return np.cross(a,b)
class Context:
    op:OperatorTable=NumpyOperatorTable()

@dataclass
class array_extension:
    data:Any
    @staticmethod
    def from_array(array:Any)->Self:
        return Self(Context.op.from_array((array)))
    def __add__(self,_)->Self:
        return self.data.__add__(_)
    def __iadd__(self,_)->Self:
        return self.data.__iadd__(_)
    def __sub__(self,_)->Self:
        return self.data.__sub__(_)
    def __isub__(self,_)->Self:
        return self.data.__isub__(_)
    def __mul__(self,_)->Self:
        return self.data.__mul__(_)
    def __imul__(self,_)->Self:
        return self.data.__imul__(_)
    def __truediv__(self,_)->Self:
        return self.data.__truediv__(_)
    def __itruediv__(self,_)->Self:
        return self.data.__itruediv__(_)
    def __array__(self)->np.ndarray:
        return self.data.__array__()
    def __getitem__(self,index:Any)->float:
        return self.data.__getitem__(index)
class float_n(array_extension):
    def dot(self,_:Self)->float:
        return Context.op.dot(self,_)
    @property
    def norm(self)->float:
        return Context.op.pow05(Context.op.sum(Context.op.pow2(self.data)))
    @property
    def normalize(self)->Self:
        return self/self.norm
class f2(float_n):
    @staticmethod
    def new(x:float,y:float) -> None:
        return f2.from_array([x,y])
    def cross(self,_:Self)->float:
        return Context.op.cross(self,_)
class f3(float_n):
    @staticmethod
    def new(x:float,y:float,z:float) -> None:
        return f2.from_array([x,y,z])
    def cross(self,_:Self)->Self:
        return Self(Context.op.cross(self,_))
class bound_n(array_extension):
    pass
class bound(bound_n):
    @staticmethod
    def new(self,start:float,end:float) -> None:
        return bound.from_array([start,end])
class bound2(bound_n):
    @staticmethod
    def new(array:l[2,'bound']) -> None:
        return bound.from_array(array)
class bound3(bound_n):
    @staticmethod
    def new(array:l[3,'bound']) -> None:
        return bound.from_array(array)
    