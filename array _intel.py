def print_array(a):
  print(f" i: ", end="")
  for i in range(len(a)):
    k = len(str((a[i]))) +2 -  len(str((i)))
    print(i, end =" "*k )
  print()
  print("  ",a)
 

def prefix(a):
  '''returns an array with same size as a where each elemnt p[k] is the sum of first k elements in a '''
  n = len(a)

  prefix_sums = [0]*n

  sum = 0
  for i in range(len(a)):
    sum += a[i]
    prefix_sums[i]+= sum


  return (prefix_sums)
