def generatePairs(limite):
    num = 1
    pairs_list = []
    while num < limite:
        pairs_list.append(num * 2)
        num += 1
    return pairs_list


print(generatePairs(10))
