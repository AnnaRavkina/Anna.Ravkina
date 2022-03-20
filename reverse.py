def my_reverse(l):
      output = []
   
      for i in l:
         output.insert(0,i)
      return output

print(my_reverse([3,4,5,6,7,8]))