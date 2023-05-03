
from requests import Session
from bs4 import BeautifulSoup as bs
import sys

def in365(day,month,year,hrs,mins,AMorPM):
    ans=0
    M = ['January','February','March','April','May','June','July','August','September','October','November','December']
    for i in range(0,len(M)):
        if(M[i]==month):
            ans = i*10000+year*1000000+day*100
    if(AMorPM == 'AM'):
        if(hrs == 12):
            hrs=0
        ans=ans+hrs+mins*0.01
    elif(AMorPM == 'PM'):
        ans=ans+12+hrs+mins*0.01
    return ans

TA = sys.argv[3]
f = open("announcements.txt", "w")
with Session() as s:
    site = s.get("https://moodle.iitb.ac.in/login/index.php")
    bs_content = bs(site.content, "html5lib")
    token = bs_content.find("input", {"name":"logintoken"})["value"]
    data = {
    'anchor': '',
    'logintoken': token,
    'username': sys.argv[1],
    'password': sys.argv[2],
    'rememberusername': '1',
    }
    s.post("https://moodle.iitb.ac.in/login/index.php",data)
    home_page = s.get("https://moodle.iitb.ac.in/my/")
    soup=bs(home_page.content,'html5lib')
    s1 = soup.find_all('div',id="nav-drawer")
    for i in s1[0].find_all('a'):
        if i.decode_contents(formatter='html').find('CS 251-2022-1')!=-1:
            link = i['href']
    course_page = s.get(link)
    soup1=bs(course_page.content,'html5lib')
    announc = [i['href'] for i in soup1.find_all('a',class_='aalink' , href=True)]
    announcements = s.get(announc[0])
    soup2 = bs(announcements.content,'html5lib')
    All_announc = [i['href'] for i in soup2.find_all('a',class_='w-100 h-100 d-block' , href=True)]
    l=[]
    for href in reversed(All_announc):
        Thread = s.get(href)
        soup_final = bs(Thread.content,'html5lib')
        div = soup_final.find_all('div',class_='mb-3',tabindex="-1")
        headers = soup_final.find_all('h3',class_='h6 font-weight-bold mb-0')
        for i in range(0,len(div)):
            s1=headers[i].text
            s2=div[i].text.strip()[3:]
            s3=s2.split("-")
            if TA == s3[0].strip():
                d=s3[1].strip()
                string =d+";"+" "+s1+"\n"
                l.append(string)
    l.sort(key=lambda strr: in365(int(strr.split(", ")[1].split(" ")[0]),strr.split(", ")[1].split(" ")[1],int(strr.split(", ")[1].split(" ")[2]),int(strr.split(", ")[2].split("; ")[0].split(" ")[0].split(":")[0]),int(strr.split(", ")[2].split("; ")[0].split(" ")[0].split(":")[1]),strr.split(", ")[2].split("; ")[0].split(" ")[1]),reverse=False)

    for i in l:
        f.write(i)
    f.close()
   