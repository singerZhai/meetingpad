from selenium.webdriver.common.by import By
from base.base_action import BaseAction


class ManageMeetingPage(BaseAction):
    back_btn = By.ID, 'com.idcvideo.haokaihuidraw:id/meeting_person_list_top_back'
    stop_voice_btn = By.ID, 'com.idcvideo.haokaihuidraw:id/meeting_person_button'
    close_meeting_btn = By.ID, 'com.idcvideo.haokaihuidraw:id/meeting_person_button_close'

    def click_back_btn(self):
        self.click(self.back_btn)

    def click_stop_voice_btn(self):
        self.click(self.stop_voice_btn)

    def click_close_meeting_btn(self):
        self.click(self.close_meeting_btn)
        