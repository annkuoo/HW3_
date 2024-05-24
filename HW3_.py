def print_list(lst):
    for i in lst:
        print(i, end=" ")
    print("\n")

def quicksort(lst, start, end):
    if start < end:
        pivot = lst[start]
        i = start
        j = end
        while i < j:
            while i < len(lst) and lst[i] <= pivot:
                i += 1
            while lst[j] > pivot:
                j -= 1
            if i < j:
                lst[i], lst[j] = lst[j], lst[i]
        lst[start], lst[j] = lst[j], lst[start]
        
        print(f"pivot: {pivot}")
        print("result: ", end="")
        print_list(lst)
        
        quicksort(lst, start, j - 1)
        quicksort(lst, j + 1, end)

def initialize():
    return [33, 67, 8, 13, 54, 119, 3, 84, 25, 41]

def main():
    lst = initialize()

    # print out the initial list
    print("initial list: ", end="")
    print_list(lst)

    # QS
    quicksort(lst, 0, len(lst) - 1)

    # print out the final result
    print("Final result:")
    print_list(lst)

if __name__ == "__main__":
    main()
