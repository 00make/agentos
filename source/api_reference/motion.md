
# 运动控制类

示例，机器狗以 0.1m/s 的速度和 0.2rad/s 的角速度行走:

```json
{"vx": 0.1, "wz": 0.2}
```

## 运动控制参数

可通过调用 set_motion_params 来设置以下参数。

| 字段 | 类型 | 单位 | 描述 |
| --- | --- | --- | --- |
| vx | float32 | m/s | 前后移动速度。向前为正。 |
| vy | float32 | m/s | 左右移动速度。向左为正。 |
| wz | float32 | rad/s | 旋转速度。绕竖直向上的轴（z轴）顺时针旋转为正。 |
| roll | float32 | rad | 身体的横滚角度。 |
| pitch | float32 | rad | 身体的俯仰角度。 |
| yaw | float32 | rad | 身体的偏航角度。 |
| body_tilt_x | float32 | m | 机器狗身体的前后偏移距离。向前为正。 |
| body_tilt_y | float32 | m | 机器狗身体的左右偏移距离。向左为正。 |
| body_height | float32 | m | 机器狗的身体高度。以四个脚落地时的平均高度为参考基准。 |
| foot_height | float32 | m | 摆腿时的抬脚高度。 |
| swing_duration | float32 | s | 腿的摆动周期，结合步态类型决定了步频。 |
| friction | float32 | N/A | 机器狗足底和地面之间的摩擦系数。 |
| scale_x | float32 | N/A | 支撑面 x 方向（机器狗身体前后方向）的大小缩放比例。默认不缩放，为 1。 |
| scale_y | float32 | N/A | 支撑面 y 方向（机器狗身体左右方向）的大小缩放比例。默认不缩放，为 1。 |
| free_leg | int32 | N/A | 在录制自定义动作时的自由腿的序号。 |
| swaying_duration | float32 | s | 机器狗在做左右摇摆动作时的摇摆周期。 |
| jump_distance | float32 | m | 向前跳跃距离。 |
| jump_angle | float32 | rad | 跳跃旋转的角度。 |
| velocity_decay | float32 | N/A | 设置指令速度的衰减比例。同时作用于所有遥控器。 |
| collision_protect | int32 | N/A | 碰撞保护功能是否开启（开启：1，关闭：0）。 |
| decelerate_time | float32 | s | 3.0 | 0.0 | 86400.0 | 设置收到最后一个来自 ROS 的速度指令后多长时间后开始减速。单位是秒。 |
| decelerate_duration | float32 | s | 3.0 | 0.0 | 86400.0 | 设置长时间收不到 ROS 速度指令后在多长时间内将速度指令逐渐降低至零。单位是秒。 |

## 用户模式

| user_mode | int32 | N/A |

| ID | 名称 | 描述 |
| --- | --- | --- |
| 1 | EXTREME | 极限模式。手动操控，极限性能。 |
| 2 | KIDS | 儿童模式。视觉辅助移动，安全、缓慢。 |
| 3 | NORMAL | 普通模式。视觉辅助自动切换步态。 |
| 4 | DANCE | 舞蹈模式。表演舞蹈动作。 |
| 5 | QUIET | 比较安静的模式。视觉辅助移动，比较缓慢。 |
| 6 | MUTE | 静音模式。静态步态移动。非常缓慢。 |
| 7 | LONG_ENDURANCE | 长续航模式。仅支持在平坦路面上使用。 |

## 运动步态

[极限模式](#用户模式)下行走时的步态。同时作用于所有遥控器。

| gait | int32 | N/A |

| ID | 名称 | 描述 |
| --- | --- | --- |
| 0 | TROTTING | 对角步态。稳定性较好，速度适中。 |
| 1 | TROTRUNNING | 对角奔跑步态。速度最快。 |
| 2 | TROTWALKING | 缓慢的对角行走步态。速度较慢。 |
| 3 | FREETROTTING | 自由对角步态。会自动根据速度调节步态，包括平衡站立。稳定性和速度兼具。 |
| 4 | STANDING | 平衡站立。站立在原地并保持平衡。 |
| 5 | BOUNDING | 跳跑步态。前后两对脚交替摆动，身体会自然前后俯仰。 |
| 6 | PACING | 踱步步态。左右两对脚交替摆动，身体会自然左右侧倾。 |
| 7 | PRONKING | 跳跃步态。四条腿一齐摆动、一齐落地。身体会上下跳跃。 |
| 8 | WALKING | 行走步态。按照常规四足动物行走时的摆腿顺序。 |
| 9 | GALLOPING | 疾驰步态。类似于马奔跑时的摆腿顺序。 |
| 10 | BRISKTROTWALKING | 比 TROTWALKING 稍快的对角步态。 |
| 11 | STATICWALKING | 准静态缓慢行走。 |
| 12 | BRISKWALKING | 准静态竞走。 |
| 13 | FASTWALKING | 准静态快速行走。 |
| 14 | FREEWALKING | 自由准静态行走步态。会根据速度指令自动调节步态。 |
| 15 | FREESTATIC | 自由静态步态。移动中保持静态稳定。会根据速度调节摆腿周期。 |

## 摆腿轨迹类型

| swing_traj_type | int32 | N/A |

| ID | 名称 | 描述 |
| --- | --- | --- |
| 0 | Efficient | 高效率的摆腿轨迹类型，更省电。 |
| 1 | General | 通用的摆腿轨迹类型，适合大多数场景。 |
| 2 | Avoid obstacle | 更适合跨越障碍物和上楼梯的摆腿轨迹类型。 |
| 3 | Elegant | 一种看起来比较优雅的摆腿轨迹。 |
| 4 | Compliant | 一种避免髋关节转动的摆腿轨迹。 |

## 地面模型

| ground_model | int32 | N/A |

| ID | 名称 | 描述 |
| --- | --- | --- |
| 0 | HORIZEN | 保持身体水平，即 Roll 和 Picth 角度都为 0. |
| 1 | OBSTACLE | 身体姿态自适应地形坡度。 |
| 2 | STAIRS | 适合于上下楼梯。 |
| 3 | SLOPE | 斜坡地形。 |
| 4 | COMMON | 通用地形。 |

# DEV测试类

## 运动模式测试

```bash
source /opt/ros/noetic/setup.bash
# Set motion mode to LIE_DOWN
rostopic pub --once /robot_control/set_mode std_msgs/Int32MultiArray "data: [1]"
```

| mode name | mode ID |
| --- | --- |
| PASSIVE | 0 |
| LIE_DOWN | 1 |
| STAND_UP | 2 |
| RL_MODEL | 3 |
| SOFT_STOP | 4 |

## 运动速度测试

```bash
source /opt/ros/noetic/setup.bash
# Set vx=0.1, vy=0.0, wz=0.3
rostopic pub --once /robot_control/set_velocity std_msgs/Float32MultiArray "data: [0.1, 0.0, 0.3]"
```

