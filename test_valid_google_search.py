from selene import browser, be, have


def test_valid_google_search(open_browser):
    browser.open('https://google.com')
    browser.element('[name="q"]').should(be.blank).type('yashaka/selene').press_enter()
    browser.element('[id="search"]').should(have.text('yashaka/selene: User-oriented Web UI browser tests in Python'))


def test_invali_google_search(open_browser):
    browser.open('https://google.com')
    browser.element('[name="q"]').should(be.blank).type('jgkhgjkhgjhgjhghjgbjhgjhgbhjgh').press_enter()
    browser.element('[id="result-stats"]').should(have.text("Результатов: примерно 0"))