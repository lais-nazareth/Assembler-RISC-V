
from riscv_data.instructions import Instructions
from riscv_data.registers import Registers

from utils import converteBin

Registers.value_regs[0] = 1
print(Registers.value_regs[0])

#print(converteBin(10,5))

#print(bin(14)[2:].zfill(7))

line = ["add", "s2", "s1", "s0"]
instruction = Instructions.instructions["add"]
bitstring = instruction["func7"] + converteBin(Registers.registers[line[3]], 5) + converteBin(Registers.registers[line[2]], 5) + instruction["func3"] + converteBin(Registers.registers[line[1]], 5) + instruction["opcode"]
print(bitstring)
print(len(bitstring))