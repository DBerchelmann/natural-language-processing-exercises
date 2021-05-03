import requests
import bs4
import pandas as pd






def get_post(urls):
    
    '''this function takes in a list of urls and then iterates through each url and pulls the title of the blog post and the content. That information is the appended into an empty dictionary. That dictionary is returned as pandas data frame'''
    
    # create empty list
    
    empty_d = []
    
    #create the for loop that uses beautiful soup to pull information
    
    for url in urls:
        
        headers = {'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.93 Safari/537.36'}
        response = requests.get(url, headers=headers)
        html = response.text
        soup = bs4.BeautifulSoup(html)
    
        article_div = soup.select(".jupiterx-main-content")[0]
        title = article_div.find('h1').text
        body_container = article_div.select('.jupiterx-post-content.clearfix')[0]
        body_content = body_container.text
       
        content = { 'title': title, 
                    'content': body_content}
        
        empty_d.append(content)

        
    # create data frame 
    df = pd.DataFrame(empty_d)
    
    return df