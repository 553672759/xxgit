'''
Created on 2017-1-4

@author: 
'''
'''
基数排序
基数排序属于分配式排序,又称桶子法
它是透过键值的部分资讯,将要排序的元素分配至某些桶种,藉以达到排序的作用
稳定性排序

'''


import math

def radix_sort(lists,radix=10):
    k=int(math.ceil(math.log(max(lists),radix)))
    bucket=[[] for i in range(radix)]
    for i in range(1,k+1):
        for j in lists:
            bucket[j/(radix**(i-1))%(radix**i)].append(j)
        del lists[:]
        for z in bucket:
            lists+=z
            del z[:]
    return lists