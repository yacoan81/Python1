# f = open('./data/portfolio.csv', 'r')
# data = f.read()
# print(data) 
# f.close()

f = open('./data/portfolio.csv', 'r')
for line in f:
	print(line)

# f.close()
# with open('./data/portfolio.csv', 'r') as f:
# 	data = f.read()

print(line) 
print(line.strip(','))
# parts = line.split(',')

# print(parts[1])