from selenium.webdriver.common.by import By
from base.base_action import BaseAction


class HoldMeetingPage(BaseAction):

    direct_meeting_btn = By.ID, "com.idcvideo.haokaihuidraw:id/selete_person_create"

    def click_direct_meeting_btn(self):
        self.click(self.direct_meeting_btn)
