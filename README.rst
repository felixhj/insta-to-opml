A python script based on instaloader by https://github.com/aandergr
With thanks

Instagram in RSS!

Overview
+Downloads a csv with all accounts you follow
+Allows you to sort these into groups quickly using number pad
+Converts these groups into OPML files ready to be imported into an RSS reader that can manage instagram, such as Feedbro
+Runs as a shell command

Apart from instaloader, the rest of this code was largely written by Chat GPT

Written in python

Dependencies:
*import instaloader
* import csv
* import pandas as pd
* from tkinter import Tk, filedialog
* from getch import getch
* from lxml import etree
* from argparse import ArgumentParser
* from glob import glob
* from os.path import expanduser
* from platform import system
* from sqlite3 import OperationalError, connect
