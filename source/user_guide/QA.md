# 常见问题与解答

1. Q: 为什么调用技能时被拒绝？

    A: 调用被拒绝大部分情况是因为正有其他高优先级的调用者在持有技能，具体可以根据返回结果分析。

2. Q: 为什么发送移动指令，机器狗不走？

    A: 首先检查调用是否被拒绝，其次查看机器狗当前是否处于可移动状态(motion_mode为3)，可发送 action_id 4 让机器狗进入可移动状态。
