def itemSize(item): return item[0]
def itemValue(item): return item[1]
def itemName(item): return item[2]

exampleItems = [(3,3,'A'),
                (4,1,'B'),
                (8,3,'C'),
                (10,4,'D'),
                (15,3,'E'),
                (20,6,'F')]

exampleSizeLimit = 32

def solveKnapsackHeuristic(items, sizeLimit):

    items = list(reversed(sorted(items, key=lambda x: x[1]/x[0])))

    min_item_size = min([i[0] for i in items])

    knapsack = []

    knapsack_size = 0
    for item in items:
        if knapsack_size + item[0] > sizeLimit:
            if knapsack_size + min_item_size > sizeLimit:
                break
            else:
                continue

        knapsack.append(item[2])
        knapsack_size += item[0]

    return knapsack

if __name__ == "__main__":
    print(solveKnapsackHeuristic(exampleItems,exampleSizeLimit))
