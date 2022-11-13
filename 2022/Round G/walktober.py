# 1 (number of days)
# 2 3 1
# 1000 2000 3000
# 1500 1500 3000

def additonal_steps(number_of_participants,number_of_days, john_id, scoreboards):
  add_steps = 0
  curr_steps_john = 0
  for day in range(number_of_days):
    curr_steps_john = scoreboards[john_id][day]
    maxSteps = curr_steps_john
    for id in range(number_of_participants):
      steps = scoreboards[id][day]
      if steps > maxSteps:
        maxSteps = steps
    add_steps += maxSteps - curr_steps_john
  return add_steps

def main():
  test_cases = int(input())
  for test_case in range(1, test_cases + 1, 1):
    splits = input().split()
    number_of_participants, number_of_days, john_id = int(splits[0]), int(splits[1]), int(splits[2])-1
    scoreboards = []
    for i in range(number_of_participants):
        scoreboard = list(map(int, input().split()))
        scoreboards.append(scoreboard)
    ans = additonal_steps(number_of_participants, number_of_days, john_id, scoreboards)

    print("Case #{}: {}".format(test_case, ans))

if __name__ == "__main__":
  main()
