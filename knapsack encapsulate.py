class dinamic:

	def getMax(self, group, row, groups, n):
		max_ = 0
		for i in range(1,n+1):
			if groups[i] == group:
				if row[i] > max_:
					max_ = row[i]
		return max_

	def IsMaxInGroup(self, n, w, groups, matrix, N):
		group = groups[n]
		max_ = 0;
		for i in range(1, N+1):
			if groups[i] == group:
				if matrix[w][i] > max_:
					max_ = matrix[w][i]

		if matrix[w][n] != max_:
			return False
		return True

W = 10
profit = [0,0,3,4,5,0,4,6,10,10,5,8,12,18,17,10,12,18,30,24,15,20,27,44,30]
weight = [0,0,1,2,5,0,1,2,5,10,1,2,4,9,17,2,3,6,15,24,3,5,9,22,30]
group = [0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 2, 2, 2, 2, 2, 3, 3, 3, 3, 3, 4, 4, 4, 4, 4]
max_profit = 0

def MCKS(profit, weight, group):
	global max_profit
	N = len(profit) - 1
	din = dinamic()
	matrix = [] 			# W + 1, N + 1
	sol = []				# W + 1, N + 1

	for i in range(W + 1):
		temp = []
		for j in range(N + 1):
			temp.append(0)
		matrix.append(temp)

	for i in range(W + 1):
		temp = []
		for j in range(N + 1):
			temp.append(False)
		sol.append(temp)

	for i in range(W + 1):
		matrix[i][0] = i

	for w in range(1, W + 1):
		for n in range(1, N + 1):
			if group[n] == 0:
				if weight[n] <= w:
					matrix[w][n] = profit[n];
					sol[w][n] = True
			else:
				if group[n] != group[n-1]:
					option1 = din.getMax(group[n-1], matrix[w], group, n)
					option2 = -10000000
					if weight[n] <= w:
						option2 = profit[n] + din.getMax(group[n-1], matrix[w-weight[n]], group, n)
					matrix[w][n] = max(option1, option2)
					if option2 > option1:
						sol[w][n] = True
					else:
						sol[w][n] = False

				if group[n] == group[n-1]:
					option1 = din.getMax(group[n]-1, matrix[w], group, n)
					option2 = -10000000
					if weight[n] <= w:
						option2 = profit[n] + din.getMax(group[n]-1, matrix[w-weight[n]], group, n)
					matrix[w][n] = max(option2, option1)
					if option2 > option1:
						sol[w][n] = True
					else:
						sol[w][n] = False

	take = []
	for i in range(N + 1):
		take.append(False)

	for n in range(N, 0, -1):
		w = W
		if sol[w][n] and din.IsMaxInGroup(n,w,group, matrix, N):
			take[n] = True
			w = w - weight[i]
		else:
			take[n] = False

	max_group = max(group)
	group_id = []
	for i in range(len(group)):
		if max_group == group[i]:
			group_id.append(i)

	max_profit = max(matrix[W])
	max_profit_id = []
	temp_profit_max_list = []
	for i in range(len(group_id)):
		temp_profit_max_list.append(matrix[W][group_id[i]])
	for i in range(len(group_id)):
		if max_profit == matrix[W][group_id[i]]:
			max_profit_id.append(group_id[i])

	print("max profit: " + str(max_profit))
	rest_profit = max_profit
	rest_weight = W
	group_number = max_group
	func(rest_weight, group_number, rest_profit, "", matrix)

temp_result = []
def get_result(result):
	temp_result.append(result)

def func(rest_weight,group_number,rest_profit , path, matrix): # rest_weiht = row
	temp_result = []

	if(rest_weight<=0 or rest_profit <=0):
		# print(path)
		get_result(path)
		# print(temp_result)
		return True
	find_profit = rest_profit
	find_profit_id = []
	for i in range(len(profit)):
		if (group[i] == group_number) and (find_profit == matrix[rest_weight][i]):
			find_profit_id.append(i)


	for i in range(len(find_profit_id)):
		temp_result.append(find_profit_id[i]+1)
		next_path = path + "%d," % (find_profit_id[i]+1)
		next_profit = rest_profit - profit[find_profit_id[i]]
		next_weight = rest_weight - weight[find_profit_id[i]]
		func(next_weight,group_number-1,next_profit,next_path, matrix)

MCKS(profit, weight, group)

# print(temp_result)
final_result = []
for i in range(len(temp_result)):
	if i == 0:
		final_result.append(max_profit)
	temp = []
	for j in range(len(temp_result[i].split(","))):
		if j < len(temp_result[i].split(","))-1:
			temp.append(int(temp_result[i].split(",")[j]))
	final_result.append(temp)
print(final_result)
#final result array is final_result. you can use this array for output.