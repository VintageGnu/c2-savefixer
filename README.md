# c2-savefixer

Fixes a [Clickpocalypse 2](https://minmaxia.com/c2/) save file if you get stuck off the side of the map.

## Usage

python c2-savefixer.py [-h] (-f FILE | -i INPUT) (-l | -r)

```
optional arguments:
  -h, --help            show this help message and exit
  -f FILE, --file FILE  Input file
  -i INPUT, --input INPUT
                        Input text
  -l, --left            Move party to the left
  -r, --right           Move party to the right 
```

Outputs the encoded save string with the party moved 5000 spaces, ready to be imported back into the game.
