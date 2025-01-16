# 技能分类

## 状态类

Published Topics

| Topic | 用途 | 消息定义 |
| --- | --- | --- |
| /alphadog_node/robot_ready | 获取机器狗是否已经入就绪状态及时间戳 | [ros_alphadog/RobotReady](#rosalphadogrobotready) |
| /alphadog_node/boot_up_state | 获取启动状态 | [ros_alphadog/BootUpState](#rosalphadogbootupstate) |
| /alphadog_node/battery_state | 获取电池状态 | [sensor_msgs/BatteryState](http://docs.ros.org/en/api/sensor_msgs/html/msg/BatteryState.html) |
| /alphadog_node/body_status | 获取机器狗身体状态 | [ros_alphadog/BodyStatusStamped](#rosalphadogbodystatusstamped) |
| /alphadog_node/robot_ctrl_status | 获取关于机器狗运动控制的所有状态信息 | [ros_alphadog/RobotCtrlStatusStamped](#rosalphadogrobotctrlstatusstamped) |
| /alphadog_node/dog_ctrl_state | 获取机器狗当前的控制状态 | [ros_alphadog/DogCtrlStateStamped](#rosalphadogdogctrlstatestamped) |
| /alphadog_node/joint_states | 获取所有关节的状态信息 | [sensor_msgs/JointState.msg](http://docs.ros.org/en/noetic/api/sensor_msgs/html/msg/JointState.html) |

(rosalphadogrobotready)=

## ros_alphadog/RobotReady

| 字段 | 类型 | 单位 | 描述 |
| --- | --- | --- | --- |
| ready | bool | - | 机器狗是否已经就绪 |
| stamp | time | - | 机器狗进入就绪状态的 ROS 时间戳 |

(rosalphadogbootupstate)=

## ros_alphadog/BootUpState

| 字段 | 类型 | 单位 | 描述 |
| --- | --- | --- | --- |
| start | bool | N/A | 是否已开始启动 |
| finish | bool | N/A | 是否已完成启动 |
| progress | float32 | N/A | 当前启动进度。范围 0.0～1.0 |
| start_time | time | N/A | 开始启动时的系统时间 |
| finish_time | time | N/A | 完成启动时的系统时间 |

(rosalphadogbodystatusstamped)=

## ros_alphadog/BodyStatusStamped

| 字段 | 类型 | 单位 | 描述 |
| --- | --- | --- | --- |
| header | std_msgs/Header | N/A | 头部信息 |
| status | [ros_alphadog/BodyStatus](#rosalphadogbodystatus) | N/A | 机器狗身体状态 |

(rosalphadogbodystatus)=

## ros_alphadog/BodyStatus

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

(rosalphadogfootstatus)=

## ros_alphadog/FootStatus

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

(rosalphadogjointstatus)=

## ros_alphadog/JointStatus

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

(rosalphadoglegstatus)=

## ros_alphadog/LegStatus

| 字段 | 类型 | 单位 | 描述 |
| --- | --- | --- | --- |
| foot | [ros_alphadog/FootStatus](#rosalphadogfootstatus) | N/A | 这条腿末端的脚的状态信息 |
| joints | [ros_alphadog/JointStatus](#rosalphadogjointstatus)[] | N/A | 这条腿每个关节的状态信息，关节的顺序是 【髋关节，大腿关节，小腿关节】 |

(rosalphadogrobotstatus)=

## ros_alphadog/RobotStatus

| 字段 | 类型 | 单位 | 描述 |
| --- | --- | --- | --- |
| body | [ros_alphadog/BodyStatus](#rosalphadogbodystatus) | N/A | 机器狗身体的状态信息 |
| legs | [ros_alphadog/LegStatus](#rosalphadoglegstatus)[] | N/A | 机器狗各条腿的状态信息 |
| estop | int32 | N/A | 紧急停止状态，参考 [EStop 状态](https://github.com/AlphaDogDeveloper/agentos_sdk/wikis/运动控制参数#estop-状态) |
| current | float32 | A | 输入电流的估计值 |

(rosalphadogrobotctrlstatusstamped)=

## ros_alphadog/RobotCtrlStatusStamped

| 字段 | 类型 | 单位 | 描述 |
| --- | --- | --- | --- |
| header | std_msgs/Header | N/A | 头部信息 |
| status | [ros_alphadog/RobotCtrlStatus](#rosalphadogrobotctrlstatus) | N/A | 关于机器狗运动控制的所有状态信息 |

(rosalphadogrobotctrlstatus)=

## ros_alphadog/RobotCtrlStatus

| 字段 | 类型 | 单位 | 描述 |
| --- | --- | --- | --- |
| current_status | [ros_alphadog/RobotStatus](#rosalphadogrobotstatus) | N/A | 机器狗当前状态 |
| desired_status | [ros_alphadog/RobotStatus](#rosalphadogrobotstatus) | N/A | 期望的机器狗的目标状态 |
| error | uint64 | N/A | 由[错误码](https://github.com/AlphaDogDeveloper/agentos_sdk/wikis/运动控制参数#错误码)构成的掩码 |
| warning | uint64 | N/A | 由[警告码](https://github.com/AlphaDogDeveloper/agentos_sdk/wikis/运动控制参数#警告码)构成的掩码 |

(rosalphadogdogctrlstatestamped)=

## ros_alphadog/DogCtrlStateStamped

| 字段 | 类型 | 单位 | 描述 |
| --- | --- | --- | --- |
| header | std_msgs/Header | N/A | 头部信息 |
| state | [ros_alphadog/DogCtrlState](#rosalphadogdogctrlstate) | N/A | 机器狗当前的控制状态 |

(rosalphadogdogctrlstate)=

## ros_alphadog/DogCtrlState

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

[返回顶部](#技能分类)
