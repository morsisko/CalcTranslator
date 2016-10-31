import re
import argparse
from datetime import datetime, timedelta

class CalculatorTranslator:
    constToReplace = "regexValue"
    normalMatches = {
        'o' : '0',
        'd' : '0',
        'i' : '1',
        'z' : '2',
        'e' : '3',
        'h' : '4',
        's' : '5',
        'l' : '7',
        'b' : '8',
        'g' : '9',
        }

    specialMatches = {
        'ó' : '0',
        'ż' : '2',
        'ź' : '2',
        'ę' : '3',
        'ś' : '5',
        'ł' : '7',
    }

    startRegex = r"(^[" + constToReplace + r"]+$)"
    defaultFormat = "%w -> %c"

    def __init__(self, inFile, outFile, includeSpecials=False, includeDots=False, maxCharacters = 8, format=defaultFormat, header=False):
        if includeSpecials is False:
            self.matches = self.normalMatches
        else:
            self.matches = {**self.normalMatches, **self.specialMatches}

        self.inFile = open(inFile, 'r', encoding='utf-8')
        self.outFile = open(outFile, 'w', encoding='utf-8')
        self.format = format
        self.includeDots = includeDots
        self.includeSpecials = includeSpecials
        self.maxCharacters = maxCharacters
        self.iteration = 0
        self.lines = 0
        self.regex = ""
        self.header = header
        self.prepareRegex()

    def prepareRegex(self):
        listOfMatchesKeys = list(self.matches.keys())
        possibleLetters = ""
        possibleLetters = possibleLetters.join(listOfMatchesKeys)
        self.regex = self.startRegex.replace(self.constToReplace, possibleLetters)

    def reverseString(self, string):
        return string[::-1]


    def convertStringToCalculatorNumbers(self, string):
        toReturn = ""
        for character in string:
            toReturn += self.matches[character]

        return self.reverseString(toReturn)

    def formatString(self, word, calcString, lenExcludingDot):
        return (self.format.replace("%w", word)
            .replace("%c", calcString)
            .replace("%i", str(self.iteration))
            .replace("%l", str(lenExcludingDot))
            .replace('\n', ""))

    def endMessage(self):
            print("Script found: " + str(self.iteration) + " word(s), of total: " + str(self.lines))

    def mainLoop(self):
        if self.header is True:
            self.outFile.write("List generated thanks to: https://github.com/morsisko/text2calc\n" +
            "Settings: includeSpecials = " + str(self.includeSpecials) + ", " +
            "includeDots = " + str(self.includeDots) + ", " +
            "maxCharacters = " + str(self.maxCharacters) + ", " +
            "format = '" + self.format + "'\n")
        
        for line in self.inFile:
            self.lines += 1
            m = re.search(self.regex, line)

            if not m:
                continue
            
            output = m.group(0)
            calculatorString = self.convertStringToCalculatorNumbers(output)

            wordLenExcludingDot = len(calculatorString)
            if wordLenExcludingDot > self.maxCharacters:
                continue
            
            if calculatorString[0] == '0':
                if self.includeDots == False:
                    continue
                
                calculatorString = "0." + calculatorString[1:]
            
            self.iteration += 1

            self.outFile.write(self.formatString(line, calculatorString, wordLenExcludingDot) + "\n")

        self.endMessage()



parser = argparse.ArgumentParser(description="Program that convert a list of words to this one, which you can write in your calculator")
parser.add_argument('in', type=str, help = "A name of file, which contains words to check")
parser.add_argument('out', type=str, help = "A name of file, which will contains the program output")
parser.add_argument('--header', action='store_false', help= "Disables the header at the beginning of out file")
parser.add_argument('--special', action='store_true', help = "Use it, if you want to create list including the special characters, like Z with dot, etc.")
parser.add_argument('--dots', action='store_false', help = "Use it, if you don't want words that starts with '0.' on your list")
parser.add_argument('-maxCharacters', type=int, help="Max length of word, excluding dot, the default value is 8", default=8)
parser.add_argument('-format', type=str, help="The format that will be used to write output. Possible values are: %%w - It will be replaced with the word, %%c - Will be replaced with the calculator numbers, %%i - Will be replaced with the order number, starting with 1 \
 %%l - Will be replaced with the length of word. Default format is equal to: %%w -> %%c", default=["%w", "->", "%c"], nargs='+')

args = vars(parser.parse_args())
print(str(args))
startTime = datetime.now()

translator = CalculatorTranslator(inFile=args['in'], outFile=args['out'], includeSpecials=args['special'], includeDots=args['dots'], format=" ".join(args['format']), maxCharacters=args['maxCharacters'], header=args['header'])
translator.mainLoop()

stopTime = datetime.now() - startTime

print("Operation took: " + str(stopTime.total_seconds()) + " seconds")
