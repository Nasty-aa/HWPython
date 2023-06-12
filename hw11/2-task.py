# Авторизоваться на сайте https://fix-online.sbis.ru/
# Перейти в реестр Контакты
# Отправить сообщение самому себе
# Убедиться, что сообщение появилось в реестре
# Удалить это сообщение и убедиться, что удалили
# Для сдачи задания пришлите код и запись с экрана прохождения теста

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver import Keys, ActionChains
from time import sleep

driver = webdriver.Chrome()
driver.maximize_window()

try:
    user_login, user_password = 'Логин', 'Пароль123'
    fix = 'https://fix-online.sbis.ru/'

    # Переходим на fix
    driver.get(fix)
    assert driver.current_url == 'https://fix-sso.sbis.ru/auth-online/?ret=fix-online.sbis.ru/', 'Перешли не туда'
    sleep(2)

    # Вводим логин
    login = driver.find_element(By.CSS_SELECTOR, '[name="Login"]')
    login.send_keys(user_login, Keys.ENTER)
    assert login.get_attribute('value') == user_login, 'Введен не тот логин'

    # Вводим пароль
    login = driver.find_element(By.CSS_SELECTOR, '[name="Password"]')
    login.send_keys(user_password, Keys.ENTER)
    assert login.get_attribute('value') == user_password, 'Введен не тот пароль'
    sleep(7)

    # Переходим в контакты
    contacts = driver.find_element(By.CSS_SELECTOR, '[name="item-contacts"]')
    assert contacts.is_displayed(), 'Нет вкладки контакты'
    contacts.click()
    sleep(2)
    contacts_tab = driver.find_element(By.CSS_SELECTOR, 'a[href="/page/dialogs"]')
    assert contacts_tab.is_displayed(), 'Нет вкладки контакты'
    contacts_tab.click()
    sleep(5)

    # Нажимаем кнопку + (Добавить сообщение)
    button_add = driver.find_element(By.CSS_SELECTOR, '[data-name="sabyPage-addButton"]')
    assert button_add.is_displayed(), 'Нет кнопки добавить сообщение'
    button_add.click()
    sleep(3)

    # Ищем пользователя в списке
    find_user = driver.find_element(By.CSS_SELECTOR, '[name="ws-input_2023-06-12"]')
    sleep(2)
    assert find_user.is_displayed(), 'Поиск не отображается'
    find_user.send_keys('Печатная')
    sleep(2)

    # Выбираем пользователя из списка
    user_in_list = driver.find_element(By.CSS_SELECTOR, '[attr-data-qa="key-a8c053e8-1d41-4efe-b66b-bcf720116bf3"]')
    assert user_in_list.is_displayed(), 'Нет пользователя в списке'
    user_in_list.click()
    sleep(2)

    # Вставляем текст сообщения
    message = driver.find_element(By.CSS_SELECTOR, '[data-qa="textEditor_slate_Field"]')
    assert message.is_displayed(), 'Поле ввода не отображается'
    message.send_keys('Текст для автотеста удалить')
    sleep(2)

    # Отправляем сообщение
    button_send_message = driver.find_element(By.CSS_SELECTOR, '[data-qa="msg-send-editor__send-button"]')
    assert button_send_message.is_displayed(), 'Нет кнопки отправить'
    button_send_message.click()
    sleep(3)

    # Находим поиск и вводим наш текст
    search_message = driver.find_element(By.CSS_SELECTOR, '[name="ws-input_2023-06-12"]')
    assert search_message.is_displayed(), 'Нет поиска'
    search_message.send_keys('Текст для автотеста удалить')
    sleep(2)
    search_button = driver.find_element(By.CSS_SELECTOR, '.controls-Button__text_clickable_bg-same')
    assert search_button.is_displayed(), 'Нет кнопки найти'
    search_button.click()
    sleep(2)

    # Ищем наше не прочитанное сообщение
    message_item = driver.find_element(By.CSS_SELECTOR, '.msg-dialogs-item_unread')
    assert message_item.is_displayed(), 'Сообщение не отобржается'

    # Наводим на сообщение и удаляем его
    action_chains = ActionChains(driver)
    action_chains.move_to_element(message_item)
    action_chains.context_click(message_item)
    action_chains.perform()
    sleep(2)
    del_message = search_message = driver.find_element(By.CSS_SELECTOR, '[title="Перенести в удаленные"]')
    del_message.click()
    sleep(2)

    # Проверяем отображение заглушки
    hint_message = driver.find_element(By.CLASS_NAME, 'hint-Template-Wrapper__hint_emptyFilteredTemplate')
    assert hint_message.is_displayed(), 'Заглушка не отображается'

    # Еще раз инициируем поиск
    search_button = driver.find_element(By.CSS_SELECTOR, '[data-qa="Search__searchButton"]')
    assert search_button.is_displayed(), 'Лупа не отображается'
    search_button.click()
    sleep(2)

    # Проверяем отображение заглушки
    hint_message = driver.find_element(By.CLASS_NAME, 'hint-Template-Wrapper__hint_emptyFilteredTemplate')
    assert hint_message.is_displayed(), 'Заглушка не отображается'
finally:
    driver.quit()
