# from catsim import estimation
# mt=estimation.MathematicalModel()
# print(mt.estimate(#index=24,items=[1,2,3,4,5,6,7,8,9,0],administered_items=[1,2,3,4,5,6,7,8,9,0],
# #response_vector=[0,1,1,1,1,1,1,1,1,1],
# current_level=3,ques_level=5,correctness=1,
# max_time=30,time_taken=40,alpha=0.8,beta=0.2))
# -*- coding: utf-8 -*-
"""Untitled7.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1L5vRXdhS9nQVSzXrH9QELSmWJKya307C
"""

# !pip install -U catsim

# this function generates an item bank, in case the user cannot provide one
from catsim.cat import generate_item_bank
# simulation package contains the Simulator and all abstract classes
from catsim.simulation import *
# initialization package contains different initial proficiency estimation strategies
from catsim.initialization import *
# selection package contains different item selection strategies
from catsim.selection import *
# estimation package contains different proficiency estimation methods
from catsim.estimation import *
# stopping package contains different stopping criteria for the CAT
from catsim.stopping import *
import catsim.plot as catplot
from catsim.irt import icc

import matplotlib.pyplot as plt

bank_size = 5000
items = generate_item_bank(bank_size)

items

it=generate_item_bank(5000, '1PL')
print(max(it[:,1]))
print(min(it[:,1]))
it[:,1]=((it[:,1]+5)*5/10)
print(max(it[:,1]))
print(min(it[:,1]))

it[:,2]=0.25

initializer = RandomInitializer()
# selector = MaxInfoSelector()
#estimator = HillClimbingEstimator()
selector =The54321Selector(5000)
estimator=MathematicalModel()
stopper = MaxItemStopper(20)

#s = Simulator(it, 1, RandomInitializer(), MaxInfoSelector(), HillClimbingEstimator(), MaxItemStopper(50))
s = Simulator(it, 1, FixedPointInitializer(0), UrrySelector(), MathematicalModel(), MaxItemStopper(50))

s.simulate(verbose=True)

examinee_index = 0
print('Accessing examinee', examinee_index, 'results...')
print('    True proficiency:', s.examinees[examinee_index])
print('    Items administered:', s.administered_items[examinee_index])
print('    Responses:', s.response_vectors[examinee_index])
print('    Proficiency estimation during each step of the test:', s.estimations[examinee_index])
len(s.response_vectors[examinee_index])
len(s.estimations[examinee_index])

ind=s.administered_items[examinee_index]
it[ind,:]
catplot.test_progress(simulator=s,index=0)
