# -*- coding: utf-8 -*-
"""Untitled2.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/17iUU8t8tsIXBv0-48EBPtJcPhorTwOIW
"""

import string
def ispangram(str):
   alphabet = "abcdefghijklmnopqrstuvwxyz"
   for char in alphabet:
      if char not in str.lower():
         return False
   return True

string = 'The quick brown fox jumps over the lazy dog.'
if(ispangram(string) == True):
   print("Yes")
else:
   print("No")