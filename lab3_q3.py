### Implementing and simulating multiplexers in PyRTL ###

import pyrtl
#gradescope not seeing update
# Now, it is time to build and simulate (for 16 cycles) a 3-bit 5:1 MUX.
# You can develop your design using either Boolean gates as above or PyRTL's
# conditional assignment.

# Declare data inputs
# < add your code here >
a = pyrtl.Input(bitwidth=1, name='a')
b = pyrtl.Input(bitwidth=1, name='b')
c = pyrtl.Input(bitwidth=1, name='c')
d = pyrtl.Input(bitwidth=1, name='d')
e = pyrtl.Input(bitwidth=2, name='e')

# Declare control inputs
s = pyrtl.Input(bitwidth=3, name='s')

# Declare outputs 
# < add your code here >
o = pyrtl.Output(bitwidth=2, name = 'o')

# Describe your 5:1 MUX implementation
# < add your code here >
with pyrtl.conditional_assignment:
    with s==0:   #int('000',2): #000   
        o |= a
    with s==1:    #int('001', 2):  #001
        o |= b
    with s==2:    #int('010', 2):  #010
        o |= c
    with s==3:     #int('011',2):  #011
        o |= d
    with s==4:   #int('100',2):  #100
        o |= e
    with s==5:
        o |= 0
    with s==6:
        o |= 0
    with s==7:
        o |= 0
        
    # with s==110: #101
 #       o = 0
   # with s==111: #110
  #      o = 0
                 #111

# Simulate and test your design for 16 cycles using random inputs
# < add your code here >
sim_trace = pyrtl.SimulationTrace()
sim = pyrtl.Simulation(tracer=sim_trace)

import random
for cycle in range(16):
    # Call "sim.step" to simulate each clock cycle of the design                
    sim.step({
        'a': random.choice([0, 1]),
        'b': random.choice([0, 1]),
        'c': random.choice([0, 1]),
        'd': random.choice([0, 1]),
        'e': random.choice([0, 1]),
        's': random.choice([0, 1, 2, 3, 4])
        })

sim_trace.render_trace()
