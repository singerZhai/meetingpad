import time
import unittest
from base.base_action import get_invite_num
from base.init_driver import init_driver
from pages.hold_meeting_page import HoldMeetingPage
from pages.home_page import HomePage
from pages.invite_meeting_page import InviteMeetingPage
from pages.manage_meeting_page import ManageMeetingPage
from pages.meeting_detail_page import MeetingDetailPage
from pages.meeting_page import MeetingPage
from pages.set_layout_out_page import SetLayoutOutPage


class TestSceneThree(unittest.TestCase):

    def setUp(self):
        self.driver = init_driver(deviceName='192.168.1.6:5555')
        self.home_page = HomePage(self.driver)
        self.meeting_page = MeetingPage(self.driver)
        self.manage_meeting_page = ManageMeetingPage(self.driver)
        self.invite_meeting_page = InviteMeetingPage(self.driver)
        self.hold_meeting_page = HoldMeetingPage(self.driver)
        self.meeting_detail_page = MeetingDetailPage(self.driver)
        self.set_layout_out_page = SetLayoutOutPage(self.driver)

    def test_scene_three(self):
        for i in range(100):
            time.sleep(1)
            self.home_page.click_create_meeting_btn()
            self.hold_meeting_page.click_direct_meeting_btn()
            num_list = get_invite_num('all')
            for a in num_list:
                time.sleep(1)
                self.meeting_page.click_invite_meeting_btn()
                self.invite_meeting_page.click_input_box_btn()
                self.invite_meeting_page.input_num(a)
                self.invite_meeting_page.click_confirm_btn()
                self.invite_meeting_page.click_invite_btn()
            for b in range(10):
                self.meeting_page.click_manage_meeting_btn()
                self.driver.swipe(1000, 830, 950, 450)
                for c in range(10):
                    self.manage_meeting_page.click_stop_voice_btn()
                self.manage_meeting_page.click_back_btn()
            for d in range(10):
                self.meeting_page.click_meeting_detail_btn()
                self.meeting_detail_page.click_back_btn()
            for e in range(10):
                self.meeting_page.click_split_screen_btn()
                self.set_layout_out_page.click_back_btn()
            for f in range(10):
                self.meeting_page.click_close_mic_btn()
            for g in range(10):
                self.meeting_page.click_close_camera_btn()
            for h in range(10):
                self.meeting_page.click_close_audio_btn()
            self.meeting_page.click_manage_meeting_btn()
            self.manage_meeting_page.click_close_meeting_btn()
