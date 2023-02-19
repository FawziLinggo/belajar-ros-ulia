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
9. Melihat message yang dikirimkan
    ```bash
    $ rostopic echo /turtle1/cmd_vel
    ```
10. cek tipe topic
    ```bash
    $ rostopic type /turtle1/cmd_vel
    ```
11. Meliat tipe message
    ```bash
    $ rosmsg show geometry_msgs/Twist
    ```
12. Publish message
    ```bash
    $ rostopic pub -1 /turtle1/cmd_vel geometry_msgs/Twist -- '[2.0, 0.0, 0.0]' '[0.0, 0.0, 1.8]'
    ```
