import time
import unittest
from base.init_driver import init_driver
from pages.answer_page import AnswerPage
from pages.manage_meeting_page import ManageMeetingPage
from pages.meeting_detail_page import MeetingDetailPage
from pages.meeting_page import MeetingPage
from pages.set_layout_out_page import SetLayoutOutPage


class TestSceneFive(unittest.TestCase):

    def setUp(self):
        self.driver = init_driver(deviceName="192.168.1.6:5555")
        self.answer_page = AnswerPage(self.driver)
        self.meeting_page = MeetingPage(self.driver)
        self.manage_meeting_page = ManageMeetingPage(self.driver)
        self.meeting_detail_page = MeetingDetailPage(self.driver)
        self.set_layout_out_page = SetLayoutOutPage(self.driver)

    def test_scene_five(self):
        for x in range(100):
            time.sleep(1)
            self.answer_page.click_answer_btn()
            self.meeting_page.click_manage_meeting_btn()
            for i in range(3):
                self.driver.swipe(950, 800, 1000, 400)
            self.manage_meeting_page.click_back_btn()
            self.meeting_page.click_meeting_detail_btn()
            self.meeting_detail_page.click_back_btn()
            self.meeting_page.click_split_screen_btn()
            # self.set_layout_out_page.click_set_layout_out2_btn()
            # self.set_layout_out_page.click_set_layout_out3_btn()
            # self.set_layout_out_page.click_set_layout_out2_btn()
            self.set_layout_out_page.click_back_btn()
            for a in range(2):
                self.meeting_page.click_close_audio_btn()
                self.meeting_page.click_close_camera_btn()
                self.meeting_page.click_close_mic_btn()
            self.meeting_page.click_exit_meeting_btn()
