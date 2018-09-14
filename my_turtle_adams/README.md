# PROJECT/ASSIGNMENT 01

#### Author: Caleb Adams


## File Structure
The file structure is standard for packages and conforms to what was required by the assignment.

the `.world`, `.inc`, `.png`, and `.yaml` files are included in the root of the package folder `my_turtle_adams` for simplicity.

The python scripts `Move_Turtle.py` and `List_Turtle.py` are located in the `my_turtle_adams/scripts/` folder.

## ROS Version and Setup on MacOS
Parallels Desktop was used to run the VM and runs Ubuntu 16.04 with ROS Kinetic. This means that the `cmd_vel` (used in indigo for the turtlebot) topic does not exist; it is replaced with the `cmd_vel_mux/input/navi` topic. These have the same functionality.

## Compilation & Running

Setting up this package has no special compilation steps, simply follow the standard ROS package steps.

For my own convince I used a one line script `runme` in the root of the package directory. The contents of this script are:

```bash
$ roslaunch turtlebot_stage turtlebot_in_stage.launch map_file:="/home/parallels/catkin_ws/src/my_turtle_adams/tutorial.yaml" world_file:="/home/parallels/catkin_ws/src/my_turtle_adams/tutorial.world"
```

To run this on another system, the paths to the `tutorial.yaml` and `tutorial.world` system must be changed appropriately.

Additionally, the `turtlebot_stage` system must be installed.

The `Listen_Turtle.py` file also logs the inverse kinematics (it outputs the wheel rotations), this was for debugging purposes.

### Running Move_Turtle

To run this:

```bash
rosrun my_turtle_adams Move_Turtle.py
```

### Running Listen_Turtle

To run this:

```bash
rosrun my_turtle_adams Listen_Turtle.py
```

## Observations

* The robot moves until it hits a wall
* The inverse kinematics were derived directly from those in class: https://uga.view.usg.edu/d2l/le/content/1627420/viewContent/24268161/View
  * At a velocity of 0.2 the wheel rotation was 0.04 for the given parameters, this can be seen when running the code
* The kinect sensor only "sees" a limited cross-section of the 3D environment in the direction it is looking
