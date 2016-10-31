# What is it?
CalcTranslator is a simple script writed in python 3.5, that allow you to parse a list of words, into a list that you can write in your calculator!

# How do I use it?
It's simple. First you need the list of words with proper syntax:

    first
	second
	and
	so
	on

Now you need to run that script. There is short help:
**It's recommend to take the -format parametr into a quotes "", eg. -format "%i. %w -> %c"**
`
usage: parser.py [-h] [--header] [--special] [--dots]
                 [-maxCharacters MAXCHARACTERS] [-format FORMAT [FORMAT ...]]
                 in out

Program that convert a list of words to this one, which you can write in your
calculator

positional arguments:
  in                    A name of file, which contains words to check
  out                   A name of file, which will contains the program output

optional arguments:
  -h, --help            show this help message and exit
  --header              Disables the header at the beginning of out file
  --special             Use it, if you want to create list including the
                        special characters, like Z with dot, etc.
  --dots                Use it, if you don't want words that starts with '0.'
                        on your list
  -maxCharacters MAXCHARACTERS
                        Max length of word, excluding dot, the default value
                        is 8
  -format FORMAT [FORMAT ...]
                        The format that will be used to write output. Possible
                        values are: 
						%w - It will be replaced with the word, 
						%c - Will be replaced with the calculator numbers, 
						%i - Will be replaced with the order number, starting with 1 
						%l - Will be replaced with the length of word.
                        Default format is equal to: %w -> %c
`

# What with the output?

Take for example the word "hello", and look at the output:
`hello == 0.7734 (5)`
Now get your calculator in hand, and type "0.7734". Great, now turn him by 180 degrees and look at the display!
![Hello](http://i.imgur.com/tYShXXx.jpg)

# Examples
An example list of polish words created by this script:

# License
Tool is developed under MIT license
