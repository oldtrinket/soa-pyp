def find_highest_number(num1, num2, num3):
  """Finds and returns the highest number among three numbers."""
  return max(num1, num2, num3)

def main():
  """Generates three random numbers between 1 and 100 and prints the highest one."""
  num1 = random.randint(1, 100)
  num2 = random.randint(1, 100)
  num3 = random.randint(1, 100)

 highest_number = find_highest_number(num1, num2, num3)
  print("The highest number is:", highest_number)

if __name__ == "__main__":
  m


 
