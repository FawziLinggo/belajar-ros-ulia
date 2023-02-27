1. jangan lupa lakukan chmod memberi izin
   ```
    $ chmod +x talker.py
    $ chmod +x listener.py
    ```
    untuk periksa dapat menggunakan command berikut :
    ```
    $ ls -l
    ```
2. pergi ke root workspace directory (catkin_ws)
   ```
    $ cd ~/catkin_ws
    ```
3. jalankan catkin_make
   ```
    $ catkin_make
    ```
4. jalankan source devel/setup.bash
   ```
   source ~/catkin_ws/devel/setup.bash
    ```
5. jalankan rosrun
   ```bash
    $ rosrun nama_package talker.py
    $ rosrun nama_package listener.py
    ```