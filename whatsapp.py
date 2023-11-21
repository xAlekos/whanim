from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
from selenium.common.exceptions import NoSuchElementException
import time
import AsciiAnimsStructure


def initialize_web_driver(user_data=None, site="https://web.whatsapp.com/"):  # #Inizializza il web driver per chrome
    # aggiungendo opzionalmente gli user data mettendone il path, dopodichè apre il sito desiderato, ritorna una
    # reference al webdriver.
    if user_data is not None:
        options = webdriver.ChromeOptions()
        options.add_argument("user-data-dir=C:/Users/User/AppData/Local/Google/Chrome/User Data")
    else:
        options = None
    web_driver = webdriver.Chrome(options=options)
    web_driver.get(site)
    return web_driver


def trova_contatto(nome, web_driver):
    desired_contact = web_driver.find_element(by=By.XPATH, value="//span[@title='%s']" % nome)
    desired_contact.click()
    web_driver.implicitly_wait(0.5)
    return desired_contact


def trova_text_box(xpath):
    desired_text_box = driver.find_element(by=By.XPATH,
                                           value=xpath)
    return desired_text_box


def clear_textbox(textbox):
    textbox.send_keys(Keys.CONTROL + "a")
    textbox.send_keys(Keys.DELETE)


def invia_frame_animazione(target_text_box, animazione, frame, invia):
    for riga_ascii in animazione[frame]:
        target_text_box.send_keys(riga_ascii)
        target_text_box.send_keys(Keys.SHIFT + Keys.ENTER)
        time.sleep(0.1)
    if invia is True:
        target_text_box.send_keys(Keys.ENTER)


def trova_messaggi_whatsapp(web_driver=None, xpath="//div[@class='_21Ahp']"):
    messaggi_whatsapp = web_driver.find_elements(by=By.XPATH, value=xpath)
    return messaggi_whatsapp


def anima_messaggio(messaggio, animazione):
    frame = 1
    while True:
        time.sleep(0.05)
        frame = not frame
        hover = ActionChains(driver).move_to_element(messaggio)
        hover.perform()
        try:
            context_button = driver.find_element(by=By.XPATH, value="//span[@data-icon='down-context']")
            context_button.click()
            time.sleep(0.05)
            tasto_modifica = trova_text_box("//div[@aria-label='Modifica']")
            tasto_modifica.click()
            text_box_modifica = driver.find_element(by=By.XPATH,
                                                    value="//p[@class='selectable-text copyable-text iq0m558w g0rxnol2']")
        except NoSuchElementException:
            esci = ActionChains(driver).send_keys(Keys.ESCAPE)
            esci.perform()
            print("Elemento non faundato")
            continue
        text_box_modifica.click()
        time.sleep(0.05)
        clear_textbox(text_box_modifica)
        invia_frame_animazione(text_box_modifica, animazione, frame, False)
        time.sleep(0.05)
        tasto_invia_modifica = driver.find_element(by=By.XPATH, value="//span[@data-icon='checkmark-medium']")
        tasto_invia_modifica.click()
        time.sleep(0.05)


AnimList = AsciiAnimsStructure.createanimslist() ##TODO FAI SI' CHE STAMPI DA ASCIIANIMNSTRUCTUR A WHATSAPP DIO BELLO
AsciiAnimsStructure.loadfromfolder(AnimList)

driver = initialize_web_driver(user_data="user-data-dir=C:/Users/User/AppData/Local/Google/Chrome/User Data",
                               site="https://web.whatsapp.com/")
input()
contatto = trova_contatto("Nome contatto", driver)
text_box_chat = trova_text_box("/html"
                               "/body/div[1]/div/div/div[5]"
                               "/div/footer/div[1]/div/span[2]/div/div[2]/div[1]/div/div[1]/p")
invia_frame_animazione(text_box_chat, AnimList[1], 0, True)
driver.implicitly_wait(2)

messaggi = trova_messaggi_whatsapp(driver)
ultimo_messaggio = messaggi[-1]


anima_messaggio(ultimo_messaggio, AnimList[1])
