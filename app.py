from modules import rss, dog_api

while True:
  print("""
  --------------------------------------
  Welcome to the interactive quick-task menu!

  What would you like to do?
  1) See the 5 most recent headlines from The Onion
  2) Find a random dog picture
  """)
  choice = input("Make a choice: ")
  
  if (choice == '1'):
    rss.show_5_onion_headlines()
  elif choice == '2':
    dog_api.get_dog_image()