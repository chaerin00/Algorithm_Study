nums=input()

count=0
for num in nums:
    sec=(ord(num)-ord('A'))//3+2
    count+=sec+1

print(count)


