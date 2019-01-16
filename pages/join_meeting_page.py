from selenium.webdriver.common.by import By
from base.base_action import BaseAction


class JoinMeetingPage(BaseAction):

    meeting_join_btn = By.ID, "com.idcvideo.haokaihuidraw:id/meeting_join_join"
    meeting_name_btn = By.XPATH, "//*[contains(@text,'88000095')]"
    bhp_btn = By.ID, 'com.idcvideo.haokaihuidraw:id/meeting_join_bhp'
    input_box = By.ID, 'com.idcvideo.haokaihuidraw:id/meeting_join_et'
    call_btn = By.ID, 'com.idcvideo.haokaihuidraw:id/meeting_join_btn'

    def click_meeting_join_btn(self):
        self.click(self.meeting_join_btn)

    def click_meeting_name_btn(self):
        self.click(self.meeting_name_btn)

    def click_bhp_btn(self):
        self.click(self.bhp_btn)

    def input_meeting_num(self, text):
        self.input(self.input_box, text)

    def click_call_btn(self):
        self.click(self.call_btn)
