#!/usr/bin/python 
import sys
import re
import time
import subprocess

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

update_page_f = 'test.html'

# ******************************************************************************
# Which week will you be updating?
def which():
  # get the posts ready to be updated and put in list
  ls = subprocess.check_output(['ls', 'post'])
  ls = ls.split('\n')
  del(ls[-1])  # deletes unnecesary blank line 

  # removes the options that have already been updated.
  # the options that have already been updated, the directorys end with a 'u'
  for i in range(len(ls)):
    if ls[i][-1] == 'u':
      del(ls[i])

  inp = 100
  # Ask the user which post will he want updated
  while inp > len(ls) or inp <= 0:
    try:
      for i in range(len(ls)):
        print str(i +1) + ': ' + ls[i]
      inp = int(raw_input("Post you like to be updated: "))
    except ValueError:
      print 'you put in a letter you mega fool'
      inp = 100

  # has to have to -1 otherwise it would be out of range
  return ls[inp -1]

# ******************************************************************************
# This function will run only every monday to change the title of the 
# week.html. 
def change_title(update_post):
  new_info_f = './post/' + update_post + '/' + update_post + '_title.txt'

  # Write the basic <head> html
  f = open(update_page_f, 'w')
  f.write(fram)
  f.close()

  # Find title message in post/date_title.txt with Regex
  f = open(new_info_f, 'r')
  match = re.search(r'Title for the whole blog post:(.+)', f.read(), re.DOTALL)
  print match.group()

  # Replace theme_titme frame with the new data
  new_theme = theme_title.replace("#TITLE", match.group(1))
  new_theme = new_theme.replace("#DATEOFMONDAY", update_post)
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
  # which will return the post to be updated to the website
  post_update = which()
  print post_update

  change_title( post_update )

  sys.exit(0)
  
if __name__ == '__main__':
  main()
