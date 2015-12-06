myAge=12

if myAge>20:     
	print('you are old')
elif myAge<10:
	print('you are young')
else: 
	print('you are in the middle')
def speakEnglish():
	print('You speak fluently')
	print('Your English is very good')
speakEnglish()

km=40
def speed(km):
	if km >60:
		print('You drive fast')
	elif km <40:
		print('You drive very slow')
	else:
		print('you drive slow')

speed(km)

def hi(name):
    print('Hi ' + name + '!')

animals= ['cow', 'dog', 'cat', 'elephant']
for name in animals:
	hi(name)
	print("next animal")


for numbers in range(1,9):
	print(numbers)