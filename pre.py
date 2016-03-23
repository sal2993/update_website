#!/usr/bin/env python

# Currenty, this program askes for user to fill in title and body for each
# post for the selected week (next 3 upcoming mondays).

import subprocess
import datetime

input_info = '''# setlocal spell spelllang=en_us
title:
post:'''

# ******************************************************************************
# This functions simply finds the next 3 upcomming monday dates
# returns the dates in ordinal date format in an array
def findmonday():
  # Get todays date
  today = datetime.date.today()

  # this array will hold the next Gregorian ordinal dates that fall on Monday
  next_mondays = []

  # diff = difference btw todays day of the week and monday
  diff = 7 - today.weekday()

  # add difference to gregorian ordinal date
  ordinal_monday = today.toordinal() + diff
  next_mondays.append(ordinal_monday)

  while (len(next_mondays) < 3):
    # increment ordinal Monday
    ordinal_monday = ordinal_monday + 7

    # add next ordinal mondays
    next_mondays.append(ordinal_monday)

  return next_mondays
  
# ******************************************************************************
# Crates the blog post names which will be .txt files to hold the post data
# Passes the array of post file names to update() to be created to files.
def create_posts(date_post):
  posts_all = []
  for i in range(5):
    x =  date_post + 't' + str(i + 1) + '.txt'
    posts_all.append(x)
    f = open(x, 'w')
    f.write(input_info)
    f.close()

  posts_all.append(date_post + '_title.txt')
  f = open(posts_all[-1], 'w')
  f.write('Title for the whole blog post:')
  f.close()

  update(posts_all, date_post)
  return

# ******************************************************************************
# Makes directory to store the files. Lets user update files. Makes a folder 
# for respective pictures. 
def update(all_posts, date):
  
  subprocess.call(['mkdir ' + 'post/' + date + 'u'], shell=True)
  for i in all_posts:
    subprocess.call(['vim', i])
    subprocess.call(['mv ' + i + ' post/' + date + 'u'], shell=True)

  subprocess.call(['mkdir ' + 'pic/' + date], shell=True)
  return

# *****************************************************************************
def main():
  # Greey user
  print 'hello user. Which week are you going to add posts too?'

  # Gets next Mondays
  mondays = findmonday()
  
  usr_inp = -100

  # Have user pick out date to update
  while (usr_inp != '1' and usr_inp != '2' and usr_inp != '3'):

    for i in range(len(mondays)):
      print 'date ' + str(i+1) + ': ' + str(datetime.date.fromordinal(mondays[i]))

    usr_inp = raw_input('Date you would like to update: ')
    if (usr_inp != '1' and usr_inp != '2' and usr_inp != '3'):
      print 'sorry, your input was invalid.'
    
  usr_inp = int(usr_inp)
  post_date = str(datetime.date.fromordinal(mondays[usr_inp-1]))

  print 'Date chose: ' + post_date
  create_posts(post_date)


#  update()
if __name__ == '__main__':
  main()
