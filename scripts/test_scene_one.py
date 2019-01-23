import unittest
import time
from base.init_driver import init_driver
from pages.address_list_page import AddressListPage
from pages.hold_meeting_page import HoldMeetingPage
from pages.home_page import HomePage
from pages.invite_meeting_page import InviteMeetingPage
from pages.join_meeting_page import JoinMeetingPage
from pages.manage_meeting_page import ManageMeetingPage
from pages.meeting_detail_page import MeetingDetailPage
from pages.meeting_page import MeetingPage
from pages.set_layout_out_page import SetLayoutOutPage


class TestSceneOne(unittest.TestCase):

    def setUp(self):
        self.driver = init_driver(deviceName='192.168.1.6:5555')
        self.home_page = HomePage(self.driver)
        self.hold_meeting_page = HoldMeetingPage(self.driver)
        self.meeting_page = MeetingPage(self.driver)
        self.set_layout_out_page = SetLayoutOutPage(self.driver)
        self.invite_meeting_page = InviteMeetingPage(self.driver)
        self.manage_meeting_page = ManageMeetingPage(self.driver)
        self.meeting_detail_page = MeetingDetailPage(self.driver)
        self.address_list_page = AddressListPage(self.driver)
        self.join_meeting_page = JoinMeetingPage(self.driver)

    def test_scene_one(self):
        """
        脚本前提:运行脚本的设备的会议室没有被占用
        脚本内容:首页召开会议/通讯录中召开会议,邀请人员入会input_num('被邀请人号码');
        所有一级菜单,包括频繁更改显示模式和分屏模式
        循环次数100:如需更改range(循环次数)
        :return:
        """
        for i in range(100):
            time.sleep(1)
            # 以下两代码为通过首页召开会议模块开会
            # self.home_page.click_create_meeting_btn()
            # self.hold_meeting_page.click_direct_meeting_btn()

            # 以下为通过首页通讯录模块中召开会议
            self.home_page.click_address_list_btn()
            self.address_list_page.click_create_meeting_btn()

            time.sleep(6)
            self.meeting_page.click_close_mic_btn()
            self.meeting_page.click_close_camera_btn()
            self.meeting_page.click_close_audio_btn()
            self.meeting_page.click_close_mic_btn()
            self.meeting_page.click_close_camera_btn()
            self.meeting_page.click_close_audio_btn()
            self.meeting_page.click_invite_meeting_btn()
            self.invite_meeting_page.click_input_box_btn()
            self.invite_meeting_page.input_num('13987654321')
            self.invite_meeting_page.click_confirm_btn()
            self.invite_meeting_page.click_invite_btn()
            self.meeting_page.click_manage_meeting_btn()
            self.manage_meeting_page.click_stop_voice_btn()
            self.manage_meeting_page.click_stop_voice_btn()
            self.manage_meeting_page.click_back_btn()
            self.meeting_page.click_meeting_detail_btn()
            self.meeting_detail_page.click_back_btn()
            # 以下为切换分屏和显示
            self.meeting_page.click_split_screen_btn()
            # self.set_layout_out_page.click_set_layout_out3_btn()
            # self.set_layout_out_page.click_one_split_screen_btn()
            # self.set_layout_out_page.click_two_split_screen_btn()
            # self.set_layout_out_page.click_three_split_screen_btn()
            # self.set_layout_out_page.click_set_layout_out2_btn()
            # self.set_layout_out_page.click_three_split_screen_btn()
            # self.set_layout_out_page.click_two_split_screen_btn()
            # self.set_layout_out_page.click_one_split_screen_btn()
            # self.set_layout_out_page.click_automatic_split_screen_btn()
            self.set_layout_out_page.click_back_btn()
            time.sleep(3)
            self.meeting_page.click_manage_meeting_btn()
            self.manage_meeting_page.click_close_meeting_btn()
            self.address_list_page.click_back_btn()
