from turtle import Screen
from snake import Snake
from food import Food
from scoreboard import Scoreboard
import time

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("Snack Game")
screen.tracer(0)

snake = Snake()
food = Food()
scoreboard = Scoreboard()

screen.listen()
screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.left, "Left")
screen.onkey(snake.right, "Right")

game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update()
    snake.move()

    #Detect Collision with food
    if snake.head.distance(food) < 15:
        food.refresh()
        for segment in snake.segments:
            if segment.pos == food.position:
                food.refresh()
                break
        food.goto(food.random_x, food.random_y)
        snake.tail_increment()
        scoreboard.update_score()

    #Detect collision with wall
    if snake.head.xcor() >= 300 or snake.head.xcor() <-291 or snake.head.ycor() >= 300 or snake.head.ycor() < -291:
        for segment in snake.segments:
            segment.undo()
        game_is_on = False
        scoreboard.game_over()

    #Detect collision with tail
    for segment in snake.segments[1:]:
        if snake.head.distance(segment) < 10:
            game_is_on = False
            scoreboard.game_over()

snake.head.color("red")
screen.update()



screen.exitonclick()
