from typing import TypeVar


class Concept():
    def __init__(self,implement):
        self.implement=implement
    def __getattr__(self,name: str):
        if(hasattr(self.implement,name)):
            return getattr(self.implement,name)
        else:
            self.implement=self.implement.convert_for(name)
            return getattr(self.implement,name)
interface=TypeVar('interface')
def concept(_:interface)->interface:
    return lambda:Concept(_)