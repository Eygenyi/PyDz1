# j=input()
# r=0
# for i in j:
#     f=int(i)
#     r=r+f
# print(r)

j=int(input())
if 99<j<1000:
    print(j//100+j%100//10+j%10)
else:
    print('неверное число')