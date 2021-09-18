import numpy as np 
import matplotlib.pyplot as plt 
import sys 

import PySpice 
import PySpice.Logging.Logging as Logging
from PySpice.Spice.Netlist import Circuit, SubCircuit, SubCircuitFactory 
from PySpice.Unit import * 

def format_output(analysis):
    results = {}
    for node in analysis.nodes.values():
        label = f'{node}'
        results[label] = np.array(node)

    return results 

#create a subcircuit 
class MySubCirc(SubCircuit):
    
    __nodes__ = ('t_in','t_out')
    def __init__ (self, name, r=1@u_kOhm):

        SubCircuit.__init__(self, name, *self.__nodes__)
        self.R('res2','t_in','t_out',9@u_kOhm)
        self.Diode('d2','t_in','t_out',model='MyDiode')

        return 

#initialize logger
logger = Logging.setup_logging()

#create circuit 
circuit = Circuit('MyCircuit')

#define diode model 
circuit.model('MyDiode', 'D', IS=4.352@u_nA, RS=0.6458@u_Ohm, BV=110@u_V, IBV=0.0001@u_V, N=1.906)

#add components to the circuit 
circuit.V('input','a',circuit.gnd,10)
circuit.R('res1','a','b',9@u_kOhm)
circuit.Diode('d1','b','c',model='MyDiode')

circuit.subcircuit(MySubCirc('sub1',r=1@u_kOhm))
circuit.X(1,'sub1','c',circuit.gnd)

#create simulator 
simulator = circuit.simulator(temperature=25, nominal_temperature=25)

#start analysis
analysis = simulator.operating_point()

output = format_output(analysis)
print(output)

exit()