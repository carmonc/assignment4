#Author:     Carl Carmoney
#Date:       Feb 25, 2015
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
    #Jugs problem

    def __init__(self,j1,j2):
        super(TspProblem, self).__init__(initial_state=(0,4,3,2,1,8,7,6,5,11,10,9,0))
           #   00   01   02   03   04   05   06   07   08   09   10   11
        self.distances = \
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
        self.num_cities=len(self.distances)
        self.rows=len(self.distances[0])
        self.tour = []


    def actions(self, s):
        # I will explain the scheme, called 2-change, with an example
        # think of randomly selecting 2 distinct edges, and cutting them out
        # and then cross connect the end points
        # See slides 40 - 45
        action = []
        frontList = []
        midList = []
        rearList = []

        # Choose a random index
        while True:
            _x = randint(1,self.num_cities-2)
            _y = randint(2,self.num_cities-1)
            if _x < _y:
                break

        #Reverse the list between _x and _y (eg: 1,2,3,6,5,4,7,8,9)

        frontList = visitorder[:_x]
        rearList = visitorder[_y:]
        midList = visitorder[_x:_y]
        tmp = []

        orderedList = frontList
        tmp = reversed(midList)
        for tmp in reversed(midList):
            orderedList.append(tmp)
        orderedList.extend(rearList)
        action = ('2-change at ' + str(_x) + ' and ' + str(_y), orderedList)

        return action

    # Check if a state is valid.               
    # work out what the improper states are and put them here and a return value
    def _is_valid(self, s):
        #FIXME!
        return ((0 <= s[0] <= self.jug1) and (0 <= s[1] <= self.jug2))

    #Result of applying an action to a state.
    def result(self, s, a):
        return a[0]

    def value(self, s, v):
        #FIXME!
        return _tour_length(self,s)

    def generate_random_restart(self, s):
        return s[randint(0,self.num_cities)]

    def _tour_length(self, s):
        return len(self.tour)

    def is_goal(self, state):
        #FIXME!
        return state == (2, 0)

    def heuristic(self, state):
        return 1

if len(sys.argv) != 3:
    print('This program takes arguments - try using some next time!')
else:
    starttime = time.time()
    #FIXME! Init params....
    problem = TspProblem(int(sys.argv[1]), int(sys.argv[2]))
    result = astar(problem)
    endtime = time.time()
    print result.path()
    print('It took ' + str(endtime - starttime) + ' to compute this answer.')
