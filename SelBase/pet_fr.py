from seleniumbase import BaseCase
import time
from settings import *


class MyTestClass(BaseCase):
    def test_1page(self):
        self.open("https://petfriends1.herokuapp.com/")
        self.highlight("/html/body/div/div/h1")
        self.assert_text("PetFriends", "h1")
        self.highlight("/html/body/nav/a")
        self.assert_link_text("PetFriends")
        self.highlight("/html/body/div/div/div[1]")
        self.assert_text("Социальная сеть для любителей животных")
        self.click('/html/body/div/div/div[2]/button') #зарегистрироваться

    def test_2page(self):
        self.open('http://petfriends1.herokuapp.com/new_user')
        self.highlight("/html/body/div/div/form/div[1]/label")
        self.assert_text("Уникальное имя")
        self.type('input[name="name"]', "User")
        self.highlight('//*[@id="NameHelp"]')
        self.assert_text("Введите уникальное имя пользователя")
        self.clear('input[name="name"]')

        self.highlight("/html/body/div/div/form/div[2]/label")
        self.assert_text("Электронная почта")
        self.type('input[name="email"]', "email")
        self.highlight('//*[@id="EmailHelp"]')
        self.assert_text("Введите адрес электронной почты")
        self.clear('input[name="email"]')

        self.highlight("/html/body/div/div/form/div[3]/label")
        self.assert_text("Пароль")
        self.type('input[name="pass"]', "pass")
        self.highlight('//*[@id="PassHelp"]')
        self.assert_text("Введите пароль")
        self.clear('input[name="pass"]')

        self.click_link("У меня уже есть аккаунт")
        self.type('input[name="email"]', email)
        self.type('input[name="pass"]', password)
        self.click('button[class="btn btn-success"]')
        time.sleep(3)

    def test_3page(self):
        self.open('http://petfriends1.herokuapp.com/new_user')
        self.click_link("У меня уже есть аккаунт")
        self.type('input[name="email"]', email)
        self.type('input[name="pass"]', password)
        self.click('button[class="btn btn-success"]')

        self.highlight('//*[@id="navbarNav"]/ul/li[1]/a')
        self.assert_link_text("Мои питомцы")
        self.highlight('//*[@id="navbarNav"]/ul/li[2]/a')
        self.assert_link_text("Все питомцы")
        self.highlight('//html/body/div/div/div[1]')
        self.assert_text("Все питомцы наших пользователей")
        self.highlight('//html/body/div/div/h1')
        self.assert_text("PetFriends", "h1")

        self.highlight('//html/body/nav/div[2]/button')
        self.assert_text("Выйти")



    def test_4page(self):
        self.open('http://petfriends1.herokuapp.com/new_user')
        self.click_link("У меня уже есть аккаунт")
        self.type('input[name="email"]', email)
        self.type('input[name="pass"]', password)
        self.click('button[class="btn btn-success"]')
        self.open('http://petfriends1.herokuapp.com/my_pets')

        self.highlight("h2")
        self.highlight('/html/body/div[1]/div/div[1]')
        self.assert_text("Питомцев:")
        self.assert_text("Друзей:")
        self.assert_text("Сообщений:")

        self.highlight('//*[@id="all_my_pets"]/table/thead/tr/th[1]')
        self.assert_text("Фото")
        self.highlight('//*[@id="all_my_pets"]/table/thead/tr/th[2]')
        self.assert_text("Имя")
        self.highlight('//*[@id="all_my_pets"]/table/thead/tr/th[3]')
        self.assert_text("Порода")
        self.highlight('//*[@id="all_my_pets"]/table/thead/tr/th[4]')
        self.assert_text("Возраст")
        self.highlight('/html/body/div[1]/div/div[2]/div/button')
        self.assert_text("Добавить питомца")
        self.click('/html/body/div[1]/div/div[2]/div/button')

        self.highlight('//*[@id="addPetsModalLabel"]')
        self.assert_text("Новый питомец")
        self.highlight('//*[@id="addPetsModal"]/div/div/div[1]/button/span')
        self.highlight('// *[ @ id = "pet_photo"]')


        #self.assert_element('img[name="photo"]')

        self.highlight('//*[@id="addPetsModal"]/div/div/div[2]/form/div[2]/label')
        self.assert_text("Имя питомца")
        self.type('//*[@id="name"]', 'pet_name')

        self.highlight('//*[@id="addPetsModal"]/div/div/div[2]/form/div[3]/label')
        self.assert_text("Порода")
        self.type('//*[@id="animal_type"]', 'wild animal')

        self.highlight('//*[@id="addPetsModal"]/div/div/div[2]/form/div[4]/label')
        self.assert_text("Возраст, лет")
        self.type('//*[@id="age"]', '11')


        self.clear('input[name="name"]')
        self.clear('input[name="animal_type"]')
        self.clear('input[name="age"]')

        self.highlight('//*[@id="addPetsModal"]/div/div/div[3]/button[1]')
        self.assert_text("Отмена")

        self.highlight('//*[@id="addPetsModal"]/div/div/div[3]/button[2]')
        self.assert_text("Добавить")

        self.click('//*[@id="addPetsModal"]/div/div/div[3]/button[1]')

        time.sleep(3)





