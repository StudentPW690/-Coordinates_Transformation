# Informacje dotyczące projektu 

#Program - wymagania do jego uruchomienia 
Przedstawiony program, należy uruchomić za pomocą Python 3.10, został on napisany na systemie operacyjnym Windows 10,
komputer jest wyposażony w kartę graficzną NVIDIA GEFORCE GTX oraz procesor intel CORE i5. 
Po uruchomieniu programu pythonowego: ```projinfa.py```, należy zapoznać się z jego wymaganiami, tzn. : zainstalowaniem
biblioteki numpy oraz biblioteki argparse. Biblioteka numpy zawiera wiele funkcji i narzędzi do przetwarzania,
analizy i manipulacji dużych danych numerycznych, co pozwala na łatwiejsze posługiwanie się funkcjami matematycznymi. 
Zaś biblioteka argparse pozwala na łatwe parsowanie argumentów wywołania programu z wiersza poleceń, 
umożliwia definiowanie zestawu argumentów, które użytkownik może przekazać do programu podczas jego uruchamiania.  

#Funkcjonalność i posługiwanie się programem 
Program służy do transforamcji współrzędnych punktów z jednego układu współrzędnych geodezyjnych na inny. 
W podanym programie przedstawione zostały transformacje ze współrzędnych: 1) geocentrycznych (XYZ) na elipsoidalne(BLH),
2) elipsoidalnych (BLH) na geocentryczne (XYZ); 3) geocentrycznych (XYZ) na topocentryczne (NEU); 
4) BL (GRS80, Krasowski, WGS84) na układ 2000;
5) BL (GRS80, Krasowski, WGS84) na układ 1992; 
Dodatkowo są obsługiwane elispoidy GRS80, Krasowski oraz WGS84. 
*Używanie programu - przykład* 
Program został został przetestowany za pomocą wiersza poleceń, zostały wpisane wartości stopniowa kąta phi (52 18 01),
wartość stopniowa lambdy (51 47 12 ), nazwa wykorzystanej elipsoidy (GRS80), numer pasa (n=7) oraz Lo (21), 
z czego zostały uzyskane wartości X (6255680.121) oraz Y (9570052.396). 
Wszystkie podane wartości zostały wprowadzone według wytycznych z programu, tzn. gdy w programie są wymagane przy
wartości stopniowej phi *--d*, to analogicznie należy wpisać wartości, np:
>projekt_1_infa>python projinfa.py --d 52 --mt 18 --sec 1.
 

zwykłąy text
Żeby uruchomić program nalezy wykonać poniższą komendę w cmd:
```python skrypt.py```
kolejne kroki