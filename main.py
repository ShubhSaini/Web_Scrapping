###### Importing Libraries needed to scrap the images
from selenium import webdriver
from save_images import make_directory,save_images_shirt,save_images_saree,save_images_tshirt
from scrap_images import scrap_images_url
from selenium.common.exceptions import StaleElementReferenceException

######### Creating an instance of google chrome
Driver_path='D:\\Shubham Work\\Web_Scraping\\chromedriver.exe'
driver=webdriver.Chrome(executable_path=Driver_path)

###### Making 3 different urls for Shirts, T-Shirts and Saree####

url={"Shirt": "https://www.amazon.in/s?k=shirts&rh=n%3A7459781031&ref=nb_sb_noss",
     "Saree": "https://www.amazon.in/s?k=saree&rh=n%3A7459780031&ref=nb_sb_noss",
     "Tshirt": "https://www.amazon.in/s?k=tshirt&rh=n%3A7459781031&ref=nb_sb_noss"
     }
####### Making Directory name in which the images get saved #####

Dir=["Shirts","Saree","Tshirts"]

####### Defining how many pages needed to be scrap #####
start_page=1
total_pages=4

###### In here I am making a for loop which will scrap Amazon pages one by one #####
### This for loop will iterate for each url category

for currenturl in url.values():
    #### Defining conditions for directory so that different categories images goes to respective directory
    if currenturl=="https://www.amazon.in/s?k=shirts&rh=n%3A7459781031&ref=nb_sb_noss":
        DIRNAME=Dir[0]
    elif currenturl=="https://www.amazon.in/s?k=saree&rh=n%3A7459780031&ref=nb_sb_noss":
        DIRNAME=Dir[1]
    elif currenturl=="https://www.amazon.in/s?k=tshirt&rh=n%3A7459781031&ref=nb_sb_noss":
        DIRNAME=Dir[2]
    print("Scrapping Data for {} ".format(DIRNAME))

    ### making directory
    make_directory(DIRNAME)

    ### Defining url where browser have to go for image scrapping
    currentpageurl=driver.get(currenturl)
    
    #### This for loop will iterate between the pages for each url category
    for page in range(start_page,total_pages):
        try:
            driver.implicitly_wait(30) #### So I am adding this as after 2 pages the code was throwing an exception of no element found###
            page_value=driver.find_element_by_xpath("//li[@class='a-selected']")
            print("The current page is: {}".format(page))
            prod_details=scrap_images_url(driver=driver)
            print("Scrapping {0} of {1} pages\n".format(page,total_pages))

            # Downloading the images for each category
            if currenturl=="https://www.amazon.in/s?k=shirts&rh=n%3A7459781031&ref=nb_sb_noss":
                save_images_shirt(data=prod_details, dirname=DIRNAME,page=page)
                print("Scrapping of page {0} Completed!!\n".format(page))
            elif currenturl=="https://www.amazon.in/s?k=saree&rh=n%3A7459780031&ref=nb_sb_noss":
                save_images_saree(data=prod_details, dirname=DIRNAME,page=page)
                print("Scrapping of page {0} Completed!!\n".format(page))
            elif currenturl=="https://www.amazon.in/s?k=tshirt&rh=n%3A7459781031&ref=nb_sb_noss":
                save_images_tshirt(data=prod_details, dirname=DIRNAME,page=page)
                print("Scrapping of page {0} Completed!!\n".format(page))

            # Moving to the next page
            print("Moving to the next page....\n")
            button_type= driver.find_element_by_xpath("//div[@class='a-text-center']//li[@class='a-last']//a").get_attribute("innerHTML")
            if button_type== "Next  →":
                driver.find_element_by_xpath("//li[@class='a-last']").click()
            else:
                driver.find_element_by_xpath("//li[@class='a-last']").click()


        except StaleElementReferenceException as Exception:
            print("We are facing an exception ")   
            exception_page=driver.find_element_by_xpath("//li[@class='a-selected']").text
            print("The page value at the time out exception is {}\n".format(exception_page))
            value= driver.find_element_by_xpath()
            link=value.get_attribute('href')
            driver.get(link)
            product_details=scrap_images_url(driver=driver)
            print("Scrapping Page{0} of {1} ".format(page,total_pages))

            page_value=driver.find_element_by_xpath("//li[@class='a-selected']").text()
            print("The current page scrapped is {}\n".format(page_value))

            # Downloading the images
            save_images(data=product_details,dirname=DIRNAME,page=page)
            print("Scrapping of page{0} Completed!!!\n".format(page))

            # Saving Date into csv file
            save_data_to_csv(data=product_details,filename="women.csv")

            # Moving to the next page
            print("Moving to the next page\n")
            button_type= driver.find_element_by_xpath("//div[@class='a-text-center']//li[@class='a-last']//a").get_attribute("innerHTML")
            if button_type== "Next":
                driver.find_element_by_xpath("//li[@class='a-last']").click()
            else:
                driver.find_element_by_xpath("//li[@class='a-last']").click()

            new_page=driver.find_element_by_xpath("//li[@class='a-selected']").text()
            print("the new page is {}".format(new_page))




