numbers = []
count = 0

while count < 5:
  num = int(input(f"Enter number {count + 1}: "))
  numbers.append(num)
  count = count + 1

for num in numbers:
  if num % 2 == 0:
     print(f"{num} is Even")
  else:
     print(f"{num} is Odd")