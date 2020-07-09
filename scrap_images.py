##### This function is used to scrap the images 

def  scrap_images_url(driver):
     img=driver.find_elements_by_xpath("//div[@class='a-section aok-relative s-image-tall-aspect']//img")
     print("Total Images in this page: ",len(img))
     product_data={}

     product_data['image_urls']=[]
        
     for image in img:
         source=image.get_attribute('src')
         product_data["image_urls"].append(source)
     print("\nReturning Scrapped Data\n")

     return product_data
     

