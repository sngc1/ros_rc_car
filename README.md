# ros_rc_car

## Run

build the packager using catkin_make, then
`$ roslaunch main.launch`

## Test

Run this package, then send Flat32 messages:

```
$ rostopic pub -1 /servo std_msgs/Float32 -- -1.0  # about 0 degree
$ rostopic pub -1 /servo std_msgs/Float32 --    0  # about 90 degree
$ rostopic pub -1 /servo std_msgs/Float32 --  1.0  # about 180 degree
```
