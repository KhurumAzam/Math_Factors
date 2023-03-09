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

if __name__ == "__main__":
    obj = Factors()
    while True:
        try:
            num = int(input("What's the number you want factor:"))
            obj.factors(num)
            try:
                choice = input("Do you want to exit program (y or n):")
                if choice == "y":
                    break
                else:
                    continue
            except Exception as e:
                print("Error in input, please enter a valid input")
        except Exception as e:
            print("Error in input, please enter a valid input")
