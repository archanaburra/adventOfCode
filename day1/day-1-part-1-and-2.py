#1 part 1
lines = open("input.txt", "r").read().split('\n')
lines = lines[:-1] ## get rid of the last '' which the int function can't parse
new_list = map(int, lines)
print sum(new_list) # 508

#1 part 2
size = len(new_list)
dubFrequency = False
freq = [0]
index = 0

while dubFrequency != True:
    new_freq = freq[len(freq) - 1] + new_list[index]
    if new_freq in freq:
        dubFrequency = True
    freq.append(new_freq)
    index = (index + 1) % size

print freq[len(freq) - 1] # 549
