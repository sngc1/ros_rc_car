#!/usr/bin/env python

import getch
import rospy
from std_msgs.msg import Float32


CONTROL_KEYS=('r', 'l', 'n', 'f', 'b', 's')      

def teleoperator():
    pub_steer = rospy.Publisher('servo/steering', Float32, queue_size=10)
    pub_throt = rospy.Publisher('servo/throttle', Float32, queue_size=10)
    rospy.init_node('kb_teleop', anonymous=True)
    rate = rospy.Rate(10) # 10hz

    cmd_steer_val = 0.0
    cmd_throt_val = 0.0
    step = 0.01
    cmd_val_max = 1.0
    cmd_val_min = -1.0

    rospy.loginfo(f'Press key: (l)eft, (r)ight, (n)eutral, (f)orward, (b)ackward, (s)top')
    while not rospy.is_shutdown():
        kb_input = getch.getch()
        if kb_input in CONTROL_KEYS: 
            cmd = kb_input
            rospy.loginfo(f'keyboard input:{cmd}')
            
            if cmd == 'n':
                cmd_steer_val = 0.0

            if cmd == 'r':
                cmd_steer_val -= step
            
            if cmd == 'l':
                cmd_steer_val += step

            if cmd == 's':
                cmd_throt_val = 0.0

            if cmd == 'b':
                cmd_throt_val -= step

            if cmd == 'f':
                cmd_throt_val += step
    
            if cmd_steer_val < cmd_val_min:
                cmd_steer_val = cmd_val_min
            if cmd_steer_val > cmd_val_max:
                cmd_steer_val = cmd_val_max
            if cmd_throt_val < cmd_val_min:
                cmd_throt_val = cmd_val_min
            if cmd_throt_val > cmd_val_max:
                cmd_throt_val = cmd_val_max

            rospy.loginfo(f'steer: {cmd_steer_val}, throttle: {cmd_throt_val}')
            pub_steer.publish(cmd_steer_val)
            pub_throt.publish(cmd_throt_val)
        #rate.sleep()

if __name__ == '__main__':
    try:
        teleoperator()
    except rospy.ROSInterruptException:
        pass
