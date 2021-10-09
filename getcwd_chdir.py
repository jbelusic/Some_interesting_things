
def main():
	print(os.getcwd())
	files = os.listdir(os.getcwd())
	print(files)
	print("\n------------------------------------------\n")
	os.chdir("C:/") # OR os.chdir("D:\\")
	print(os.getcwd())
	files = os.listdir(os.getcwd())
	print(files)

if __name__ == '__main__':
	import os
	main()
