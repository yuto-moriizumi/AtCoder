n = int(input())
box = [99999999]
for _ in range(n):
    # print(box)
    i = int(input())
    if (max(box) < i):
        box.append(i)
    else:
        idx = -1
        for j in range(len(box)):
            #print(box[j], i, box[idx], box[j] >= i, box[idx] > box[j])
            if (idx == -1 and box[j] >= i):
                idx = j
            if (box[j] >= i and box[idx] > box[j]):
                idx = j
        box[idx] = i
print(len(box))
