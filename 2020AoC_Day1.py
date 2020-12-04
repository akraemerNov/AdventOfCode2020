#Problem 1: Find 2 numbers that have a sum of 2020, answer is the product 
## of the 2 numbers

#Problem 2: Find 3 numbers that have a sum of 2020, answer is the product of 
## the 3 numbers

import numpy as np
toy_input = [1721,979,366,299,675,1456]
real_input = [1150,1579,1361,1319,1201,1253,1806,1783,1164,1772,1920,1428,1918,
              245,1504,1952,1057,1977,704,1119,1971,1200,1650,1795,1877,1932,
              1811,1981,1803,1366,1580,1986,1976,1063,1895,1143,1991,1061,1855,
              1947,1134,1800,1898,1778,1964,1949,1103,1770,1321,2005,1758,1181,
              1140,1873,1946,1540,1909,1710,1705,1313,1196,1084,1870,1610,1708,
              1810,1133,1375,1264,1921,1624,41,1899,1226,1757,1978,1485,1385,
              1526,1653,1130,1223,1577,1912,1894,276,954,1269,1769,1924,93,1165,
              1812,1092,1402,1284,1903,1884,1581,1887,1963,1983,1233,1445,1974,
              1956,1691,1954,2000,1469,1875,955,1334,1116,1700,1818,1790,1704,
              1901,1072,1848,1990,1724,1719,1638,1311,1474,1837,1801,1929,1791,
              1317,1643,1632,1813,1488,1129,1998,1771,1793,1074,1826,1935,1462,
              1230,1797,1878,1751,1993,1437,1967,1844,1438,1969,1175,1823,1124,
              1922,154,936,1117,1145,1308,1320,1767,1850,1809,1350,1820,1082,
              1597,1913,1766,1701,1294,1556,2006,1480,1953,1104,1861,1966,1248,
              1671,1955,1863,1202,1356,1842,2010,1288,1067,1576,1295,1760,1888,
              1639,1282,1633,1619]

#simple answer
for i in real_input:
  for j in real_input:
    if j == 2020-i:
      print(j,i,i*j)

for i in real_input:
  for j in real_input:
    for k in real_input:
      if k == 2020-i-j:
        print(i,j,k, i*j*k)
        
#answer after my rabbit hole

def elf_expense1(go):
  inp = np.array(go)  
  addends = []

  for i in range(len(inp)):
    answer = inp+inp[i]
    if 2020 in answer:
        addends.append(inp[i])
  print('Addends:',addends)
  print('Added:', addends[0]+addends[1])
  print('Multiplied:',addends[0]*addends[1])

print('Day 1 | Problem 1')
print('Toy answer:')
elf_expense1(toy_input)
print('\n\nReal answer:')
elf_expense1(real_input)

#problem 2
toy_array = np.array(toy_input)
real_array = np.array(real_input)

def elf_expense2(input_array):
  addends = []
  gotit = False
  for i in range(len(input_array)):
    i_temp = np.append(input_array[i+1:],input_array[:i+1])
    for j in range(len(input_array)):
      j_temp =  np.append(input_array[j+2:],input_array[:j+2])
      add3 = input_array + i_temp + j_temp
      if 2020 in add3:
        loc = np.where(add3==2020)
        got1 = input_array[loc][0]
        got2 = i_temp[loc][0]
        got3 = j_temp[loc][0]
        addends.append([got1,got2,got3])
        gotit = True
  
  for i in range(1,len(addends)):
    a = set(addends[0]).intersection(addends[i])
    if len(a) != 3:
      gotit = False
  if gotit:
    print('Addends:',addends[0])
    print('Added:', sum(addends[0]))
    print('Multiplied:', np.prod(np.array(addends[0])))
  else:
    print('Something is not right!!!!!')
    print('Results:',addends)

print('\n\nDay 1 | Problem 2')
print('Toy answer:')
elf_expense2(toy_array)

print('\n\nReal answer')
elf_expense2(real_array)
