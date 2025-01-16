# 技能调用

```{toctree}
:caption: skill
:maxdepth: 1
:titlesonly:

interaction
skill
```

- **Basic Skill**: 原始技能。是对传感器和执行器等底层硬件能力的简单封装。只能被调用，不会调用其他技能。

- **Cognitive Skill**: 认知技能。对传感器数据等各种感知到信息进行高抽象级的分析，将分析结果存入 WorldModel。不能被调用，也不会调用其他技能。

- **Application Skill**: 组合技能。通过调用 Basic Skill 和其他 Application Skill 以及使用 WorldModel 实现的复杂技能。可以被其他技能调用，也可以调用 Basic Skill 和其他 Application Skill。

- **Role Skill**: 交互技能。通过调用 Application Skill 和 Basic Skill 以及使用 WorldModel 实现的复杂技能。不可以被调用。

## 原始技能

- [alphadog](#alphadog): 机器狗基础数据信息，包括电量、里程计、运动控制状态等信息。
- [do_action](#do_action): 执行原生动作，例如站立、趴下、(准备)移动、跳舞等动作。
- [set_motion_params](#set_motion_params): 设置运动参数，例如移动速度、抬腿高度、移动时的步态等。
- [set_volume](#set_volume): 设置扬声器音量。
- [set_fan](#set_fan): 设置机器狗内部风扇的启停、强度，主要用于给电池降温。
- [set_screen](#set_screen): 设置屏幕亮度。
- [camera](#camera): 发布相机画面。
- [tof](#tof): 发布TOF传感器数据。
- [lidar](#lidar): 发布激光雷达数据。

## 认知技能

- [touch_detect](#touch_detect): 发布触摸事件。
- [slam](#slam): 定位及建图，发布定位及障碍物地图数据。
- [vision](#vision): 提供不同的视觉能力，提供对于环境的理解。
- [voice](#voice): 语音识别技能，支持中英文识别。

## 组合技能

- [self_charging](#self_charging): 自动充电。
- [do_nav](#do_nav): 导航技能，结合slam的定位和建图信息进行导航。
- [do_dog_behavior](#do_dog_behavior): 一系列综合了动作、表情、声音的仿生行为。
- [set_walking_style](#set_walking_style): 设置走路的风格。

## 交互技能

- [simple_interact](#交互技能): 条件反射式的简单交互能力。包括触摸反应、眨眼、充电提示等。
- [immune_system](#交互技能): 免疫系统。包括: 自主降温（风扇控制）、环境温湿度反应、电量过低自动关机等。
- [voice_interaction](#交互技能): 语音交互。包括聊天、动作指令、音乐播放等。
- [visual_interaction](#交互技能): 视觉行为交互。看到主人或陌生人的反应。
- [auto_routine](#交互技能): 日常自主行为。

## 技能详解

### alphadog

Published Topics

| Topic | 用途 | 消息定义 |
| --- | --- | --- |
| /alphadog_node/robot_ready | 获取机器狗是否已经入就绪状态及时间戳 | [ros_alphadog/RobotReady](#ros_alphadogrobotready) |
| /alphadog_node/boot_up_state | 获取启动状态 | [ros_alphadog/BootUpState](#ros_alphadogbootupstate) |
| /alphadog_node/battery_state | 获取电池状态 | [sensor_msgs/BatteryState](http://docs.ros.org/en/api/sensor_msgs/html/msg/BatteryState.html) |
| /alphadog_node/body_status | 获取机器狗身体状态 | [ros_alphadog/BodyStatusStamped](#ros_alphadogbodystatusstamped) |
| /alphadog_node/robot_ctrl_status | 获取关于机器狗运动控制的所有状态信息 | [ros_alphadog/RobotCtrlStatusStamped](#ros_alphadogrobotctrlstatusstamped) |
| /alphadog_node/dog_ctrl_state | 获取机器狗当前的控制状态 | [ros_alphadog/DogCtrlStateStamped](#ros_alphadogdogctrlstatestamped) |
| /alphadog_node/joint_states | 获取所有关节的状态信息 | [sensor_msgs/JointState.msg](http://docs.ros.org/en/noetic/api/sensor_msgs/html/msg/JointState.html) |

### ros_alphadog/RobotReady

| 字段 | 类型 | 单位 | 描述 |
| --- | --- | --- | --- |
| ready | bool | - | 机器狗是否已经就绪 |
| stamp | time | - | 机器狗进入就绪状态的 ROS 时间戳 |

### ros_alphadog/BootUpState

| 字段 | 类型 | 单位 | 描述 |
| --- | --- | --- | --- |
| start | bool | N/A | 是否已开始启动 |
| finish | bool | N/A | 是否已完成启动 |
| progress | float32 | N/A | 当前启动进度。范围 0.0～1.0 |
| start_time | time | N/A | 开始启动时的系统时间 |
| finish_time | time | N/A | 完成启动时的系统时间 |

### ros_alphadog/BodyStatusStamped

| 字段 | 类型 | 单位 | 描述 |
| --- | --- | --- | --- |
| header | std_msgs/Header | N/A | 头部信息 |
| status | [ros_alphadog/BodyStatus](#ros_alphadogbodystatus) | N/A | 机器狗身体状态 |

### ros_alphadog/BodyStatus

| 字段 | 类型 | 单位 | 描述 |
| --- | --- | --- | --- |
| x | float32 | m | 机器狗身体中心位置相对于初始位置的 x 坐标 |
| y | float32 | m | 机器狗身体中心位置相对于初始位置的 y 坐标 |
| z | float32 | m | 机器狗身体中心离地面（脚的中心的平均高度）的高度 |
| roll | float32 | rad | 机器狗身体的横滚角度 |
| pitch | float32 | rad | 机器狗身体的俯仰角度 |
| yaw | float32 | rad | 机器狗身体相对于初始朝向的转身角度 |
| vx | float32 | m/s | 前进速度 |
| vy | float32 | m/s | 横向移动速度（左为正方向） |
| vz | float32 | m/s | 垂直方向速度（上为正方向） |
| wx | float32 | rad/s | 机器狗身体的横滚角速度 |
| wy | float32 | rad/s | 机器狗身体的俯仰角速度 |
| wz | float32 | rad/s | 机器狗身体的转身角速度 |
| ax | float32 | m/(s^2) | 前进加速度 |
| ay | float32 | m/(s^2) | 横向加速度 |
| az | float32 | m/(s^2) | 垂直加速度 |

### ros_alphadog/FootStatus

| 字段 | 类型 | 单位 | 描述 |
| --- | --- | --- | --- |
| x | float32 | m | 脚相对于初始机器狗位置的 x 坐标 |
| y | float32 | m | 脚相对于初始机器狗位置的 y 坐标 |
| z | float32 | m | 机器狗身体中心离地面（脚的中心的平均高度）的高度 |
| vx | float32 | m/s | 脚在 x 方向的速度 |
| vy | float32 | m/s | 脚在 y 方向的速度 |
| vz | float32 | m/s | 脚在竖直方向的速度 |
| contact | float32 | N/A | 脚与地面或其他物体接触的概率。数值范围是 [0.0, 1.0] |
| ext_force_x | float32 | N | 脚在 x 方向所受到的外部作用力的估计值 |
| ext_force_y | float32 | N | 脚在 y 方向所受到的外部作用力的估计值 |
| ext_force_z | float32 | N | 脚在竖直方向所受到的外部作用力的估计值 |

### ros_alphadog/JointStatus

| 字段 | 类型 | 单位 | 描述 |
| --- | --- | --- | --- |
| q | float32 | rad | 关节角度位置 |
| qd | float32 | rad/s | 关节角速度 |
| tau | float32 | N·m | 关节扭矩 |
| kp | float32 | N·m/rad | 关节位置增益 |
| kd | float32 | N·m/(rad/s) | 关节速度增益 |
| alarm | int32 | N/A | 关节报警，0 表示正常 |
| temperature | int32 | centigrade | 关节温度 |
| status | int8 | N/A | 关节状态码，0 表示掉线，1 表示正常 |

### ros_alphadog/LegStatus

| 字段 | 类型 | 单位 | 描述 |
| --- | --- | --- | --- |
| foot | [ros_alphadog/FootStatus](#ros_alphadogfootstatus) | N/A | 这条腿末端的脚的状态信息 |
| joints | [ros_alphadog/JointStatus](#ros_alphadogjointstatus)[] | N/A | 这条腿每个关节的状态信息，关节的顺序是 【髋关节，大腿关节，小腿关节】 |

### ros_alphadog/RobotStatus

| 字段 | 类型 | 单位 | 描述 |
| --- | --- | --- | --- |
| body | [ros_alphadog/BodyStatus](#ros_alphadogbodystatus) | N/A | 机器狗身体的状态信息 |
| legs | [ros_alphadog/LegStatus](#ros_alphadoglegstatus)[] | N/A | 机器狗各条腿的状态信息 |
| estop | int32 | N/A | 紧急停止状态，参考 [EStop 状态](https://github.com/AlphaDogDeveloper/agentos_sdk/wikis/运动控制参数#estop-状态) |
| current | float32 | A | 输入电流的估计值 |

### ros_alphadog/RobotCtrlStatusStamped

| 字段 | 类型 | 单位 | 描述 |
| --- | --- | --- | --- |
| header | std_msgs/Header | N/A | 头部信息 |
| status | [ros_alphadog/RobotCtrlStatus](#ros_alphadogrobotctrlstatus) | N/A | 关于机器狗运动控制的所有状态信息 |

### ros_alphadog/RobotCtrlStatus

| 字段 | 类型 | 单位 | 描述 |
| --- | --- | --- | --- |
| current_status | [ros_alphadog/RobotStatus](#ros_alphadogrobotstatus) | N/A | 机器狗当前状态 |
| desired_status | [ros_alphadog/RobotStatus](#ros_alphadogrobotstatus) | N/A | 期望的机器狗的目标状态 |
| error | uint64 | N/A | 由[错误码](https://github.com/AlphaDogDeveloper/agentos_sdk/wikis/运动控制参数#错误码)构成的掩码 |
| warning | uint64 | N/A | 由[警告码](https://github.com/AlphaDogDeveloper/agentos_sdk/wikis/运动控制参数#警告码)构成的掩码 |

### ros_alphadog/DogCtrlStateStamped

| 字段 | 类型 | 单位 | 描述 |
| --- | --- | --- | --- |
| header | std_msgs/Header | N/A | 头部信息 |
| state | [ros_alphadog/DogCtrlState](#ros_alphadogdogctrlstate) | N/A | 机器狗当前的控制状态 |

### ros_alphadog/DogCtrlState

| 字段 | 类型 | 单位 | 描述 |
| --- | --- | --- | --- |
| error | uint64 | N/A | 由[错误码](https://github.com/AlphaDogDeveloper/agentos_sdk/wikis/运动控制参数#错误码)构成的掩码 |
| warning | uint64 | N/A | 由[警告码](https://github.com/AlphaDogDeveloper/agentos_sdk/wikis/运动控制参数#警告码)构成的掩码 |
| estop | int32 | N/A | 由[EStop 状态](https://github.com/AlphaDogDeveloper/agentos_sdk/wikis/运动控制参数#estop-状态)构成的掩码 |
| user_mode | int32 | N/A | [user mode](https://github.com/AlphaDogDeveloper/agentos_sdk/wikis/运动控制参数#用户模式) |
| controller_type | int32 | N/A | [遥控器类型](https://github.com/AlphaDogDeveloper/agentos_sdk/wikis/运动控制参数#遥控器类型) |
| action | int32 | N/A | [Action ID](https://github.com/AlphaDogDeveloper/agentos_sdk/wikis/动作列表) |
| motion_mode | int32 | N/A | [motion mode](https://github.com/AlphaDogDeveloper/agentos_sdk/wikis/运动控制参数#运动控制模式) |
| velocity_controller | int32 | N/A | The type of controller used for controlling speed |
| gait | int32 | N/A | [Gait](https://github.com/AlphaDogDeveloper/agentos_sdk/wikis/运动控制参数#运动步态) |
| standing | bool | N/A | Whether the robot dog is currently in a four-legged standing state |

[&uarr;返回](#原始技能)

### camera

Published Topics

| Topic | 用途 | 消息定义 |
| --- | --- | --- |
| /alpha_livestream/grabber/image | 相机画面 | [sensor_msgs/CompressedImage](http://docs.ros.org/en/noetic/api/sensor_msgs/html/msg/CompressedImage.html) |
| /alpha_camera/uvc_camera/camera_info | 相机参数 | [sensor_msgs/CameraInfo](http://docs.ros.org/en/noetic/api/sensor_msgs/html/msg/CameraInfo.html) |

[&uarr;返回](#原始技能)

### tof

Published Topics

| Topic | 用途 | 消息定义 |
| --- | --- | --- |
| /tof_sensor/tof_left | 下巴左侧的ToF探测数据，单点 | [sensor_msgs/LaserScan](http://docs.ros.org/en/noetic/api/sensor_msgs/html/msg/LaserScan.html) |
| /tof_sensor/tof_right | 下巴右侧的ToF探测数据，单点 | [sensor_msgs/LaserScan](http://docs.ros.org/en/noetic/api/sensor_msgs/html/msg/LaserScan.html) |
| /tof_sensor/tof_mid | 额头的ToF探测数据，单点 | [sensor_msgs/LaserScan](http://docs.ros.org/en/noetic/api/sensor_msgs/html/msg/LaserScan.html) |

[&uarr;返回](#原始技能)

### lidar

| Topic | 用途 | 消息定义 |
| --- | --- | --- |
| /lidar_node/scan2 | 雷达数据，绝对角度 | [agent_msgs/LaserScan2](http://docs.ros.org/en/noetic/api/sensor_msgs/html/msg/LaserScan.html) |
| /lidar_node/point_cloud | 雷达数据，点云 | [sensor_msgs/PointCloud](http://docs.ros.org/en/noetic/api/sensor_msgs/html/msg/PointCloud.html) |

[&uarr;返回](#原始技能)

### do_action

execute args

| 字段 | 类型 | 示例 | 说明 |
| -------------- | -------------- | -------------- |-------------- |
| action_id | int | 1 | 动作 ID。详见 [动作列表](https://github.com/AlphaDogDeveloper/agentos_sdk/wikis/动作列表) |

示例，趴下:

```json
{"action_id": 2}
```

站立:

```json
{"action_id": 4}
```

[&uarr;返回](#原始技能)

### set_motion_params

可设置的参数参考: [运动控制参数](https://github.com/AlphaDogDeveloper/agentos_sdk/wikis/运动控制参数)

示例，机器狗以 0.1m/s 的速度和 0.2rad/s 的角速度行走:

```json
{"vx": 0.1, "wz": 0.2}
```

[&uarr;返回](#原始技能)

### set_volume

execute args

| 字段 | 类型 | 示例 | 说明 |
| -------------- | -------------- | -------------- |-------------- |
| volume | float | 0.3 | 音量的数值范围是 [0.0, 1.0]，设置 0.0 时为静音，设置 1.0 时音量最大 |

示例，将音量设为0.9:

```json
{"volume": 0.9}
```

[&uarr;返回](#原始技能)

### set_fan

execute args

| 字段 | 类型 | 示例 | 说明 |
| -------------- | -------------- | -------------- |-------------- |
| enable | int | 1 | 0: 关闭，1: 打开 |
| duty_cycle | float | 0.5 | 转速，取值范围 [0.0, 1.0] |

示例，打开风扇，转速 50%:

```json
{"enable": 1, "duty_cycle": 0.5}
```

调整转速到 100%:

```json
{"duty_cycle": 1.0}
```

关闭风扇:

```json
{"enable": 0}
```

[&uarr;返回](#原始技能)

### set_screen

execute args

| 字段 | 类型 | 示例 | 说明 |
| -------------- | -------------- | -------------- |-------------- |
| backlight | int | 1 | 是否开启背光，0: 关闭，1: 打开 |
| brightness | float | 0.3 | 亮度 |

示例，打开背光，亮度设为0.8:

```json
{"backlight": 1, "brightness": 0.8}
```

[&uarr;返回](#原始技能)

### touch_detect

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

### slam

Published Topics

| Topic | 用途 | 消息定义 |
| --- | --- | --- |
| /alphago_slam/cost_map | 全局地图 | [nav_msgs/OccupancyGrid](https://docs.ros.org/en/noetic/api/nav_msgs/html/msg/OccupancyGrid.html) |
| /alphago_slam/slam_odom | 全局定位 | [nav_msgs/Odometry](http://docs.ros.org/en/noetic/api/nav_msgs/html/msg/Odometry.html) |

[&uarr;返回](#原始技能)

### vision

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

[&uarr;返回](#原始技能)

### voice

execute args

| 字段 | 类型 | 示例 | 说明 |
| -------------- | -------------- | -------------- |-------------- |
| type | string | tts | tts 或 stt |
| text | string | 你好 | 若是文字转语音，需要此参数 |

示例，TTS:

```json
{
  "type":"tts",
  "text":"你好，我是小白，让我们一起来玩吧!"
}
```

ASR:

```json
{
  "type":"stt"
}
```

[&uarr;返回](#原始技能)

### self_charging

自主充电技能，空参数即可，需要在机器狗面对充电桩时调用。

[&uarr;返回](#原始技能)

### do_nav

使用slam定位和地图进行导航。

execute args

| 字段 | 类型 | 示例 | 说明 |
| -------------- | -------------- | -------------- |-------------- |
| goal | geometry_msgs/PoseStamped | - | 全局目标点 |
| xy_goal_tolerance | float | - | 位置容差，默认 0.5 m |
| yaw_goal_tolerance | float | - | 角度容差，默认 1 radian |
| max_vel | json | - | 速度限制，若不指定，则默认限速为 {"max_vx": 0.35, "max_vy": 0.12, "max_wz": 1.5} |

示例，导航到地图的(1.0, 0.0)位置:

```json
{
  "goal": {
    "header": {
      "seq": 0,
      "stamp": {
        "secs": 1548893288,
        "nsecs": 792883108
      },
      "frame_id": "map"
    },
    "pose": {
      "position": {
        "x": 1.0,
        "y": 0.0,
        "z": 0.0
      },
      "orientation": {
        "x": 0.0,
        "y": 0.0,
        "z": 0.0,
        "w": 1.0
      }
    }
  },
  "xy_goal_tolerance": 0.1,
  "yaw_goal_tolerance": 0.5,
  "max_vel": {
    "max_vx": 0.35,
    "max_vy": 0.12,
    "max_wz": 3.15,
  }
}
```

[&uarr;返回](#原始技能)

### do_dog_behavior

让机器狗执行一个即有行为。

execute args

| 字段 | 类型 | 示例 | 说明 |
| -------------- | -------------- | -------------- |-------------- |
| behavior | string | shake_self | 行为的名称，参见 [行为列表](https://github.com/AlphaDogDeveloper/agentos_sdk/wikis/行为列表) |

示例，让狗抖一抖：

```json
{"behavior": "shake_self"}
```

[&uarr;返回](#原始技能)

### set_walking_style

execute args

| 字段 | 类型 | 说明 |
| --- | --- | --- |
| emotion | string | 走路风格类型 |
| intensity | float | 风格强度。取值范围 [0.0, 1.0]，默认 1.0 |

风格列表:

| 名称 | 描述 | 名称 | 描述 |
| --- | --- | --- | --- |
| Base | 基础风格 | Bored | 无聊 |
| Curious | 好奇 | Excitement | 兴奋 |
| Distress | 悲伤 | Contentment | 满足 |
| Fear | 害怕 | Anger | 愤怒 |
| Joy | 快乐 | Shyness | 羞怯 |
| Affection | 喜爱 | Escape | (用于)脱困 |
| Outdoor | 户外 | - | - |

[&uarr;返回](#原始技能)
