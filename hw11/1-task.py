# Перейти на https://sbis.ru/
# Перейти в раздел "Контакты"
# Найти баннер Тензор, кликнуть по нему
# Перейти на https://tensor.ru/
# Проверить, что есть блок новости "Сила в людях"
# Перейдите в этом блоке в "Подробнее" и убедитесь, что открывается https://tensor.ru/about
# Для сдачи задания пришлите код и запись с экрана прохождения теста


from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep

driver = webdriver.Chrome()
driver.maximize_window()

try:
    tensor = 'https://tensor.ru/'
    sbis = 'https://sbis.ru/'
    # Переходим на сайт 'https://sbis.ru/' и проверяем куда пришли
    driver.get(sbis)
    assert driver.current_url == sbis, 'Не верная ссылка'
    sleep(2)
    # Ищем кнопку контакты и нажимаем (переходим по ссылке)
    contacts = driver.find_element(By.CSS_SELECTOR, '.sbisru-Header__menu-item> a[href="/contacts"]')
    assert contacts.is_displayed(), 'Кнопка контакты не отображается'
    contacts.click()
    sleep(2)
    # Ищем баннер Тензор и переходим по ссылке
    tensor_href = driver.find_elements(By.CLASS_NAME, 'sbisru-Contacts__border-left> a[href="https://tensor.ru/"]')
    assert tensor_href[0].is_displayed(), 'Баннер не отображается'
    tensor_href[0].click()
    sleep(2)
    # Переходим на новую вкладку
    handles = driver.window_handles
    driver.switch_to.window(handles[1])
    # Проверяем куда пришли
    assert driver.current_url == tensor, 'Не верная ссылка'
    # Ищем баннер "Сила в людях"
    blocknews = driver.find_element(By.CSS_SELECTOR, '.tensor_ru-Index__block4-content .tensor_ru-Index__card-title')
    assert blocknews.is_displayed(), 'Баннер "Сила в людях" не отображается'
    driver.execute_script("return arguments[0].scrollIntoView(true);", blocknews)
    sleep(2)
    # Ищем кнопку подробнее и переходим по ссылке
    about = driver.find_element(By.CSS_SELECTOR, '.tensor_ru-Index__card-text> a[href="/about"]')
    assert about.is_displayed(), 'Кнопка подробнее не отображается'
    about.click()
    sleep(2)
    assert driver.current_url == 'https://tensor.ru/about', 'Не верная ссылка'

finally:
    driver.quit()
