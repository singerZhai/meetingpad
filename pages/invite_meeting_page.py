from selenium.webdriver.common.by import By
from base.base_action import BaseAction


class InviteMeetingPage(BaseAction):
    back_btn = By.ID, 'com.idcvideo.haokaihuidraw:id/selete_person_top_back'

    def click_back_btn(self):
        self.click(self.back_btn)
