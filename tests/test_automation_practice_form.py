import os
import tests
from selene import browser, have, command


def test_complete_and_submit_form():
    browser.open('/automation-practice-form')

    browser.driver.execute_script("$('#fixedban').remove()")
    browser.driver.execute_script("$('footer').remove()")
    # browser.driver.execute_script("document.body.style.zoom = '0.5'")

    # WHEN
    browser.element('#firstName').type('Fedor')
    browser.element('#lastName').type('Bubnov')
    browser.element('#userEmail').type('fedor.bubnov_test@gmail.com')
    browser.element('[name=gender][value=Male]').perform(command.js.click)
    browser.element('#userNumber').type('9990006666')

    browser.element('#dateOfBirthInput').click()
    browser.element('.react-datepicker__month-select').click().all('option').element_by(have.text('July')).click()
    browser.element('.react-datepicker__year-select').click().all('option').element_by(have.text('1997')).click()
    browser.element(f'.react-datepicker__day--0{'03'}').click()

    browser.element('#subjectsInput').type('biology').press_enter()
    browser.element('#subjectsInput').type('chem').press_enter()
    browser.all('[for^=hobbies-checkbox]').element_by(have.text('Sports')).click()
    browser.all('[for^=hobbies-checkbox]').element_by(have.text('Music')).click()

    browser.element('#uploadPicture').set_value(
        os.path.abspath(
            os.path.join(os.path.dirname(tests.__file__), '../images/mayk-vazovski-s-litsom-salli-8.jpg')
        )
    )

    browser.element('#currentAddress').type('Sadovaya, 14')
    browser.element('#state').click().all('[id^=react-select-3-option]').element_by(have.text('Haryana')).click()
    browser.element('#city').click().all('[id^=react-select-4-option]').element_by(have.text('Karnal')).click()

    browser.element('#submit').click()

    #THEN
    browser.element('.table').all('td').even.should(
        have.exact_texts(
            'Fedor Bubnov',
            'fedor.bubnov_test@gmail.com',
            'Male',
            '9990006666',
            '03 July,1997',
            'Biology, Chemistry',
            'Sports, Music',
            'mayk-vazovski-s-litsom-salli-8.jpg',
            'Sadovaya, 14',
            'Haryana Karnal',
        )
    )
