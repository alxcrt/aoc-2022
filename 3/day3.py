
def get_priority(c):
  # Lowercase item types a through z have priorities 1 through 26.
  if c >= 'a' and c <= 'z':
    return ord(c) - ord('a') + 1
  # Uppercase item types A through Z have priorities 27 through 52.
  elif c >= 'A' and c <= 'Z':
    return ord(c) - ord('A') + 27

def day1():
  f = open("./input.txt", "r")

  total = 0
  for line in f.read().splitlines():
    n = len(line)
    fist,second = line[:n//2], line[n//2:]
    freq = {}
    for i in range(n//2):
      freq[fist[i]] = freq.get(fist[i], []) + [1]
      freq[second[i]] = freq.get(second[i], []) + [2]

    # get the keys with value atleast 1 and 2
    common = [k for k,v in freq.items() if 1 in v and 2 in v]

    for c in common:
      total += get_priority(c)
  
  print(total)

def day2():
  f = open("./input.txt", "r")

  total = 0
  lines = f.read().splitlines()
  for i in range(0, len(lines), 3):
    group = lines[i:i+3]
    freq = {}
    j = 1
    for elf in group:
      for c in elf:
        freq[c] = freq.get(c, []) + [j]
      j += 1

    # get the keys with value atleast 1 and 2 and 3
    common = [k for k,v in freq.items() if 1 in v and 2 in v and 3 in v]

    for c in common:
      total += get_priority(c)
  
  print(total)


day1()
day2()