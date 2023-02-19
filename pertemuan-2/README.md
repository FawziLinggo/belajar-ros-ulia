# Command 

1. Pembuatan ros package
   ```bash
    $ cd ~/catkin_ws/src
    $ catkin_create_pkg jetbot_ulia rospy std_msgs roscpp
    $ cd ~/catkin_ws
    $ catkin_make
    ```
2. Menjalankan rosrun turtlesim buka di terminal baru
   ```bash
    $ rosrun turtlesim turtlesim_node
    ```
3. Melihat list topic
   ```bash
    $ rostopic list
    ```
4. Melihat info topic
   ```bash
    $ rostopic info /turtle1/cmd_vel
    ```
5. Melihat list node
   ```bash
    $ rosnode list
    ```
6. Melihat info node
   ```bash
    $ rosnode info /turtlesim
    ```
7. Menjalankan rosrun turtlesim teleop buka diterminal baru
   ```bash
    $ rosrun turtlesim turtle_teleop_key
    ```

8. Menjalankan ros graph
   ```bash
    $ rosrun rqt_graph rqt_graph
    ```