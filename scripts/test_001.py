import allure, pytest

class Test_001:

    @pytest.allure.severity(pytest.allure.severity_level.BLOCKER)
    @allure.step(title="这是一个测试步骤01")
    def test_001_1(self):
        print("--->test_001_1")
        allure.attach("标题", "具体内容")
        assert True

    @pytest.allure.severity(pytest.allure.severity_level.CRITICAL)
    @allure.step(title="这是一个测试步骤02")
    def test_001_2(self):
        allure.attach("用户名", "张三")
        allure.attach("密码", "123456")
        print("--->test_001_2")
        assert True




