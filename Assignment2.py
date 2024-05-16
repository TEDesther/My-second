x=2000
st=[]

for i in range(2000+1):
    y=x+i
    if(y%2==0 and y%3==0 and y%5==0 and y%7==0 and y%11==0):
        # print(y, "Success")
        st.append(y)
    else:
        # print(y,"Fail")
        pass
print(st)




