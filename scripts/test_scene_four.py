import time
import unittest
from base.base_action import write_files
from base.init_driver import init_driver
from pages.home_page import HomePage
from pages.setting_page import SettingPage


class TestSceneFour(unittest.TestCase):

    def setUp(self):
        self.driver = init_driver(deviceName='192.168.1.6:5555')
        self.home_page = HomePage(self.driver)
        self.setting_page = SettingPage(self.driver)

    def test_scene_four(self):
        for a in range(100):
            time.sleep(1)
            self.home_page.click_setting_btn()
            self.setting_page.click_setting_btn()
            self.setting_page.click_tools_btn()
            for b in range(10):
                self.driver.tap([(950, 850)])
                time.sleep(10)
                ele1 = self.setting_page.get_packet_loss()
                ele2 = self.setting_page.get_shake()
                write_files(ele1 + "\t" + ele2)
            self.setting_page.click_version_btn()
            self.setting_page.click_back_btn()
