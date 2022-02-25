import requests

#make an API call and store the response
url='https://api.github.com/search/repositories?q=language:python&sort=stars'
headers={'accept':'application/vnd.github.v3+json'}
r=requests.get(url, headers=headers)
print(f"status code:{r.status_code}")

#store API response in a variable
response_dict=r.json()
print(f"Total repositories: {response_dict['total_count']}")

#explore informations about the repositories
repo_dicts=response_dict['items']
print('repositories returned', len(repo_dicts))

#examine the first repository
repo_dict=repo_dicts[0]

print("selected information about each repository:\n")
for repo in repo_dicts :    
    print("\nSelected informations about first repository")
    print("name: ", repo['name'])
    print("owner: ", repo['owner']['login'])
    print("stars: ", repo['stargazers_count'])
    print("repository: ", repo['html_url'])
    print("created: ", repo['created_at'])
    print("updated: ", repo['updated_at'])
    print("description: ", repo['description'])