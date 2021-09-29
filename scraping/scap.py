#Generate urls 
base_url="https://github.com/search?"
def generate_page_urls(base_url, num_pages):
    page_urls = []

    for counter in range(1, num_pages + 1):
    full_url = base_url + "p=" + str(counter) + "&q=open+education&type=Repositories"
    page_urls.append(full_url)

    return page_urls

#Create 3 urls
page_urls=generate_page_urls(base_url,3)
print(page_urls)

#for all pages
def extract_github_urls (page_urls):
    github_list=[]
    from time import sleep
    for test4 in page_urls:
    import requests
    from bs4 import BeautifulSoup
    git_req = requests.get(test4)
    soup = BeautifulSoup(git_req.text, "html.parser")
    rep_categ=soup.find_all(class_="repo-list-item hx_hit-repo d-flex flex-justify-start py-4 public source")

# for each g on that page look up the title and url and store it in a list

    for test5 in rep_categ: 
        name_rep=test5.find("a").attrs["href"]
        rep_descr= test5.find("p",class_="mb-1").text.replace('\n','').replace('  ','')
        github_list.append({"Name Repository": name_rep,
                        "Description": rep_descr})
        sleep(0.5)
     return github_list
github_list = extract_github_urls(page_urls)


print(github_list)
