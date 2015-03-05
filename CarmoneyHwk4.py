#Author:     Carl Carmoney
#Date:       Mar 04, 2015
#Subject:    CS495-35W Artificial Intelligence
#Professor:  Bruno A.
#
#Comments from various runs are below the sourcecode
#Assignment #4

from simpleai.search import SearchProblem, hill_climbing_random_restarts
import sys
import pdb
import random
import time

class TspProblem(SearchProblem):

    def __init__(self,distances, initial):
        super(TspProblem, self).__init__(initial_state=(0,4,3,2,1,8,7,6,5,11,10,9,0))
        self.distances = distances
        self.num_cities=len(self.distances)
        self.rows=len(self.distances[0])
        self.tour = []
        #self.route = initial[1:]
        self.route = initial
        print self.route
        self.hops = len(self.route)
        self._max = self.calc_max()

    def calc_max(self):
        max = 0
        #Iterate over all elements, create a sum (which is MAX).
        for row in range(0, self.hops-1):
            for col in range(0,self.hops-1):
                max=max + int(self.distances[row][col])
        return max


    def actions(self, s):
        # I will explain the scheme, called 2-change, with an example think of
        # randomly selecting 2 distinct edges, and cutting them out and then
        # cross connect the end points
        # See slides 40 - 45.

        # Move this into a function and invoke it 4 or 5 times appending the
        # result to actions.
        # Call it once? Call it multiple times? Experiment with it!
        actions = []
        frontList = []
        midList = []
        rearList = []

        # Choose a random index
        _x = random.randint(2, self.hops-2)
        _y = random.randint(_x+1, self.hops-1)

        #Reverse the list between _x and _y (eg: 1,2,3,6,5,4,7,8,9)
        # Slicing Mechanism
        frontList = self.route[:_x]
        rearList = self.route[_y:]
        midList = self.route[_x:_y]
        tmp = []

        orderedList = frontList
        tmp = reversed(midList)
        for tmp in reversed(midList):
            orderedList.append(tmp)
        orderedList.extend(rearList)
        actions.append(('2-change at ' + str(_x) + ' and ' + str(_y), orderedList))

        return actions

    # Check if a state is valid.               
    # work out what the improper states are and put them here and a return value
    def _is_valid(self, s):
        '''
        Starting and ending state element are the same
        No city is visited more than one (exclude 1st and last)
        '''
        # Endpoints of route the same?
        endpoints_same = s[0] == s[-1]
        
        result = True
       
        # Check if Starting and ending state element are the same
        if endpoints_same:
            #Good, create a sublist missing the endpoints from above
            sublist = []
            sublist = s[1:len(s)-1]

            # Check that all elements are unique
            length = len(sublist)
            for idx in range(0,length):
                item2chk = sublist[idx]
                if sublist.count(item2chk) > 1:
                    result = False
                    break

        return ( endpoints_same and result ) 

    def result(self, s, a):
        '''
        Result of applying an action to a state.
        '''
        return a[1]

    def value(self, s):
        ''' 
        Hill climber wants big values. Sales person wants small
        Ergo, max-tourlength.
        '''
        return int(self.calc_max()) - int(self._tour_length(s))

    def generate_random_state(self):
        neworder = []
        alist = self.route[:]
        neworder.append(alist.pop(0))
        last = alist.pop(len(alist)-1)        
        for i in range(0,len(alist)):
            neworder.append(alist.pop(random.randint(0,len(alist)-1)))
        neworder.append(last)
        self.route = neworder[:]
        return self.route

    def _tour_length(self, s):
        # create a loop, 
        #iterate over tour, 
        #get indices (row,col) to get length, add them all, return
        #HINT: Do not use a foreach loop.
        
        tourlen = 0
        lhs_idx = 0
        rhs_idx = 0
        hops = len(s)
        for item in range(0,hops-2):            
            lhs_idx = s[item]
            rhs_idx = s[item+1]
            tourlen = tourlen + self.distances[lhs_idx][rhs_idx]
        return tourlen 

    #FIXME!
#    def is_goal(self, state):
#        return state == (2, 0)

    def heuristic(self, state):
        return 1

def usage():    
    print 'This program takes arguments - try using some!'
    print '\n\nex: python CarmoneyHwk4.py 0 1 2 3 4 5 6 7 0'
    print '\n    The route must begin and end with the same value\n    such as \'0\' in the example.'
    print '\n    Minimum amount of routes is 4'
    print '    Maximum amount of routes is 12'
    
        
if 4 < len(sys.argv) < 15:
           #   00   01   02   03   04   05   06   07   08   09   10   11
    matrix= \
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

    route = []
    for i in sys.argv[1:]:
        route.append(int(i))
    if route[0] == route[-1]:
        starttime = time.time()
        problem = TspProblem(matrix , route)
        result = hill_climbing_random_restarts(problem, restarts_limit=200)
        endtime = time.time()
        for i in result.path():
            print i
        print('It took ' + str(endtime - starttime) + ' to compute this answer.')
    else:
        usage()
else:
    usage()
