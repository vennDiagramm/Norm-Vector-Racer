import random
import turtle
import math

t = turtle.Turtle()
t.hideturtle()
screen = turtle.Screen()
turtle.bgcolor("#E4A211")
turtle.title("The Norm Vector Racer!")


def pythagorean_sum(numbers):
  # Calculate the sum of squares
  sum_of_squares = sum(num**2 for num in numbers)
  # Take the square root of the sum of squares
  result = math.sqrt(sum_of_squares)
  rounded_res = round(result, 2)
  return rounded_res


def player_turn(player_turtle, player_name):
  # Generate 3 random numbers
  random_numbers = [random.randint(1, 20) for _ in range(3)]
  # Calculate the expected result using pythagorean_sum()
  expected_result = pythagorean_sum(random_numbers)

  # Display the random numbers
  print("===========================================================")
  print("For Test Purposes. Answer: ", expected_result)
  print("Find the Norm of the Vector")
  print(f"{player_name} got: v = {random_numbers}\n")

  while True:
    # Ask for the player's answer
    user_answer = float(
        input(f"{player_name}, what is the norm of the vector? "))

    # Check if the user's answer matches the expected result
    if user_answer == expected_result:
      print("Correct! Moving closer to the goal\n")
      move = 100  # Move based on the sum of the random numbers
      player_turtle.fd(move)
      break
    else:
      print("Incorrect answer.\n")
      break


def create_players():
  turtle.register_shape("p1.gif")
  turtle.register_shape("p2.gif")
  turtle.register_shape("p3.gif")

  p1 = turtle.Turtle()
  p1.color("blue")
  p1.shape("p1.gif")
  p1.penup()
  p1.setheading(90)
  p1.goto(250, -200)

  p2 = p1.clone()
  p2.shape("p2.gif")
  p2.color("red")
  p2.penup()
  p2.goto(0, -200)

  p3 = p2.clone()
  p3.shape("p3.gif")
  p3.color("#414042")
  p3.penup()
  p3.goto(-250, -200)

  return p1, p2, p3


def finish_line(p1, p2, p3):
  p1.goto(310, 230)
  p1.pendown()
  p1.lt(90)
  p1.forward(150)
  p1.penup()
  p1.goto(250, -200)

  p2.goto(70, 230)
  p2.pendown()
  p2.lt(90)
  p2.forward(150)
  p2.penup()
  p2.goto(0, -200)

  p3.goto(-160, 230)
  p3.pendown()
  p3.lt(90)
  p3.forward(150)
  p3.penup()
  p3.goto(-250, -200)

  # P1,P2,P3 position
  p1.rt(90)
  p2.rt(90)
  p3.rt(90)


def talk(message, x, y):
  t.penup()
  t.goto(x, y)
  t.pendown()
  t.write(message, align="center", font=("Arial", 16, "normal"))


def name(p1, p2, p3):
  p1 = input("Enter Player 1: ")
  p2 = input("Enter Player 2: ")
  p3 = input("Enter Player 3: ")

  t.pencolor("blue")
  talk(p1, 250, -300)

  t.pencolor("red")
  talk(p2, 0, -300)

  t.pencolor("#414042")
  talk(p3, -250, -300)


def play(p1, p2, p3):
  i = 0
  global current_player
  current_player = 1

  for i in range(20):
    if p1.ycor() >= 220:
      print("Player 1 Wins!")
      t.pencolor("blue")
      talk("PLAYER 1 WINS!", 0, 0)
      talk("PLAYER 1 WINS!", 270, 200)
      break
    elif p2.ycor() >= 220:
      print("Player 2 Wins!")
      t.pencolor("red")
      talk("PLAYER 2 WINS!", 70, 200)
      break
    elif p3.ycor() >= 220:
      print("Player 3 Wins!")
      t.pencolor("#414042")
      talk("PLAYER 3 WINS!", -170, 200)
      break
    else:
      if current_player == 1:
        player_turn(p1, "Player 1")
      elif current_player == 2:
        player_turn(p2, "Player 2")
      elif current_player == 3:
        player_turn(p3, "Player 3")
      current_player = (current_player % 3) + 1


p1, p2, p3 = create_players()
finish_line(p1, p2, p3)
name("", "", "")
play(p1, p2, p3)
turtle.mainloop()
