def calc(rounds):
    points = 1
    points += (rounds - 1) // 5
    return points



def main():
    test_cases = int(input())
    for test_case in range(1, test_cases + 1, 1):
        rounds = int(input())
        ans = calc(rounds)
        print("Case #{}: {}".format(test_case, ans))

if __name__ == "__main__":
  main()
