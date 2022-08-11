num = int(input("How many numbers?\n"))
total_sum = 0
for n in range(num):
    numbers = int(input("Enter any number\n"))
    total_sum += numbers
avg = total_sum/num
print("Average is: ", avg)
