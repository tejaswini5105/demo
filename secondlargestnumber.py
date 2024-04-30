def second_largest(lst):
    largest = second_largest = float('-inf')
    
    for num in lst:
        if num > largest:
            second_largest = largest
            largest = num
        elif num > second_largest and num != largest:
            second_largest = num
            
    return second_largest

input_list = [3, 5, 7, 2, 8, 5, 9]
print(second_largest(input_list))