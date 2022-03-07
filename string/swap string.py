# -*- coding: utf-8 -*-
"""
Created on Mon Mar  7 11:55:45 2022

@author: user
"""

word = input("enter a string seperated by 2 commas:")
word_list = word.split(" ")
first_letter_1 = word_list[0][0]
first_letter_2=word_list[1][0]
print(first_letter_2+word_list[0][1:]+""+first_letter_1+word_list[1][1:])


