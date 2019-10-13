#!/usr/bin/env python

import rospy
from std_msgs.msg import Float32
import RPi.GPIO as GPIO

class Servo():

    def __init__(self, pin):
        # SG90
        self.l_max = 2.5
        self.r_max = 12

        #self.newtral = 6.5
        #self.l_max = 4.7
        #self.r_max = 9
        self.pin = pin

        self.pwm_range = self.r_max - self.l_max
        
        GPIO.setmode(GPIO.BCM)
        GPIO.setup(self.pin, GPIO.OUT)
        self.servo = GPIO.PWM(self.pin, 50)
        self.servo.start(0.0)

    def callback(self, data):
        if data.data > 1 or data.data < -1:
            rospy.loginfo(f'out of range {data.data}')
        self.servo.ChangeDutyCycle(self.rate2pwmcycle(data.data))

    def rate2pwmcycle(self, rate):
        input_range = 2  # -1 ~ 1
        input_min = -1
        pwm_cycle = (((rate - input_min) * self.pwm_range) / input_range) + self.l_max
        rospy.loginfo(f'pwm input: {pwm_cycle}')
        return pwm_cycle

    def stop(self):
        self.servo.stop()
        GPIO.cleanup()


def main():
    servo = Servo(pin=23)
    rospy.init_node('servo_controller', anonymous=True)
    rospy.Subscriber("servo", Float32, servo.callback)
    try:
        rospy.spin()
    finally:
        servo.stop()

if __name__ == '__main__':
    main()

