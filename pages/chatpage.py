
from pages.Base import Base
class ChatPage(Base):

    search = 'new UiSelector().description("搜索").resourceId("cn.guoguo.chat:id/search")'

    more = 'new UiSelector().resourceId("cn.guoguo.chat:id/more")'

    tu_zhu = "cn.guoguo.chat:id/iv_bottom_pour"

    qun_zu = "cn.guoguo.chat:id/nameTextView"


    def search_btn(self):
        self.by_android_uiautomator(self.search).click()

    def more_btn(self):
        self.by_android_uiautomator(self.more).click()

    def tuzhu(self):
        self.by_id(self.tu_zhu).click()


    def qunzu(self):
        self.by_id_elements(self.qu_zu).click()




