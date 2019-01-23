from selenium.webdriver.common.by import By
from base.base_action import BaseAction


class AnswerPage(BaseAction):
    answer_btn = By.ID, "com.idcvideo.haokaihuidraw:id/jieting"
    hang_up_btn = By.ID, "com.idcvideo.haokaihuidraw:id/jujie"

    def click_answer_btn(self):
        self.click_keep_waiting(self.answer_btn)

    def click_hang_up_btn(self):
        self.click_keep_waiting(self.hang_up_btn)
