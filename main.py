def prime_checker(number):
  prime_count = 0
  if number == 2:
    print("It's a prime number.")
  elif number == 1:
    print("It's not a prime number.")
  else:
    for i in range(2, number):
      if number % i == 0:
        prime_count += 1
    if prime_count > 0:
      print("It's not a prime number.")
    elif prime_count == 0:
      print("It's a prime number.")

n = int(input("Check this number: "))
prime_checker(number=n)