#Nathan Cheshire
#nvc29
#CSE1284-03 String exericse program
#Assigned by Jesse on 11/02/18

import sys
from collections import OrderedDict

def main():

    try:

        while True:

            IntegerNumber = ''

            try:

                IntegerNumber = int(input('Enter any positive or negative integer (non-decimal number): '))

            except ValueError as e:
                print('Sorry, but that is not a valid integer.')

            except Exception as e:
                print('Sorry, but something went wrong\nError: ',e)

            else:

                print('\nWord:\n' + SendIt(str(IntegerNumber)) + '\n')

                print('Roman Numeral:\n' + write_roman(IntegerNumber) + '\n')

                Again()

    except Exception as e:
        print('')

def Again():

    Continue = input('Would you like to enter another number (Y/N)? ')

    while Continue.lower() != 'y' and Continue.lower() != 'n':

        print('Sorry, but that is not a valid choice.')

        Continue = input('Would you like to enter another number (Y/N)? ')

    if (Continue.lower() == 'y'):
        print('')
        main()

    else:
        sys.exit()

def SendIt(FixIt):

    try:

        Prefixes = ['','-thousand','-million','-billion','-trillion','-quadrillion',
                    '-quintillion','-sextillion','-septillion', '-octillion', '-nonillion',
                    '-decillion', '-undecillion', '-duodecillion', '-tredecillion',
                    '-quattuordecillion','-quindecillion', '-sexdexillion', '-septendecillion',
                    '-octodecillion', '-novemdecillion', '-vigintillion','-centillion']

        Negative = False

        for i in FixIt:

            if i == '0':
                FixIt = FixIt[1:]
            elif i != '0':
                break

        IntegerNumber = int(FixIt)

        if IntegerNumber < 0:

            Negative = True

            IntegerNumber *= -1

        Numbers = [int(x) for x in str(IntegerNumber)]

        while len(Numbers) % 3 != 0:
            Numbers = [0] + Numbers

        Numbers = list(map(str, Numbers))

        Numbers = Split(Numbers, len(Numbers) // 3)

        NewNumbers = []

        for i in Numbers:

            AddingToNewNumbers = [int(numeric_string) for numeric_string in i]

            NewNumbers.append(AddingToNewNumbers)

        Numbers = NewNumbers

        ThreeNumbersList = []

        for i in Numbers:

            Word = ' '.join(ThreeLetterWord(i).split())

            ThreeNumbersList.append(Word)

        ThreeNumbersList.reverse()

        NumberNamesList = []

        for i in range(0,len(ThreeNumbersList)):

            CorrectWord = ThreeNumbersList[i] + '' + Prefixes[i]

            if CorrectWord == Prefixes[i]:

                continue

            NumberNamesList.append(CorrectWord)

        NumberNamesList.reverse()

        ReturnWord = ''

        if Negative == True:
            ReturnWord += 'Negative '

        for word in NumberNamesList:
            ReturnWord += ' ' + word

        ReturnWord = ' '.join(ReturnWord.split())

        return ReturnWord

    except IndexError:
        print('I don\'t think that you can actually do something useful with a number that big.')

        main()

    except Exception as e:
        print('Sorry, but something went wrong.\nError:',e)

def Split(TheList, wanted_parts = 1):

    length = len(TheList)

    return [TheList[i*length // wanted_parts: (i+1)*length // wanted_parts]
             for i in range(wanted_parts) ]

def ThreeLetterWord(number):

   ThreeDigitNumber = int(str(number[0]) + str(number[1]) + str(number[2]))

   if ThreeDigitNumber < 100:

       if ThreeDigitNumber < 20 and ThreeDigitNumber > 9:

           if ThreeDigitNumber == 10:
               return 'ten'
           elif ThreeDigitNumber == 11:
               return 'eleven'
           elif ThreeDigitNumber == 12:
               return 'twelve'
           elif ThreeDigitNumber == 13:
               return 'thirteen'
           elif ThreeDigitNumber == 14:
               return 'fourteen'
           elif ThreeDigitNumber == 15:
               return 'fifteen'
           elif ThreeDigitNumber == 16:
               return 'sixteen'
           elif ThreeDigitNumber == 17:
               return 'seventeen'
           elif ThreeDigitNumber == 18:
               return 'eighteen'
           elif ThreeDigitNumber == 19:
               return 'nineteen'

       elif ThreeDigitNumber <= 9:

            if ThreeDigitNumber == 0:

                return ''

            return WordFor0To9(ThreeDigitNumber)

       else:

           ReturnWord = WordForTens(number[1]) + ' ' + WordFor0To9(number[2])

           return ReturnWord

   FinalWord = ''

   HundredsWord = WordFor0To9(number[0])

   FinalWord = str(HundredsWord) + ' hundred ' + str(FinalWord)

   if number[1] == 0:

       FinalWord = FinalWord + ' ' + WordFor0To9(number[2])

       return FinalWord

   number.pop(0)

   num = int(str(number[0]) + str(number[1]))

   if num < 20:

       if num == 10:
           return FinalWord + ' ten'
       elif num == 11:
           return FinalWord + ' eleven'
       elif num == 12:
           return FinalWord + ' twelve'
       elif num == 13:
           return FinalWord + ' thirteen'
       elif num == 14:
           return FinalWord + ' fourteen'
       elif num == 15:
           return FinalWord + ' fifteen'
       elif num == 16:
           return FinalWord + ' sixteen'
       elif num == 17:
           return FinalWord + ' seventeen'
       elif num == 18:
           return FinalWord + ' eighteen'
       elif num == 19:
           return FinalWord + ' nineteen'

   else:

       TensPlace = WordForTens(number[0])

       FinalWord = FinalWord + ' ' + TensPlace + ' ' + WordFor0To9(number[1])

   return FinalWord

def WordForTens(num):

    if num == 2:
        return 'twenty'
    elif num == 3:
        return 'thirty'
    elif num == 4:
        return 'forty'
    elif num == 5:
        return 'fifty'
    elif num == 6:
        return 'sixty'
    elif num == 7:
        return 'seventy'
    elif num == 8:
        return 'eighty'
    elif num == 9:
        return 'ninety'

def WordFor0To9(num):

    if num == 0:
        return ''
    elif num == 1:
        return 'one'
    elif num == 2:
        return 'two'
    elif num == 3:
        return 'three'
    elif num == 4:
        return 'four'
    elif num == 5:
        return 'five'
    elif num == 6:
        return 'six'
    elif num == 7:
        return 'seven'
    elif num == 8:
        return 'eight'
    elif num == 9:
        return 'nine'

def write_roman(num):

    try:

        roman = OrderedDict()
        roman[1000] = "M"
        roman[900] = "CM"
        roman[500] = "D"
        roman[400] = "CD"
        roman[100] = "C"
        roman[90] = "XC"
        roman[50] = "L"
        roman[40] = "XL"
        roman[10] = "X"
        roman[9] = "IX"
        roman[5] = "V"
        roman[4] = "IV"
        roman[1] = "I"

        def roman_num(num):
            for r in roman.keys():
                x, y = divmod(num, r)
                yield roman[r] * x
                num -= (r * x)
                if num > 0:
                    roman_num(num)
                else:
                    break

        return "".join([a for a in roman_num(num)])

    except Exception as e:
        print('Sorry, but I can\'t convert a number that big into a Roman Numeral')

        return 0

main()