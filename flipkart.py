#Web Crawling - fetching the data from internet/web
import urllib.request as url#send request to the website an getting response from website
import bs4
#Beautiful Soup 4 - this is used to fetch the data
#goto CMD , and type pip install bs4 lxml
product_name = input("Enter Product Name : ").replace(" ","+")
path = "https://www.flipkart.com/search?q="+product_name
#HTML DATA
response = url.urlopen(path)
# print(response)
# lxml - library XML -HTML as well as XML data
data = bs4.BeautifulSoup(response,'lxml')
# print(data)
path = "https://www.flipkart.com" + data.find("a",class_="k7wcnx")["href"]
response = url.urlopen(path)
data = bs4.BeautifulSoup(response,'lxml')
product_name = data.find("span",class_="LMizgS")
print(product_name.text)
price = data.find("div",class_="hZ3P6w bnqy13")
print("Price : ",price.text)
rating = data.find("div",class_="MKiFS6")
print(f"Rating : {rating.text}🌟")
