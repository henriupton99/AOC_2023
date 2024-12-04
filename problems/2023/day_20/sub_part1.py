from collections import deque
from typing import Union
FILENAME = "input.txt"
identifier_to_typename = {"&":"conjunction","%":"flip-flop"}

class Module:
    "Class module in order to represent the flip-flops and conjunction"
    def __init__(self,name,type,outputs):
        """Initialization of the class

        Args:
            name (str): name of the module
            type (str): type of the module : &=conjunction, %=flip-flop
            outputs (_type_): destination/target modules of the module 
        """
        self.name = name
        self.outputs = outputs
        self.type = identifier_to_typename[type]
        
        # Create a memory for the module :
        # - for flip-flops: only two states on/off that will change their output
        # - for conjunctions: output depends of the last output it receives from each origin module
        # (so we store each last output from each origin module in a dictionnary)
        if self.type == "flip-flop":
            self.memory = "off"
        if self.type == "conjunction":
            self.memory = {}
            
    def propagate(self, origin_module, pulse) -> Union[str,None]:
        """Propagation function of the module : wrt its memory and input pulse,it outputs a specific pulse

        Args:
            origin_module (str): name of the origin module to store in memory in case of conjunction module
            pulse (str): input pulse from the origin module "low" or "high"

        Returns:
            pulse (Union[str,None]): output pulse to propagate
        """
        # Case of flip-flop modules : if input pulse is low, then swith mode and return opposite pulse
        if self.type == "flip-flop":
            if pulse == "low":
                self.memory = "off" if self.memory == "on" else "on"
                return "high" if self.memory == "on" else "low"   
            
        # Case of conjunction modules : return low if all pulses in his memory are high else high
        if self.type == "conjunction":
            self.memory[origin_module] = pulse
            return "high" if any(p=="low" for p in self.memory.values()) else "low"
        return None

# Define modules and broadcast outputs :
modules = {}
broadcast_targets = []
for line in open(FILENAME):
    left, right = line.strip().split(" -> ")
    outputs = right.split(", ")
    if left == "broadcaster":
        broadcast_targets = outputs
    else:
        type = left[0]
        name = left[1:]
        modules[name] = Module(name,type,outputs)

# Initialization of the memories :
for name, module in modules.items():
    for output in module.outputs:
        if output in modules and modules[output].type == "conjunction":
            modules[output].memory[name] = "low"

low = high = 0
# We do 1000 button presses :
for button_pushes in range(1000):
    low += 1
    # Create a deque in order to store tasks (origin_module,output_module,pulse_type) :
    queue = deque([("broadcaster", o, "low") for o in broadcast_targets])
    
    while queue:
        # take the first task in the queue (priority assumption):
        origin, target, pulse = queue.popleft()
        # Update the counts of low/high pulses :
        if pulse == "low":
            low += 1
        else:
            high += 1
        
        if target not in modules:
            continue
        
        # Propagate from origin module to their output modules :
        out_pulse = modules[target].propagate(origin,pulse)
        # If out_pulse is None its means the modules doesnt propagate so we skip:
        if out_pulse:
            for x in modules[target].outputs:
                queue.append((modules[target].name,x,out_pulse))
                print(f"{origin} -{out_pulse} -> {target}")

print(low * high)