import selenium
import requests
import time
from selenium import webdriver
from selenium.webdriver.common.by import By

url = f'https://www.nikon.co.uk/api/v1/search/product/query?language=en-GB&pageSize=12&from=0&ProductCategoryList=131&ProductSubCategoryList=137&sort=newest'

response = requests.get(url)
items = response.json()["items"]
driver = webdriver.Chrome()
for i in items:
    # 'i' is an element in items (Its name is not a special thing)
    CameraLink = i["url"]
    CameraLink = "https://www.nikon.co.uk" + CameraLink
    driver.get(CameraLink)
    driver.implicitly_wait(10)
    n = 0

    # Cookie accept
    try:
        agree_cookie = driver.find_element(By.ID, "onetrust-accept-btn-handler")
        time.sleep(3)
        agree_cookie.click()
    except selenium.common.exceptions.NoSuchElementException:
        pass
    driver.implicitly_wait(10)

    # Click "Load More" button to load all information
    all_buttons = driver.find_elements(By.TAG_NAME, value="button")
    load_more_button = None
    for but in all_buttons:
        # print(but.text)
        if but.text == "Load More":
            load_more_button = but
    if load_more_button is None:
        print("Can't find load more button")
        exit()
    load_more_button.click()

    # get all information
    driver.implicitly_wait(0.5)
    spec_table = driver.find_element(By.ID, value="a-TechSpecs")
    specs = spec_table.find_elements(by=By.CLASS_NAME, value="col-span-4")
    camera_info = {}
    for spec in specs:
        try:
            key = str()
            value = str()
            tags = spec.find_elements(by=By.TAG_NAME, value="span")
            for tag in tags:
                if tag.get_attribute("class").find("h5") > -1:
                    key = tag.text
                elif tag.get_attribute("class").find("h6") > -1:
                    value = tag.text
            if len(key) > 0 and len(value) > 0:
                camera_info[key] = value
        except:
            print("WTF is this????")

    # control data format
    # 0 model
    name = str(CameraLink)
    name = name.split('/')
    print(name[6])
    # 1 CameraType
    print('Type:')
    print(camera_info['Type'])
    # 2 Image Sensor
    print('Image Sensor:')
    try:
        print(camera_info['Image Sensor'])
    except KeyError as e:
        print(camera_info['Image sensor'])
    # 3 Total pixels
    print('Total pixels:')
    print(camera_info['Total pixels'])
    # 4 Effective pixels
    print('Effective pixels:')
    print(camera_info['Effective pixels'])
    # 5 Image size (pixels)
    print('Image size (pixels):')
    print(camera_info['Image size (pixels)'])
    # 6 File formats (picture)
    print('File formats (picture):')
    try:
        print(camera_info['File formats'])
    except KeyError as e:
        print(camera_info['Storage file formats'])
    # 7 Frame size (pixels) and frame rate
    print('Frame size and frame rate (movie):')
    try:
        print(camera_info['Frame size (pixels) and frame rate'])
    except KeyError as e:
        print(camera_info['Movie - frame size (pixels) and frame rate'])
    # 8 Video File format
    print('File format (movie):')
    try:
        print(camera_info['Video File format'])
    except KeyError as e:
        print(camera_info['Movie - file format'])
    # 9 Frame advance Rate
    print('Shutter speed:')
    print(camera_info['Shutter speed'])
    # 10 ISO Sensitivity
    print('ISO:')
    try:
        print(camera_info['ISO sensitivity'])
    except KeyError as e:
        print(camera_info['ISO sensitivity (Recommended Exposure Index)'])
    # 11 Dimensions (W x H x D)
    print('Dimensions (W x H x D):')
    print(camera_info['Dimensions (W x H x D)'])
    # 12 Weight
    print('Weight:')
    print(camera_info['Weight'])
    # 13 price
