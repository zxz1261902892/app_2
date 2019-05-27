import allure


class Test_002:

    def test_add_png(self):

        with open("/Users/mac/Desktop/sh-app8-day08/scripts/abc.png", "rb") as f:
            # 添加图片内容到测试报告，以附件的方式
            allure.attach("截图", f.read(), allure.attach_type.PNG)
