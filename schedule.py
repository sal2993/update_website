#!/usr/bin/env python


'''

This program checks every Monday morning to see if there is a post (denoted by
being in the directory: ~/capthat/posts/ and ends with a 'u') that is dated
as the date of the Monday that it is checking. If the program finds a post
that needs to be updated, it then this program runs update.py

Programmer: Sal Camara

'''

import sys
import re
import time
import datetime
import logging
import subprocess

# Checks posts and finds the ones that end with a u.
# passes the posts ready to be updated to parse_updates()
def get_updates():

  p_updates = []  
  ls = subprocess.check_output(['ls ~/capthat/post/'], shell=True)
  ls = ls.split('\n')
  del(ls[-1])
  for i in ls:
    if i[-1] == 'u':
      print i
      p_updates.append(i)
  parse_updates(p_updates)
  return
 
# Recives a list of dates-posts ready to be uploaded to site (denoted by being
# in the directory: ~/capthat/posts/ and ends with a 'u') then it makes those
# dates into ordinal format
def parse_updates(updates):
  ordinal_dates = []
  today = datetime.date.today()


  # Gets current ordinal date
  today_ordinal = get_ordinal(today.year, today.month, today.day)

  for date in updates:
    match = re.search(r'(\d\d\d\d)-(\d\d)-(\d\d)', date )
    ordin = get_ordinal(int(match.group(1)), int(match.group(2)), \
                        int(match.group(3)))

    print ordin
    if ordin == today_ordinal:
      post_to_site(ordin)
      break

  transfer_job = './tes.py ' + str(updates[0]) + ' &'
  subprocess.call( transfer_job , shell=True)
  return

# Found a post that needs to be updated! Now this program will pass on the buck
# to update.py then sleep till next Monday :) (lucky!)
def post_to_site(post_ordinal_date):
  formal_date = str(get_formal(post_ordinal_date)) + 'u'
  subprocess.call(['ls','-l'], shell=True)

  return


# Receives formal date, returns ordinal date
def get_ordinal(year, month, day):
  ordinal = datetime.date(year, month, day)
  return ordinal.toordinal()

# Recieves ordinal date, returns formal date
def get_formal(ordinal):
  date = datetime.date.fromordinal(ordinal)
  return date

def main():
  while True:
    get_updates()
    time.sleep(60)
    print 'schedule.py'
  


if __name__ == "__main__":
  main()
