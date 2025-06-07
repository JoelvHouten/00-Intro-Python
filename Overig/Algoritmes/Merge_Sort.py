# Merge-Sort

def merge_sort(lijst):
    if len(lijst) <= 1:
        return lijst
    midden = len(lijst) // 2
    linkerhelft = merge_sort(lijst[:midden])
    rechterhelft = merge_sort(lijst[midden:])
    return merge(linkerhelft, rechterhelft)

def merge(left, right):
    resultaat = []
    while left and right:
        if left[0] < right[0]:
            resultaat.append(left.pop(0))
        else:
            resultaat.append(right.pop(0))
    resultaat.extend(left)
    resultaat.extend(right)
    return resultaat

lijst = [38, 27, 43, 3, 9, 82, 10]
resultaat = merge_sort(lijst)
print(resultaat)
