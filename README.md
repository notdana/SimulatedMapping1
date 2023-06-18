# ROS2 Gazebo Simulation with SLAM Toolbox

This repository contains code for a ROS2 Gazebo simulation using the Humble Hawksbill version on Ubuntu 22.04 Jammy Jellyfish. The simulation utilizes Gazebo as the simulator and teleop_twist_keyboard for robot movement.

## Acknowledgment

This project was inspired by and based on the work of the [ https://github.com/joshnewans/articubot_one.git ]

## Prerequisites

- ROS2 Humble Hawksbill
- Ubuntu 22.04 Jammy Jellyfish
- Gazebo
- teleop_twist_keyboard

## Getting the code on your machine
 
1. Create a workspace
```
mkdir map_ws
```

2. Go inside the ws and create a src folder
```
cd map_ws
mkdir src
```

3. Go inside the src folder and clone the repo
```
cd src
git clone https://github.com/DanaWentBananas/SimulatedMapping1.git
```

4. Go back to the ws
```
cd ..
```
OR
```
cd path_to/map_ws
```

5. build it
```
colcon build
```

## Running the Simulation

To run the simulation, follow the steps below:

1. Launch the robot state publisher:
```
ros2 launch dev_pkg rsp.launch.py
```

2. Launch rviz2 for visualization:
```
rviz2
```

3. Running gazebo in an alternative way since the normal way was giving an error when it was spawning the entity
```
gazebo -s libgazebo_ros_init.so -s libgazebo_ros_factory.so ~/dev_ws/src/dev_pkg/worlds/obstacles.world
```

4. Spawn the robot entity:
```
ros2 run gazebo_ros spawn_entity.py -topic robot_description -entity bott
```

5. Launch the SLAM Toolbox to generate a map: (it subscribes to /scan and /tf topics and published to /map)
```
ros2 launch slam_toolbox online_async_launch.py params_file:=~/dev_ws/src/dev_pkg/config/mapper_params_online_async.yaml
```

6. Control the robot using the keyboard:
```
ros2 run teleop_twist_keyboard teleop_twist_keyboard
```


