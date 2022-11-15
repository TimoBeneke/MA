state = 0b1000010010110001000011
length = 4194304

# LFSR der Form (0, 1, 22)

def lfsr(length, state):
    outputs = []
    for i in range(length):
        outputs.append(state)
        newbit = ((state ^ (state >> 1)) & 1)
        state = (state >> 1) | (newbit << 21)
    return outputs


result = lfsr(length, state)
print(len(result))

# Anzahl Einsen und Nullen für outputs.append(state & 1)
"""numOne = 0
numZero = 0

for i in result:
    if i == 1:
        numOne += 1
    else:
        numZero += 1

print ("Number of Zeroes: " + str(numZero))
print ("Number of Ones: " + str(numOne))"""

if result[0] == result[-1]:
    print("Maximum Period")
