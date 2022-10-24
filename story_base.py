import requests
url = "https://question-generator.p.rapidapi.com/"
story_file = open('story.txt', 'r')
story = {
    'text': story_file.read()
}
resp = requests.request("GET", url, params=story)
print(resp.text)
# sentences = story_file.read().splitlines()

# print(sentences)

import requests

url = "https://question-generator.p.rapidapi.com/"

querystring = {"text":"London Wildlife Trust, founded in 1981, is the local nature conservation charity for Greater London. It is one of 46 members of the Royal Society of Wildlife Trusts (known as The Wildlife Trusts), each of which is a local nature-conservation charity for its area. The trust aims to protect London's wildlife and wild spaces, and it manages over 40 nature reserves in Greater London. The trust's oldest reserves include Sydenham Hill Wood (pictured), which was managed by Southwark Wildlife Group before 1982 and was thus already a trust reserve at that date. The campaign to save Gunnersbury Triangle began that same year, succeeding in 1983 when a public inquiry ruled that the site could not be developed because of its value for nature. The trust has some 50 members of staff and 500 volunteers who work together on activities such as water management, chalk grassland restoration, helping people with special needs, and giving children an opportunity to go pond-dipping.","nbr":"10"}

headers = {
	"X-RapidAPI-Key": "e3f39a2cccmsh0106d74b48432f7p11baa9jsn6b4d7a999172",
	"X-RapidAPI-Host": "question-generator.p.rapidapi.com"
}

response = requests.request("GET", url, headers=headers, params=querystring)

print(response.text)
