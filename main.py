print("Welcome to my first game.\n\n")

name = input("What is your name? ")
age = int(input("What is your age? "))

print("\nHello", name)

health = 10;

if age >= 18:
  print("You are old enough to play.")

  wants_to_play = input("\nDo you want to play?[yes/no] ").lower()
  if wants_to_play == "yes":
    print("You are starting with", health, "health")
    print("Let's Play--->")

    left_or_right = input("First choice... Left or Right?[left/right] ").lower()
    if left_or_right == "left":
      
      ans = input("\nNice, you follow the path and reach a lake... Do you swim across or go around?[across/around] ").lower()
      if ans == "around":
        print("\nYou went around and reached the other side of the lake.")
      elif ans == "across":
        print("\nYou managed to get across, but were bit by a snake and lost 5 helath.")
        health -= 5
      ans = input("\nYou notice a house and a river. Which do you go to?[river/house]: ").lower()
      if ans == "house":
        print("\nYou go to the house and are greted by the owner... He doesn't like you and you lose 5 health.")
        health -= 5

        if health <= 0:
          print("\nYou now have 0 health and you lost the game...")
        else:
          print("\nYou have survived... You win!")
      else:
        print("\nYou fell in the river and lost...")
    else:
      print("\nYou fell down and lost.")   
  else:
    print("\nCya...")
else:
  print("\nYou are not old enogh to play.")