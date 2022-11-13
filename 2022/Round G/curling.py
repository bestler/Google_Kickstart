import numpy as np

def calc_result(r_house, r_stone, postions_team1, positions_team2):
  count_team1 = 0
  count_team2 = 0

  dists_team1 = []
  dists_team2 = []
  for position in postions_team1:
    dist = np.sqrt(position[0] ** 2 + position[1] **2)
    if dist - r_stone <= r_house :
      dists_team1.append(dist)

  for position in positions_team2:
    dist = np.sqrt(position[0] ** 2 + position[1] **2)
    if dist - r_stone <= r_house:
      dists_team2.append(dist)  

  dists_team1.sort()
  dists_team2.sort()
  
  best_stone_team1 = 0
  best_stone_team2 = 0

  if len(dists_team1) > 0:
    best_stone_team1 = dists_team1[0]
  else:
    best_stone_team1 = 1_000_000_000_000

  if len(dists_team2) > 0:
    best_stone_team2 = dists_team2[0]
  else:
    best_stone_team2 = 1_000_000_000_000

  if best_stone_team1 < best_stone_team2:
    while(len(dists_team1) > 0):
      best_stone_team1 = dists_team1.pop(0)
      if (best_stone_team1 < best_stone_team2):
        count_team1 += 1
    return (count_team1, count_team2)
  if best_stone_team2 < best_stone_team1:
    while(len(dists_team2) > 0):
      best_stone_team2 = dists_team2.pop(0)
      if (best_stone_team2 < best_stone_team1):
        count_team2 += 1    
  return (count_team1, count_team2)


def main():
  test_cases = int(input())
  for test_case in range(1, test_cases + 1, 1):
    splits = input().split()
    r_stone, r_house = int(splits[0]), int(splits[1])
    count_team1 = int(input())

    positions_team1 = []
    positions_team2 = []
    for i in range(count_team1):
      splits = input().split()
      x,y = int(splits[0]), int(splits[1])
      positions_team1.append((x,y))

    count_team2 = int(input())

    for i in range(count_team2):
      splits = input().split()
      x,y = int(splits[0]), int(splits[1])
      positions_team2.append((x,y))
    
    ans = calc_result(r_house, r_stone, positions_team1, positions_team2)

    print("Case #{}: {} {}".format(test_case, ans[0], ans[1]))

if __name__ == "__main__":
  main()