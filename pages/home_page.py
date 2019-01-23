from selenium.webdriver.common.by import By
from base import init_driver
from base.base_action import BaseAction


class HomePage(BaseAction):
    create_meeting_btn = By.ID, "com.idcvideo.haokaihuidraw:id/activity_iv_createmeeting"
    join_meeting_btn = By.ID, "com.idcvideo.haokaihuidraw:id/activity_iv_joinmeeting"
    address_list_btn = By.ID, "com.idcvideo.haokaihuidraw:id/activity_iv_maillist"
    setting_btn = By.ID, "com.idcvideo.haokaihuidraw:id/home_xuan_shi_setting_iv"

    def click_create_meeting_btn(self):
        self.click(self.create_meeting_btn)

    def click_join_meeting_btn(self):
        self.click(self.join_meeting_btn)

    def click_address_list_btn(self):
        self.click(self.address_list_btn)

    def click_setting_btn(self):
        self.click(self.setting_btn)


if __name__ == '__main__':
    HomePage(driver=init_driver).click_create_meeting_btn()
