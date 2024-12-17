from functools import cache

with open("input.txt") as f:
    registers, program = f.read().split("\n\n")

registers = [r for r in registers.split("\n") if r.strip()]
ra, rb, rc = [int(r.split(":")[1]) for r in registers]
program = list(map(int, program.split(":")[1].strip().split(",")))


@cache
def get_combo(operand, ra, rb, rc):
    if operand <= 3:
        return operand

    if operand == 4:
        return ra

    if operand == 5:
        return rb

    if operand == 6:
        return rc


@cache
def adv(op, ra, rb, rc):
    combo = get_combo(op, ra, rb, rc)
    div = 2**combo
    return ra // div


@cache
def bxl(op, rb):
    rb ^= op
    return rb


@cache
def bst(op, ra, rb, rc):
    combo = get_combo(op, ra, rb, rc)
    return combo % 8


def part1(ra, rb, rc, program):
    ins = 0
    out = []
    while ins < len(program):
        operand = program[ins + 1]
        if program[ins] == 0:
            ra = adv(operand, ra, rb, rc)
        elif program[ins] == 1:
            rb = bxl(operand, rb)
        elif program[ins] == 2:
            rb = bst(operand, ra, rb, rc)
        elif program[ins] == 3:
            if ra != 0:
                ins = int(operand)
                continue
        elif program[ins] == 4:
            rb = rb ^ rc
        elif program[ins] == 5:
            out.append(bst(operand, ra, rb, rc))
        elif program[ins] == 6:
            rb = adv(operand, ra, rb, rc)
        elif program[ins] == 7:
            rc = adv(operand, ra, rb, rc)

        ins += 2

        # print(f"Out: {out}")
        # print(f"Register A: {ra}")
        # print(f"Register B: {rb}")
        # print(f"Register C: {rc}")

    return out


# print(part1(ra, rb, rc, program))


def part2(ra, pos):
    # B -> A % 8
    # B -> B ^ 7
    # C -> A // 2 ** B
    # B -> B ^ C
    # B -> B ^ 4
    # OUT -> B % 8
    # A -> A // 8
    # JMP 0
    if pos == len(program):
        return ra

    for i in range(8):
        out = part1(ra * 8 + i, 0, 0, program)
        if out and out[0] == program[-(pos + 1)]:
            if result := part2(ra * 8 + i, pos + 1):
                return result


print(part2(0, 0))
