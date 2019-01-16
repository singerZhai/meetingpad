import time
import unittest
from base.init_driver import init_driver
from pages.home_page import HomePage
from pages.join_meeting_page import JoinMeetingPage
from pages.meeting_page import MeetingPage


class TestJoinMeeting(unittest.TestCase):

    def setUp(self):
        self.driver = init_driver(deviceName='192.168.1.6:5555', port='4723')
        self.home_page = HomePage(self.driver)
        self.join_meeting_page = JoinMeetingPage(self.driver)
        self.meeting_page = MeetingPage(self.driver)

    def test_join_meeting(self):
        # while True:
        for i in range(100):
            self.home_page.click_join_meeting_btn()
            # 以下两行代码为在可加入会议列表中点击相应会议入会
            # self.join_meeting_page.click_meeting_join_btn()
            # self.join_meeting_page.click_meeting_name_btn()

            # 以下三行代码为拨号盘呼叫入会
            self.join_meeting_page.click_bhp_btn()
            self.join_meeting_page.input_meeting_num(text='88000095')
            self.join_meeting_page.click_call_btn()
            time.sleep(6)
            self.meeting_page.click_close_audio_btn()
            self.meeting_page.click_close_camera_btn()
            self.meeting_page.click_close_mic_btn()
            self.meeting_page.click_close_audio_btn()
            self.meeting_page.click_close_camera_btn()
            self.meeting_page.click_close_mic_btn()
            time.sleep(20)
            self.meeting_page.click_exit_meeting_btn()
