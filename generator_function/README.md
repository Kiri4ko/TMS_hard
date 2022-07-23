# **Generator Functions**

1. The **gen_pin_code.py** uses the geretaor function to create pin codes.
   The numbers follow without repetition, but can be repeated in the pin code.
   Line 13 sets the size of the pin code, by default the pin code consists of four digits.
2. The **gen_pin_simple.py** is a simple version, given that the numbers can be repeated sequentially.
3. File **guessing_game.py** is a guessing game. In the thirteenth line the first argument is the number of attempts
   to guess the digit, the second and third arguments are the range of guessable digits.
4. File **guessing_game_simple.py** is a light version of the game - guess what.
   The "randit" specifies the range, the cycle "for" the number of attempts. 👇

```
num_game = randint(0, 10)
game = (int(input("Your number - ")) for i in range(4))
```
