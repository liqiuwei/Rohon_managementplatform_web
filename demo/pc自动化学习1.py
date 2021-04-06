import time

from pywinauto.application import Application
from pywinauto import mouse
from pywinauto.keyboard import send_keys
from pywinauto.timings import wait_until,Timings

# 根据路径打开一个程序
# app = Application(backend="uia").start(r"RHClient.exe")

# 根据进程连接一个已经打开的程序
# app = Application(backend="win32").connect(process=3344)
# dlg = app['微冲交易客户端']
# dlg['Edit'].type_keys('123456')
# dlg.print_control_identifiers()
# time.sleep(3)
# dlg.child_window(title="下单", class_name="Button").click_input()

# -----登录后的结算提示------
# dlg = app['微冲交易客户端']
# dlg.print_control_identifiers()
# dlg.child_window(title="确认", auto_id="1", control_type="Button").click_input()
#-----登录后的结算提示 - -----
# dlg = app['账户: 123456 开户人:李秋维 经纪公司: ETF期权']
# shuju = dlg.child_window(title="您目前的风险级别已达到追保，请立即追加保证金或减仓", auto_id="1104", control_type="Text")
# print(shuju.texts())


# 根据句柄连接一个已经打开的程序
# app = Application(backend="uia").connect(handle=3670464)
# print(app)
# 选择窗口，根据类名
# dlg= app['类名/标题']
# 打印窗口的所有的控件
# dlg.print_control_identifiers()
# 选择窗口，根据标题
# dlg = app['微冲交易客户端']
# dlg.print_control_identifiers()
# 窗口最大化
# dlg.maximize()
# 窗口最小化
# dlg.minimize()
# 窗口恢复正常大小
# dlg.restore()
# 查看窗口显示状态,最大化是1 正常是0
# data = dlg.get_show_state()
# print(data)
# 获取当前窗口显示的坐标
# rect = dlg.rectangle()
# print(rect)
# 关闭窗口
# dlg.close()

# 选择控件(选择菜单栏)
# dlg = app['账户: 123456 开户人:李秋维 经纪公司: ETF期权']
# dlg.wait(wait_for='ready',timeout=30,retry_interval=2)
# print('等待通过')
# dlg.print_control_identifiers()
# dlg.maximize()
# menu = dlg['Menu']
# print(menu.children())
# menu.print_control_identifiers()
# 选择菜单栏下面的系统  报错了
# menu = dlg['Menu']['系统']
# menu.print_control_identifiers()
# 选择菜单栏下面的系统
# xitong = menu.child_window(title="系统", control_type="MenuItem")
# xitong.print_control_identifiers()

# 查看控件类型
# print(xitong.wrapper_object())
# 查看控件支持的方法 dir查看对象所支持的方法
# print(dir(xitong.wrapper_object()))
# 查看窗口的文本
# print((xitong.window_text()))
# print(xitong.texts())
# 获取子控件
# print(xitong.children())
# 获取控件的类名
# print(xitong.class_name())
# 获取控件的属性返回字典
# print((xitong.get_properties()))

# 对窗口进行截图
# pic = xitong.capture_as_image()
# print(pic)
# 保存截图
# pic.save('01.png')

# --------菜单的相关操作--------
# 获取菜单的子菜单项
# print(menu.items())
# 通过下标去选择菜单项
# m = menu.item_by_index(1)
# print(m)
# 通过路径选择菜单项(可以跨层级，比如获取到系统下面的提交日志)，在客户端上无法实现
# m = menu.item_by_path('系统->提交日志')
# print(m)

# 获取子菜单项
# print(menu.items())
# 点击系统菜单
# xitong.click_input()
# time.sleep(1)
# 点击系统下面的查询金额
# menu.item_by_path('查询金额').click_input()

#----------------等待机制--------------------
# 等待窗口处于可见状态
# dlg = app['账户: 123456 开户人:李秋维 经纪公司: ETF期权']
#            等待可见状态       等待20秒        2秒轮询一次
# dlg.wait(wait_for='ready',timeout=20,retry_interval=2)
# print('等待通过')
# 等待窗口处于不处于某个状态
# dlg = app['账户: 123456 开户人:李秋维 经纪公司: ETF期权']
# dlg.wait_not(wait_for_not='ready',timeout=20,retry_interval=2)

# 等待cput低于某个值
# app = Application(backend="uia").connect(process=11120)
# 等待应用程序CPU占用低于5%，等待10秒钟，每1秒钟轮询一遍
# app.wait_cpu_usage_lower(threshold=5,timeout=10,usage_interval=1)

# 等待机制timings模块
# """等待函数返回结果为5的时候继续执行下去"""
i = 0
def work():
    global i
    i +=1
    print('当前i等于',i)
    return i

# 等待10秒钟，每1秒钟执行一遍1函数，一直等到结果等于5
wait_until(10, 1, work, 5)
print('等待通过')
# 将等待的计时器设置成默认值
# Timings.Defaults()
# 将等待时间加倍（慢2倍）
# Timings.slow()
# 将所有计时除以2(快两倍)




# time.sleep(1)
#
# dlg['Edit'].type_keys('123456')
# # dlg.print_control_identifiers()
#
# send_keys('{TAB}')
# send_keys('1234561')
# dlg['Button'].click_input()
# time.sleep(15)
# dlg = app['账户: 123456 开户人:李秋维 经纪公司: ETF期权']
# dlg.print_control_identifiers()
# el = dlg['Static'].texts()
