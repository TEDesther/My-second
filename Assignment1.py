num=5000
st=[]

for i in range(2000+1):
    new=num+i
    if(new%2==0):
        # print(new, "multiple of 2")
        st.append(new)

    elif(new%3==0):
        # print(new, "multiple of 3")
        st.append(new)

    else:
        # print(new, "Fail")
        pass


print(st)






