def bubble_sort(elements):
    size = len(elements)


    for i in range(size-1):
        swapped = False
        for j in range(size-1-i):
            if elements[j] > elements[j+1]:
                tmp = elements[i]
                elements[j] = elements[j+1]
                elements[j+1] = tmp
                swapped = True
        if not swapped:
            break

if __name__ == '__main__':
    elements = [5,9,2,1,67,34,88,34]
    #elements = [1,2,3]
    elements = ["bang", "apple", "carrot"]

    bubble_sort(elements)
    print(elements)