# 3 (test_cases)
# 2 (number_of_fabrics)
# blue 2 1 (color, durability, id)
# yellow 1 2 ((color, durability, id))
# 2
# blue 2 1
# brown 2 2
# 1
# red 1 1

import numpy as np

def calc(fabrics):
    sorted_by_durability = sorted(fabrics, key=lambda k: (k['durability'], k['id']))
    sorted_by_color = sorted(fabrics, key=lambda k: (k['color'], k['id']))
    sorted_id_durability = np.array([d['id'] for d in sorted_by_durability])
    sorted_id_color = np.array([d['id'] for d in sorted_by_color])
    changes = np.sum(sorted_id_durability == sorted_id_color)
    return changes


def main():
    test_cases = int(input())
    for test_case in range(1, test_cases + 1, 1):
        number_of_fabrics = int(input())
        fabrics = []
        for i in range(number_of_fabrics):
            splits = input().split()
            fabric = {}
            fabric['id'] = int(splits[2])
            fabric['durability'] = int(splits[1])
            fabric['color'] = splits[0]
            fabrics.append(fabric)
        #print(fabrics)
        ans = calc(fabrics)
        print("Case #{}: {}".format(test_case, ans))

if __name__ == "__main__":
  main()
