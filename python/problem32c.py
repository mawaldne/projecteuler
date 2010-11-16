# Yet another fast solution...Whats going on here?

products=set([])
for a in range(4,99):
  if a%10 and a%11:
   for b in range(123,int(10000/a)):
    nums=set(list(str(a)+str(b)+str(a*b)))
    if len(nums)==9 and not '0' in nums:
      print(str(a)+" "+str(b)+" "+str(a*b))
      products.add(a*b)
print(sum(products))