from datetime import date

from demoqa_tests.model.pages.practice_form import PracticePage
from demoqa_tests.model.data.student import Student, Hobby

practice_form = PracticePage()


def test_registration():
    student = Student(
        first_name='Kirill',
        last_name='Kozhevnikov',
        email='test@g.ru',
        phone='8123456789',
        address='Moscow',
        birthday=date(1990, 10, 5),
        gender='Male',
        subject='Chemistry',
        hobby=[Hobby.Music, Hobby.Sports],
        image='img.jpg',
        state='NCR',
        city='Delhi')

    practice_form.open()
    practice_form.fill(student).submit()
    practice_form.assert_results_registration(student)
