def pesudo_random_generator(initial_vector,coef,n=100):
	if len(initial_vector)!=len(coef):
		raise Exception("two list must have  the same length")
	output_list=initial_vector
	
	for i in range(n):
		output_list=calc_next(coef,output_list)

	print(output_list)
	return output_list
def check_element(input_list):
	for ele in input_list:
		if not (ele==1 or ele==0):
			raise Exception("element of list must be 1 or 0")



def calc_next(coef,output_list):
	output=0
	index=-1
	for i  in range(len(coef)):
		output+=coef[index]*output_list[index]
		index-=1

	output=output%2
	output_list.append(output)
	return output_list



if __name__=="__main__":
	coef=[1,0,1]
	initial=[0,0,1]
	initial2=[1,1,0]
	pesudo_random_generator(initial,coef,n=100)
	print("")
	pesudo_random_generator(initial2,coef,n=100)