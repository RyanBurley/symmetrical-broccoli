import math as mh
import random as rd

def generate_star_positions(nsrc):
    '''
    Function to generate right ascension and declination coordinates in degrees
    '''
    # from wikipedia
    r_asc = '00:45:44.3'
    dec = '43:16:09'

    day, minu, sec = dec.split(':')
    dec = int(day)+int(minu)/60+float(sec)/3600

    hour, minu, sec = r_asc.split(':')
    r_asc = 15*(int(hour)+int(minu)/60+float(sec)/3600)
    r_asc = r_asc/mh.cos(dec*mh.pi/180)

    ras = []
    decs = []
    for _ in range(nsrc):
        ras.append(r_asc + rd.uniform(-1,1))
        decs.append(dec + rd.uniform(-1,1))

    return ras, decs

def write_positions(ras,decs,nsrc):
    '''
    Function to print star coordinates to a CSV file
    '''
    path = '/Users/Ryan/Software/ADACS_Workshop/sky_catalogue'
    # now write these to a csv file for use by my other program
    with open(path+'/data/output/catalogue.csv','w',encoding="utf8") as file:
        print("id,ra,dec", file=file)
        for i in range(nsrc):
            print(f"{i:07d}, {ras[i]:12f}, {decs[i]:12f}", file=file)

def clip_to_radius():
    '''
    Placeholder function
    '''
