from selenium.webdriver.common.by import By
from base.base_action import BaseAction


class SetLayoutOutPage(BaseAction):
    set_layout_out1_btn = By.ID, 'com.idcvideo.haokaihuidraw:id/set_layout_out1'
    set_layout_out2_btn = By.ID, 'com.idcvideo.haokaihuidraw:id/set_layout_out2'
    set_layout_out3_btn = By.ID, 'com.idcvideo.haokaihuidraw:id/set_layout_out3'
    automatic_split_screen_btn = By.ID, 'com.idcvideo.haokaihuidraw:id/automatic_split_screen_ib'
    one_split_screen_btn = By.ID, 'com.idcvideo.haokaihuidraw:id/one_split_screen_ib'
    two_split_screen_btn = By.ID, 'com.idcvideo.haokaihuidraw:id/two_split_screen_ib'
    three_split_screen_btn = By.ID, 'com.idcvideo.haokaihuidraw:id/three_split_screen_ib'
    four_split_screen_btn = By.ID, 'com.idcvideo.haokaihuidraw:id/four_split_screen_ib'
    back_btn = By.ID, 'com.idcvideo.haokaihuidraw:id/set_layout_top_back'

    def click_set_layout_out1_btn(self):
        self.click(self.set_layout_out1_btn)

    def click_set_layout_out2_btn(self):
        self.click(self.set_layout_out2_btn)

    def click_set_layout_out3_btn(self):
        self.click(self.set_layout_out3_btn)

    def click_automatic_split_screen_btn(self):
        self.click(self.automatic_split_screen_btn)

    def click_one_split_screen_btn(self):
        self.click(self.one_split_screen_btn)

    def click_two_split_screen_btn(self):
        self.click(self.two_split_screen_btn)

    def click_three_split_screen_btn(self):
        self.click(self.three_split_screen_btn)

    def click_four_split_screen_btn(self):
        self.click(self.click_four_split_screen_btn)

    def click_back_btn(self):
        self.click(self.back_btn)
