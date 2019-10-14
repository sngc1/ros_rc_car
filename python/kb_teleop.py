#!/usr/bin/env python

import getch
import rospy
from std_msgs.msg import Float32


CONTROL_KEYS=('r', 'l', 'n')      

def teleoperator():
    pub = rospy.Publisher('servo', Float32, queue_size=10)
    rospy.init_node('kb_teleop', anonymous=True)
    rate = rospy.Rate(10) # 10hz

    cmd_val = 0.0
    step = 0.1
    cmd_val_max = 1.0
    cmd_val_min = -1.0

    rospy.loginfo(f'Press key: (l)eft, (r)ight, (n)eutral')
    while not rospy.is_shutdown():
        kb_input = getch.getch()
        if kb_input in CONTROL_KEYS: 
            cmd = kb_input
            rospy.loginfo(f'keyboard input:{cmd}')
            
            if cmd == 'n':
                cmd_val = 0.0

            if cmd == 'r':
                cmd_val -= step
            
            if cmd == 'l':
                cmd_val += step

            if cmd_val < cmd_val_min:
                cmd_val = cmd_val_min
            if cmd_val > cmd_val_max:
                cmd_val = cmd_val_max

            rospy.loginfo(f'cmd_val: {cmd_val}')
            pub.publish(cmd_val)
        #rate.sleep()

if __name__ == '__main__':
    try:
        teleoperator()
    except rospy.ROSInterruptException:
        pass
