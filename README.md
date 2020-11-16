# facebook login automation

This repository is a basic automation of a faceook login

“Selenium automates browsers. That’s it! What you do with that power is entirely up to you. Primarily it is for automating web applications for testing purposes but is certainly not limited to just that” — from selenium website.

We can use selenium in many languages like Java and Python. Here, we will use selenium to Automate Facebook Login Using Python.

## There are 3 requirements

1. Create your env

2. install Selenium in your env, go to terminal and type,

pip install selenium

3. Optional: Intall PyLint

pip install pylint

## 2. ChromeDriver— to download chromedriver, click here.
ChromeDriver or any other browser’s driver like firefox also needs to be downloaded by us because when we want to automate something with selenium, these drivers are necessary, without them, we can not open any browser, and if we can not open a browser then we can not automate anything, Right!

Before you download the chromedriver, keep in mind that the version of the chromedriver you are downloading should match with the version of the Chrome Browser which is installed in your system.

To check the version of your Chrome Browser, follow the given steps–

1. Open your Chrome Browser

2. Click on three dots available at the top-right position of the Browser.


## 3. Then click on “Help” and then finally click on “About Google Chrome”.

## 4. Then you will see the installed version of Chrome installed on your system.

You should check your Chrome Browser’s version and download it as shown here.

Now, we are all setup to Automate Facebook Login Using Python or anyother things you want to automate with Python.

So, let’s code for “the automate facebook login using Python“.

First, import webdrivers from selenium as follows–

from selenium import webdriver
Now, import Keys–

from selenium.webdriver.common.keys import Keys
Now, import time module–

import time
After all imports, we will indicate the user that the program has started–

print("test case started")
Now we will open our Chrome Browser as follows–

driver = webdriver.Chrome()
Here, inside the Chrome(), you need to give the path of the chromedriver which you have installed, or you can just copy and paste the chromedriver in the same folder/directory where this program(you are coding in) exists and leave the Chrome() as it is.

If you want to maximize the windows automatically, then type–

driver.maximize_window()
As we have opened the Chrome Browser, now we need to open the facebook login page, so to open any url, we just need to write–

driver.get("url")
We need to open the facebook login page, so we will type–

driver.get("https://www.facebook.com")
After this, the login page will get opened automatically.

So, now we need to enter the login creditionals i.e. email-id and password Right! and after that we need to click on the “Log In” button. Also, we want all this to be done automatically.

Here comes the basic HTML part in role i.e. if you know the basics of HTML then it will be a benefit for you to automate Facebook login using Python.

If not, let me do this for you, selenium uses HTML elements to define blocks of different types like paragraph, headings, horizontal line, and many more like this. To know more detailed information about HTML elements, click here.

Every HTML elements have some attributes. An attribute is used to define the characteristics of an HTML element and is placed inside the element’s opening tag.

We use HTML attributes to target the elements for example, to enter email-id inside “email id” block on the facebook login page, we need it one of the available attributes like name, id, class, etc.

If we get the attribute of that element, we can pass values to that element accordingly and if the element is a button, then also we can use its attribute to click on that button.

In selenium with python, we have many ways to reach any element by using the following attributes–

find_element_by_xpath
find_element_by_class_name
find_element_by_id
find_element_by_name
find_element_by_link_text
find_element_by_css_selector
And many more.

Now, you will be wondering, how to get those attributes or the other things?

This is very simple, go to the Facebook login page, right-click on the page anywhere, and then click on the “Inspect” available at the bottom.

Then, you will see an icon available which contains the arrow same as your mouse arrow on your screen, in the newly opened box, just click on that icon.

Now, on the right side, you can see the available attributes of that “email” block and use them in your automation program.

In the same way, you can get any element’s attribute.

In this program, we will use XPath which is considered best for these types of uses. To get the XPath of any element, simply right click on that elements highlighted part in the inspect element, then take your mouse to “copy” and then click on “Copy XPath”.

Now, to fill that email-id block we need to type–

driver.find_element_by_xpath('XPath_you_copied').send_keys("email-id here")
In the same way, we can fill the “password” block–

driver.find_element_by_xpath('XPath_you_copied').send_keys("password here")
Now, as we have entered the correct details, we need to click on the “Log In” button. For this we need to type–

driver.find_element_by_xpath('XPath_you_copied').send_keys(Keys.ENTER)
Now, we will close the browser using–

driver.close()

## Congratulation, you have successfully completed all the steps to Automate Facebook Login Using Python.


