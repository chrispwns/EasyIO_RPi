import RPi.GPIO as GPIO
from time import sleep
 
class LED_Animate:
    """
   Built to handle common LED Function
   :param *args: LED's to initialize as output
       only has to initialized on the first call
   """
    def __init__(self, *args):
        # Initialize ON and OFF variables for easier to read code
        self.ON = GPIO.HIGH
        self.OFF = GPIO.LOW
        # Broadcom numbering
        GPIO.setmode(GPIO.BCM)
        # Console warnings off
        GPIO.setwarnings(False)
       
        # set LED's for output
        for arg in args:
            GPIO.setup(arg, GPIO.OUT)
 
    def blink(self, LED, duration, timeout, num_of_blinks):
        """
       Handles blinking effects for each of the colors
       :param LED: which GPIO the LED is at
       :param duration: time in seconds that each led is lit
       :param timeout: time between each blink
       :param num_of_blinks: how many times to blink
       :return: none
       """
        for i in range(num_of_blinks):
            GPIO.output(LED, self.ON)# LED ON
            sleep(duration) # LED stays on for duration
            GPIO.output(LED, self.OFF) # LED off
            sleep(timeout)# LED stays off until time for next blink
 
    def sweep(self, duration, timeout, *args, **kwargs):
        """
       Sweep across colors in an order defined by the user.
       :param duration: time in seconds each led it lit
       :param timeout: time between each blink
       :param *args: LED's to sweep, in desired order
       :param reverse = Bool: if True LED's will go in reverse order after initial sweep
       :param repeat: number of times to repeat the sequence
       """
        # Check for optional fields
        if kwargs is not None:
 
            # Reverse and repeating
            if 'reverse' in kwargs and kwargs["reverse"] == True\
                and 'repeat' in kwargs: # reverse
 
                for i in range( kwargs['repeat'] ):
                    LED_list = [] # Array to store all LED's in
                    LED_rev_list = [] # list to store reverse values
                   
                    for arg in args:
                        LED_list.append(arg)# Add LED's to Array
                        LED_rev_list.append(arg) # list to be reversed and apended
 
                    LED_rev_list.reverse() # reverse the list
                    # append list of reversed values except the first value, which
                        # would be a repeat of the last value
                    for i in range( 1, len(LED_list)-1 ):
                        LED_list.append( LED_rev_list[i] )
 
                    # ouput the reversed LED's
                    for i in range( len(LED_list) ):
                        GPIO.output( LED_list[i], self.ON )
                        sleep( duration )
                        GPIO.output( LED_list[i], self.OFF )
                        sleep( timeout )
           
            # Reverse and not repeating
            elif 'reverse' in kwargs and kwargs["reverse"] == True:
                LED_list = [] # Array to store all LED's in
                LED_rev_list = [] # list to store reverse values
               
                for arg in args:
                    LED_list.append(arg)# Add LED's to Array
                    LED_rev_list.append(arg) # list to be reversed and apended
 
                LED_rev_list.reverse() # reverse the list
                # append list of reversed values except the first value, which
                    # would be a repeat of the last value
                for i in range( 1, len(LED_list) ):
                    LED_list.append( LED_rev_list[i] )
     
                for i in range( len(LED_list) ): # ouput the reversed LED's
                    GPIO.output( LED_list[i], self.ON )
                    sleep( duration )
                    GPIO.output( LED_list[i], self.OFF )
                    sleep( timeout )
                   
            # Repeat in kwargs, but not reversing      
            elif 'repeat' in kwargs:
                for repeat in range( kwargs['repeat'] ):
                    for arg in args:
                        GPIO.output(arg, self.ON) # current LED on
                        sleep(duration)
                        GPIO.output(arg, self.OFF) # current LED off
                        sleep(timeout)
                   
               
               
        else: # No kwargs    
            for arg in args:
                GPIO.output(arg, self.ON) # current LED on
                sleep(duration)
                GPIO.output(arg, self.OFF) # current LED off
                sleep(timeout)
 
    def hold(self, LED, time_to_hold):
        """
       Holds an LED on for specified time.
       :param LED: GPIO location of the LED
       :param time_to_hold: time in seconds to hold the led
       """
        GPIO.output(LED, self.ON)
        sleep(time_to_hold)
        GPIO.output(LED, self.OFF)