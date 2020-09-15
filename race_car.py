class Solution:
    def racecar(self, target: int) -> int:
        instructions = {}
        speeds = {}
        instructions[1] = "A"
        speeds[1] = 1
        for i in range(1, target + 1):
            # A, RA, RRA
            if i not in instructions:
                continue
            for op in ["A", "RA", "RRA"]:
                if op == "A":
                    speed = speeds[i] * 2

                else:  # op == "RA" or op == "RRA":
                    if speed > 0:
                        speed = -1
                    else:
                        speed = 1
                j = i + speed

                instruction = instructions[i] + op
                if j in instructions:

                    if len(instructions[j]) > len(instruction):
                        instructions[j] = instruction
                        speeds[j] = speed

                else:
                    instructions[j] = instruction
                    speeds[j] = speed

        return len(instructions[target])
