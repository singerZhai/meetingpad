import time
import unittest
from base.init_driver import init_driver
from pages.hold_meeting_page import HoldMeetingPage
from pages.home_page import HomePage
from pages.invite_meeting_page import InviteMeetingPage
from pages.manage_meeting_page import ManageMeetingPage
from pages.meeting_detail_page import MeetingDetailPage
from pages.meeting_page import MeetingPage
from pages.set_layout_out_page import SetLayoutOutPage


class TestCreateAndCloseMeeting(unittest.TestCase):

    def setUp(self):
        self.driver = init_driver(deviceName='192.168.1.6:5555')
        self.home_page = HomePage(self.driver)
        self.hold_meeting_page = HoldMeetingPage(self.driver)
        self.meeting_page = MeetingPage(self.driver)
        self.set_layout_out_page = SetLayoutOutPage(self.driver)
        self.invite_meeting_page = InviteMeetingPage(self.driver)
        self.manage_meeting_page = ManageMeetingPage(self.driver)
        self.meeting_detail_page = MeetingDetailPage(self.driver)

    def test_create_and_close_meeting(self):
        for i in range(100):
            self.home_page.click_create_meeting_btn()
            self.hold_meeting_page.click_direct_meeting_btn()
            time.sleep(6)
            self.meeting_page.click_close_mic_btn()
            self.meeting_page.click_close_camera_btn()
            self.meeting_page.click_close_audio_btn()
            self.meeting_page.click_close_mic_btn()
            self.meeting_page.click_close_camera_btn()
            self.meeting_page.click_close_audio_btn()
            self.meeting_page.click_invite_meeting_btn()
            self.invite_meeting_page.click_back_btn()
            self.meeting_page.click_manage_meeting_btn()
            self.manage_meeting_page.click_stop_voice_btn()
            self.manage_meeting_page.click_back_btn()
            self.meeting_page.click_meeting_detail_btn()
            self.meeting_detail_page.click_back_btn()
            self.meeting_page.click_split_screen_btn()
            self.set_layout_out_page.click_set_layout_out3_btn()
            self.set_layout_out_page.click_one_split_screen_btn()
            self.set_layout_out_page.click_two_split_screen_btn()
            self.set_layout_out_page.click_three_split_screen_btn()
            self.set_layout_out_page.click_set_layout_out2_btn()
            self.set_layout_out_page.click_three_split_screen_btn()
            self.set_layout_out_page.click_two_split_screen_btn()
            self.set_layout_out_page.click_one_split_screen_btn()
            self.set_layout_out_page.click_automatic_split_screen_btn()
            self.set_layout_out_page.click_back_btn()
            time.sleep(3)
            self.meeting_page.click_exit_meeting_btn()
