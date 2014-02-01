#!/usr/bin/env python2.7
#Author:Steven Jimenez
#Subject: Python Programming 
#HW 1


#Merge Sort that Calls a non-recursive function to sort lists
def mergesort(a):
  #if singleton return singleton
  if len(a)==1:
    return a

 
  #find mindpoint of list
  n = len(a)/2
    
  #split the list into sorted halves. left-Right
  left = mergesort(a[:n])
  right = mergesort(a[n:])
    
  #Combine sorted halves
  return mergelists(left,right)

#Takes in unsorted lists and returns a sorted list
def mergelists(lft,rgt):
  #New list that will be sorted
  sorted = []
  
  #While the lists are not empty compare and sort them in new list
  while len(lft) and len(rgt):
    if lft[0] < rgt[0]:
      sorted.append(lft.pop(0))
    else:
      sorted.append(rgt.pop(0))
  
  #If one of the lists are empty, send the non empty list to the new list
  if len(lft):
    sorted.extend(lft);
  if len(rgt):
    sorted.extend(rgt)
  return sorted

#Merge Sort that calls a recursive function to sort list
def mergesort2(a):

  #If list is a singleton return singleton
  if len(a)==1:
    return a
 
  #Find midpoint of lists
  n = len(a)/2
    
  #Divide current list into two halves and call function to sort
  left = mergesort2(a[:n])
  right = mergesort2(a[n:])
    
  #Bring together the new sorted lists
  return mergelists2(left,right)

def mergelists2(lft,rgt):
  
  #If one list is empty return the other
  if lft == []:
    return rgt
  
  if rgt == []:
    return lft
 
  #Find which element is the lesser of the two elements
  #Send that element to the array and continue merging the rest 
  if lft[0] < rgt[0]:
    return [lft[0]] + mergelists2(lft[1:],rgt)
  
  else:
     return [rgt[0]]+ mergelists2(lft,rgt[1:])

     