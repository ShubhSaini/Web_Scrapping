##### This function is used to scrap the images 

def  scrap_images_url(driver):
     #price=driver.find_elements_by_xpath("//img[@class='sb_1kFdf5oU']")
     img=driver.find_elements_by_xpath("//img[@class='s-image']")
     print(len(img))
     product_data={}

     product_data['image_urls']=[]
        
     for image in img:
         source=image.get_attribute('src')
         product_data["image_urls"].append(source)
     print("R S Data")

     return product_data
     

