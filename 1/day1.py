def part1():
  f = open("./input.txt", "r")
  max_cal = 0
  current_cal = 0
  for cal in f.read().splitlines():
      if cal == "":
          if current_cal > max_cal:
              max_cal = current_cal
          current_cal = 0
      else:
        current_cal += int(cal)

  if current_cal > max_cal:
      max_cal = current_cal
  current_cal = 0
      
  print(max_cal)

def part2():
  f = open("./input.txt", "r")
  elfs_cal = []
  current_cal = 0 
  for cal in f.read().splitlines():
      if cal == "":
          elfs_cal.append(current_cal)
          current_cal = 0
      else:
        current_cal += int(cal)

  elfs_cal.append(current_cal)
  
  elfs_cal.sort(reverse=True)
  print(sum(elfs_cal[:3]))

part1()
part2()