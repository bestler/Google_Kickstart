def result(number_of_ints, ints):
    calculated_sum = 0
    #lists = []
    pos_start = 0
    pos_end = 1
    while pos_start < number_of_ints:
        curr_list = ints[pos_start:pos_end]
        if sum(curr_list) >= 0:
            #lists.append(curr_list)
            calculated_sum += sum(curr_list)
            pos_end += 1
            if pos_end > number_of_ints:
                pos_start += 1
                pos_end = pos_start + 1
        else:
            pos_start += 1 
            pos_end = pos_start + 1

    #print(lists)
    return calculated_sum
    

def main():
    test_cases = int(input())
    for test_case in range(1, test_cases + 1, 1):
        number_of_ints = int(input())
        ints = list(map(int, input().split()))
        ans = result(number_of_ints, ints)
        print("Case #{}: {}".format(test_case, ans))

if __name__ == "__main__":
    main()