from demoqa_tests.model.pages import practice_form


def test_student_registration_form():
    practice_form.given_opened('https://demoqa.com/automation-practice-form')
    practice_form.type_firstname('Test')
    practice_form.type_lastname('Test')
    practice_form.type_email('Test@mail.com')
    practice_form.select_gender('Male')
    practice_form.type_phone_number('1111111111')
    practice_form.click_on_datepicker()
    practice_form.pick_month('May')
    practice_form.pick_year('1992')
    practice_form.pick_day('09')
    practice_form.type_subject('English')
    practice_form.select_hobby('Sports')
    practice_form.scroll_to_address()
    practice_form.type_address('test address')
    practice_form.upload_picture('resources/img.png')
    practice_form.select_state('NCR')
    practice_form.select_city('Delhi')
    practice_form.submit()

    practice_form.assert_fields(
            'Test Test',
            'Test@mail.com',
            'Male',
            '1111111111',
            '09 May,1992',
            'English',
            'Sports',
            'img.png',
            'test address',
            'NCR Delhi'
    )
