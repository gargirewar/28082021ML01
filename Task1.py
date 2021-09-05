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
>>> s1= "Nice to have it"
>>> s2= " here"
>>> s1 + s2
'Nice to have it here'
>>> #ques 4
>>> a= [1,2,[3,4],[5,[100,200,['hello']],23,11],1,7]
>>> a[3] [1:2] [0] [-1:] [0] [0]
'hello'
>>> #ques 5
>>> a= [1,2,[3,4],[5,[100,200,['hello']],23,11],1,7]
>>> a.insert(0,"Nice to have it")
>>> a.insert(7,"here")
>>> a
['Nice to have it', 1, 2, [3, 4], [5, [100, 200, ['hello']], 23, 11], 1, 7, 'here']
>>> #ques 6
>>> num=[386,462,47,418,907,344,236,375,823,566,597,978,328,615,953,345,399,162,758,219,918,237,412,566,826,248,866,950,626,949,687,217,815,67,104,58,512,24,892,894,767,553,81,379,843,831,445,742,717,958,743,527]
>>> for i in num:
	if i==237:
		print(i)
		break;
	elif i%2==0:
		print(i)

		
386
462
418
344
236
566
978
328
162
758
918
237
>>> #ques 7
>>> color_list_1= set(["White", "Black", "Red"])
>>> color_list_2= set(["Red", "Green"])
>>> color_list_1.difference(color_list_2)
{'White', 'Black'}
>>> #ques 8
>>> s= 'abcdefghijklmnopqrstuvwxyz'
>>> query= 'hello sir'
>>> p=True
>>> for i in s:
	if i not in query:
		p==False
		break
	if p==0:
		pangram
	else:
		not pangram

		
False
>>> #ques 9
>>> n= input()
5
>>> k=0
>>> for i in range(1,4):
	k+=int(n*i)

	
>>> k
615
>>> #ques 10
>>> x,y=input().split('#')
23 54 12#98 3 17
>>> x=[int(i) for i in x.split()]
>>> y=[int(i) for i in y.split()]
>>> print(x,y)
[23, 54, 12] [98, 3, 17]
>>> #ques 11
>>> a=input().split(',')
without,hello,bag,world
>>> a.sort()
>>> print(','.join(a))
bag,hello,without,world
>>> #ques 12
>>> d={'Student': ['Rahul', 'Kishore', 'Vidhya', 'Raakhi'], 'Marks': [57,87,67,79]}
>>> max(d['Marks'])
87
>>> d['Marks'].index(max(d['Marks']))
1
>>> print(d['Student'][d['Marks'].index(max(d['Marks']))])
Kishore
>>> #ques 13
>>> s= input()
hello world! 123
>>> l=d=0
>>> for i in s:
	if i.isalpha():
		l+=1
	elif i.isnumeric():
		d+=1
	else:
		pass

	
>>> print('LETTERS',l);print('DIGITS',d)
LETTERS 10
DIGITS 3
>>> #ques 14
>>> d={'Name':['Akash', 'Soniya', 'Vishakha', 'Akshay', 'Rahul', 'Vikas'], 'Subject':['Python', 'Java', 'Python', 'C', 'Python', 'Java'], 'Ratings':[8.4,7.8,8,9,8.2,5.6]}
>>> d.items()
dict_items([('Name', ['Akash', 'Soniya', 'Vishakha', 'Akshay', 'Rahul', 'Vikas']), ('Subject', ['Python', 'Java', 'Python', 'C', 'Python', 'Java']), ('Ratings', [8.4, 7.8, 8, 9, 8.2, 5.6])])
>>> python=newData={k:v[::2] for (k,v) in d.items()}
>>> python
{'Name': ['Akash', 'Vishakha', 'Rahul'], 'Subject': ['Python', 'Python', 'Python'], 'Ratings': [8.4, 8, 8.2]}
>>> #ques 15
>>> n=int(input('enter a number:'))
enter a number:14
>>> a=[i for i in range(0,n+1) if i%7==0]
>>> a
[0, 7, 14]
>>> ##############################