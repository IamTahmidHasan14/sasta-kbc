def q3():
  print("\nQ.3 (Amoun will be 1500 or 0)")
  print("What is the capital of Australia?")
  print("1.Delhi  2.Dhaka  3.Bankok  4.Canberra")
  t3 = int(input("Choose your answer:"))
  if (t3 == option[3]):
    print("Correct, You won 1500")
  else:
    print("Wrong, You lost all")


def q2():
  print("\nQ.2 (Amoun will be 1000 or 0)")
  print("What is the capital of India?")
  print("1.Delhi  2.Dhaka  3.Bankok  4.Canberra")
  t2 = int(input("Choose your answer:"))
  if (t2 == option[0]):
    print("Correct, You won 1000")
    q3()
  else:
    print("Wrong, You lost all")


print("\nWELLCOME TO KBC")
print("\nQ.1 (Amoun will be 500)")
print("What is the capital of Bangladesh?")
print("1.Delhi  2.Dhaka  3.Bankok  4.Canberra")
t1 = int(input("Choose your answer:"))
option = [1, 2, 3, 4]
if (t1 == option[1]):
  print("Correct, You won 500")
  q2()
else:
  print("Wrong")
