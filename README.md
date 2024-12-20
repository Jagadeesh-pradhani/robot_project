# robot_project

# Create a workspace
```
mkdir -p ~/robot_ws/src/
cd robot_ws/src/
```

Clone and build the repository <br>

```
cd ~/robot_ws/src/
git clone https://github.com/Jagadeesh-pradhani/robot_project.git
cd ~/robot_ws/
catkin_make
source ~/robot_ws/devel/setup.bash
```

Run the simulation <br>
- Terminal-1
  ```
  cd ~/robot_ws/
  source ~/robot_ws/devel/setup.bash
  roslaunch robot_project robot_gazebo.launch
  ```
- Terminal-2 <br>
  Starts controller, rviz and rqt <br>
  In the rqt click oon 2 topics to set the arm, to a position.
  ```
  cd ~/robot_ws/
  source ~/robot_ws/devel/setup.bash
  roslaunch robot_project robot_control.launch
  ```
  ![image](https://github.com/user-attachments/assets/4a8b53f6-3e1c-4bc9-aa12-0345ad1d1566)
- Terminal-3
  ```
  cd ~/robot_ws/
  source ~/robot_ws/devel/setup.bash
  python3 src/robot_project/src/move.py
  ```
