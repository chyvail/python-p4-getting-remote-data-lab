import requests
import json

class GetRequester:

    def __init__(self, url):
        self.url = url

    def get_response_body(self):
        response = requests.get(self.url)
        return response.content

    def load_json(self):
        dict_list = []
        contents = json.loads(self.get_response_body())
        for content in contents:
            dict_list.append(content)
        return dict_list

getty = GetRequester('https://learn-co-curriculum.github.io/json-site-example/endpoints/people.json')
#print(getty.get_response_body())
print(getty.load_json())
