l = [1,2,2,2,3,4,5,6,7,7,7]
ans = 0
for nums in l:
    ans = ans ^ nums
    print(ans, end = " ")