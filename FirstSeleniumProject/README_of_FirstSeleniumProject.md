### Testing Amazon site with Selenium Pytest
                                
Here is an option for automatically testing a site using the Chrome browser.                                                       
                                                   
[utils.py](https://github.com/NailyaKhus/QA-Automation-Practice/blob/main/FirstSeleniumProject/utils.py) - this file contains functions which are used in testing                           
                             
In the **Test** folder you can find two python files.                       
                                  
The first is [Test_general_check_out.py](https://github.com/NailyaKhus/QA-Automation-Practice/blob/main/FirstSeleniumProject/Test/Test_general_check_out.py) which contains the following tests:                                      
- The main page is loded                                    
- The label of the title of the main page is 'Amazon'                             
- Searching the item and checking that the found item has the word from the request in the title                              
- Image of the found item is callable                                         
- Saving the item's id and pressing to the 'Add to Cart' button and Checking that there is the only item in the Cart                                     
- The id of the item in the Cart is equal to the added item's id.                    
                                      
The second is [Test_negative_testing.py](https://github.com/NailyaKhus/QA-Automation-Practice/blob/main/FirstSeleniumProject/Test/Test_negative_testing.py) which contains the negative testing of signing-in:                                       
- Through fail emails                                     
- Through fail phone numbers.


