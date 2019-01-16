from appium import webdriver


def init_driver(deviceName, port=4723):
    # server 启动参数
    desired_caps = dict()
    # 设备信息
    desired_caps['platformName'] = 'Android'
    desired_caps['platformVersion'] = '5.0.1'
    desired_caps['deviceName'] = deviceName
    # app的信息
    desired_caps['appPackage'] = 'com.idcvideo.haokaihuidraw'
    desired_caps['appActivity'] = 'com.idcvideo.view.HomeActivity'
    # 声明我们的driver对象
    driver = webdriver.Remote(('http://127.0.0.1:%s/wd/hub' % port), desired_caps)
    return driver


if __name__ == '__main__':
    driver = init_driver(deviceName='192.168.1.6:5555')
