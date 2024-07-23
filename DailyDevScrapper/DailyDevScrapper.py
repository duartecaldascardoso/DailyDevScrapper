import requests
from bs4 import BeautifulSoup
from gtts import gTTS

url = "https://daily.dev/"
# url = input("Fill in your url please")

# Get request to the provided URL
response = requests.get(url)

if response.status_code == 200:
    soup = BeautifulSoup(response.content, 'html.parser')
    page_text = soup.get_text().lower()

    speech = gTTS(text=page_text, lang='en', slow=False)
    speech.save("dailyDevContent.mp3")
else:
    print(f"Failed to retrieve the content from the webpage. Obtained status code: {response.status_code}")
