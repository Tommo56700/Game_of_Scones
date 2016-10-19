just did a bunch of testing, ignoring the puzzle situation you're working on;

1.The loop is a bit "clingy" after you perform an action, the "you can" in the print menu appears fast and disorientates you, maybe we could use a time.sleep() there?

2. If you type retreat into the game whilst fighting a boss. It automatically defeats the boss(could keep that as a cheat in-case we need to speedily run through it again) although i doubt anyone will figure out you can do that.

3. Following error after defeating mary berry:
You take the Super Secret Formula

Traceback (most recent call last):
  File "C:\Users\rdsta\Google Drive\CM1101\Group Work\Game_of_Scones-master\Game_of_Scones-master\game.py", line 1045, in <module>
    main()
  File "C:\Users\rdsta\Google Drive\CM1101\Group Work\Game_of_Scones-master\Game_of_Scones-master\game.py", line 1035, in main
    you_won()
  File "C:\Users\rdsta\Google Drive\CM1101\Group Work\Game_of_Scones-master\Game_of_Scones-master\youwon.py", line 7, in you_won
    input("Ding dong old chap, the wicked witch is dead! You pry a piece of crumpled\nparchment from her cold, dead hands which reveals to you the secret recipe of\nMary\u2019s magical scones. (Flour, butter, milk, eggs). You bake the perfect scone\nand the curse that has plagued this land is forever broken.")
  File "C:\Users\rdsta\AppData\Local\Programs\Python\Python35-32\lib\encodings\cp850.py", line 12, in encode
    return codecs.charmap_encode(input,errors,encoding_map)
UnicodeEncodeError: 'charmap' codec can't encode character '\u2019' in position 156: character maps to <undefined>