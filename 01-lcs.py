#!/usr/bin/env python
# -*- coding: utf-8 -*-
# CODE: longest consecutive sequence

class Solution:
    # @param num, a list of integer
    # @return an integer
    def longestConsecutive(self, num):
    	hashNum={}
        maxlength=1
        for item in num:
        	hashNum[item] = 1

        for i in range(0,len(num)):
        	number = num[i]

        	if hashNum[number] > 0:
        		length=1
        		hashNum[number] = 0
        		j=1

        		godown=True
        		goup=True

        		while(goup or godown):
        			if goup and hashNum.has_key(number+j):
        				length = length + 1
        				hashNum[number+j] = 0
        			else:
        				goup=False

        			if godown and hashNum.has_key(number-j):
        				length = length + 1
        				hashNum[number-j] = 0
        			else:
        				godown=False	

        			j=j+1

        		if length > maxlength:	
        			maxlength = length

        return maxlength

if __name__ == '__main__':
  #TESTING
	a=Solution()
	print a.longestConsecutive([9,1,4,7,3,-1,0,5,8,-1,6,2])
