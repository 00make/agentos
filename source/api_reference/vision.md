# 视觉类

## camera

Published Topics

| Topic | 用途 | 消息定义 |
| --- | --- | --- |
| /alpha_livestream/grabber/image | 相机画面 | [sensor_msgs/CompressedImage](http://docs.ros.org/en/noetic/api/sensor_msgs/html/msg/CompressedImage.html) |
| /alpha_camera/uvc_camera/camera_info | 相机参数 | [sensor_msgs/CameraInfo](http://docs.ros.org/en/noetic/api/sensor_msgs/html/msg/CameraInfo.html) |

## tof

Published Topics

| Topic | 用途 | 消息定义 |
| --- | --- | --- |
| /tof_sensor/tof_left | 下巴左侧的ToF探测数据，单点 | [sensor_msgs/LaserScan](http://docs.ros.org/en/noetic/api/sensor_msgs/html/msg/LaserScan.html) |
| /tof_sensor/tof_right | 下巴右侧的ToF探测数据，单点 | [sensor_msgs/LaserScan](http://docs.ros.org/en/noetic/api/sensor_msgs/html/msg/LaserScan.html) |
| /tof_sensor/tof_mid | 额头的ToF探测数据，单点 | [sensor_msgs/LaserScan](http://docs.ros.org/en/noetic/api/sensor_msgs/html/msg/LaserScan.html) |

## lidar

| Topic | 用途 | 消息定义 |
| --- | --- | --- |
| /lidar_node/scan2 | 雷达数据，绝对角度 | [agent_msgs/LaserScan2](http://docs.ros.org/en/noetic/api/sensor_msgs/html/msg/LaserScan.html) |
| /lidar_node/point_cloud | 雷达数据，点云 | [sensor_msgs/PointCloud](http://docs.ros.org/en/noetic/api/sensor_msgs/html/msg/PointCloud.html) |

## touch_detect

Published Topics

| Topic | 用途 | 消息定义 |
| --- | --- | --- |
| /agent_skill/touch_detect/touch | 触摸事件 | [std_msgs/Int32](http://docs.ros.org/en/noetic/api/std_msgs/html/msg/Int32.html) |

事件定义

|Value| Description|
|---|---|
|1 | 下巴被触摸 |
|2 | 下巴从触摸切换到未触摸 |
|3 | 后脑勺被触摸 |
|4 | 后脑勺从触摸切换到未触摸 |

## slam

Published Topics

| Topic | 用途 | 消息定义 |
| --- | --- | --- |
| /alphago_slam/cost_map | 全局地图 | [nav_msgs/OccupancyGrid](https://docs.ros.org/en/noetic/api/nav_msgs/html/msg/OccupancyGrid.html) |
| /alphago_slam/slam_odom | 全局定位 | [nav_msgs/Odometry](http://docs.ros.org/en/noetic/api/nav_msgs/html/msg/Odometry.html) |

## vision

技能特点

- 人脸
  - 人脸检测
  - 人脸位姿估计(6DoF)
  - 人脸识别
  - 人脸录入(需要满足尺寸、清晰度、角度要求)
- 人体
  - 人体跟踪
  - 人体位置估计(3DoF)
  - 人形ReID
- 事件管理
  - 录入新的人(RegisterNewPerson)
  - 人出现(PersonAppear)
  - 人消失(PersonDisappear)

Published Topics

| Topic | 用途 | 消息定义 |
| --- | --- | --- |
| /agent_skill/vision/persons | 人体识别 | [agent_msgs/PersonStamped](https://github.com/AlphaDogDeveloper/agentos_sdk/tree/master/agent_msgs/msg/PersonInfoStamped.msg) |
| /agent_msgs/event/vision | 视觉事件 | [agent_msgs/Event](https://github.com/AlphaDogDeveloper/agentos_sdk/tree/master/agent_msgs/msg/Event.msg) |

人体消息定义

| 字段 | 类型 |  说明 |
| -------------- | -------------- |-------------- |
| track_id | int64 | 人体跟踪id |
| id | int64 | 人体id，负数为陌生人，正数为熟人 |
| name | string | 暂不可用 |
| id_confidence | float32 | 暂不可用 |
| is_face_visible | bool | 是否识别到人脸 |
| face_box | [agent_msgs/Box](https://github.com/AlphaDogDeveloper/agentos_sdk/tree/master/agent_msgs/msg/Box.msg) | 人脸框 |
| head_pose | [geometry_msgs/Pose](http://docs.ros.org/en/noetic/api/geometry_msgs/html/msg/Pose.html) | 人脸在世界坐标系中的位姿 |
| is_body_visible | bool | 是否识别到人体 |
| body_box | [agent_msgs/Box](https://github.com/AlphaDogDeveloper/agentos_sdk/tree/master/agent_msgs/msg/Box.msg) | 人体框 |
| body_pose | [geometry_msgs/Pose](http://docs.ros.org/en/noetic/api/geometry_msgs/html/msg/Pose.html) | 人体在世界坐标系中的位置 |
| velocity | [geometry_msgs/Vector3](http://docs.ros.org/en/melodic/api/geometry_msgs/html/msg/Vector3.html) | 人体移动速度 |

**Tips**:

- 目标检测到的人最开始都为陌生人。
- 当人脸离摄像头较近，角度合适画面清晰的情况下，会录入人脸，给当前的人分配正的 id。同时会录入人形特征。
- 针对某一个新检测到的人，都会尝试人脸识别和ReID。当人脸识别匹配上，或者人形特征匹配上的时候，该人的id都会置为对应的录入人脸时分配的 id。

视觉事件定义

| 事件名 | 字段 | 说明 |
| -------------- | -------------- |-------------- |
| PersonAppear | person_id: int64<br>latest_appear_time: int64 | 已知人出现 |
| PersonDisappear | person_id: int64<br>showup_time: int64 | 已知人消失 |
| RegisterNewPerson | person_id: int64 | 录入了新的人 |

## self_charging

自主充电技能，空参数即可，需要在机器狗面对充电桩时调用。
