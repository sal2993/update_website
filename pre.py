#!/usr/bin/env python

# Currenty, this program askes for user to fill in title and body for each
# post for the week.

import subprocess
import datetime

input_info = '''# setlocal spell spelllang=en_us
title:
post:'''

def update(all_posts, date):
  
  for i in all_posts:
    subprocess.call(['vim', i])
    subprocess.call(['mv ' + i + ' post/'], shell=True)

  subprocess.call(['mkdir ' + 'pic/' + date], shell=True)
  return


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

def main():
  print 'hello user. Which week are you going to add posts too?'
  mondays = findmonday()
  
  for i in range(len(mondays)):
    print 'date ' + str(i+1) + ': ' + str(datetime.date.fromordinal(mondays[i]))

  usr_inp = -100
  while (usr_inp != '1' and usr_inp != '2' and usr_inp != '3'):
  
    usr_inp = raw_input('Date you would like to update: ')
    print usr_inp
    #if (usr_inp != 1 or usr_inp != 2 or usr_inp != 3):
      #print 'sorry, your input was invalid.'
    
  usr_inp = int(usr_inp)
  post_date = str(datetime.date.fromordinal(mondays[usr_inp-1]))

  print 'you win: ' + post_date
  create_posts(post_date)


#  update()
if __name__ == '__main__':
  main()
