### I have changed the locator tags for security purposes. However it won't be difficult for the viewers to understand what's going on!


import time
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
def remove_html_tags(text): #for clearing HTML tags in the paragraph.
    """Remove html tags from a string"""
    import re
    clean = re.compile('<.*?>')
    return re.sub(clean, '', text)
def findnth(string, substring, n):
    parts = string.split(substring, n + 1)
    if len(parts) <= n + 1:
        return -1
    return len(string) - len(parts[-1]) - len(substring)

def grabber(inp):

    url = "URL"+str(inp) #can't disclose the target site. Baby!!
    chrome_driver_path = '/Users/mahmud/Desktop/demopython/selenium_project/chromedriver'
    driver = webdriver.Firefox()
    driver.get(url)
    html=driver.page_source



    time.sleep(10)

    #Job Title Start
    title_start = html.find('<span data-automation="afd-sdfa-title" class="3hjhhaf3FshsVCSTjhdjhksad"><span class=""><h1>')+94
    x=html[title_start:]
    title_end=x.find('</h1>')
    Job_Name=x[:title_end]
    print(Job_Name)
    #Job Title End


    #Company Name Start
    a=html.find('<section aria-labelledby="HeaderBaby">')
    b=html[a:].find('<h2><span class="y2HaLtB">')
    c=html[a+b:].find('<span data-automation="dfgsf4-title" class="_j382y5@)-_42322134"><span class="">')
    d=html[a+b+c:].find('<span class="">')
    e=html[a+b+c+d:].find('>')
    f=html[a+b+c+d+e+1:]
    g=f.find('</span>')
    Company_Name=f[:g]
    print(Company_Name)

    #Company Name End


    #Job Description Start
    a=html.find('<div data-automation="IamInevitable" class="_2e4Pi2B">')
    b=html[a:].find('>')
    c=html[a+b+1:]
    d=c.find('</div>')
    c=c[:d]
    Job_Description=remove_html_tags(c)
    print(Job_Description)
    #Job Description End


    #Job Location Start
    a=html.find('<span class="232jkl+hjk_2jkldjhkl"><span class=""><strong class="2342sdIwjk">')
    b=html[a:]
    c=findnth(b,'>',2)
    d=b[c+1:]
    e=d.find('<')
    Job_Location=d[:e]
    print(Job_Location)
    #Job Location End


    #Industry Start
    a=findnth(html,'<span class="sdfa3)_#235hjkhanchjkl"><span class=""><strong class="sadgkl23@#@">',3)
    a=html[a:]
    b=findnth(a,'>',2)
    c=a[b+1:]
    d=c.find('</')
    Industry_Name=c[:d]
    print(Industry_Name)
    #Industry End

    #Parttime/Fulltime/Contract Start Job Type Start
    a=html.find('<dd data-automation="235iouioajkdsjkl"><span class="wt29028395009jjkdl;jkl;"><span class="345345235">')
    a=html[a:]
    b=findnth(a,'>',2)
    c=a[b+1:]
    d=c.find('</')
    Job_Type=c[:d]
    print(Job_Type)
    #Job Type End


    #-Salary Start
    b=html.find('<span class="lsjkdfgl;jkl;ldlkke;l">')
    a=html[b:]
    b=a.find('>')
    a=a[b+1:]
    b=a.find('<')
    Salary=a[:b]
    print(Salary)
    #Salary End

    driver.close()

grabber(50437405)### I have changed the locator tags for security purposes. However it won't be difficult for the viewers to understand what's going on!


import time
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
def remove_html_tags(text): #for clearing HTML tags in the paragraph.
    """Remove html tags from a string"""
    import re
    clean = re.compile('<.*?>')
    return re.sub(clean, '', text)
def findnth(string, substring, n):
    parts = string.split(substring, n + 1)
    if len(parts) <= n + 1:
        return -1
    return len(string) - len(parts[-1]) - len(substring)

def grabber(inp):

    url = "URL"+str(inp) #can't disclose the target site. Baby!!
    chrome_driver_path = '/Users/mahmud/Desktop/demopython/selenium_project/chromedriver'
    driver = webdriver.Firefox()
    driver.get(url)
    html=driver.page_source



    time.sleep(10)

    #Job Title Start
    title_start = html.find('<span data-automation="afd-sdfa-title" class="3hjhhaf3FshsVCSTjhdjhksad"><span class=""><h1>')+94
    x=html[title_start:]
    title_end=x.find('</h1>')
    Job_Name=x[:title_end]
    print(Job_Name)
    #Job Title End


    #Company Name Start
    a=html.find('<section aria-labelledby="HeaderBaby">')
    b=html[a:].find('<h2><span class="y2HaLtB">')
    c=html[a+b:].find('<span data-automation="dfgsf4-title" class="_j382y5@)-_42322134"><span class="">')
    d=html[a+b+c:].find('<span class="">')
    e=html[a+b+c+d:].find('>')
    f=html[a+b+c+d+e+1:]
    g=f.find('</span>')
    Company_Name=f[:g]
    print(Company_Name)

    #Company Name End


    #Job Description Start
    a=html.find('<div data-automation="IamInevitable" class="_2e4Pi2B">')
    b=html[a:].find('>')
    c=html[a+b+1:]
    d=c.find('</div>')
    c=c[:d]
    Job_Description=remove_html_tags(c)
    print(Job_Description)
    #Job Description End


    #Job Location Start
    a=html.find('<span class="232jkl+hjk_2jkldjhkl"><span class=""><strong class="2342sdIwjk">')
    b=html[a:]
    c=findnth(b,'>',2)
    d=b[c+1:]
    e=d.find('<')
    Job_Location=d[:e]
    print(Job_Location)
    #Job Location End


    #Industry Start
    a=findnth(html,'<span class="sdfa3)_#235hjkhanchjkl"><span class=""><strong class="sadgkl23@#@">',3)
    a=html[a:]
    b=findnth(a,'>',2)
    c=a[b+1:]
    d=c.find('</')
    Industry_Name=c[:d]
    print(Industry_Name)
    #Industry End

    #Parttime/Fulltime/Contract Start Job Type Start
    a=html.find('<dd data-automation="235iouioajkdsjkl"><span class="wt29028395009jjkdl;jkl;"><span class="345345235">')
    a=html[a:]
    b=findnth(a,'>',2)
    c=a[b+1:]
    d=c.find('</')
    Job_Type=c[:d]
    print(Job_Type)
    #Job Type End


    #-Salary Start
    b=html.find('<span class="lsjkdfgl;jkl;ldlkke;l">')
    a=html[b:]
    b=a.find('>')
    a=a[b+1:]
    b=a.find('<')
    Salary=a[:b]
    print(Salary)
    #Salary End

    driver.close()

grabber(50437405)
