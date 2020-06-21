# This is the script to show everything I have worked on and I use 

import pandas as pd
import matplotlib.pyplot as plt
from argparse import ArgumentParser
import sys, os, glob, json, requests
import src.main_functions as fn

# B) Create a python script and name it `main.py`. Requirements for this script:
# - `main.py` must not have more than 100 lines.
#  - Separate code into other `.py` files. Create functions or classes if needed.
#- It must receive at least 2 params via command-line flags `--param1` `--param2`.
#  - Use `argparse` for this task.
#  - Those parameters should be used to filter the dataset.


parser = ArgumentParser(description="This function returns a little report about the number of dogs and the  most commons breeds in the borough selected, and pictures if the breed."
                        
parser.add_argument("--breed",type=str, help="Select the breed:")
parser.add_argument("--borough",type=str, help= "Choose a borough between Manhattan, Brooklyn, Queens, Bronx or Staten Island")
#Should I put a list of the breeds somewhere?                        
args = parser.parse_args()

                        
data = pd.read_csv('OUTPUT/data.csv')

#ni puta idea de lo q estoy haciendo
#creo que aqui tengo que poner las funciones que vayan al dfclean y me devuelvan los datos que quiero utilizando pandas
