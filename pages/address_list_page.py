from selenium.webdriver.common.by import By
from base.base_action import BaseAction


class AddressListPage(BaseAction):
    create_meeting_btn = By.ID, 'com.idcvideo.haokaihuidraw:id/dialog_mail_list_btn1'
    back_btn = By.ID, 'com.idcvideo.haokaihuidraw:id/video_source_top_tv'

    def click_create_meeting_btn(self):
        self.click(self.create_meeting_btn)

    def click_back_btn(self):
        self.click(self.back_btn)
