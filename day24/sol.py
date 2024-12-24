
with open('input.txt') as f:
    start, ins = f.read().split("\n\n")
    start = [line for line in start.split("\n") if line.strip()]
    ins = [line for line in ins.split("\n") if line.strip()]

values = {}
for line in start:
    k, v = line.split(":")
    values[k] = int(v)

def calc(left, right, op):
    if op == "AND":
        return values[left] & values[right]
    if op == "OR":
        return values[left] | values[right]
    if op == "XOR":
        return values[left] ^ values[right]

def part1(ins):
    z = {}
    while True:
        if not ins:
            break
        next_ins = []
        for line in ins:
            left, op, right, _, out = line.split(" ")
            if left in values and right in values:
                values[out] = calc(left, right, op)
                if out.startswith('z'):
                    z[out] = values[out]
            else:
                next_ins.append(line)         
        
        ins = next_ins.copy()
    

    out = [str(v) for _, v in sorted(z.items(), key=lambda x: x[0], reverse=True)]
    return int("".join(out), 2)

# print(part1(ins))


