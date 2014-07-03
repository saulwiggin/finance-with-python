"""
  Name     : 4375OS_10_30_binary_search_bible_word.py
  Book     : Python for Finance
  Publisher: Packt Publishing Ltd. 
  Author   : Yuxing Yan
  Date     : 12/26/2013
  email    : yany@canisius.edu
             paulyxy@hotmail.com
"""

x=load('c:/temp/uniqueWords.pickle')
x.to_csv('c:/temp/uniquewords.csv')

myword='stool'

def binaryText(x, target, my_min=1, my_max=None):
    if my_max is None:
        my_max = len(x) - 1
    while my_min <= my_max:
        mid = (my_min + my_max)//2
        midval = x.iloc[mid]
        if midval.values < target:
            my_min = mid + 1
        elif midval.values > target:
            my_max = mid - 1
        else:
            return mid
    raise ValueError
    
    
print binaryText(x,myword)