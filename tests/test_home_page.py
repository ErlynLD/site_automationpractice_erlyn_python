from pages.ap_home_page import Home


def test_home_click_sign_in(browser):

    URL = "http://automationpractice.com/"
    browser.get(URL)

    HOME_PAGE = Home(browser)
    title = HOME_PAGE.click_on_sign_in_link()
    if title == "Login - My Store":
        pass
    else:
        assert 0
