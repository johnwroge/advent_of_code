import os, re, math

"""
3 registers A, B, C can hold any integer

line of 3 bit numbers 0 - 7

eight instructions (3 bit number)

0 -> 1 -> 2 -> 3 -> halt

literal operand - number itself 
combo operand - 0 - 3 (literal of 0 - 3), 4 - A, 5 - B, 6 - C, 7- (DNE)

opcodes
0 - division of numerator (/) (A registrar)/ 2 ^ combo operand 
then truncated and written to A registrar 

1 - xor (^) of registrar B ^ operand and stores in B

2 - combo operand % 8  , thens writes to B 

3 - nothing if 0, else 

6 - 0 - division of numerator (/) (A registrar)/ 2 ^ combo operand 
then truncated and written to B registrar 

7 - 0 - division of numerator (/) (A registrar)/ 2 ^ combo operand 
then truncated and written to C registrar 

"""
import re

def parse_assembly_file(filename):
    with open(os.getcwd() + f'/2024/Day_17/{filename}', 'r') as file:
        content = file.read()
    registers = {}
    register_pattern = r'Register ([ABC]): (\d+)'
    matches = re.findall(register_pattern, content)
    for register, value in matches:
        registers[register] = int(value)
    
    program_pattern = r'Program: ([\d,]+)'
    program_match = re.search(program_pattern, content)
    if program_match:
        program_list = [int(x) for x in program_match.group(1).split(',')]
    else:
        program_list = []
    return registers, program_list

def Part_One(initial_A):
    registers, program = parse_assembly_file('data.txt')
    i = 0
    j = 1
    outputs = []  
    while i < len(program) and j < len(program):
        opcode = program[i]
        operand = program[j]
        current = None
        if opcode == 0:
            if 0 <= operand <= 3:
                power = operand
            elif operand == 4:
                power = registers.get('A')
            elif operand == 5:
                power = registers.get('B')
            elif operand == 6:
                power = registers.get('C')
            current = math.floor(registers.get('A') / (2 ** power))
            registers['A'] = current
        elif opcode == 1:
            current = registers.get('B') ^ operand
            registers['B'] = current
        elif opcode == 2:
            if 0 <= operand <= 3:
                value = operand
            elif operand == 4:
                value = registers.get('A')
            elif operand == 5:
                value = registers.get('B')
            elif operand == 6:
                value = registers.get('C')
            current = value % 8 
            registers['B'] = current
        elif opcode == 3:
            if registers.get('A') == 0:
                i += 2
                j += 2
            else:
                i = operand
                j = i + 1
        elif opcode == 4:
            registers['B'] = registers.get('B') ^ registers.get('C')
        elif opcode == 5:
            if operand == 4:
                outputs.append(registers.get('A') % 8)
            elif operand == 5:
                outputs.append(registers.get('B') % 8)
            elif operand == 6:
                outputs.append(registers.get('C') % 8)
            else:
                outputs.append(operand % 8)
        elif opcode == 6:
            if 0 <= operand <= 3:
                power = operand
            elif operand == 4:
                power = registers.get('A')
            elif operand == 5:
                power = registers.get('B')
            elif operand == 6:
                power = registers.get('C')
            current = math.floor(registers.get('A') / (2 ** power))
            registers['B'] = current
        elif opcode == 7:
            if 0 <= operand <= 3:
                power = operand
            elif operand == 4:
                power = registers.get('A')
            elif operand == 5:
                power = registers.get('B')
            elif operand == 6:
                power = registers.get('C')
            current = math.floor(registers.get('A') / (2 ** power))
            registers['C'] = current
        
        if opcode != 3 or registers.get('A') == 0:  
            i += 2
            j += 2
            
    return ','.join(str(x) for x in outputs)







def try_value(initial_A, program, check_length=None):
    registers = {'A': initial_A, 'B': 0, 'C': 0}
    i = 0
    j = 1
    outputs = []  
    
    while i < len(program) and j < len(program):
        opcode = program[i]
        operand = program[j]
        current = None
      
        if opcode == 0:  
            if 0 <= operand <= 3:
                power = operand
            elif operand == 4:
                power = registers.get('A')
            elif operand == 5:
                power = registers.get('B')
            elif operand == 6:
                power = registers.get('C')
            current = math.floor(registers.get('A') / (2 ** power))
            registers['A'] = current
        elif opcode == 1:
            current = registers.get('B') ^ operand
            registers['B'] = current
        elif opcode == 2:
            if 0 <= operand <= 3:
                value = operand
            elif operand == 4:
                value = registers.get('A')
            elif operand == 5:
                value = registers.get('B')
            elif operand == 6:
                value = registers.get('C')
            current = value % 8 
            registers['B'] = current
        elif opcode == 3:
            if registers.get('A') == 0:
                i += 2
                j += 2
            else:
                i = operand
                j = i + 1
        elif opcode == 4:
            registers['B'] = registers.get('B') ^ registers.get('C')
        elif opcode == 5:
            if operand == 4:
                outputs.append(registers.get('A') % 8)
            elif operand == 5:
                outputs.append(registers.get('B') % 8)
            elif operand == 6:
                outputs.append(registers.get('C') % 8)
            else:
                outputs.append(operand % 8)
        elif opcode == 6:
            if 0 <= operand <= 3:
                power = operand
            elif operand == 4:
                power = registers.get('A')
            elif operand == 5:
                power = registers.get('B')
            elif operand == 6:
                power = registers.get('C')
            current = math.floor(registers.get('A') / (2 ** power))
            registers['B'] = current
        elif opcode == 7:
            if 0 <= operand <= 3:
                power = operand
            elif operand == 4:
                power = registers.get('A')
            elif operand == 5:
                power = registers.get('B')
            elif operand == 6:
                power = registers.get('C')
            current = math.floor(registers.get('A') / (2 ** power))
            registers['C'] = current
        
        if opcode != 3 or registers.get('A') == 0:  
            i += 2
            j += 2
        if check_length and len(outputs) >= check_length:
            return outputs[-check_length:]
            
    return outputs

def Part_Two():
    _, program = parse_assembly_file('data.txt')
    print("Original program:", program)
    
    candidates = [0] 
    
    for length in range(1, len(program) + 1):
        new_candidates = []
        
        for num in candidates:
            for offset in range(8):
                a = (8 * num) + offset
                
                test_output = try_value(a, program, check_length=length)
                
                if test_output == program[-length:]:
                    new_candidates.append(a)
        
        candidates = new_candidates
        print(f"Length {length}: Found {len(candidates)} candidates")
        
        if not candidates:
            return None
            
    return min(candidates) if candidates else None

if __name__ == '__main__':
     print(Part_One())
    print(Part_Two())
  
