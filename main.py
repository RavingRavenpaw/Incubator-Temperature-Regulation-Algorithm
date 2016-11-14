import time
setTemp = int(input("Set temperature to: "))

while(1==1):
	temp = int(input("Current temperature: "))
	correction = setTemp - temp
	if correction > 0:
		print("Light is now on")
		time.sleep(5)
	if correction < 0:
		print("Light is now off")
		time.sleep(5)
