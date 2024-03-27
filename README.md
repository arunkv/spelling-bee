# Spelling Bee Solver

Generates all words for the New York Times [Spelling Bee](https://www.nytimes.com/puzzles/spelling-bee) game.

## Usage

`spelling_bee.py [-h] -c CENTER -o OTHER [-m MIN] -d DICT`

Options:
```
  -h, --help                 show this help message and exit
  -c CENTER, --center CENTER Center letter
  -o OTHER, --other OTHER    Other letters
  -m MIN, --min MIN          Minimum word length
  -d DICT, --dict DICT       Dictionary file
```

## Example
> `./spelling_bee.py -c n -o ruoajd -d WORD.LST`

```
Total words: 37
Pangrams: ['adjourn']
Valid words: ['runaround', 'nonjuror', 'runround', 'adjourn', 'unround', 'adnoun', 'anuran', 'around', 'donjon', 'jordan', 'randan', 'adorn', 'donna', 'donor', 'jnana', 'radon', 'rondo', 'round', 'ruana', 'anna', 'anoa', 'anon', 'darn', 'dona', 'durn', 'naan', 'nada', 'nana', 'nard', 'nona', 'noon', 'noun', 'nurd', 'rand', 'roan', 'unau', 'undo']
```

## License
Apache License 2.0
