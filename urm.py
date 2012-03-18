#! /usr/bin/python

import sys

#parses a URM instruction out of a line
def parse_inst(inst):
    op = inst[0].lower()
    args = map(int, inst[1:].split(','))
    if op == "z":
    	return (0,args[0],0,0)
    elif op == "s":
        return (1,args[0],0,0)
    elif op == "t":
    	return (2, args[0], args[1], 0)
    elif op == "j":
    	return (3, args[0], args[1], args[2])
    else:
    	return None

#takes a file-like object of lines containing
# URM instructions and returns a URM program
def parse_program(program):
    inst_list = []
    instructions = (parse_inst(line) for line in program)
    for instruction in instructions:
        if instruction:
	    inst_list.append(instruction)
        else:
	    pass #handle exceptions later
    return inst_list

#largest register number mentioned in a program
def rho(program):
    return max(max(inst[1], inst[2]) for inst in program) + 1

#executes inst on list registers and changes
# programCounter to fit. modifies registers
def execute(inst, registers, programCounter):
    if inst[0] == 0: #zero
	registers[inst[1]] = 0
    elif inst[0] == 1: #successor
	registers[inst[1]] = registers[inst[1]] + 1
    elif inst[0] == 2: #transfer
	registers[inst[2]] = registers[inst[1]]
    elif inst[0] == 3: #jump
	if registers[inst[1]] == registers[inst[2]]:
	    return inst[3]
    else:
	raise ValueError("Illegal instruction")
    return programCounter + 1

def computation(program, urm_input):
    programCounter = 0
    registers = list(urm_input) + [0 for _ in xrange(rho(program) - len(urm_input))]
    while programCounter < len(program):
	programCounter = execute(program[programCounter], registers, programCounter)
	yield programCounter, tuple(registers)

if __name__ == '__main__':
    if len(sys.argv) >= 2:
        program_file = open(sys.argv[1])
        program = parse_program(program_file)
        print sys.argv[2:]
        inputs = map(int, sys.argv[2:])
        for step in computation(program, inputs):
            print step
