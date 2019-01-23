import yaml
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait


class BaseAction:

    def __init__(self, driver):
        self.driver = driver

    def find_element(self, location, timeout=20.0, poll_frequency=1.0):
        location_by, location_value = location
        wait = WebDriverWait(self.driver, timeout, poll_frequency)
        return wait.until(lambda x: x.find_element(location_by, location_value))

    def find_elements(self, location, timeout=20.0, poll=1.0):
        location_by, location_value = location
        wait = WebDriverWait(self.driver, timeout, poll)
        return wait.until(lambda x: x.find_elements(location_by, location_value))

    def click(self, location):
        self.find_element(location).click()

    def click_keep_waiting(self, location):
        while True:
            try:
                self.find_element(location).click()
                return
            except KeyError:
                pass

    def input(self, location, text):
        ele = self.find_element(location)
        ele.clear()
        ele.send_keys(text)

    def press_back(self):
        self.driver.press_keycode(4)

    def press_enter(self):
        self.driver.press_keycode(66)

    def find_toast(self, message, timeout=3):
        """
        # message: 预期要获取的toast的部分消息
        """
        message = "//*[contains(@text,'" + message + "')]"  # 使用包含的方式定位

        element = self.find_element((By.XPATH, message), timeout, 0.1)
        return element.text

    def is_toast_exist(self, message):
        try:
            self.find_toast(message)
            return True
        except Exception:
            return False


def get_invite_num(num):
    with open('../data/data.yaml', 'rb') as f:
        res = yaml.load(f)
    demo_list = list()
    for i in res['invite_num'].values():
        demo_list.append(i)
    if num == 'all':
        return demo_list
    if num in demo_list:
        return demo_list[num]
    elif num not in demo_list:
        print('本地yaml文件中不存在此数据')


def write_files(text):
    with open("../data/network_tools.txt", 'a')as f:
        f.write(text + "\n")


if __name__ == '__main__':
    print(get_invite_num('all'))
