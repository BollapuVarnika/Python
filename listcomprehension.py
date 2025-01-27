l=[10,15,20,25,30,40,45,60]
# ans=[ele for ele in l if ele%5==0 and ele%3==0]
# print(ans)

ans1=[ele if ele%5==0 and ele%3==0 else False for ele in l ]
print(ans1)

squares={x:x**2 for x in range(1,11) if x%2==0}
print(squares)