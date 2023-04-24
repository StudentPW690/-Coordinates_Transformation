# -*- coding: utf-8 -*-
"""
Created on Thu Apr 20 12:55:59 2023

@author: Natalia
"""
#parsery
import numpy as np
import argparse
class Transformation_2000:
    def __init__(self, dd, mt, sec, d, m, s, elipsoida, n, Lo):
        self.dd = dd
        self.mt = mt
        self.sec = sec
        self.d = d
        self.m = m
        self.s = s
        self.elipsoida = elipsoida
        self.n = n
        self.Lo = Lo
        
    def get_a_e2(self):
        if self.elipsoida == 'WGS84':
            a = 6378137.000
            e2 = 0.00669437999014
        elif self.elipsoida == 'GRS80':
            a = 6378137.000
            e2 = 0.00669438002290
        elif self.elipsoida == 'KRASOWSKI':
            a = 6378245.000
            e2 = 0.00669342162297
        else:
            print('Nieobsługiwana elipsoida!')
            exit()
        return a, e2
    
    def convert_phi_lam_to_rad(self):
        fia = np.deg2rad(self.dd + self.mt / 60 + self.sec / 3600)
        lambdaa = np.deg2rad(self.d + self.m / 60 + self.s / 3600)
        L0=np.deg2rad(self.Lo)
        return fia, lambdaa, L0

    def sigma(self):
        fia, lambdaa, L0 = self.convert_phi_lam_to_rad()
        a, e2 = self.get_a_e2()
        b2=a**2*(1-e2)
        er2=(((a**2)-(b2))/(b2))
        t=np.tan(fia)
        ni2=(er2)*((np.cos(fia))**2)
        l=lambdaa-L0    
        A0=1-(e2/4)-((3*(e2)**2)/64)-((5*(e2)**3)/256)
        A2=(3/8)*((e2+((e2**2)/4)+((15*(e2)**3))/128))
        A4=(15/256)*(e2**2+((3*((e2)**3))/4))
        A6=(35*((e2)**3))/3072
        sigma=a*(A0*fia-A2*np.sin(2*fia)+A4*np.sin(4*fia)-A6*np.sin(6*fia))
        N=a/(np.sqrt(1-e2*(np.sin(fia))**2))
        return sigma, N, t, ni2, l
    
    def xygk(self):
        sigma, N, t, ni2, l = self.sigma()
        fia, lambdaa, L0 = self.convert_phi_lam_to_rad()
        Xgk=sigma+((l**2)/2)*N*np.sin(fia)*np.cos(fia)*(1+((l**2)/12)*((np.cos(fia))**2)*(5-(t**2)+9*(ni2)+4*((ni2)**2))+((l**4)/360)*((np.cos(fia))**4)*(61-58*(t**2)+(t**4)+270*(ni2)-330*(ni2)*(t**2)))
        Ygk=l*N*np.cos(fia)*(1+((l**2)/6)*((np.cos(fia))**2)*(1-(t**2)+(ni2))+((l**4)/120)*((np.cos(fia))**4)*(5-18*(t**2)+(t**4)+14*(ni2)-58*(ni2)*(t**2)))
        return Xgk, Ygk
    
    def xy2000(self):
        n = self.n
        Xgk, Ygk = self.xygk()
        Xgk2000=0.999923*Xgk
        Ygk2000=0.999923*Ygk+n*1000000+500000 
        return Xgk2000, Ygk2000

def parse_args():
    parser = argparse.ArgumentParser(description='Konwerter współrzędnych geocentrycznych na topocentryczne')
    parser.add_argument('--dd', type=int, required=True, help='Wartość stopniowa phi')
    parser.add_argument('--mt', type=int, required=True, help='Wartość minutowa phi')
    parser.add_argument('--sec', type=int, required=True, help='Wartość sekundowa phi')
    parser.add_argument('--d', type=int, required=True, help='Wartość stopniowa lambdy')
    parser.add_argument('--m', type=int, required=True, help='Wartość minutowa lambdy')
    parser.add_argument('--s', type=int, required=True, help='Wartość sekundowa lambdy')
    parser.add_argument('--elipsoida', type=str, required=True, choices=['WGS84', 'GRS80', 'KRASOWSKI'],
                        help='Elipsoida odniesienia')
    parser.add_argument('--n', type=int, required=True, help='Numer pasa odwzorowawczego')
    parser.add_argument('--Lo', type=int, required=True, help='Wartość stopniowa pasa odwzorowawczego')
    return parser.parse_args()

if __name__ == "__main__":
    args = parse_args()
    
    try:
        dd = args.dd
        mt = args.mt
        sec=args.sec
        d=args.d
        m=args.m
        s=args.s
        elipsoida=args.elipsoida
        n=args.n
        Lo=args.Lo
        converter = Transformation_2000(dd, mt, sec, d, m, s, elipsoida, n, Lo)
    except ValueError as err:
        print(err)
    else:
        Xgk2000, Ygk2000 = converter.xy2000()
        print('x =', f'{Xgk2000:.3f}', 'm')
        print('y =', f'{Ygk2000:.3f}', 'm')