import time

from pywinauto.application import Application
from pywinauto import mouse
from pywinauto.keyboard import send_keys
from pywinauto.timings import wait_until, Timings

# app =Application(backend="uia").start("notepad.exe")
# 选择主窗口
# dlg =app['无标题 - 记事本']
# dlg.print_control_identifiers()
# 选择编辑框
# dlg['Edit'].type_keys('自动化测试添加的')

# 替换
# dlg.menu_select('编辑->替换(R)')
# 选择替换窗口
# time.sleep(3)
# app = dlg['替换']
# app.print_control_identifiers()
# 选种查找的编辑框
# app.child_window(title="查找内容(N):", auto_id="1152", control_type="Edit").type_keys('自动化测试添加的')

# 选择替换为的编辑框
# app.child_window(title="替换为(P):", auto_id="1153", control_type="Edit").type_keys('66666')
# app.child_window(title="全部替换(A)", auto_id="1025", control_type="Button").click_input()

# ________________________模拟键盘操作__________________________
# 按 F1
# send_keys('{F1}')
# 按win键打开cmd，进入python
# send_keys('{LWIN}')
# send_keys('cmd')
# time.sleep(1)
# send_keys('{ENTER}')
# send_keys('python')
# 写进一行
# send_keys('{LWIN}cmd{ENTER}python')

# 修饰符
# + : Shift
# ^ : Ctrl
# % : A/t
# ^S ：保存
# 全选
# send_keys('^a')

# 快捷键Ctrl+Shift+a
# send_keys('^%a')

# ---------------鼠标的操作-----------------------
# 鼠标单击()默认左键
# mouse.click(coords=(580,52))
# 鼠标右击
# mouse.right_click(coords=(1000,500))
# 鼠标双击左键
# mouse.double_click(button='left', coords=(1000, 500)
# 点击鼠标中间键
# mouse.wheel_click(coords=(1000,500))

# 按下鼠标
# mouse.press(coords=(1000,16))
# 释放鼠标
# mouse.release(coords=(1000,500))
# 鼠标滚轮  在1000，400的位置往上滚动8次，-8就是往下滚
# mouse.scroll(coords=(1000,400,),wheel_dist=8)
# 鼠标位置移动
# mouse.move(coords=(0,0))

#-------------系统提示区域的操作，任务栏-------------
# app = Application('uia').connect(path='explorer')
# app['任务栏'].print_control_identifiers()

#隐藏区域
# app = Application('uia').connect(path='explorer')
# # app['任务栏'].print_control_identifiers()
# task = app['任务栏'].child_window(title="通知 V 形", auto_id="1502", control_type="Button")
# task.click()
# app['通知溢出']['钉钉'].click_input()

# __________获取控件的位置____________
# v = app['任务栏'].child_window(title="通知 V 形", auto_id="1502", control_type="Button")
#           获取位置     获取位置的中心点
# weizhi = v.rectangle().mid_point()
# 获取到中心点之后就可以 通过鼠标点击
# mouse.double_click(coords=(weizhi.x,weizhi.y))

# 打印所有的窗口
# 1、前置条件是点开需要操作的窗口
# print(app.windows())