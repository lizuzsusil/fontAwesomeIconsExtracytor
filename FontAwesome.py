import requests
from bs4 import BeautifulSoup

fontAwesomeExt = ["accessibility", "alert", "animals", "arrows", "audio_video", "automotive", "autumn", "beverage", "brands", "buildings", "business", "camping", "charity", "chat", "chess", "childhood", "clothing", "code", "communication", "computers", "construction", "currency", "datetime", "design", "editors", "education", "emoji", "energy", "files", "finance","fitness", "food","fruits_vegetables", "games", "genders", "halloween", "hands", "holiday", "hotel", "household", "images", "interfaces", "logistics", "maps", "maritime", "marketing", "mathematics", "medical", "moving", "music", "objects", "payment_shopping", "pharmacy", "political", "religion", "science", "science_fiction", "security", "shapes", "shopping", "social", "spinners", "sports", "spring", "status", "summer","tabletop_gaming","toggle", "travel", "users_people", "vehicles", "weather", "winter", "writing"]
# fontAwesomeExt = ["automotive"]

for x in fontAwesomeExt:

 URL = 'https://www.w3schools.com/icons/fontawesome5_'+x+'.asp'

 #print(URL)
 
 # Make the HTTP request to the URL
 response = requests.get(URL)
 #print(response.content)
 
 # Parse the HTML of the webpage
 soup = BeautifulSoup(response.text, 'html.parser')
 
 # Find the table containing the data
 table = soup.find('table', {'id': 'icontable_0'})
 
 #print(table)
 
 # Find all the rows in the table
 rows = table.find_all('tr')
 
 # Create the HTML structure
 html = '<section id="'+x+'-icons">\n\t<h2 class="page-header text-center">'+ x.capitalize()+' Icons</h2>\n\t<div class="row fontawesome-icon-list">\n'
 
 # Iterate over the rows and extract the data from the second column
 for row in rows:
     cols = row.find_all('td')
     font_name = cols[1].text.strip()
     html += f'\t\t<div class="fa-item col-md-3 col-sm-4 text-center mb-2">\n\t\t\t<i class="{font_name}"></i> <div class="small">{font_name}</div> \n\t\t</div>\n'
 
 # Close the HTML structure
 html += '\t</div>\n</section>'
 
 # Print the resulting HTML
 print(html)