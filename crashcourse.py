# PRINT
print("i'm dead inside")


########################
# PYTHON AS A CALCULATOR

1+1

5/2
5/2. # this is not the same in python 2.7

17 % 3  # the % operator returns the remainder of the division

5 ** 2  # 5 squared


########################
# variables

potatoes = 5
bananas = 3
potatoes * bananas


########################
# strings

'wonderful spam'
'don\'t eat the eggs'

eggs = 'don\'t eat the eggs'
spam = 'wonderful spam'

eggs + spam
eggs + ' ' + spam


########################
# while loops

while True:
	print("redrum")

# control-C to stop

while 1==1:
	print("take the blue pill")

# control-C to stop

a = 0
while a < 4:
	# print(a)
	print("all work no play makes jack a dull boy")
	a = a + 1

########################
#FIBONACCI
a = 0
b = 1

while a < 100:
	print(a)
	a, b = b, a+b



########################
#Text Scrambler


# slice notation
url = 'http://www.shoptillyoudrop.com'
url[0]      # displays: h
url[1]      # displays: t
url[0:7]    # displays: http://
url[:7]     # displays: http://
url[7:]     # displays: www.shoptillyoudrop.com
url[-3:]    # displays: com
url[11:-4]  # displays: shoptillyoudrop


# string methods
url.upper()       # HTTP://WWW.SHOPTILLYOUDROP.COM
url.count('w')    # 3
url.count('www')  # 1
css = url.find('://')    # 4

mytext = "What to do with this all? Paste it to the wall with some photos and see what it looks like. Wait, paste these two pages together and cut in the middle. Paste it all together, end to end, and send it out like a big piano-roll. After all, it's not but matter. There's nothing sacred about words."

textlist = mytext.split()

import random

random.shuffle(textlist)
print(textlist)

scrambledtext = ' '.join(textlist)


########################
#Assignment
#make a text scrambler that creates 100 versions


mytext = "Je vais voir avec le SPAV si c’est possible pour eux d’attendre et d’intégrer la partie audio sur laquelle vous retravaillez avec Clément. Je te tiens informé"
textlist = mytext.split()
a=0

while a < 100:
	random.shuffle(textlist)
	scrambledtext = ' '.join(textlist)
	print(scrambledtext)
	a = a + 1


