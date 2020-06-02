from collections import defaultdict
import sys
def smallest(S):
      distinct_count = len(set(list(S)))
      n = len(S)
      freq= defaultdict(int)
      first= 0
      minlen = sys.maxsize
      distinct= 0 
      for j in range(n):
        freq[S[j]] += 1
        if freq[S[j]] == 1:
          distinct += 1
        
        if distinct_count == distinct:
          while freq[S[first]] > 1:
            if freq[S[first]] > 1:
              freq[S[first]] -= 1
            first+= 1
          
          currlen = j -first + 1
          minlen = min(minlen, currlen)
      return minlen
S = input()
out=smallest(S)
print (out)
