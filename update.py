#!/usr/bin/python 
import sys
import re
import time

fram = '''<!DOCTYPE html>
<html class="no-js" lang="en">
  <head>
    <meta charset="utf-8" />
    <meta name="viewport" content="width=device-width, initial-scale=1.0" />
    <title>Cap That | Welcome</title>
    <link rel="stylesheet" href="/css/foundation.css" />
    <link rel="stylesheet" type="text/css" href="/css/app.css" />
    <script src="js/vendor/modernizr.js"></script>
  </head>
  <body>

  <!-- Begin Logo -->
  <div class="logo_background">
    <div class="row">
      <div class="large-4 colums">
        <a href="/"><img src="/images/logo.jpg"></a>
      </div>
    </div>
  </div>

  <!-- Begin top nav bar -->
  <div class="topbar">
    <ul class="topbar">
      <li class="topbar"><a class="zheader" href="/">Home</a></li>
      <li class="topbar"><a class="zheader" href="/archives.html">Archives</a></li>
      <li class="topbar"><a class="zheader" href="/about.html">About</a></li>
      <li class="topbar"><a class="zheader" href="/contact.html">Contact</a></li>
      <li class="topbar_end"><a class="zheader" target="_blank" href="https://instagram.com/cap_that/">IG</a></li>
    </ul>
  </div>
  <br>
'''

theme_title = '''
  <!-- Topic of the week -->
  <div class="row">
    <div class="large-10 colums">
      <h1><b>#TITLE</b></h1>
      <p>#DATEOFMONDAY</p>
    </div>
  </div>

'''

pic_section = '''  <!-- Day 1 -->
  <section class="main" style="background-image: url('/images/themeimgs/#PICTURE');">
  </section>
  '''


bpost = '''  <div class="row">
    <div class="large-1 columns">
      <h4 class="tpost_date" >#DAY_OF_THE_WEEK</h4>
    </div>
    <div class="large-9 columns">
      <h1 class="tpost_title">#POST_TITLE</h1>
      <p class="tpost_body">#POST_BODY
      </p>
      <hr>
    </div>
    <div class="large-2 columns">
      <p> </p>
    </div>
  </div>

'''

new_info_f = 'updateweek.xml'
update_page_f = 'test.html'

#*******************************************************************************
# This function will run only every monday to change the title of the 
# week.html. 
def change_title():

  # Write the basic <head> html
  f = open(update_page_f, 'w')
  f.write(fram)
  f.close()

  # Find title message in updateweek.xml with Regex
  f = open(new_info_f, 'r')
  match = re.search(r'<message>\n(.+)</message>', f.read(), re.DOTALL)

  # Replace theme_titme frame with the new data
  new_theme = theme_title.replace("#TITLE", match.group(1))
  new_theme = new_theme.replace("#DATEOFMONDAY", '1-1-3001')
  f.close()

  # Write new data to the new week.html file
  f = open(update_page_f, 'a')
  f.write(new_theme)

  f.close()
  
# ******************************************************************************
def change_post():
  # Find what dat you need to post by searching the week.html for <!-- Day # -->

# CAN BE ERRORS, FIX THAT
  for i in range(5):

    # open the files with the post data
    post = 'post' + str(i) + '.txt'
    f = open(post, 'r')
    post_data = f.read()
    f.close()

    # Get data from post files
    post_title = re.search(r'title:(.+)', post_data)
    post_body = re.search(r'post:(.+)', post_data, re.DOTALL)

    # Add img to html frame
    pic_sec = pic_section.replace("", "")

    
    # Add data to html frame then mv to /data/www


    # sleep for some seconds
    time.sleep(60)



  
  
# post = bpost.replace('#DAY_OF_THE_WEEK', 'Sat')
# post = post.replace('#POST_TITLE', 'Bird in the air')
# post = post.replace('#POST_BODY', 'this is a bird i shot on friday')


def main():
  change_title()

  sys.exit(0)
  
if __name__ == '__main__':
  main()
