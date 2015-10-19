from selenium import webdriver
#para manejar las teclas, cursores, flechas, retorno
from selenium.webdriver.common.keys import Keys
import unittest


class TestGooglePage(unittest.TestCase):
    
    @classmethod
    def setUpClass(cls):
        cls.driver = webdriver.Firefox()
        cls.driver.get('https://www.google.com.mx/')

    #Al iniciar la prueba
    """def setUp(self):
        self.driver = webdriver.Firefox()
        #Abre la pagina solicitada
        self.driver.get('https://www.google.com.mx/')"""

    def test_prueba_titulo_de_google(self):
        self.assertEqual('Google', self.driver.title)

    def test_prueba_buscar_un_termino_ingenieria_software(self):
        buscar = self.driver.find_element_by_class_name('gsfi')
        buscar.send_keys('ingenieria de software')
        #para simular que se dio un "Enter"
        buscar.send_keys(Keys.RETURN)

        #self.assertIn('ingenieria de software', self.driver.title)
        elementos = self.driver.find_elements_by_class_name('r')
        self.assertFalse(len(elementos),0)

        #buscar un boton y dar click en el
        #boton = self.driver.find_element_by_name('btnK')
        #boton.click()

    #Al terminar la prueba
    def tearDown(self):
        #se cierra el navegador
        self.driver.close()

if __name__ == '__main__':
    unittest.main()
