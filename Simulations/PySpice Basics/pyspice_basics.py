import numpy as np 
import matplotlib.pyplot as plt 
import sys 

import PySpice 
import PySpice.Logging.Logging as Logging 
from PySpice.Spice.Netlist import Circuit 
from PySpice.Unit import * 

#create output parsing 
def format_output(analysis):
    results = {}
    for node in analysis.nodes.values():
        label = f'{node}'
        results[label] = np.array(node)
    return results 

#define logger 
logger = Logging.setup_logging() 

#create a circuit 
circuit = Circuit('Voltage Divider')

#add components 
circuit.V('input','in',circuit.gnd, 10@u_V)
circuit.R('res1','in','out', 9@u_kOhm)
circuit.R('res2','out',circuit.gnd, 11@u_kOhm)

#create a simulator instance 
simulator = circuit.simulator(temperature=25, nominal_temperature=25)

#run analysis 
analysis = simulator.operating_point() 

output = format_output(analysis)
print(output)

exit()