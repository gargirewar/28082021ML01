Python 3.9.6 (tags/v3.9.6:db3ff76, Jun 28 2021, 15:26:21) [MSC v.1929 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> #ques 2
>>> 5**9
1953125
>>> 3//2
1
>>> 7//3
2
>>> 7/3
2.3333333333333335
>>> 6==6
True
>>> a=20; a+=30; print(a)
50
>>> True * False
0
>>> True & False
False
>>> True and False
False
>>> ((6>3) and (7<4) or (18==3)) and (9>3)
False
>>> True is False
False
>>> ((True == False) or (False > True)) and (False <= True)
False
>>> #ques 3
>>> s1 = "Nice to have it"
>>> s2 = " here"
>>> s = s1 + s2
>>> s
'Nice to have it here'
>>> #ques 4
>>> a= [1,2,[3,4],[5,[100,200,['hello']],23,11],1,7]
>>> a[3] [1:2] [0] [-1:] [0] [0]
'hello'
>>> #ques 5
>>> a= [1,2,[3,4],[5,[100,200,['hello']],23,11],1,7]
>>> a[3].insert(0,"Nice to have it")
>>> a[3].insert(5,"here")
>>> a
[1, 2, [3, 4], ['Nice to have it', 5, [100, 200, ['hello']], 23, 11, 'here'], 1, 7]
>>> #ques 7
>>> color_list_1= set(["White", "Black", "Red"])
>>> color_list_2= set(["Red", "Green"])
>>> color_list_1.difference(color_list_2)
{'Black', 'White'}
>>> 