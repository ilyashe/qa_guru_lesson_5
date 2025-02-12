import os
from selene import browser, have, command


def test_complete_and_submit_form():
    browser.open('https://demoqa.com/automation-practice-form')
    browser.element('#firstName').type('Fedor')
    browser.element('#lastName').type('Bubnov')
    browser.element('#userEmail').type('fedor.bubnov_test@gmail.com')
    browser.element('#gender-radio-1').perform(command.js.click)
    browser.element('#userNumber').type('9990006666')

    browser.element('#dateOfBirthInput').perform(command.js.click)
    browser.element('.react-datepicker__month-select').perform(command.js.click).element('option[value="7"]').perform(command.js.click)
    browser.element('.react-datepicker__year-select').perform(command.js.click).element('option[value="1997"]').perform(command.js.click)
    browser.element('.react-datepicker__day--003').perform(command.js.click)

    browser.element('#subjectsInput').type('biology').press_enter()
    browser.element('#subjectsInput').type('chem').press_enter()

    browser.element('#hobbies-checkbox-1').perform(command.js.click)
    browser.element('#hobbies-checkbox-3').perform(command.js.click)

    browser.element('#uploadPicture').send_keys(os.path.abspath('images/mayk-vazovski-s-litsom-salli-8.jpg'))

    browser.element('#currentAddress').type('Sadovaya, 14')

    browser.element('#state').perform(command.js.scroll_into_view)
    browser.element('#state').click().all('div[id^="react-select-3-option"]').element_by(have.text('Haryana')).perform(command.js.click)
    browser.element('#city').click().all('div[id^="react-select-4-option"]').element_by(have.text('Karnal')).click()

    browser.element('#submit').perform(command.js.click)

    browser.element('.table').should(have.text('Fedor Bubnov'))
    browser.element('.table').should(have.text('fedor.bubnov_test@gmail.com'))
    browser.element('.table').should(have.text('Male'))
    browser.element('.table').should(have.text('9990006666'))
    browser.element('.table').should(have.text('03 February,2025'))
    browser.element('.table').should(have.text('Biology, Chemistry'))
    browser.element('.table').should(have.text('Sports, Music'))
    browser.element('.table').should(have.text('mayk-vazovski-s-litsom-salli-8.jpg'))
    browser.element('.table').should(have.text('Sadovaya, 14'))
    browser.element('.table').should(have.text('Haryana Karnal'))

    browser.quit()