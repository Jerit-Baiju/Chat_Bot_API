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
