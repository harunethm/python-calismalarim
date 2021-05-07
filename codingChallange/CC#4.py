example = ["Next", "Gen", "Next", "Coder", "Coder"]
bool = False
for i in range(0, len(example) - 1, 1):
    if(bool):
        i -= 1
        bool = False
    for j in range(i + 1, len(example) - 1):
        if(example[i] == example[j]):
            example.remove(example[j])
            bool = True

print(example)  