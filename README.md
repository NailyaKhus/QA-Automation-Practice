# Testing Tasks - QA Automation Practice                               
                                         
Here I've collected examples for automated testing.                             
                                                    
### 1_Pytest_DivisionFunction Folder - Testing Division Function Using  Pytest                                                       
                                             
In the [utils.py](https://github.com/NailyaKhus/QA-Automation-Practice/blob/main/1_Pytest_DivisionFunction/utils.py) file, you'll find division function itself.                                                         
In the [tests](https://github.com/NailyaKhus/QA-Automation-Practice/tree/main/1_Pytest_DivisionFunction/tests) folder, you'll find tests for the function using pytest's mark.parametrize decorator.                                                                                                         
                                                     
### 2_Pytest_File_Data_Testing Folder - Testing Text File's Content                                                       
                                               
In the [utils.py](https://github.com/NailyaKhus/QA-Automation-Practice/blob/main/2_Pytest_File_Data_Testing/utils.py) file, you'll find function for reading from file which is used in testing.                                                                          
                                                
In the **tests** folder, there are:                                  
                                     
[conftest.py](https://github.com/NailyaKhus/QA-Automation-Practice/blob/main/2_Pytest_File_Data_Testing/tests/conftest.py) - Contains text file cleaning function which uses pytest's fixture decorator.                                        
                                 
[test_file_workers.py](https://github.com/NailyaKhus/QA-Automation-Practice/blob/main/2_Pytest_File_Data_Testing/tests/test_file_workers.py) - Contains tests for reading from text file.                                      
                            
[testfile.txt](https://github.com/NailyaKhus/QA-Automation-Practice/blob/main/2_Pytest_File_Data_Testing/tests/testfile.txt) - Text file itself.                                                
                                         
                                 
### 3_SeleniumPytest_AmazonSite Folder - Testing Amazon Site With Selenium Pytest                                                       
                                                   
In the [utils.py](https://github.com/NailyaKhus/QA-Automation-Practice/blob/main/FirstSeleniumProject/utils.py) file, you'll find functions used in testing.                           
                             
In the **Test** folder, there are two Python files:                       
                                  
1. [Test_general_check_out.py](https://github.com/NailyaKhus/QA-Automation-Practice/blob/main/FirstSeleniumProject/Test/Test_general_check_out.py) - Contains tests for:                                      
- Loading the main page                                    
- Verifying the title of the main page is 'Amazon'                             
- Searching for an item and checking the title                              
- Checking the image of the found item                                         
- Saving the item's ID, adding it to the cartand, and verifying it's the only item in the cart                                     
- Verifying the ID of the item in the cart matches the added item's ID.                    
                                      
2. [Test_negative_testing.py](https://github.com/NailyaKhus/QA-Automation-Practice/blob/main/FirstSeleniumProject/Test/Test_negative_testing.py) Contains negative tests for signing in with:                                       
- Invalid emails                                     
- Invalid phone numbers.


