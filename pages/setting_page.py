from selenium.webdriver.common.by import By
from base.base_action import BaseAction


class SettingPage(BaseAction):
    setting_btn = By.ID, "com.idcvideo.haokaihuidraw:id/setting_btn"
    tools_btn = By.ID, "com.idcvideo.haokaihuidraw:id/networking_btn"
    version_btn = By.ID, "com.idcvideo.haokaihuidraw:id/version_btn"
    binding_admin_btn = By.ID, "com.idcvideo.haokaihuidraw:id/team_dialog_btn"
    meetingpad_name_box = By.ID, "com.idcvideo.haokaihuidraw:id/meeting_pad_name_et"
    check_btn = By.ID, "com.idcvideo.haokaihuidraw:id/networking_check_bt"
    packet_loss = By.ID, "com.idcvideo.haokaihuidraw:id/networking_packetloss_tv"
    shake = By.ID, "com.idcvideo.haokaihuidraw:id/networking_churn_tv"
    back_btn = By.ID, "com.idcvideo.haokaihuidraw:id/video_source_top_back"

    def click_setting_btn(self):
        self.click(self.setting_btn)

    def click_tools_btn(self):
        self.click(self.tools_btn)

    def click_version_btn(self):
        self.click(self.version_btn)

    def input_meetingpad_name(self, text):
        self.input(self.meetingpad_name_box, text)

    def click_check_btn(self):
        self.click(self.check_btn)

    def click_back_btn(self):
        self.click(self.back_btn)

    def get_packet_loss(self):
        ele = self.find_element(self.packet_loss)
        return "丢包率:" + ele.text

    def get_shake(self):
        ele = self.find_element(self.shake)
        return "抖动:" + ele.text
