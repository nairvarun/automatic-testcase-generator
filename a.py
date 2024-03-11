import re
def parse_cfg(cfg_file):
    blocks = {}
    loops = {}
    current_block = None
    current_loop = None

    with open(cfg_file, 'r') as file:
        for line in file:
            line = line.strip()

            if line.startswith(';;'):
                continue
            elif line.startswith('<bb'):
                current_block = int(line.split()[1])
                blocks[current_block] = {'succs': []}
            elif line.startswith('Loop'):
                current_loop = int(line.split()[1])
                loops[current_loop] = {'nodes': []}
            elif line.startswith('header'):
                header = int(line.split()[1])
                loops[current_loop]['header'] = header
            elif line.startswith('latch'):
                latch = int(line.split()[1])
                loops[current_loop]['latch'] = latch
            elif line.startswith('nodes'):
                nodes = [int(x) for x in line.split(':')[1].strip().split()]
                loops[current_loop]['nodes'] = nodes
            elif line.startswith(';; '):
                continue
            elif line:
                succs = [int(x) for x in line.split()[1:]]
                blocks[current_block]['succs'] = succs

    return blocks, loops

def generate_test_cases(blocks, loops):
    test_cases = []

    # Generate test cases for each independent path
    for loop in loops.values():
        header = loop['header']
        latch = loop['latch']
        nodes = loop['nodes']

        # Generate test cases for the loop header
        test_cases.extend(generate_path_test_cases(blocks, [header]))

        # Generate test cases for the loop body
        test_cases.extend(generate_path_test_cases(blocks, nodes[nodes.index(header):nodes.index(latch) + 1]))

        # Generate test cases for skipping the loop
        if header not in blocks[latch]['succs']:
            test_cases.extend(generate_path_test_cases(blocks, [latch]))

    return test_cases

def generate_path_test_cases(blocks, path):
    test_cases = []
    conditions = []

    for i in range(len(path) - 1):
        block = path[i]
        next_block = path[i + 1]
        succs = blocks[block]['succs']

        if next_block in succs:
            condition = f"if ({next_block} in {succs})"
            conditions.append(condition)
        else:
            print(f"Warning: CFG inconsistency detected for block {block} and successor {next_block}")

    test_case = '; '.join(conditions)
    test_cases.append(test_case)

    return test_cases

# Parse the CFG file
blocks, loops = parse_cfg('3.c.cfg')

# Generate test cases
test_cases = generate_test_cases(blocks, loops)

# Print test cases
for i, test_case in enumerate(test_cases, start=1):
    print(f"Test Case {i}: {test_case}")
