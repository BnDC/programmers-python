def solution(operations):
    heap = []
    for operation in operations:
        type_, num = operation.split(" ")
        num = int(num)
        if type_ == "D" and len(heap) > 0:
            if num == 1:
                heap.pop()
            else:
                heap.pop(0)
        elif type_ == "I":
            heap.append(num)
        heap.sort()
    return [heap[-1], heap[0]] if len(heap) > 0 else [0, 0]


print(solution(["I 16", "I -5643", "D -1", "D 1", "I 123", "D -1"]) == [0, 0])
print(solution(["I -45", "I 653", "D 1",
                "I -642", "I 45", "I 97",
                "D 1", "D -1", "I 333"]) == [333, -45])