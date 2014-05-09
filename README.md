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

    $ ./thatWordGame.py dogecoin
    Words found: 108
    ['cone', 'coni', 'codein', 'congo', 'conge', 'coin', 'coigned', 'conoid', 'cine', 'coned', 'cod', 'cog', 'con', 'condo', 'coding', 'coed', 'codon', 'coigne', 'code', 'coign', 'coden', 'cooed', 'coo', 'cedi', 'cion', 'ceding', 'coined', 'cogon', 'cig', 'cooing', 'coon', 'dice', 'ding', 'dine', 'dino', 'den', 'dingo', 'do', 'de', 'deco', 'die', 'deign', 'deni', 'doing', 'don', 'doc', 'dog', 'doe', 'dogie', 'din', 'dinge', 'doge', 'done', 'dong', 'dig', 'eng', 'eon', 'ego', 'end', 'en', 'ed', 'geodic', 'ged', 'gen', 'goo', 'god', 'goodie', 'gie', 'genic', 'go', 'good', 'goon', 'geoid', 'gid', 'goonie', 'gone', 'gied', 'gien', 'gin', 'iced', 'incog', 'ice', 'icon', 'ion', 'in', 'id', 'noogie', 'nog', 'neg', 'ne', 'noo', 'nod', 'node', 'noodge', 'nodi', 'nide', 'no', 'nice', 'oi', 'once', 'odic', 'odeon', 'on', 'oe', 'od', 'ono', 'one', 'ode']


Right now, the word list contains all words from the *Official Tournament and Club  Word List* for Scrabble. This contains a little over 150,000 words.

To increase the number of words, replace the words.csv file in the extras folder with a new CSV with the same name. Then, run the moveWords.py script. The replacement file *must* be in the same format.
