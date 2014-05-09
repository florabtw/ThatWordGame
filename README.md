That Word Game
==============

I have no idea what the name of this game is, but I decided to program it for fun.

To run, simply type:

    python thatWordGame.py
  
or:

    chmod +x thatWordGame.py
    ./thatWordGame.py
    
What does this game actually do? Well, it finds all the words that can be made from a source word.

Here is an example:

    $ ./thatWordGame.py 
    Choose a word: dogecoin
    
    ['coin', 'code', 'dog', 'do', 'die', 'end', 'ego', 'good', 'go', 'in', 'ice', 'icon', 'i', 'nod', 'no', 'nice', 'one', 'on', 'once']
    
Right now it only contains around 2300 of the most common English words.

To increase the number of words, replace the words.txt file in the extras folder with a new CSV with the same name. Then, run the moveWords.py script.
