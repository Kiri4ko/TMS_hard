# **The mini game to solve a logic puzzle**

1. There are two buckets, one 3 liters and the other 5 liters and an unlimited amount of water.
2. The user can:\
   Pour water into any bucket.\
   Pour water from any bucket.\
   Pour water from one bucket to another.\
   User wins if he managed to get exactly 4 liters.
3. The user enters one of seven commands:\
fill_5l\
fill_3l\
pour_5l\
pour_3l\
pour_from_5_in_3\
pour_from_3_to_5\
exit 
4. The program runs until the user gets 4 liters or exits. 
5. There cannot be a negative amount of water in the buckets. 
6. The buckets cannot hold more than the calculated bucket capacity (3L and 5L). 
7. The program has a move counter and returns to the user the number of moves for which he has solved the problem.
8. The best result - 6 moves.
