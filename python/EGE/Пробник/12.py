for n in range(3,10001):
    st='1'+'2'*n
    while '12' in st or '3322' in st or '2222' in st:
        if '12' in st:
            st=st.replace('12','33',1)
        if '2222' in st:
            st=st.replace('2222','1',1)
        if '3322' in st:
            st=st.replace('3322','21',1)
    if sum([int(x) for x in st])==218:
        print(n)
        break
