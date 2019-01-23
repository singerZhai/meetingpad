from selenium.webdriver.common.by import By
from base.base_action import BaseAction


class MeetingPage(BaseAction):
    invite_meeting_btn = By.ID, "com.idcvideo.haokaihuidraw:id/invite_meeting_iv"
    manage_meeting_btn = By.ID, "com.idcvideo.haokaihuidraw:id/manage_meeting_iv"
    meeting_detail_btn = By.ID, "com.idcvideo.haokaihuidraw:id/meeting_detail_iv"
    split_screen_btn = By.ID, "com.idcvideo.haokaihuidraw:id/split_screen_iv"
    close_audio_btn = By.ID, "com.idcvideo.haokaihuidraw:id/close_audio_iv"
    close_camera_btn = By.ID, "com.idcvideo.haokaihuidraw:id/close_camera_iv"
    close_mic_btn = By.ID, "com.idcvideo.haokaihuidraw:id/close_mic_iv"
    exit_meeting_btn = By.ID, "com.idcvideo.haokaihuidraw:id/close_meeting_iv"

    def click_invite_meeting_btn(self):
        self.click(self.invite_meeting_btn)

    def click_manage_meeting_btn(self):
        self.click(self.manage_meeting_btn)

    def click_meeting_detail_btn(self):
        self.click(self.meeting_detail_btn)

    def click_split_screen_btn(self):
        self.click(self.split_screen_btn)

    def click_close_audio_btn(self):
        self.click(self.close_audio_btn)

    def click_close_camera_btn(self):
        self.click(self.close_camera_btn)

    def click_close_mic_btn(self):
        self.click(self.close_mic_btn)

    def click_exit_meeting_btn(self):
        self.click(self.exit_meeting_btn)
