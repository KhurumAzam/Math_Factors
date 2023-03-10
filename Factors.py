class Factors:
    nums = []

    def factors(self, num1):
        try:
            for i in range(num1 + 1):
                for j in range(num1 + 1):
                    if i * j == num1 and not ((i,j) in self.nums or (j,i) in self.nums):
                        self.nums.append((i,j))
                        print(f"{i} & {j} are a factor of {num1}")
                    else:
                        continue
        except Exception as e:
            print("Error in calculation:",e)

    def list_factors(self):
        temp = tuple(set(self.nums))
        temp2 = []
        for i in tuple(set(self.nums)):
            for j in i:
                temp2.append(j)
        temp2.sort()
        print(f"Factors are: {temp2}")

if __name__ == "__main__":
    obj = Factors()
    while True:
        try:
            num = int(input("What's the number you want factor:"))
            obj.factors(num)
            obj.list_factors()
            try:
                choice = input("Do you want to exit program (y or n):")
                if choice == "y":
                    break
                else:
                    obj.nums = []
                    continue
            except Exception as e:
                print("Error in input, please enter a valid input")
        except Exception as e:
            print("Error in input, please enter a valid input")
