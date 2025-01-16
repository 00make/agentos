# 交互列表

## 基础状态控制

|    ID     |    名称    |    描述    |
| --------- | --------- | ---------- |
|0|BOOT_UP / ESTOP|启动、EStop、待机。所有执行器进入未使能状态|
|1|WAKE_UP|从 EStop 状态唤醒|
|20736|stand|保持站立姿态|
|20737|recovery_pose|恢复标准站姿|
|3|RECOVERY_STAND|从翻倒状态恢复站立|

## 姿态控制

|    ID     |    名称    |    描述    |
| --------- | --------- | ---------- |
|16|STAND_ON_FOUR_LEGS|四腿站立|
|17|STAND_ON_THREE_LEGS|三腿站立|
|18|STAND_ON_TWO_LEGS|两腿站立|
|2|GET_DOWN|趴下|
|5|SIT|坐立|
|6|SOFT_STOP|缓慢趴下|
|20738|half_sit|半趴姿态|
|20739|lie_on_elbows|调整至前肢支撑的半趴姿态|
|20740|stand_high|高姿态站立|

## 日常行为动作

|    ID     |    名称    |    描述    |
| --------- | --------- | ---------- |
|20481|shake_self|抖动身体|
|20482|fast_rotate|快速旋转一圈|
|20483|wag_tail|摇尾巴|
|20484|prostrate|匍匐前进|
|20503|front_rear_strech|完整伸懒腰动作|
|20490|rear_strech|后腿伸展|
|20491|front_strech|前腿伸展|
|20509|shit|排便动作|
|20513|bark|叫声动作|
|20573|long_fart|长时间放屁动作|
|20574|short_fart|短促放屁动作|
|513|PEE|撒尿动作|
|20551|pee_2|改良版撒尿动作|

## 互动表现动作

|    ID     |    名称    |    描述    |
| --------- | --------- | ---------- |
|514|SHAKE_HAND|挥手动作|
|20541|shake_hand_2|握手动作|
|20542|wave_hand|挥手致意|
|20543|clap_hand|击掌互动|
|545|COAX|撒娇动作|
|20530|cute|萌态撒娇|
|20531|stick|亲昵贴近|
|20534|affection|表达喜爱|
|20549|affection_7s|左右摆动身体表达喜爱|
|20486|ask_for_play|邀请玩耍姿态|
|20487|enjoy_being_touched|被抚摸时的愉悦反应|
|20510|bow|鞠躬致意|
|20511|stand_at_ease|稍息站立|
|20571|stand_at_attention|立正站姿|
|20512|confused|表现困惑|
|20539|think|思考状态|
|20554|wait_for_praise|期待表扬姿态|

## 探索动作

|    ID     |    名称    |    描述    |
| --------- | --------- | ---------- |
|20488|sniff_left|向左嗅探|
|20489|sniff_right|向右嗅探|
|20518|sniff_left_slow|缓慢向左嗅探|
|20519|sniff_right_slow|缓慢向右嗅探|
|20532|sniff_ahead|向前方嗅探|
|20533|sniff_ahead_3|连续三次向前嗅探|
|20575|sniff_up|向上方嗅探|
|20499|explore_road_yaw|左右探路动作|
|20500|explore_road_roll|前后探路动作|
|20501|search_env_yaw|左右环视环境|
|20502|search_env_roll|上下查看环境|

## 表演动作

|    ID     |    名称    |    描述    |
| --------- | --------- | ---------- |
|625|DYNAMIC_DANCE|可配置参数的舞蹈动作|
|20529|dance_4x1500|标准舞蹈套路|
|20553|lion_dance|舞狗特色舞蹈|
|20566|dance_with_beats|8拍节奏舞蹈|
|20568|dance_with_beatsx4|4拍节奏舞蹈|
|20567|shoulder_dance|肩部扭动舞蹈|
|20555|lucky_cat_1|坐姿招财动作|
|20556|lucky_cat_2|站姿招财动作|

## 运动控制

|    ID     |    名称    |    描述    |
| --------- | --------- | ---------- |
|4|MOVE|移动准备状态|
|517|MANIPULATE|单腿世界坐标系操纵|
|518|LIFT_LEG|单腿关节坐标系操纵|
|1792|JOINTS_ACTION|关节动作控制|
|20524|step_forward|向前迈步|
|20528|step_back|向后迈步|
|20525|rotate_180|顺时针旋转180度|
|20526|rotate_-180|逆时针旋转180度|

## 头部动作

|    ID     |    名称    |    描述    |
| --------- | --------- | ---------- |
|20505|nod_head|点头|
|20506|shake_head|摇头|
|20507|nod_head_twice|连续点头两次|
|20508|shake_head_twice|连续摇头两次|
|20521|look_around|环视四周方案1|
|20522|look_around_2|环视四周方案2|
|20523|look_around_3|环视四周方案3|
|20535|look_around_5|环视四周方案5|
|20536|look_around_6|环视四周方案6|
|20537|look_around_7|环视四周方案7|
|20563|nod_with_beats|带节奏的点头动作|

## 特殊动作

|    ID     |    名称    |    描述    |
| --------- | --------- | ---------- |
|20504|push_up|俯卧撑动作|
|20514|swim|模拟游泳动作|
|20515|rub_eyes|揉眼睛动作|
|20516|point_to_sky_left|左前爪指向天空|
|20517|point_to_sky_right|右前爪指向天空|
|20520|push_ahead|向前推动作|
|20569|be_sleepy|直接进入睡眠姿态|
|20572|nod_off|打瞌睡动作|
|20570|flex_muscles|展示肌肉动作|
|20564|joy_walk|欢快踏步配合摇头|
|20576|bark_bark|低姿态吠叫动作|
