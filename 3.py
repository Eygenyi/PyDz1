j=input()
if len(j)>6 or len(j)<6:
    print('error')
elif int(j[0])+int(j[1])+int(j[2])==int(j[3])+int(j[4])+int(j[5]):
    print('yes')
else:
    print('no')