def intersection(list1, list2):
    result = [list(filter(lambda x: x in list1, sublist)) for sublist in list2]
    return result


list1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14]
list2 = [[12, 18, 23, 25, 45], [7, 11, 19, 24, 28], [1, 5, 8, 18, 15, 16]]

print(intersection(list1, list2))
