# bounce.py
#
# Exercise 1.5

ball_height = 100 # meters
bounce_modifier = 3.0/5

for i in range(10):
    ball_height = round(ball_height * bounce_modifier, ndigits=4)
    print(i, ball_height)