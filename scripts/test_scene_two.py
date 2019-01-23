import time
import unittest
from base.init_driver import init_driver
from pages.home_page import HomePage
from pages.join_meeting_page import JoinMeetingPage
from pages.manage_meeting_page import ManageMeetingPage
from pages.meeting_detail_page import MeetingDetailPage
from pages.meeting_page import MeetingPage
from pages.set_layout_out_page import SetLayoutOutPage


class TestSceneTwo(unittest.TestCase):

    def setUp(self):
        self.driver = init_driver(deviceName='192.168.1.6:5555')
        self.home_page = HomePage(self.driver)
        self.join_meeting_page = JoinMeetingPage(self.driver)
        self.meeting_page = MeetingPage(self.driver)
        self.manage_meeting_page = ManageMeetingPage(self.driver)
        self.meeting_detail_page = MeetingDetailPage(self.driver)
        self.set_layout_out_page = SetLayoutOutPage(self.driver)

    def test_scene_two(self):
        """
        脚本前提:有一个常开的会议,会中PC频繁开关切换共享,将配合的会议号填写在下面text='会议号';
        脚本内容:拨号盘呼叫会议入会,会议界面的所有一级菜单全部按一遍,然后停留会中20s,观察会议中接收共享情况
        循环入会100次,如需更改次数,range(循环次数)
        :return:
        """
        for i in range(100):
            time.sleep(1)
            self.home_page.click_join_meeting_btn()
            # 以下三行代码为拨号盘呼叫入会
            self.join_meeting_page.click_bhp_btn()
            self.join_meeting_page.input_meeting_num(text='88000090')
            self.join_meeting_page.click_call_btn()
            time.sleep(6)
            self.meeting_page.click_close_audio_btn()
            self.meeting_page.click_close_camera_btn()
            self.meeting_page.click_close_mic_btn()
            self.meeting_page.click_close_audio_btn()
            self.meeting_page.click_close_camera_btn()
            self.meeting_page.click_close_mic_btn()
            self.meeting_page.click_manage_meeting_btn()
            self.manage_meeting_page.click_back_btn()
            self.meeting_page.click_meeting_detail_btn()
            self.meeting_detail_page.click_back_btn()
            self.meeting_page.click_split_screen_btn()
            self.set_layout_out_page.click_back_btn()
            time.sleep(20)
            self.meeting_page.click_exit_meeting_btn()
