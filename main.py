def bubble_sort(num_list):
    n = len(num_list)
    for i in range(n-1):
        for j in range(0, n-i-1):
            if num_list[j] > num_list[j + 1]:
                print(f"The value in position {j} is higher than {j + 1}")
                num_list[j], num_list[j + 1] = num_list[j + 1], num_list[j]


input_list = list(map(int, input("Input a list of numbers with spaces in between: ").split()))
print(f"the start list is {input_list} \n")
bubble_sort(input_list)
print(f"the sorted list is {input_list}")
input()