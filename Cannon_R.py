import time
from selenium import webdriver
from selenium.webdriver.common.by import By

# 1 get all links about Camera
CameraType = ['eos-r8', 'eos-r50', 'eos-r100', 'eos-r6-mark-ii', 'eos-r3', 'eos-r5', 'eos-r7', 'eos-r10', 'eos-rp']
count = len(CameraType)
type_count = 0
for i in range(count):
    a = 'https://www.canon.co.uk/cameras/'
    b = CameraType[i]
    c = '/specifications/'
    CameraLink = a + b + c
    i = i + 1
    print("======================================")
    print(b)
    print("======================================")
    driver = webdriver.Chrome()
    driver.get(CameraLink)
    # cookie
    time.sleep(1)
    agree_cookie = driver.find_element(By.ID, value="_evidon-accept-button")
    agree_cookie.click()
    # get all information
    metal = driver.find_element(By.XPATH, value='/html/body/section[2]/div/div')
    camera_info = {}
    # get all small table
    uls = metal.find_elements(By.TAG_NAME, value='ul')
    # join every small table
    for ul in uls:
        lis = ul.find_elements(By.TAG_NAME, value="li")
        for li in lis:
            # print(li.text)
            try:
                key = str()
                value = str()
                tags = li.find_elements(By.TAG_NAME, value='div')
                for tag in tags:
                    if tag.get_attribute("class").find("key") > -1:
                        key = tag.text
                    elif tag.get_attribute("class").find("value") > -1:
                        value = tag.text
                if len(key) > 0 and len(value) > 0:
                    if key == "Type":
                        key = key + str(type_count)
                        type_count = type_count + 1
                    camera_info[key] = value
            except:
                print("not find the information")
    type_count = 0
    # print useful information
    # 1 CameraType
    print('Type:')
    print('Mirrorless')
    # 2 Image Sensor
    print('Image Sensor:')
    print(camera_info['Type0'])
    # 3 Total pixels
    print('Total pixels:')
    print(camera_info['Total Pixels'])
    # 4 Effective pixels
    print('Effective pixels:')
    print(camera_info['Effective Pixels'])
    # 5 Image size (pixels)
    print('Image size (pixels):')
    print(camera_info['Image Size'])
    # 6 File formats (picture)
    print('File formats (picture):')
    print(camera_info['Still Image Type'])
    # 7 Frame size (pixels) and frame rate
    print('Frame size and frame rate (movie):')
    print(camera_info['Movie Size'])
    # 8 Video File format
    print('File format (movie):')
    print(camera_info['Movie Type'])
    # # 9 Frame advance Rate
    print('Shutter speed:')
    try:
        print(camera_info['Speed'])
    except KeyError as e:
        print(camera_info['null'])
    # # 10 ISO Sensitivity
    print('ISO:')
    try:
        print(camera_info['ISO Sensitivity\nOpen'])
    except:
        print(camera_info['ISO'])
    # 11 Dimensions (W x H x D)
    print('Dimensions (W x H x D):')
    print(camera_info['Dimensions (W x H x D)'])
    print(camera_info['Dimensions (W x H x D)'])
    # 12 Weight
    print('Weight:')
    print(camera_info['Weight (Body Only)'])
    # 13 price

    print("======================================")
