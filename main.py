import time
setTemp = int(input("Set temp to: "))

while(1==1):
	#For testing
	#temp = int(input("Current temp: "))
	
	#Get temperature from from sensor
	python get_temp.py
	
	#Determine wether temp is too high or too low,
	#and how far off it is
	correction = setTemp - temp
	if correction > 0:
		#print("Light is now on")
		#[Code for energizing relay to turn on light here]
		time.sleep(5)
	if correction < 0:
		#print("Light is now off")
		#[Code for denergizing relay to turn off light here]
		time.sleep(5)
