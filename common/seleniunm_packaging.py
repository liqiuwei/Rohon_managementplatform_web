from config.config import PNG_PATH_YZM
from PIL import Image
from common.kuaishibie_packaging import base64_api
import pywinauto
from pywinauto.keyboard import send_keys
from selenium.webdriver import ActionChains
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from config import config
from middleware.heandler import Hadnler


class BasePage:
    title = None

    def __init__(self, driver):
        self.driver = driver

        try:
            WebDriverWait(self.driver, timeout=20, poll_frequency=0.5).until(
                expected_conditions.title_contains(self.title))
        except Exception as err:
            Hadnler.logger.error('你的操作没有进入{}页面可能会引发异常{}'.format(self.title, err))

    def find_element(self, locator):
        """查找元素"""
        el = self.driver.find_element(*locator)
        return el

    def find_elements(self, locator):
        """查找多个元素"""
        el = self.driver.find_elements(*locator)
        return el

    # def screen_shon(self):
    #     """截图"""
    #     path = config.IMG_PATH
    #     ts = datetime.now().strftime("%Y%m%d%H%M%S")
    #     filename = os.path.join(path, ts + '.png')
    #     self.driver.save_screenshoy(filename)

    def Situation_box(self, locator):
        """清除输入框的默认值"""
        data = self.wait_element_visible(locator)
        self.driver.execute_script("arguments[0].value = '';", data)
        return self

    def wait_element_visible(self, locator, timeout=20, poll=0.5):
        """显性等待某一个元素出现"""
        try:
            el = WebDriverWait(self.driver, timeout=timeout, poll_frequency=poll).until(
                expected_conditions.visibility_of_element_located(locator)
            )
            return el
        except Exception as err:
            Hadnler.logger.error('{}元素找不到{}'.format(locator, err))

    def wait_element_clickable(self, locator, timeout=20):
        """等待某个元素可以被点击"""
        try:
            el = WebDriverWait(self.driver, timeout=timeout).until(
                expected_conditions.element_to_be_clickable(locator)
            )
            return el
        except Exception as err:
            Hadnler.logger.error('{}元素找不到{}'.format(locator, err))
            # self.screen_shon()

    def wait_element_presence(self, locator, timeout=20, poll=0.5):
        """等待某一个元素出现"""
        try:
            el = WebDriverWait(self.driver, timeout=timeout, poll_frequency=poll).until(
                expected_conditions.presence_of_element_located(locator)
            )
            return el
        except Exception as err:
            Hadnler.logger.error('{}元素找不到{}'.format(locator, err))

    def scroll(self, height, width):
        """页面的滚动
        >>>
        height：竖坐标：垂直坐标，width：横坐标
        """
        if height is None:
            height = 0
        if width is None:
            width = 0
        js_code = 'window.scrollTo({},{});'.format(width, height)
        self.driver.execute_script(js_code)

    def move_to(self, locator):
        """鼠标移动到某个元素
        >>>
        locator：鼠标移动到这个元素位置
        """
        el = self.driver.find_element(*locator)
        ActionChains(self.driver).move_to_element(el).perform()
        return self

    def switch_iframe(self, locator, timeout=20):
        """切换到iframe,(内嵌窗口)
        >>>
        locator：定位iframe的元素
        """
        WebDriverWait(self.driver, timeout=timeout).until(
            expected_conditions.frame_to_be_available_and_switch_to_it(locator))
        return self

    def click(self, locator):
        """点击某个元素（带显性等待）"""
        self.wait_element_clickable(locator).click()
        return self

    def isPresent(self, Xpath):
        """判断元素是否存在"""
        try:
            self.driver.find_element_by_xpath(Xpath)
        except Exception as err:
            return False
        return True

    def upload_files(self, file_path, file, *args):
        """win窗口的形式上传文件"""
        app = pywinauto.Desktop()
        dlg = app['打开']
        dlg['123'].click()
        send_keys(file_path)
        send_keys('{ENTER}')
        dlg['文件名(&N):Edit'].type_keys('"{}"'.format(file))
        for i in args:
            send_keys('"{}"'.format(i))
        dlg['打开&O'].click()

    def Identification_verification_code(self, xpath):
        """识别登录验证码"""
        path = config.PNG_PATH
        self.driver.save_screenshot(path)
        # 获取元素的矩形
        rect = self.find_element(xpath).rect
        # 计算 图片上下左右边界位置
        l = rect['x'] + 10  # 图片左边界坐标
        t = rect['y']  # 图片上边界坐标
        r = (rect['x'] + rect['width'])  # 图片右边界坐标
        b = (rect['y'] + rect['width']) - 60  # 图片下边界坐标
        loc = (l, t, r, b)
        # 从页面中截图验证码
        pic = Image.open(path)
        v_pic = pic.crop(loc)
        v_code = PNG_PATH_YZM
        v_pic.save(v_code)
        # 识别验证码内容
        result = base64_api(v_code)
        return result
