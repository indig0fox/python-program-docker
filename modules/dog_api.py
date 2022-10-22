import os
import io
import requests
from PIL import Image, ImageShow
import tempfile
import json
from .text_to_ascii import convert_to_ascii_art


class DogImage:
  def __init__(self, res_dict):
    self.id = res_dict['id']
    self.url = res_dict['url']


def get_dog_image():
  url = 'https://api.thedogapi.com/v1/images/search'
  params = {
    "limit" : 1
  }
  headers = {
    "x-api-key": 'live_wygb74p7ybIQ4iNxUCzbKC28ULAsyc3Gd42VTzNFbIUqeTHOcAOVO8tDxrF0GlY1'
  }

  res = requests.get(url, params=params, headers=headers)
  json = res.json()
  print(json[0]['url'])

  # dog_image = DogImage(res.json()[0])

  # out_dir = '.'
  # buffer = tempfile.SpooledTemporaryFile(max_size=1e9)
  # r = requests.get(dog_image.url, stream=True)
  # if r.status_code == 200:
  #     downloaded = 0
  #     filesize = int(r.headers['content-length'])
  #     for chunk in r.iter_content(chunk_size=1024):
  #         downloaded += len(chunk)
  #         buffer.write(chunk)
  #         # print(downloaded/filesize)
  #     buffer.seek(0)

  #     image = Image.open(io.BytesIO(buffer.read()))
  #     W, H = (round(image.width / 50), round(image.height / 50))
  #     # image.resize((W, H))
  #     # print(convert_to_ascii_art(image))
      
      
  #     image.save(os.path.join(out_dir, 'image.jpg'), quality=85)
  # buffer.close()