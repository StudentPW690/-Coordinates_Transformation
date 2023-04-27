import argparse
import numpy as np

class Transformacje:
    def __init__(self, elipsoida):
        self.elipsoida = elipsoida
        self.a, self.e2 = self.set_elipsoid_parameters()

    def set_elipsoid_parameters(self):
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
    
    def deg2dms(self, dd):
        deg = np.trunc(dd)
        mnt = np.trunc((dd-deg)*60)
        sec = ((dd-deg)*60-mnt)*60 
        return f'{deg:.0f} {abs(mnt):.0f} {abs(sec):.5f}'
    
    def blh2xyz(self, phi, lamb, h):
        N=self.a/np.sqrt(1-self.e2*np.sin(phi)**2)
        x=(N+h)*np.cos(phi)*np.cos(lamb)
        y=(N+h)*np.cos(phi)*np.sin(lamb)
        z=(N*(1-self.e2)+h)*np.sin(phi)
        return x, y, z
    
    def xyz2blh(self,x,y,z):
        p = np.sqrt(x**2+y**2)
        f = np.arctan(z/(p*(1-self.e2)))
        while True:
            N = self.a/np.sqrt(1-self.e2*np.sin(f)**2)
            h = p/np.cos(f)-N
            f_poprzednie = f
            f = np.arctan(z/(p*(1-(N*self.e2)/(N+h))))
            if abs(f_poprzednie-f) < 0.00001/206265:
                break 
        N = self.a/np.sqrt(1-self.e2*np.sin(f)**2)
        h = p/np.cos(f)-N
        lam = np.arctan2(y, x)
        phi = self.deg2dms(np.rad2deg(f))
        lam = self.deg2dms(np.rad2deg(lam))
        return phi, lam, h
    
    def neu(self,x,y,z,s,az,zen):
        a,e2=self.set_elipsoid_parameters()
        p = np.sqrt(x**2+y**2)
        f = np.arctan(z/(p*(1-e2)))
        while True:
            N = a/np.sqrt(1-e2*np.sin(f)**2)
            h = p/np.cos(f)-N
            f_poprzednie = f
            f = np.arctan(z/(p*(1-(N*e2)/(N+h))))
            if abs(f_poprzednie-f) < 0.00001/206265:
                break 
        N = a/np.sqrt(1-e2*np.sin(f)**2)
        h = p/np.cos(f)-N
        lam = np.arctan2(y, x)
        n = s*np.sin(zen)*np.cos(az)
        e = s*np.sin(zen)*np.sin(az)
        u = s*np.cos(zen)
        neu = np.array([n, e, u])
        Rneu = np.array([[-np.sin(f)*np.cos(lam), -np.sin(lam), np.cos(f)*np.cos(lam)], 
                         [-np.sin(f)*np.sin(lam), np.cos(lam), np.cos(f)*np.sin(lam)],
                         [np.cos(f), 0, np.sin(f)]])
        xyz = Rneu @ neu
        xb = x + xyz[0]
        yb = y + xyz[1]
        zb = z + xyz[2]
        return(xb,yb,zb)
    
    def xy2000(self,fia, lambdaa, n, Lo):
        L0=np.deg2rad(Lo)
        a, e2 = self.set_elipsoid_parameters()
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
        Xgk=sigma+((l**2)/2)*N*np.sin(fia)*np.cos(fia)*(1+((l**2)/12)*((np.cos(fia))**2)*(5-(t**2)+9*(ni2)+4*((ni2)**2))+((l**4)/360)*((np.cos(fia))**4)*(61-58*(t**2)+(t**4)+270*(ni2)-330*(ni2)*(t**2)))
        Ygk=l*N*np.cos(fia)*(1+((l**2)/6)*((np.cos(fia))**2)*(1-(t**2)+(ni2))+((l**4)/120)*((np.cos(fia))**4)*(5-18*(t**2)+(t**4)+14*(ni2)-58*(ni2)*(t**2)))
        Xgk2000=0.999923*Xgk
        Ygk2000=0.999923*Ygk+n*1000000+500000 
        return Xgk2000, Ygk2000
    
    def xy1992(self,fia, lambdaa):
        L0=np.deg2rad(19)
        a, e2 = self.set_elipsoid_parameters()
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
        Xgk=sigma+((l**2)/2)*N*np.sin(fia)*np.cos(fia)*(1+((l**2)/12)*((np.cos(fia))**2)*(5-(t**2)+9*(ni2)+4*((ni2)**2))+((l**4)/360)*((np.cos(fia))**4)*(61-58*(t**2)+(t**4)+270*(ni2)-330*(ni2)*(t**2)))
        Ygk=l*N*np.cos(fia)*(1+((l**2)/6)*((np.cos(fia))**2)*(1-(t**2)+(ni2))+((l**4)/120)*((np.cos(fia))**4)*(5-18*(t**2)+(t**4)+14*(ni2)-58*(ni2)*(t**2)))
        Xgk1992=0.9993*Xgk-5300000
        Ygk1992=0.9993*Ygk+500000 
        return(Xgk1992, Ygk1992)

def parse_args():
    parser = argparse.ArgumentParser(description='Konwerter współrzędnych geodezyjnych na kartezjańskie')
    parser.add_argument("-f", type=str, required=True, help="scieżka do pliku wejciowego")
    parser.add_argument('-t', type=str, required=True, help='rodzaj transformacji')
    return parser.parse_args()

if __name__ == "__main__":
    args = parse_args()
    try:
        sciezka_do_pliku_wejsciowego = args.f
    except ValueError as Wlasciwy_typ_niewlasciwa_wartosc:
        print(Wlasciwy_typ_niewlasciwa_wartosc)
    else:
        with open(sciezka_do_pliku_wejsciowego, "r") as file:
            lines = file.readlines()

        with open("plik_wynikowy.txt", "w") as outfile:
            for line in lines:
                values = line.split()
                if args.t == 'blh2xyz':
                    elipsoida = values[7]
                    phi = np.deg2rad(int(values[0])+int(values[1])/60+float(values[2])/3600)
                    lamb= np.deg2rad(int(values[3])+int(values[4])/60+float(values[5])/3600)
                    h=float(values[6])
                    converter = Transformacje(elipsoida)                  
                    x, y, z = converter.blh2xyz(phi, lamb,h)
                    outfile.write(f'x = {x:.3f} m\n')
                    outfile.write(f'y = {y:.3f} m\n')
                    outfile.write(f'z = {z:.3f} m\n')
                    outfile.write('\n') # Add a newline between each set of values
                    values.append(f'x = {x:.3f} m')
                    values.append(f'y = {y:.3f} m')
                    values.append(f'z = {z:.3f} m')
                elif args.t == 'xyz2blh':
                    elipsoida = values[-1]
                    x=float(values[0])
                    y=float(values[1])
                    z=float(values[2])
                    converter = Transformacje(elipsoida)
                    phi, lam, h = converter.xyz2blh(x,y,z)
                    outfile.write(f'phi = {phi} \n')
                    outfile.write(f'lam = {lam} \n')
                    outfile.write(f'h = {h:.3f} m\n')
                    outfile.write('\n') 
                    values.append(f'phi = {phi} \n')
                    values.append(f'lam = {lam} \n')
                    values.append(f'h = {h:.3f} m\n')
                elif args.t == 'xyz2neu':
                    elipsoida = values[4]
                    x=float(values[0])
                    y=float(values[1])
                    z=float(values[2])
                    s=float(values[3])
                    az=np.deg2rad(int(values[5])+int(values[6])/60+float(values[7])/3600)
                    zen=np.deg2rad(int(values[8])+int(values[9])/60+float(values[10])/3600)
                    converter = Transformacje(elipsoida)
                    xb, yb, zb = converter.neu(x,y,z,s,az,zen)
                    outfile.write(f'xb = {xb:.3f} m\n')
                    outfile.write(f'yb = {yb:.3f} m\n')
                    outfile.write(f'zb = {zb:.3f} m\n')
                    outfile.write('\n')
                    values.append(f'xb = {xb:.3f} m\n')
                    values.append(f'yb = {yb:.3f} m\n')
                    values.append(f'zb = {zb:.3f} m\n')
                elif args.t == 'fl22000':
                    elipsoida = values[6]
                    fia = np.deg2rad(int(values[0])+int(values[1])/60+float(values[2])/3600)
                    lambdaa= np.deg2rad(int(values[3])+int(values[4])/60+float(values[5])/3600)
                    n=int(values[7])
                    Lo=int(values[8])
                    converter = Transformacje(elipsoida)
                    Xgk2000, Ygk2000 = converter.xy2000(fia,lambdaa,n, Lo)
                    outfile.write(f'Xgk2000 = {Xgk2000:.3f} m\n')
                    outfile.write(f'Ygk2000 = {Ygk2000:.3f} m\n')
                    outfile.write('\n') 
                    values.append(f'Xgk2000 = {Xgk2000:.3f} m\n')
                    values.append(f'Ygk2000 = {Ygk2000:.3f} m\n')
                elif args.t == 'fl21992':
                    elipsoida = values[-1]
                    fia = np.deg2rad(int(values[0])+int(values[1])/60+float(values[2])/3600)
                    lambdaa= np.deg2rad(int(values[3])+int(values[4])/60+float(values[5])/3600)
                    converter = Transformacje(elipsoida)
                    Xgk1992, Ygk1992 = converter.xy1992(fia,lambdaa)
                    outfile.write(f'Xgk1992 = {Xgk1992:.3f} m\n')
                    outfile.write(f'Ygk1992 = {Ygk1992:.3f} m\n')
                    outfile.write('\n') 
                    values.append(f'Xgk1992 = {Xgk1992:.3f} m\n')
                    values.append(f'Ygk1992 = {Ygk1992:.3f} m\n')
                else:
                    print('Brak innych transformacji')
                    
                    
                    