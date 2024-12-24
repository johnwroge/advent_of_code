from dataclasses import dataclass
from typing import Optional, List, Union

@dataclass
class Wire:
    value: Optional[bool]

@dataclass
class LogicGate:
    inputs: List[Union[Wire, "LogicGate"]]
    output: List[Union[Wire, "LogicGate"]] = None

    def compute(self):
        raise NotImplementedError("Needs to be implemented in downstream class")

@dataclass
class And(LogicGate):
    def compute(self):
        if any(i == None for i in self.inputs):
            raise ValueError("Gate not fully ready")
        if len(self.inputs) != 2:
            raise ValueError("Requires two inputs")
        return input[0].value & input[1].value
    

@dataclass
class Or(LogicGate):
    def compute(self):
        if any(i == None for i in self.inputs):
            raise ValueError("Gate not fully ready")
        if len(self.inputs) != 2:
            raise ValueError("Requires two inputs")
        return input[0].value | input[1].value
    
MEM = {}

class Circuit:



Or(And(inputs=[Wire(1), Wire(0)]), Wire(0))