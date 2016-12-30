# EasyIO_RPi
Easier GPIO interaction with Raspberry Pi

EasyIO_RPi adds aditional layers of functionality to the standard RPi.GPIO to make simple, but functional animated LED's faster
with less redundant code.

# Usage Examples
Assuming there is a blue LED on GPIO 5 a yellow LED on GPIO 22, and a yellow LED on GPIO 19

```python
import LED_Animate
    from EasyIO_Rpi import LED_Animate
    
    blu = 5
    red = 22
    ylw = 19
```

Pass the LED's into the LED_Animate. It will handle GPIO.setmode() so you don't have to.

```python

    led = LED_Animate( blu, red, ylw )
 
 ```
 
to <b> blink </b> an LED 3 times with .5 seconds between each blink and each blink lasting one second

```python

    led.blink( blu, 1, .5, 3 )

```
![](https://github.com/chrispwns/EasyIO_RPi/blob/master/images/blinking_blue.gif)

to <b> sweep across a set of LED's </b> use the <b> sweep </b> method

```python

  # led.sweep( duration, timeout, *LEDs , **options )
  # duration is the time the LED is on
  # timeout is the time between an LED turning off and another Turning on
  
    led.sweep( .05, .1, red, blu, ylw )
    
    # to sweep the LED's and then reverse ass reverse=True
    
    led.sweep( .05, .1, red, blu, ylw, reverse=True )
    
    # You can also specify the amount of times the sweep should repeat itself
    led.sweep( .05, .1, red, blu, ylw, repeat=2 )
    
    # repeat also works with reverse
    led.sweep( .05, .1, red, blu, ylw, reverse=True, repeat=2 )
```
<b>Sweep</b>

![](https://raw.githubusercontent.com/chrispwns/EasyIO_RPi/master/images/plain_sweep.gif)

<b>Sweep with Reverse </b>

![](https://github.com/chrispwns/EasyIO_RPi/blob/master/images/reverse_sweep.gif)


<b>Sweep with Repeat </b>

![](https://github.com/chrispwns/EasyIO_RPi/blob/master/images/repeat_sweep.gif)

<b> Sweep with Repeat + reverse </b>

![](https://github.com/chrispwns/EasyIO_RPi/blob/master/images/reverse_repeat_sweep.gif)


to <b> pause on one color </b> for a set amount of time use <b> hold </b>

```python

    led.hold(blu, 3) # where 3 is the time (in seconds) to hold the color
```
