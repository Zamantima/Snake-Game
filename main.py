from turtle import Turtle, Screen
from snake import Snake
from food import Food
import time
import food
from scoreboard import Scoreboard


screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("My Snake Game")
screen.tracer(0) #method in screen class

snake = Snake()
food = Food()
score = Scoreboard()


screen.listen()
screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.left, "Left")
screen.onkey(snake.right, "Right")

is_game_on = True
while is_game_on:
   screen.update()
   time.sleep(0.1)
   snake.move()

   if snake.head.distance(food) < 15:
      food.refresh()
      snake.extend()
      score.increase_score()

   #Detect collision with wall
   if snake.head.xcor() > 290 or snake.head.xcor() < -290 or snake.head.ycor() > 290 or snake.head.ycor() < -290:
      is_game_on = False
      score.game_over()

   #Detect collision with tail
   for segment in snake.segments[1:]:
      if snake.head.distance(segment) < 10:
         is_game_on = False
         score.game_over()



screen.exitonclick()