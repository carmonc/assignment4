#Author:     Carl Carmoney
#Date:       Feb 25, 2015
#Subject:    CS495-35W Artificial Intelligence
#Professor:  Bruno A.
#
#Comments from various runs are below the sourcecode

# coding=utf-8
from simpleai.search import SearchProblem, astar
import sys
import pdb
import time

class WaterJugsProblem(SearchProblem):
    #Jugs problem

    def __init__(self,j1,j2):
        super(WaterJugsProblem, self).__init__(initial_state=(0, 0))
        self.jug1=j1
        self.jug2=j2

    def comp_c1_action(self, s):
        '''pour all of first into second. Any overflow goes on to the ground.'''
        c1 = s[1]+s[0]
        if c1 > self.jug2:
            c1 = self.jug2
        return ('c1-pour all of first into second', (0, c1))

    def comp_c2_action(self, s):
        '''pour all of second into first. Any overflow goes on to the ground.'''
        c2 = s[0] + s[1]
        if c2 > self.jug1:
            c2 = self.jug1
        return ('c2-pour all of second into first', (c2, 0))

    def comp_d1_action(self, s):
        '''pour first into second until latter if full. Remaining stays in first.'''
        needed_d1 = self.jug1-s[0]
        if needed_d1 >= s[1]:
            needed_d1 = s[1]
        d1s0=s[0]+needed_d1
        d1s1=s[1]-needed_d1
        return ('d1-pour first into second until latter if full', (d1s0,d1s1))

    def comp_d2_action(self ,s):
        '''pour second into first until latter if full. Remaining stays in second.'''
        needed_d2 = self.jug2-s[1]
        if needed_d2 >= s[0] :
            needed_d2 = s[0]
        d2s0=s[0]-needed_d2
        d2s1=s[1]+needed_d2
        return ('d2-pour second into first until latter if full', (d2s0,d2s1))

    def actions(self, s):
        # Possible actions from a state.
        # we try to generate every possible state and then filter those
        # states that are valid
        #[('some String value' , (new state for jug1),(new state for jug2)]

        action = []

        # Check jug1 not already full - fill it. Leave s[1] alone.
        if s[0] < self.jug1:
            action.append(('a1-fill first jug from pump',(self.jug1,s[1])))

        # Check jug2 not already full - fill it. Leave s[0] alone.
        if s[1] < self.jug2:
            action.append(('a2-fill second jug from pump',(s[0],self.jug2)))

        # Empty jug1 only if it contains something...
        if s[0] > 0:
            action.append(('b1-empty first onto ground',(0,s[1])))

        # Empty jug2 only if it contains something...
        if s[1] > 0:
            action.append(('b2-empty second onto ground',(s[0],0)))

        # if jug2 is not full, pour all of first into second
        if s[1] < self.jug2:
            action.append(self.comp_c1_action(s))

        # if jug1 is not full, pour all of second into first
        if s[0] < self.jug1:
            action.append(self.comp_c2_action(s))

        # Check if jug1 less than full AND jug2 has something to give
        # If jug1 has room, fill it until full, leave remainder in jug2
        # If jug1 already full, do nothing.
        if s[0] < self.jug1 and s[1] > 0:
            action.append(self.comp_d1_action(s))

        # Check if jug2 less than full AND jug1 has something to give
        # If jug2 has room, fill it until full, leave remainder in jug1
        # If jug2 already full, do nothing.
        if s[1] < self.jug2 and s[0] > 0:
            action.append(self.comp_d2_action(s))

        return action

    #Check if a state is valid.               
    # work out what the improper states are and put them here and a return value
    def _is_valid(self, s):
        return ((0 <= s[0] <= self.jug1) and (0 <= s[1] <= self.jug2))

    #Result of applying an action to a state.
    def result(self, s, a):
        return a[1]

    def is_goal(self, state):
        return state == (2, 0)

    def heuristic(self, state):
        return 1

if len(sys.argv) != 3:
    print('This program takes arguments - try using some next time!')
else:
    starttime = time.time()
    problem = WaterJugsProblem(int(sys.argv[1]), int(sys.argv[2]))
    result = astar(problem)
    endtime = time.time()
    print result.path()
    print('It took ' + str(endtime - starttime) + ' to compute this answer.')
