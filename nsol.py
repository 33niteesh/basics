#1
def add(a,b):
    return a + b
#2    
def max(a,b):
    if (a>b):
        print ("a is max")
    else:
        print ("b is max")
#3
def fact(n):
    if (n==0 or n==1):
        return 1
    else:
        return n*fact(n-1)
#4
def si(p,t,r):
    return (p*t*r)/100
#5
def ci(p,t,r):
    return (p*((1+r/100)**t-1))
#6
def sum_of_digits(n):
    i=0
    while (n>0):
        i=i+(n%10)
        n=n//10
    return i
#7
def amst(n):
    m=n  
    a=str(n)
    b=len(a)
    i=0
    while (n>0):
        i=i+(n%10)**b
        n=n//10
    if (m==i):
        print ("its an amstrong")
    else:
        print ("not an amstrong")
    #if we not put return statement it state none in out put
#8
def area_circle(r):
    return (3.141*r**2)
#9
def prime(n):
    for i in range(2,n):
        if (n%i==0):
            print ("not a prime")
            break
    else:
        print ("its a prime")
#10
def prime_interval(m,n):
    for i in range(m,n+1):
            if i>1:
             for j in range(2,n):
                    if (i%j==0):
                      break
            else:
                print (i)
#11            
def fib(n):
    if n==0:
        return 0
    elif n==1:
        return 1
    else:
        return fib(n-1)+fib(n-2)
#12
def fib_or_not(n):
    import math
    a=(5*n*n+4)
    b=(5*n*n-4)
    c=math.sqrt(a)
    d=math.sqrt(b)
    if(c*c==a or d*d==b):
        print('its a fibinacci')
    else:
        print('not a fibinacci')
#13
def sum_of_cb(n):
    return (n*(n+1)/2)**2//1
#14
def sum_of_n(n):
    return (n*(n+1))/2
#15
def sum_of_sqre_of_n(n):
    return n*(n+1)*((2*n+1))//6
#16
def ascii(n):
    return ord(n)
#17
def prime1(n):
    if(n>1):
        i=1
        while(i<n-1):
            i=i+1
            a=n%i
            
            if(a==0):
                return a
        else:
            return 'its prime'
#18
def sort(arr):
    l=len(arr)
    b=[]
    while (l>0):
        m=max(arr)
        b.append(m)
        arr.remove(m)
        l=l-1
    print('dessending order',b)
    return 'assending order',b[::-1]
#19
def sum_of_arr(arr):
    sum=0
    for i in range(0,len(arr)):
        sum=sum+arr[i]
    return sum 
#20
def max_in_arr(arr):
    return max(arr)

#21
def largest(arr):
    max = arr[0]
    for i in range(1, len(arr)):
        if arr[i] > max:
            max = arr[i]
    return max
#22
def rot(array,d):
       return  array[d:len(array)]+array[0:d]

#23
def rem_of_arr_divided_by_n(arr,n):
    pro=1
    for i in range(0,len(arr)):
        pro=pro*arr[i]
    return pro%n
#24
def swaplist_1st_and_last(list):
    l=len(list)
    a=list[0]
    list[0]=list[l-1]
    list[l-1]=a
    return list
#25
def lenoflist(list):
    return len(list)
#26
def clearlist(list):
    return list.clear
#27
def placevalue(n):
    l=n
    j=0
    while (n>0):
        i=(n%10)
        n=n//10
        j=j+1
        print(j,'s place of number is',i)
    return 'number is',l
#28
def duplicate(list):
    a=[]
    for i in range(0,len(list)):
        for j in range(i+1,len(list)):
            if (list[i]==list[j]):
                if list[i] in a:
                    break
                else:
                    a.append(list[i])
    return a
        

#29 
def removeduplicate(list):
    a=[]
    for i in range(0,len(list)):
        for j in range(i+1,len(list)):
            if (list[i]==list[j]):
                if list[i] in a:
                    break
                else:
                    a.append(list[i])
    for k in range(0,len(a)):
        list.remove(a[k])
    return list
#30
def cumsumlist(list):
    a=[]
    sum=0
    for i in range(0,len(list)):
        sum=list[i]+sum
        a.append(sum)
    return a

#31
def palindrome(n):
    m=str(n)
    if (m==m[::-1]):
        return 'its a palindrome'
    else:
        return 'not a palindrome'
#32
def sum_dig_list(list):
    arr=[]
    for n in range(0,len(list)):
        m=list[n]
        k=str(m)
        l=len(k)
        i=0
        while (m>0):
            i=i+m%10
            m=m//10
        arr.append(i)   
    return arr
#33
def positive_list(list):
    for i in list:
        if(i<0):
            list.remove(i)
    return list
        
#34
def negetive_list(list):
    for i in range(0,len(list)):
        if (list[i]>0):
            list.remove(list[i])
    return list

#35
def even_list(list):
    for i in list:
        if(i%2!=0):
            list.remove(i)
    return list
#36
a=[[1,2,3],[1,2,3],[1,2,3]]
b=[[1,2,3],[1,2,3],[1,2,3]]
r=[[0,0,0],[0,0,0],[0,0,0]]
for i in range(0,len(a)):
    for j in range(0,len(a[0])):
        r[i][j]=a[i][j]+b[i][j]
for i in range(0,len(r)):
    for j in range(0,len(r[0])):
        print(r[i][j])
#37
import numpy as np
a=np.array([[6,1,1],[1,3,-3],[2,8,7]])
b=np.array([[1,2,3],[1,2,3],[1,2,3]])
c=np.array([1,1,3])
print(np.add(a,b))
print(np.subtract(a,b))
#38
print(np.dot(a,b))
#39
print(np.transpose(a))
#40
print(np.linalg.det(a))
#41 
print(np.linalg.inv(a))
#42 to find unqnowns as A*UNKNOWN=C
#unqnown =A inverse*C
print(np.dot(np.linalg.inv(a),c))
#43
print(np.trace(a))
#44
print(np.mean(c))
#45
print(np.median(c))
#46
import statistics
print(statistics.mode(c))
#47 for  how many times element is repeated
def count(d,m):
    print(d.count(m))
#48
def round(n):
    print(round(4.6))
#49
def abs(n):
    print(abs(-4.6))
#50
def int(n):
    print(int(-4.6))
#51
def max_int(n):
    return n//1
#52
def col_matrics(mat,c):
    for i in range(0,len(mat)):
        print(mat[i][c-1])
    return ''
print(col_matrics([[1,2,3],[1,2,3],[1,2,3]],1))
#53
def Rank_of_matrice(mat):
    import numpy
    return(numpy.linalg.matrix_rank(mat))
#54
def trace_of_mat(mat):
# we can use np.trace(matrice)
    sum=0
    for i in range(0,len(mat)):
            sum=sum+mat[i][i]
    return sum  
#56
def upper_triangler_mat(mat):
    for i in range(0,len(mat)):
        for j in range(0,len(mat[0])):
             if i>j:
                 mat[i][j]=0
    return mat,'upper triangler'
#57
def lower_triangler_mat(mat):
    for i in range(0,len(mat)):
        for j in range(0,len(mat[0])):
             if i<j:
                 mat[i][j]=0
    return mat,'lower triangler'
#58
def dia_of_mat(mat):

    for i in range(0,len(mat)):
            print(mat[i][i])
    return 'are the diagonal elements'



#59
def vre_con_matrics_str(mat):
    b=[]
    j=0
    while(len(b)<len(mat)):
        sum=''
        for i in range(0,len(mat)):
            sum=sum+str(mat[i][j])
        b.append(sum)
        j=j+1
    return b
#60
def hor_con_matrics_str(mat):
    b=[]
    j=0
    while(len(b)<len(mat)):
        sum=''
        for i in range(0,len(mat)):
            sum=sum+str(mat[j][i])
        b.append(sum)
        j=j+1
    return b
#61
def vre_con_matrics(mat):
    b=[]
    j=0
    while(len(b)<len(mat)):
        sum=0
        for i in range(0,len(mat)):
            sum=sum+(mat[i][j])
        b.append(sum)
        j=j+1
    return b
#62
def hor_con_matrics(mat):
    b=[]
    j=0
    while(len(b)<len(mat)):
        sum=0
        for i in range(0,len(mat)):
            sum=sum+(mat[j][i])
        b.append(sum)
        j=j+1
    return b
#63 number conversions (binqry,octal,hexa,etc...)
def to_m(n,m):
    i=[]
    while(n>0):
        a=n%m
        n=n//m
        i.append(a)
    b=i[::-1]
    for j in range(0,len(b)):
        print(b[j],end='')
    return ''
#64
def rev(n):
    return n[::-1]
#65
def rev_of_sen(a):
    b=a.split('+')
    return '-'.join(b[::-1])
#66
def array_join(a):
    return ' '.join(a)
#67
#remove charecter in str
def rem_from_str(a,m,z):
    # string.replace(old char,new char,how many number of old char it should remove)
    return a.replace(m,' ',z)
    
#68 to remove element through index
def rem_i_from_str(n,i):
    return n[0:i]+n[i+1:len(n)]

#69
def rem_fromstr(n,i):
    s=n[i]
    a=n.split(str(s))
    return ' '.join(a)
#70
def sub_str(str,sub):
    if sub in str:
        print('found')
    else:
        print('not found')
#71
def sub_str_replace(string,sub,a):
    
    if sub in string:
         n=string.replace(str(sub),' ',a)
         return n
    else:
        return 'not found'
#72
def cout_sub_in_str(n,m):
    a=n.count(str(m))
    return a
#73
def len_str(n):
    return len(n)
#74
def frq_of_word_in_str(n):
    a=n.split(' ')
    for i in range (0,len(a)):
            b=a.count(a[i])
            print(b,'is frequency of',a[i])
    return ''
#75
def even_len_in_str(n):
    a=n.split(' ')
    for i in range(0,len(a)):
        if len(a[i])%2==0:
            print(a[i],':is an even length word in a string')
        else:
            print(a[i],':is an odd length word in a string')
    return '' 
#76
def pascal(n):
    a=n.split('_')
    c=' '.join(a)
    #return ' '.join(n.slipt('_'))
    return c
#76
def pascal_n(n,s,j):
    return str(j).join(n.split(str(s)))
#77
def vow_in_word_of_str(n):
    if 'a' and 'e' and 'i' and 'o' and "u" in n:
        print('all vowels are found in:')
        return n
    else:
        return 'not found all vovels'
#78
def mat_in_pair_str(a,b):
    v=[]
    for i in range(0,len(a)):
        if a[i] in b:
            v.append(a[i])
            
    return v
#79   ----------nsol1---------
def least_freq_str(n):
    o=[]
    for i in range(0,len(n)):
        p=n.count(n[i])
        if p==1:
             o.append(n[i])
    return o 
#80
def max_freq_of_str(n):
    r=[]
    for i in range(0,len(n)):
        a=n.count(n[i])
        r.append(a)
    f=max(r)
    for i in range(0,len(n)):
        if n.count(n[i])==f:
            return (n[i])

#81
def spe_str(n):
    
    if '[' in  n:
        return 'string has speacial charecter'
    elif '@' in n:
        return 'string has speacial charecter'
    elif '!' in n:
        return 'string has speacial charecter'
    elif '#' in n:
        return 'string has speacial charecter'
    elif '$' in n:
        return 'string has speacial charecter'
    elif '%' in n:
        return 'string has speacial charecter'
    elif '^' in n:
        return 'string has speacial charecter'
    elif '&' in n:
        return 'string has speacial charecter'
    elif '*' in n:
        return 'string has speacial charecter'
    elif '(' in n:
        return 'string has speacial charecter'
    elif ')' in n:
        return 'string has speacial charecter'
    else:
        return 'string has no speacial charecter'


#82
def greater_than_len_k(n,l):
    a=n.split(' ')
    for i in range(0,len(a)):
        s=len(a[i])
        if s>=l:
            print(a[i])
    return ''

#83
def bin_or_not(n):
    a=[]
    
    for i in range(0,len(n)):
        a.append(int(n[i]))
    if max(a)==1 and min(a)==0:
        return 'its a binary'
    else:
        return 'its not a binary'
#84 re write this programme with s1+s2 and remove all duplicates 
def non_dupl_both_dtr(s1,s2):
    s3=s1.split(' ')
    s4=s2.split(' ')
    if len(s3)>len(s4):
        for i in range(0,len(s4)):
            if s4[i] in s3:
                s3.remove(s4[i])
                s4.remove(s4[i])
        return s3+s4
    else:
        for i in range(0,len(s3)):
            if s3[i] in s4:
                s4.remove(s3[i])
                s3.remove(s4[i])
        return s4+s3
#85 
def ascii_to_chr(n):
    return chr(n)
#86
def crack_password(n):
    if  len(n)==1:
        import random
        string=''
        i=0
        while (n!=string):
            a=chr(random.randint(97,122))
            string=str(a)
            print(a)
            i=i+1
    
    if  len(n)==2:
        import random
        string=''
        i=0
        while (n!=string):
            a=chr(random.randint(97,122))
            b=chr(random.randint(97,122))
            string=str(a)+str(b)
            print(a,b)
            i=i+1
    if  len(n)==3:
        import random
        string=''
        i=0
        while (n!=string):
            a=chr(random.randint(97,122))
            b=chr(random.randint(97,122))
            c=chr(random.randint(97,122))
            string=str(a)+str(b)+str(c)
            print(a,b,c)
            i=i+1
    if  len(n)==4:
        import random
        string=''
        i=0
        while (n!=string):
            a=chr(random.randint(97,122))
            b=chr(random.randint(97,122))
            c=chr(random.randint(97,122))
            d=chr(random.randint(97,122))
            string=str(a)+str(b)+str(c)+str(d)
            print(a,b,c,d)
            i=i+1
    return string,'is your string ,its cracked in',i,'iterations'
#87
def url_or_not(s5):
    if 'http//' in s5:
        print('string contain url')
    else:
        print('no url in string')  
    return ''
#88
def otp_crack(n):
    num=0
    i=0
    import time
    t1=time.time()
    while(n!=num):
        import random
        num=random.randint(0000,9999)
        print(num)
        i=i+1
    t2=time.time()
    t=t2-t1
    print('it took',t,'time')
    return num,'generated in',i,'iterations'
#89 check if a str can become empty by recursive deletion
def delta(n,m):
    a=n.split(str(m))
    b=''.join(a)
    if (m==b):
        return 'yes'
    else:
        return 'no'
#90
def non_du(st1,st2):
    s1=st1.split(' ')
    s2=st2.split(' ')
    s=s1+s2
    o=[]
    for i in range(0,len(s)):
        c=s.count(s[i])
        if c==1:
            o.append(s[i])
    return o
#a={
#   'key1':'1',
#    'key2':'2'
#}
#print(a)
#a['key3']='3'
#print(a)
#a['key1']='0'
#print(a)
#del a['key2']
#print(a)
#print(a['key1'])
#d={
#   1:'1',
#    1:'2',
#    2:2,
#    3:3
#}
#in dictionary it takes key values only one time
#print(d)
#91
d={
    'a':[1,5,0],
    'b':[2,3,4],
}
i=d['a']+d['b']
print(i)
g=[]
for j in range(0,len(i)):
    g.append(i[j])
    
g.sort()
print(g)
#92
print(sum(g))
#93
print(d['a'])
#94 for getting nth vlue in a specific key
print(d['a'][2])
#95
del d['a']
print(d)
#96
del  d['b'][2]
print(d)
#97 merge two dictonaries must not contain same key values becoz it take only 1 key
dict1={'name':'madhuri','age':20}
dict2={'nam':'niteesh','ge':19}
res = {** dict1 ,** dict2}
print(res)
p1={
'key2':3,
'key1':1,
'key3':1}
print(sorted(p1.keys()))
print(sorted(p1.items()))
print(sorted(p1.values()))
#98 key value list flat list
d2={'name':['jan','feb','mar'],'mon':[1,2,3]}
a=[]
b=[]
c=[]
for i in range(0,len(d2['mon'])):
    a.append(d2['name'][i])
    b.append(d2['mon'][i])
for j in range(0,len(a)):
    c.append(a[j])
    c.append(b[j])
print(c)
#99
e={'key1':2,'key4':4}
e['key0']=3
i={'key3':3}
#100 add key at beginning of dictionary
print({**i,**e})
#101
a=[1,2,'o']
print(a.__sizeof__(),'bytes')
print(i.__sizeof__(),'bytes')
d=(1,2,['o'])
#102 tuples stores data in low memory than lists
print(d.__sizeof__(),'bytes')
#103 
lis=[1,2,3]
l=len(lis)
k=[]
for i in range(0,l):
        k.append((lis[i],lis[i]**l))
print(k)
#104 
f=[(2,3),(6,7)]
y=(7,11)
for i in range(0,len(f)):
    if y[0]  in f[i]:
        print(f[i])
    elif y[1] in f[i]:
        print(f[i])
#105
a=[1,2,3,4,5,6,7,8,9,106]   
b=round(len(a)/2)   
t=1
mid=a[b]
if t==mid:
    print('found t is mid element at position',a.index(t+1))
elif t>mid:
    for i in range(b+1,len(a)):
        if t==a[i]:
            print('found element after mid value at position',a.index(t+1))
elif t<mid:
    for i in range(0,b):
        if t==a[i]:
            print('found element left side mid value at position',a.index(t+1))
#106 get index of
k=a.index(t)
print(k)
#107
fruits = ["apple", "banana", "cherry"]
x, y, z = fruits
print(x+ ' ','hello')
print(y)
print(z)
#108
x = range(6)
c=[0,1,2,3,4,5,6]
print(x)
'''array is not speacial data type it comes under same type of list'''
#109
print(type(x)) 
print(type(c))
#110
x = ({"apple", "banana", "cherry"},1,frozenset({'1','2'}))
print(type(x)) 
print(type(x[0])) 
print(type(x[2])) 
#111
x = bytearray(5)
y = b'hello'
z= bytes(5)
print(x)
print(type(x)) 
print(memoryview(x))
print(y)
print(type(y))
print(memoryview(y))
print(z)
print(type(z))
print(memoryview(z))
#112 format
quantity = 3
itemno = 567
price = 49.95
myorder = "I want {} pieces of item {} for {} dollars."
print(myorder.format(quantity, itemno, price))
'''

   Method	            Description
capitalize()	    Converts the first character to upper case
casefold()	        Converts string into lower case
center()	        Returns a centered string
count()	            Returns the number of times a specified value occurs in a string
encode()	        Returns an encoded version of the string
endswith()	        Returns true if the string ends with the specified value
expandtabs()	    Sets the tab size of the string
find()	            Searches the string for a specified value and returns the position of where it was found
format()	        Formats specified values in a string
format_map()	    Formats specified values in a string
index()	            Searches the string for a specified value and returns the position of where it was found
isalnum()	        Returns True if all characters in the string are alphanumeric
isalpha()	        Returns True if all characters in the string are in the alphabet
isdecimal()	        Returns True if all characters in the string are decimals
isdigit()	        Returns True if all characters in the string are digits
isidentifier()	    Returns True if the string is an identifier
islower()	        Returns True if all characters in the string are lower case
isnumeric()	        Returns True if all characters in the string are numeric
isprintable()	    Returns True if all characters in the string are printable
isspace()	        Returns True if all characters in the string are whitespaces
istitle()	        Returns True if the string follows the rules of a title
isupper()	        Returns True if all characters in the string are upper case
join()	            Joins the elements of an iterable to the end of the string
ljust()	            Returns a left justified version of the string
lower()	            Converts a string into lower case
lstrip()	        Returns a left trim version of the string
maketrans()	        Returns a translation table to be used in translations
partition()	        Returns a tuple where the string is parted into three parts
replace()	        Returns a string where a specified value is replaced with a specified value
rfind()	            Searches the string for a specified value and returns the last position of where it was found
rindex()	        Searches the string for a specified value and returns the last position of where it was found
rjust()	            Returns a right justified version of the string
rpartition()	    Returns a tuple where the string is parted into three parts
rsplit()	        Splits the string at the specified separator, and returns a list
rstrip()	        Returns a right trim version of the string
split()	            Splits the string at the specified separator, and returns a list
splitlines()	    Splits the string at line breaks and returns a list
startswith()	    Returns true if the string starts with the specified value
strip()	            Returns a trimmed version of the string
swapcase()	        Swaps cases, lower case becomes upper case and vice versa
title()	            Converts the first character of each word to upper case
translate()	        Returns a translated string
upper()	            Converts a string into upper case
zfill()	            Fills the string with a specified number of 0 values at the beginning 
'''
#113
thislist = list(("apple", "banana", "cherry")) # note the double round-brackets
print(thislist)
#114
thislist = ["apple", "banana", "cherry"]
thislist.insert(2, "watermelon")
print(thislist)
'''
 Method	       Description
append()	Adds an element at the end of the list
clear()	    Removes all the elements from the list
copy()	    Returns a copy of the list
count()	    Returns the number of elements with the specified value
extend()	Add the elements of a list (or any iterable), to the end of the current list
index()	    Returns the index of the first element with the specified value
insert()	Adds an element at the specified position
pop()	    Removes the element at the specified position
remove()	Removes the item with the specified value
reverse()	Reverses the order of the list
sort()	    Sorts the list'''
#115 multi assign values
tup = ("app", "nana", "crry", "sterry", "rasry")
(x, *y, z) = tup
print(x)
print(y)
print(z)
#116
thisset = set(("apple", "banana", "cherry")) # note the double round-brackets
print(thisset)
#117 we cant cange the elements in set becouse it doent has order or key but we can add,remove,update(sets),delet   element to it
thisset.add('mango')
'''it doent contain duplicate elements'''
print(thisset)
#118 to  add sets
thisset = {"apple", "banana", "cherry"}
tropical = {"pineapple", "mango", "papaya"}
thisset.update(tropical)
print(thisset)
#119
thisset.remove("banana")
thisset.discard("mango")
#pop will remove 1st element
thisset.pop()

print(thisset)
#120
x = {"apple", "banana", "cherry"}
y = {"google", "microsoft", "apple"}
z = x.intersection(y)
print(z)
'''
Method	            Description
add()	                        Adds an element to the set
clear()	                        Removes all the elements from the set
copy()	                        Returns a copy of the set
difference()	                Returns a set containing the difference between two or more sets
difference_update()	            Removes the items in this set that are also included in another, specified set
discard()	                    Remove the specified item
intersection()	                Returns a set, that is the intersection of two other sets
intersection_update()	        Removes the items in this set that are not present in other, specified set(s)
isdisjoint()	                Returns whether two sets have a intersection or not
issubset()	                    Returns whether another set contains this set or not
issuperset()	                Returns whether this set contains another set or not
pop()	                        Removes an element from the set
remove()	                    Removes the specified element
symmetric_difference()	        Returns a set with the symmetric differences of two sets
symmetric_difference_update()	inserts the symmetric differences from this set and another
union()	                        Return a set containing the union of sets
update()	                    Update the set with the union of this set and others'''
'''
As of Python version 3.7, dictionaries are ordered. In Python 3.6 and earlier, dictionaries are unordered.
'''
#121
thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}

x = thisdict.keys()
y=thisdict.values()
z=thisdict.items()
print(x,y,z)
'''
Method	  Description
clear()	        Removes all the elements from the dictionary
copy()	        Returns a copy of the dictionary
fromkeys()	    Returns a dictionary with the specified keys and value
get()	        Returns the value of the specified key
items()	        Returns a list containing a tuple for each key value pair
keys()	        Returns a list containing the dictionary's keys
pop()	        Removes the element with the specified key
popitem()	    Removes the last inserted key-value pair
setdefault()	Returns the value of the specified key. If the key does not exist: insert the key, with the specified value
update()	    Updates the dictionary with the specified key-value pairs
values()	    Returns a list of all the values in the dictionary'''
a = 200
b = 33
c = 500
if a > b or a > c:
  print("At least one of the conditions is True")
#122
def asq(n):
    x=lambda a,b:a*n*b
    return x
b=asq(2)
print(b(9,2))
#123
#instade of using two or more for loops use zip
x = [1, 2, 3, 4]
y = [4, 5, 6, 7]
z = []

for i, j in zip(x, y):
  z.append(i + j)
print(z)
#124
import numpy as np

arr1 = np.array([10, 20, 30, 40, 50, 60])
arr2 = np.array([3, 7, 9, 8, 2, 33])

newarr = np.mod(arr1, arr2)

print(newarr)
#125
import numpy as np

arr1 = np.array([10, 20, 30, 40, 50, 60])
arr2 = np.array([3, 7, 9, 8, 2, 33])

newarr = np.remainder(arr1, arr2)

print(newarr)
#126
import numpy as np

arr1 = np.array([10, 20, 30, 40, 50, 60])
arr2 = np.array([3, 7, 9, 8, 2, 33])

newarr = np.divmod(arr1, arr2)

print(newarr)
#127
arr = np.trunc([-3.1666, 3.6667])
arr1=np.fix([-3.1666, 3.6667])
arr2 = np.floor([-3.1666, 3.6667])
arr3 = np.ceil([-3.1666, 3.6667])
arr4 = np.around([3.1666, 2])
print(np.log2(arr))
print(arr,arr1,arr2,arr3,arr4)
#128
import numpy as np

arr1 = np.array([1, 2, 3])
arr2 = np.array([1, 2, 3])

newarr = np.sum([arr1, arr2], axis=1)
new=np.sum([arr1, arr2], axis=0)
print(newarr,new)
#129
import numpy as np

arr1 = np.array([1, 2, 3, 4])
arr2 = np.array([5, 6, 7, 8])
n=np.prod(arr1)
newarr = np.prod([arr1, arr2], axis=1)

print(n,newarr)
#130
newarr = np.diff(arr1)
print(newarr)
#131
arr = np.array([3, 6, 9])
import numpy as np

arr = np.array([20, 8, 32, 36, 16])

gcd = np.gcd.reduce(arr)
lcm = np.lcm.reduce(arr)
print(gcd,lcm)
#132
arr = np.array([np.pi/2, np.pi/3, np.pi/4, np.pi/5])
x = np.sin(arr)
print(x)
#133
import numpy as np

arr = np.array([90, 180, 270, 360])

x = np.deg2rad(arr)

print(x)
#134 inverse trignimetric function
import numpy as np

x = np.arcsin(1.0)

print(x)
#135
import pandas as pd

a = [1, 7, 2]
b =  ['ka','djb','ef']
l = pd.Series(a)
m = pd.Series(a, index = ["x", "y", "z"])
n=pd.DataFrame(a)
o=pd.DataFrame(a,b)
print(l,m,n,o)
#we cant access dict directly with out using keys 
dict={
    'key1':['h','i','j'],
    'key2':[1,2,3]
}
#but we can convert dict to dataframe using pandas and 
#acess with out keys
df=pd.DataFrame(dict)
print(df)
df=pd.DataFrame(dict,index=['r1','r2','r3'])
print(df)
calories = {"day1": 420, "day2": 380, "day3": 390}
myvar = pd.Series(calories)
print(myvar)
#in Series key name in dict acts as index 
myvar = pd.Series(calories, index = ["day1", "day2"])
print(myvar)
data = {
  "calories": [420, 380, 390],
  "duration": [50, 40, 45]
}

#load data into a DataFrame object:
df = pd.DataFrame(data,index=['1','2','3'])
print(df.loc['2'])
print(df.loc['1'])
#read rows
print(df.loc[['3']])
print(df.loc[['2','1']])
#df.loc[[rownames to print as table]], [row names print values]
print(df.loc[['1','2','3']])
#to change values
df.loc[['1','duration']==55]
print(df)
#read colomns
print(df.columns)
print(df.calories)
print(df.info())
for i in range(0,len(df.calories)):
    if df.calories[i]>300:
                print(df.calories[i],df.duration[i])
#or
print(df['calories'])
import pandas as pd

df = pd.read_csv('data.csv')
df = pd.read_csv('data.csv')
#filling 120 in null in empty cell
df.fillna(120,inplace=True)
#filling 120 in null in Data row
df['Date'].fillna(120,inplace=True)
#dropping all empty rows
df.dropna( inplace = True)
#dropping all empty rows in Date if has null 
df.dropna(subset=['Date'], inplace = True)
#to drop 12 row
df.drop(12,inplace=True)
print(df.to_string())
#removing duplicate rows
df.drop_duplicates(inplace = True)
#to get graphical data
data = {
  "calories": [420, 380, 580],
  "duration": [50, 40, 45]
}
df = pd.DataFrame(data,index=['1','2','3'])
df.plot()
import matplotlib.pyplot as plt
plt.show()
plt.plot(df.duration,df.calories)
plt.show()

import scipy as sp

print(dir(sp.constants))
#for exampple 
print(sp.constants.liter)
print(sp.constants.micron)
print(sp.constants.light_year)
print(sp.constants.golden_ratio)
print(sp.constants.golden_ratio)

#Three lines to make our compiler able to draw:

import matplotlib.pyplot as plt
import numpy as np

xpoints = np.array([1, 8,9])
ypoints = np.array([3, 10,20])
#plt.plot(x,y,
#marker marker='shapes',
#markersize ms=number,
#markeredgecolor mec='color 1st letter',
# markerfacecolor mfc='color 1st letter',
# linestyle ls=' dashed,dotted,,,etc',
# color c='1st letter of color')
plt.subplot(2, 4, 1)
plt.plot(xpoints, ypoints,marker='*',ms=15,mfc='r',mec='g',ls = '-.',lw='3',c='m')
font1 = {'family':'serif','color':'blue','size':20}
font2 = {'family':'serif','color':'darkred','size':15}

plt.title("Title", fontdict = font1)
plt.xlabel("x axis name", fontdict = font2)
plt.ylabel("y axis name", fontdict = font2)

plt.subplot(2, 4, 2)
plt.plot(xpoints, ypoints,marker='*',ms=15,mfc='r',mec='g',ls = '-.',lw='3',c='m')
plt.grid(axis = 'y')
plt.subplot(2, 4, 3)
plt.grid(axis = 'x')
plt.subplot(2, 4, 4)
plt.grid()

plt.subplot(2, 4, 5)
plt.scatter(xpoints,ypoints)
plt.show()
import matplotlib.pyplot as plt
import numpy as np

x = np.array([5,7,8,7,2,17,2,9,4,11,12,9,6])
y = np.array([99,86,87,88,111,86,103,87,94,78,77,85,86])
colors = np.array(["red","green","blue","yellow","pink","black","orange","purple","beige","brown","gray","cyan","magenta"])

plt.scatter(x, y, c=colors)

plt.show()
import matplotlib.pyplot as plt
import numpy as np

x = np.random.randint(100, size=(100))
y = np.random.randint(100, size=(100))
colors = np.random.randint(100, size=(100))
sizes = 10 * np.random.randint(100, size=(100))

plt.scatter(x, y, c=colors, s=sizes, alpha=0.5, cmap='nipy_spectral')

plt.colorbar()
plt.show()

x = np.random.normal(170, 10, 250)

plt.hist(x)
plt.show()
x = np.array([1,2,3,4,5])
y = np.array([20,10,30,50,12])
plt.bar(x,y,width=0.1,color='red')
plt.show()  
x = np.array([1,2,3,4,5])
y = [20,10,30,50,12]
plt.pie(x,labels=y)
plt.show() 

x = np.array([35, 25, 25, 15])
y = ["Apples", "Bananas", "Cherries", "Dates"]
s = [0.2, 0, 0.5, 0]

plt.pie(x, labels = y, explode = s, shadow = True)
plt.show() 






