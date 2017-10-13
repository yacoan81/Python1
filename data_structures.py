# tupples 

t = ('AA', '2017-0607', 100, 32.7)
# print(t)
print(len(t))
print(t[0])
print(t[2]*t[3])

# t[0] = 'BB' # tupples are inmutable  

name, data, price, shares = t #packing, unpacking
print(name)

#list objects
names = ['IBM', 'YHOO', 'AA', 'CAT' ]
print(names)
print(names[0])
names[1] = 'YAHOO' 

names.append('IBM')
names.insert(1, 'FB')
print(names)

#sets -- removes duplicates
distinct_names = {'IBM', 'FB', 'MSBT', 'IMB', 'CAT', 'AA', 'IBM'}
print(distinct_names)

print(names)
print(set(names))

print('AA' in distinct_names)
print('JJ' in distinct_names)

#Dictionaries
prices = {
	'IBM': 91.2,
	'MSFT': 95.2,
	'AA': 45.3,
	'YHOO': 9.23
}

print(prices['IBM'])

prices['IBM'] = 89.2
print(prices['IBM'])
print('IBM' in prices)

# lists
items = [ ('AA', 145, 13.3), ('IBM' , 670, 24.5) , ('YHOO', 100, 29.3)]
print(items[1])

prices = {
	'IBM': {'low':89.2, 'high':95.2, 'current':92.5}
	}
print(prices['IBM']['low'])