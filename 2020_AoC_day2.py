def clean_input(input_list):
  clean = []
  c = [x.strip('\n').split(' ') for x in input_list]
  for x in c:
    counts = [int(n) for n in x[0].split('-')]
    letter = x[1].strip(':')
    password = x[2]
    clean.append([counts[0],counts[1], letter,password])
  return clean
  
fin = 'AoC_Day2_input.txt'
with open(fin, 'r') as f:
  real_input = f.readlines()

real_input = clean_input(real_input)

valid = 0
invalid = 0

for i in real_input:
  # print(i)
  min = i[0]
  max = i[1]
  string = i[-1]
  char = i[-2]
  count = string.count(char)
  if min <= count <= max:
    valid += 1
  else:
    invalid += 1
  # print(count)
print('valid: ',valid)
print('invalid: ',invalid)

#problem 2 
valid = 0
invalid = 0
for i in real_input:
  pos1 = i[0]-1
  pos2 = i[1]-1
  string = i[-1]
  char = i[-2]
  check1 = string[pos1]
  check2 = string[pos2]
  if check1 == char and check2 ==char:
    invalid+=1
  elif check1 != char and check2 != char:
    invalid+=1
  else:
    valid+=1
valid