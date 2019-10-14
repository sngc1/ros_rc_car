# ros_rc_car

## Servo control test

### Build and run

build the package using catkin_make, then
`$ roslaunch servo_control.launch`

### Test

Run servo_controller node, then send Flat32 message from terminal:

```
$ rostopic pub -1 /servo std_msgs/Float32 -- -1.0  # about 0 degree
$ rostopic pub -1 /servo std_msgs/Float32 --    0  # about 90 degree
$ rostopic pub -1 /servo std_msgs/Float32 --  1.0  # about 180 degree
```

### Control servo from keyboard

1. start servo_control as described below
2. `$ rosrun ros_rc_car kb_input`

then type l, r, n

