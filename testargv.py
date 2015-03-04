import sys
import random

program_name = sys.argv[0]
visitorder = sys.argv[1:]
count = len(visitorder)

print count
for visit in visitorder:
    print visit
distances = \
     [[  0,5472,5092,5393,5416,4584,4905,3852,4477,5261,4843,5930], \
     [5472,   0,1315, 927,1505, 944,1157,1945,7225,1127, 687, 459], \
     [5092,1315,   0,2166,2724,1572, 294,1241,6029, 236,1489,1542], \
     [5393, 927,2166,   0, 578, 973,1947,2422,7793,2010, 819,1096], \
     [5416,1505,2724, 578,   0,1367,2491,2839,8172,2579,1295,1636], \
     [4584, 944,1572, 973,1367,   0,1290,1474,6832,1511, 263,1387], \
     [4905,1157, 294,1947,2491,1290,   0,1064,6094, 362,1228,1458], \
     [3852,1945,1241,2422,2839,1474,1064,   0,5371,1412,1605,2356], \
     [4477,7225,6029,7793,8172,6832,6094,5371,   0,6263,6977,7551], \
     [5261,1127, 236,2010,2579,1511, 362,1412,6263,   0,1392,1319], \
     [4843, 687,1489, 819,1295, 263,1228,1605,6977,1392,   0,1125], \
     [5930, 459,1542,1096,1636,1387,1458,2356,7551,1319,1125,   0]]

#cols=len(distances[0])
#rows=len(distances)

print '3rd row'
print distances[3]

print 'visitorder = '
print visitorder
print 'count = ' + str(count)
print visitorder[count-1]

total = 0

for row in range(0,count-1):
    for col in range(0,count-1):
        item = distances[row][col] 
        print item
        total=total+int(item)

print total

print distances[11][10]


for t in range(0,5):
    neworder = []
    alist = [0,1,2,3,4,5,6,7,8,9,0]

    print alist

    neworder.append(alist.pop(0))
    last = alist.pop(len(alist)-1)
    for i in range(0,len(alist)):
        neworder.append(alist.pop(random.randint(0,len(alist)-1)))
        #item = alist.pop(random.randint(1,len(alist)-1))
    
    neworder.append(last)
    print neworder
    print '----------------'
