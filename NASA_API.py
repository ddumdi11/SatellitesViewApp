import requests
import re
import imageio
from skimage import transform,io

# get json with information (including name and date) about Earth pictures
response = requests.post("https://api.nasa.gov/planetary/earth/imagery",
    params = {
      'api_key':"avKRwQxxxxxxxxx"
    })

# convert json to Python object
data = response.json()
print(data)

# create regex pattern to get separately year, month and day of an image
dates_pattern = r"^(?P<year>d{4})-(?P<month>d{2})-(?P<day>d{2})"

# download images and save each to ./images folder
for img in data['contextWrites']['to']:
   # get year, month and day with regex to create image url
   matches = re.search(dates_pattern, img['date'])
   year = matches.group('year')
   month = matches.group('month')
   day = matches.group('day')
   image_name = img['image']
   img_url = f'https://epic.gsfc.nasa.gov/archive/natural/{year}/{month}/{day}/png/{image_name}.png'
   # save image to ./images folder
   img_data = requests.get(img_url).content
   with open(f'images/{image_name}.png', 'wb') as handler:
       handler.write(img_data)

index = range(len(data['contextWrites']['to']))
images = []

# resize images and create gif from them
for i in index:
   img_name = data["contextWrites"]["to"][i]["image"]
   img = io.imread(f'images/{img_name}.png')
   small_img = transform.resize(img, (500, 500), mode='symmetric', preserve_range=True)
   images.append(small_img)
imageio.mimsave('images/earth500.gif', images)