# bounce.py
#
# Exercise 1.5
def main():
	h = 100
	numberOfValues = 10
	for i in range(1,numberOfValues+1):
		h *= 0.6
		print(i,round(h,4))
if __name__ == '__main__':
	main()