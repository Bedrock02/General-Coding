#!/usr/bin/env python2.7
#Author:Steven Jimenez
#Subject: Python Programming
#search algorithm searches for kth smallest data within the list

from random import randrange

def quickselect(list,k):
   #Generate random number
  pivot = randrange(len(list))
  #Create two lists based on the pivot value
  #left contains values less than pivot
  #right contains values greater and equal to pivot
  left = [x for x in list if x < list[pivot]]
  right = [x for x in list if x >= list[pivot]]

  #looking for kth smallest
  #CASE:1 Found kth Smallest
  if len(left) == k-1:
    return list[pivot]
 
  #CASE:2 Choose Right List for next Search
  #Must change k. Must subtract by len of left list + pivot
  if len(left) < k-1:
    return quickselect(right,k-len(left))
  #CASE:3
  #Choose Left List for next Search
  if len(left) > k-1:
    return quickselect(left,k)
