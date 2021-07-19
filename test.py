import re

class File:
   def match(self, word: str) -> str:
      tet = "apples-192"
      
      x = re.search('apples', tet.lower())
      if x:
         print("match has been found")
      else:
         print("has failed")



obj = File()
apples = int(1230)
obj.match(apples)