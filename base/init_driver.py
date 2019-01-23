from appium import webdriver


def init_driver(deviceName):
    # server 启动参数
    desired_caps = dict()
    # 设备信息
    desired_caps['platformName'] = 'Android'
    desired_caps['platformVersion'] = '5.0.1'
    desired_caps['deviceName'] = deviceName
    # app的信息
    desired_caps['appPackage'] = 'com.idcvideo.haokaihuidraw'
    desired_caps['appActivity'] = 'com.idcvideo.view.SplashActivity'
    # 声明我们的driver对象
    driver = webdriver.Remote('http://127.0.0.1:4723/wd/hub', desired_caps)
    return driver


if __name__ == '__main__':
    driver = init_driver(deviceName='192.168.1.6:5555')
    # ip = driver.find_element_by_id("com.idcvideo.haokaihuidraw:id/ip_tv")
    # meeting_code = driver.find_element_by_id("com.idcvideo.haokaihuidraw:id/home_xuan_shi_account_number_tv")
    # print('ip地址为:' + ip.text)
    # print('会议室为:' + meeting_code.text)
