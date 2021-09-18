import numpy as np 
import matplotlib.pyplot as plt 
import os 

import PySpice 
import PySpice.Logging.Logging as Logging 
from PySpice.Spice.Netlist import Circuit 
from PySpice.Unit import * 

def format_output(analysis):
    results = {}
    for node in analysis.nodes.values():
        label = f'{node}'
        results[label] = np.array(node)

    return results 

logger = Logging.setup_logging()

circuit = Circuit('DC Sweep')

#create model 
circuit.model('MyDiode', 'D', IS=4.352@u_nA, RS=0.6458@u_Ohm, BV=110@u_V, IBV=0.0001@u_V, N=1.906)

#add components 
circuit.V('input','in',circuit.gnd, 10@u_V)
circuit.Diode('d1','in','out', model='MyDiode')
circuit.R('r1','out',circuit.gnd, 1@u_kOhm)

print(circuit)

simulator = circuit.simulator(temperature=27, nominal_temperature = 27)

analysis = simulator.dc(Vinput=slice(0,5,0.001)) 

output = format_output(analysis)

fig = plt.figure()
plt.plot(output['in'],output['out'])
plt.grid()
plt.xlabel('input [V]')
plt.ylabel('output [V]')

fig.savefig('sweep output.png', dpi=300)
plt.close(fig)
