import csv

def read_portfolio(filename, * , errors = 'warn'): # the * forces you to use the name of the variable in the call
	'''
	Reads a csv file in list.
	'''
	if errors not in { 'warn', 'silent', 'raise' }:
		raise ValueError("errors must to be one of 'warn', 'silent', 'raise'")
	
	portfolio = []	#List of records
	
	with open(filename ,"r") as f:
		rows = csv.reader(f, skipinitialspace=True)
		headers = next(rows) #skip a line
		for rowno, row in enumerate(rows, start=1):
			try:
				row[0] = int(row[0])
				row[1] = int(row[1])
			except ValueError as err:
				if errors == 'warn':
					print('row:',rowno, 'Bad row:', row, 'reason:',err )
				elif errors == 'raise':
					raise # Reraises the last exception 
				else:
					pass #Ignores
				continue	#skips to the next row
			# total += row[1] 
			# record = tuple(row)
			record = {
				'year':row[0],
				'score':row[1],
				'Name':row[2]

			}
			portfolio.append(record)
	return portfolio

portfolio = read_portfolio('./data/missing.csv', errors='silent')
# print(portfolio)
total = 0.0

# for holding in portfolio:
	# total += holding[0]
for holding in portfolio:
	total += holding['score']

# for score  in portfolio:
	# total += score
	# print(score[1])
	
print('total is: {:>2.2f}'.format(total))  
# total = portfolio_cost('./data/missing.csv', errors='silent') #putting the name of the variable in this case is best practices
# print('Total is: {:>2.2f}'.format(total))  