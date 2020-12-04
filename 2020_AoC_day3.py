def trees(input, p):
  s = [0,0]
  tree = 0
  for ix,i in enumerate(input):
    if len(i) > 0:
      if ix == s[1]+p[1]:
        jump = s[0]+p[0]
        if jump >= len(i):
          increase = jump//len(i)
          i = i + i*(increase + 1)
        spot = i[jump]
        if spot == '#':
          tree+=1
        s = [s[0]+p[0], s[1]+p[1]]
  return tree
  
fin = 'AoC_Day3_input.txt'

with open(fin, 'r') as f:
  a = f.read()
a = a.split('\n')

one =trees(a, p)
print(one)
p2 = (1,1)
two = trees(a,p2)
print(two)
p3 = (5,1)
three = trees(a,p3)
print(three)
p4 = (7,1)
four = trees(a,p4)
print(four)
p5 = (1,2)
five = trees(a,p5)
print(five)

print('answer :',one*two*three*four*five)