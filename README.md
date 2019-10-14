# ros_rc_car

## Servo control test

### Build and run

build the package using catkin_make, then
`$ roslaunch servo_control.launch`

### Test

* Steering test
Run streering_controller and throttle_controller node, then send Flat32 message from terminal:

```
$ rostopic pub -1 /servo/steering std_msgs/Float32 -- -1.0  # about 0 degree
$ rostopic pub -1 /servo/sterring std_msgs/Float32 --    0  # about 90 degree
$ rostopic pub -1 /servo/sterring std_msgs/Float32 --  1.0  # about 180 degree
```

* Throttle test
```
$ rostopic pub -1 /servo/throttle std_msgs/Float32 -- -1.0  # backward max
$ rostopic pub -1 /servo/throttle std_msgs/Float32 --    0  # stop
$ rostopic pub -1 /servo/throttle std_msgs/Float32 --  1.0  # forward max
```

### Control servo from keyboard

1. start servo_control as described below
2. `$ rosrun ros_rc_car kb_input`

then type l, r, n, f, b, s


