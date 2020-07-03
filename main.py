###### Importing Libraries neesed to scrap the images
from selenium import webdriver
from save_images import make_directory,save_images
from scrap_images import scrap_images_url
from selenium.common.exceptions import StaleElementReferenceException

######### Creating an instance of google chrome
Driver_path='D:\\Shubham Work\\Web_Scraping\\chromedriver.exe'
driver=webdriver.Chrome(executable_path=Driver_path)

###### Making 3 different urls for Shirts, T-Shirts and Saree####

currentpageurl=driver.get('https://www.amazon.in/s?k=shirts&rh=n%3A7459781031&ref=nb_sb_noss')
#currentpageurl=driver.get('https://www.amazon.in/s?k=saree&rh=n%3A7459780031&ref=nb_sb_noss')
#currentpageurl=driver.get('https://www.amazon.in/s?k=tshirt&rh=n%3A7459781031&ref=nb_sb_noss')

####### Making Directory name in which the images get saved #####

DIRNAME="Shirt"
#DIRNAME="Saree"
#DIRNAME="T-shirt"
make_directory(DIRNAME)

####### Defining how many pages needed to be scrap #####
start_page=1
total_pages=3

###### In here I am making a for loop which will scrap Amazon pages one by one #####
for page in range(start_page,total_pages):
    try:
        prod_details=scrap_images_url(driver=driver)
        print("Scrapping page {0} of {1} pages".format(page,total_pages))
        page_value=driver.find_element_by_xpath("//li[@class='a-selected']")
        print("The current page is {}".format(page_value))
        
        # Downloading the images
        save_images(data=prod_details,dirname=DIRNAME,page=page)
        print("Scrapping of page{0}Done!!".format(page))
        
        # Saving data into into a csv file
        # save_data_to_csv(data=prod_details,filename="men.csv")

        # Moving to the next page
        print("Moving to the next page")
        button_type= driver.find_element_by_xpath("//div[@class='a-text-center']//li[@class='a-last']//a").get_attribute("innerHTML")
        if button_type== "Next  →":
            driver.find_element_by_xpath("//li[@class='a-last']").click()
        else:
            driver.find_element_by_xpath("//li[@class='a-last']").click()

       # new_page=driver.find_element_by_xpath( "").text
       #  print("The new page is: {}".format(new_page))

    except StaleElementReferenceException as Exception:
        print("We are facing an exception")   
        exception_page=driver.find_element_by_xpath("//li[@class='a-selected']").text
        print("The page value at the time out exception is {}".format(exception_page))
        value= driver.find_element_by_xpath()
        link=value.get_attribute('href')
        driver.get(link)
        product_details=scrap_images_url(driver=driver)
        print("Scrapping Page{0} of {1} ".format(page,total_pages))

        page_value=driver.find_element_by_xpath("//li[@class='a-selected']").text()
        print("The current page scrapped is{}".format(page_value))

        # Downloading the images
        save_images(data=product_details,dirname=DIRNAME,page=page)
        print("Scrapping of page{0} done!!!".format(page))

        # Saving Date into csv file
        save_data_to_csv(data=product_details,filename="women.csv")

        # Moving to the next page
        print("Moving to the next page")
        button_type= driver.find_element_by_xpath("//div[@class='a-section a-spacing-none a-padding-base']//li[@class='a-last']//span").get_attribute("innerHTML")
        if button_type== "Next":
            driver.find_element_by_xpath("//li[@class='a-last']").click()
        else:
            driver.find_element_by_xpath("//li[@class='a-last']").click()

        new_page=driver.find_element_by_xpath("//li[@class='a-selected']").text()
        print("the new page is {}".format(new_page))








