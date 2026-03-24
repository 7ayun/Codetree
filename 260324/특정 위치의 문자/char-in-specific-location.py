char = input()

text = ["L", "E", "B", "R", "O", "S"]

idx = None

for i in range(len(text)):
    if text[i] == char:
        idx = i

print(idx)