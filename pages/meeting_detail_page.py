from selenium.webdriver.common.by import By
from base.base_action import BaseAction


class MeetingDetailPage(BaseAction):
    back_btn = By.ID, 'com.idcvideo.haokaihuidraw:id/yao_qing_back'

    def click_back_btn(self):
        self.click(self.back_btn)
