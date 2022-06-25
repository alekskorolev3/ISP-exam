#tasks = ["A", "A", "A", "B", "B", "B"]
tasks = ["A", "A", "A", "B", "B", "B", "B", 'B', 'B', 'Q', "C", "D", "C"]
n = 2
last = [-100] * 26
kol = [0] * 26
for i in range(len(tasks)):
    kol[ord(tasks[i]) - ord('A')] += 1

taken = 0
i = -1
while taken < len(tasks):
    i += 1
    max_kol, max_index = 0, -1
    for j in range(26):
        if i - last[j] > n and kol[j] > max_kol:
            max_kol = kol[j]
            max_index = j
    if max_index == -1:
        print("w", end=" ")
        continue
    last[max_index] = i
    kol[max_index] -= 1
    taken += 1
    print(chr(ord('A') + max_index), end=" ")

print("\nans: ", i + 1)
