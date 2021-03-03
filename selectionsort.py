

def selectionsort(self):
    for i in range(len(self)):
        minx = i
        for j in range(i+1, len(self)):
            if self[j] < self[minx]:
                minx = j
        (self[i], self[minx])= (self[minx], self[i])
    return self

array = [45, 10, 20, 8, 68, 35]
print(selectionsort(array))