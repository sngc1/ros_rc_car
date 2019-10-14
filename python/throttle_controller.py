#!/usr/bin/env python

import rospy
from std_msgs.msg import Float32
import RPi.GPIO as GPIO

class Servo():

    def __init__(self, pin):
        self.forward_max = 10.0
        self.backward_max = 3.0
        self.stop = 6.6
        self.pin = pin

        self.pwm_range = self.forward_max - self.backward_max
        
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
        pwm_cycle = (((rate - input_min) * self.pwm_range) / input_range) + self.backward_max
        rospy.loginfo(f'pwm input: {pwm_cycle}')
        return pwm_cycle

    def stop(self):
        rospy.loginfo('cleanup throttle servo')
        self.servo.stop()
        GPIO.cleanup()


def main():
    servo = Servo(pin=24)
    rospy.init_node('throttle_controller', anonymous=True)
    rospy.Subscriber("servo/throttle", Float32, servo.callback)
    try:
        rospy.spin()
    finally:
        servo.stop()

if __name__ == '__main__':
    main()

