def calc(liters):
    ans = 0
    c = 1
    while (ans + c <= liters):
        ans += c
        c *= 2
    return ans

def main():
    test_cases = int(input())
    for test_case in range(1, test_cases + 1, 1):
        splits = input().split()
        number_of_containers, number_of_queries = int(splits[0]), int(splits[1])
        liters = 0
        for i in range(number_of_containers - 1):
            splits = input().split()
            id1, id2 = int(splits[0]), int(splits[1])
        for i in range(number_of_queries):
            fill_in_containter = int(input())
            liters += 1

        ans = calc(number_of_containers, liters)
        print("Case #{}: {}".format(test_case, ans))

if __name__ == "__main__":
  main()
