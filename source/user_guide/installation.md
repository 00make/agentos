# 安装指南

## 编译安装

### 1. 电脑(上位机)操作系统要求

- Ubuntu 20.04
- [ROS Noetic](http://wiki.ros.org/noetic/Installation/Ubuntu)

### 2. 下载编译

```powershell
source /opt/ros/noetic/setup.bash
mkdir -p ~/agent_ws/src
cd ~/agent_ws
git clone https://github.com/AlphaDogDeveloper/agentos_sdk.git src/
catkin build
source devel/setup.bash 
```

## 开始使用

### 1. 连接机器狗WiFi

打开“蔚蓝机器狗APP”，在”宠物“页面的右上角选单中选择“通用”，然后点击“Wi-Fi与安全”，得到机器狗的WiFi名称和密码，电脑(上位机)连接此WiFi。

### 2. 配置ROS环境变量

```powershell
ifconfig
# 查看无线IP地址，例如：10.10.10.132

export ROS_MASTER_URI=http://10.10.10.10:11311
export ROS_HOSTNAME=<无线IP>
# 将<无线IP>替换为实际IP地址，例如：export ROS_HOSTNAME=10.10.10.132
```

### 3. 测试

- 获取机器狗当前的运动控制状态

```powershell
rostopic echo /alphadog_node/dog_ctrl_state
```

- 调用`do_action`技能使机器狗站立

```powershell
rosrun actionlib_tools axclient.py /agent_skill/do_action/execute agent_msgs/ExecuteAction
```

Goal内容如下:

```text
> invoker: 'test_skill' invoke_priority: 15 hold_time: 3.0  args: '{"action_id": 4}'
```

以上接口调用成功，则说明电脑(上位机)可以与机器狗进行消息的互通，可以进行下一步的开发工作。
