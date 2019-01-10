import serial
import time

arduino = serial.Serial("/dev/ttyACMO")
arduino.baudrate = 9600


if __name__ == '__main__':

	while (1):

		data = arduino.readline()
		time.sleep(.1)
		data = arduino.readline()
		pieces = data.split("\t")

		distance = pieces[0]
		angle = pieces [1]

		print(distance)
		print(angle)

		time.sleep(.1)


