import nxt, thread, time
import nxt.bluesock # Make sure you remember this!
b = nxt.bluesock.BlueSock('00:16:53:10:22:3D').connect() #replace the string with the one you got earlier
#b = nxt.find_one_brick()

mx = nxt.Motor(b, nxt.PORT_A)

def turnmotor(m, power, degrees):
	m.turn(power, degrees)
#how long from start until the last instruction is ended
length = 1

def runinstruction():
	#THIS IS THE IMPORTANT PART!
	thread.start_new_thread(
		turnmotor,
		(mx, 127, 10))
seconds = 0
while 1:
	print "Tick %d" % seconds
	runinstruction()
	seconds = seconds + 1
	time.sleep(.01)
