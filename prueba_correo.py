# -*- coding:utf-8 -*-
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import unittest


class TestMailPage(unittest.TestCase):
    
    """
    @classmethod
    def setUpClass(cls):
        cls.driver = webdriver.Firefox()
        #Abre la pagina solicitada
        cls.driver.get('https://www.gmail.com/')"""

    #Al iniciar la prueba
    def setUp(self):
        self.driver = webdriver.Firefox()
        #Abre la pagina solicitada
        self.driver.get('https://www.gmail.com/')

    """def test_prueba_titulo_de_google(self):
        self.assertEqual('Gmail', self.driver.title)"""
    
    def test_prueba_iniciar_sesion(self):
        buscar = self.driver.find_element_by_id('Email')
        buscar.send_keys('kiritobaz@gmail.com')
        boton_next = self.driver.find_element_by_id('next')
        boton_next.click()
        self.driver.implicitly_wait(2)
        buscar = self.driver.find_element_by_id('Passwd')
        buscar.send_keys('x')
        boton_next = self.driver.find_element_by_id('signIn')
        boton_next.click()
        self.driver.implicitly_wait(40)
        buscar = self.driver.find_element_by_class_name('yW')
        buscar.click()
        self.driver.implicitly_wait(20)
        buscar = self.driver.find_element_by_class_name('hP')
        assert buscar.text == (u'Nuevo acceso desde la aplicación Firefox en Linux')


    #Al terminar la prueba
    def tearDown(self):
        #se cierra el navegador
        self.driver.close()

if __name__ == '__main__':
    unittest.main()
