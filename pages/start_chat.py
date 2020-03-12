from pages.Base import Base

class StartChat(Base):

    start_chat = 'new UiSelector().text("发起群聊")'

    return_lastPage = 'new UiSelector().description("转到上一层级")'

    confirm = 'cn.guoguo.chat:id/confirm'

    search = 'cn.guoguo.chat:id/searchEditText'

    chat_group = 'cn.guoguo.chat:id/llGroup'

    friend_list = "cn.guoguo.chat:id/contactLinearLayout"

    def start_chat_loc(self):
        self.by_android_uiautomator(self.start_chat).click()

    def to_lastPage(self):
        self.by_android_uiautomator(self.return_lastPage).click()

    def confirm_btn(self):
        self.by_id(self.confirm).click()


    def search_btn(self, content):
        self.by_id(self.search).send_keys(content)

    def chatGroup_btn(self):
        self.by_id(self.chat_group).click()

    def frined_list_select(self):
        self.by_id_elements(self.friend_list)

