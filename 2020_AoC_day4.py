fin = 'AoC_Day4_input.txt'
with open(fin, 'r') as f:
  a = f.read()

a = [x.replace('\n',' ').split(' ') for x in a.split('\n\n')]

def digit(val):
  #Take a given string value and determine if it is a digit or not
  if val.isdigit():
    return int(val)
  else:
    return 0
    
def between(start, end, val, incl=True):
  #Given a start value, end value, and value, determine if the value is between
  # the start and end. 
  # Incl represents if the comparison should be inclusive
  if incl:
    if start <= val <= end:
      return True
    else:
      return False
  if not incl:
    if start < val < end:
      return True
    else:
      return False


num = 0

for i in a:
  valid = []
  for f in i:
    f = f.split(':')
    if f[0] == 'byr':
      #if the value is a digit and is between the given ints, 
      # append True, else false
      valid.append(between(1920, 2002, digit(f[1])))

    if f[0] == 'iyr':
      valid.append(between(2010,2020,digit(f[1])))
      # if f[1].isdigit():
      #   if 2010 <= int(f[1]) <= 2020:
      #     valid.append(True)
      #   else:
      #     valid.append(False)
      # else:
      #   valid.append(False)

    if f[0] == 'eyr':
      valid.append(between(2020,2030,digit(f[1])))

    if f[0] == 'hgt':
      if f[1][-2:] == 'cm':
        valid.append(between(150,193,digit(f[1][:-2])))

      elif f[1][-2:] == 'in':
        valid.append(between(59,76,digit(f[1][:-2])))
      else:
        valid.append(False)   

    if f[0] == 'hcl':
      if f[1][0] == '#':
        temp = []
        if len(f[1][1:])==6:
          for c in f[1][1:]:
            if c in '0123456789abcdef':
              temp.append(True)
            else:
              temp.append(False)
          if False not in set(temp):
            valid.append(True)
          else:
            valid.append(False)
        else:
          valid.append(False)
    if f[0] == 'ecl':
      if f[1] in ['amb','blu','brn','gry','grn','hzl','oth']:
        valid.append(True)
      else:
        valid.append(False)
    if f[0] == 'pid':
      if len(f[1]) == 9 and '.' not in f[1]:
        if f[1].isdigit():
          valid.append(True)
        else:
          valid.append(False)
      else:
        valid.append(False)

  #check that all the required fields hit and are valid if so, add valid count
  if len(valid) == 7 and False not in set(valid):
    num +=1

print(num)    

