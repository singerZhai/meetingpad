from selenium.webdriver.common.by import By
from base.base_action import BaseAction


class InviteMeetingPage(BaseAction):
    back_btn = By.ID, 'com.idcvideo.haokaihuidraw:id/selete_person_top_back'
    input_box_btn = By.ID, 'com.idcvideo.haokaihuidraw:id/selete_person_sd'
    input_box = By.ID, 'com.idcvideo.haokaihuidraw:id/selete_person_et'
    confirm_btn = By.ID, 'com.idcvideo.haokaihuidraw:id/selete_person_ok'
    invite_btn = By.ID, 'com.idcvideo.haokaihuidraw:id/selete_person_create'

    def click_back_btn(self):
        self.click(self.back_btn)

    def click_input_box_btn(self):
        self.click(self.input_box_btn)

    def input_num(self, text):
        self.input(self.input_box, text)

    def click_confirm_btn(self):
        self.click(self.confirm_btn)

    def click_invite_btn(self):
        self.click(self.invite_btn)
