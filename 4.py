def merge_lists(list1, list2, reverse=False):
    i = 0
    j = 0
    result = []

    while i < len(list1) and j < len(list2):
        if list1[i] <= list2[j]:
            result.append(list1[i])
            i += 1
        else:
            result.append(list2[j])
            j += 1

    while i < len(list1):
        result.append(list1[i])
        i += 1

    while j < len(list2):
        result.append(list2[j])
        j += 1


    if reverse:
        rev = []
        for k in range(len(result)-1, -1, -1):
            rev.append(result[k])
        return rev

    return result

print("მაგალითი 1: გადავეცით [1, 3, 10] და [0, 4, 7, 9]\n",merge_lists([1, 3, 10], [0, 4, 7, 9]))
print("მაგალითი 2: გადავეცით [1, 3, 10], [0, 4, 7, 9] და True\n",merge_lists([1, 3, 10], [0, 4, 7, 9], True))
print("მაგალითი 3: გადავეცით [3, 5, 7, 9], [1, 2, 9] და True\n",merge_lists([3, 5, 7, 9], [1, 2, 9], True))
