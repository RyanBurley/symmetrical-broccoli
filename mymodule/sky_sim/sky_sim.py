import math as mh
import random as rd

def generate_star_positions(nsrc):
    '''
    Function to generate right ascension and declination coordinates in degrees
    '''
    # from wikipedia
    r_asc = '00:42:44.3'
    dec = '41:16:09'

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

    radius = 1

    ras, decs = crop_to_circle(ras,decs,r_asc,dec,radius)

    return ras, decs

def write_positions(ras,decs,nsrc):
    '''
    Function to print star coordinates to a CSV file
    '''
    path = '/Users/Ryan/Software/ADACS_Workshop/sky_catalogue'
    # now write these to a csv file for use by my other program
    with open(path+'/data/output/catalogue.csv','w',encoding="utf8") as file:
        print("id,ra,dec", file=file)
        for i in range(len(ras)):
            print(f"{i:07d}, {ras[i]:12f}, {decs[i]:12f}", file=file)

def crop_to_circle(ras,decs,r_asc,dec,radius):
    '''
    Placeholder function
    '''
    cut_ras = []
    cut_decs = []

    for i in range(len(ras)):
        if ((r_asc - ras[i])**2 + (dec - decs[i])**2 < radius**2):
            cut_ras.append(ras[i])
            cut_decs.append(decs[i])

    return cut_ras, cut_decs
    


