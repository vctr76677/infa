with open("bu.txt", "r", encoding="utf-8") as f:
    content = f.read()

count = 0

for i in range(len(content)):
    if content[i] in ".!?":
        if i + 1 == len(content) or content[i + 1] not in ".!?":
            count += 1

print(count)