# Informacje dotyczące projektu 

***Program transformujący dane - wymagania do jego uruchomienia***
<br> Przedstawiony program, należy uruchomić za pomocą Python 3.10, został on napisany na systemie operacyjnym Windows 10, 64-bitowym.
Jeden z komputerów jest wyposażony w kartę graficzną NVIDIA GEFORCE GTX 1660Ti, procesor AMD Ryzen 7 4800H with Radeon Graphics oraz
pamięć RAM o wielkości 16 GB.
<br> Drugi komputer wykorzystany do napisania projektu posiada system operacyjny Windows 10, 64-bitowy, pamięć RAM 16 GB,
procesor Intel CORE i7 oraz kartę graficzną NVIDIA GEFORCE GTX 1660Ti.
<br> Użytkowanie programu jest możliwe, jedynie po uprzednim zainstalowaniu języka programowania Python w jednej z najnowszysch wersji, np. 3.10.
<br>Aby skorzystać z jednego z programów należy zakomentować za pomocą symbolu kratki (#) wszystkie pozostałe programy. 
<br>Tzn. zaznaczyć wszystkie programy, poza tym, który ma być użyty i kliknąć CTRL+1, bądź ręcznie wstawić kratki w każdą linię nieużywanego w danym momencie kodu.
<br>Następnie należy uruchomić "Wiersz polecenia" na komputerze użytkownika, przejść do odpowiedniego folderu, w którym znajduje się plik programu (.py) oraz 
pliki z danymi (.txt) i uruchomić program.
<br> Po uruchomieniu programu python: ```projinfa.py```, należy zapoznać się z jego wymaganiami, tzn. : zainstalowaniem biblioteki numpy oraz biblioteki argparse. 
<br>Biblioteka numpy zawiera wiele funkcji i narzędzi do przetwarzania,
analizy i manipulacji dużych danych numerycznych, co pozwala na łatwiejsze posługiwanie się funkcjami matematycznymi. 
Zaś biblioteka argparse pozwala na łatwe parsowanie argumentów wywołania programu z wiersza poleceń, 
umożliwia definiowanie zestawu argumentów, które użytkownik może przekazać do programu podczas jego uruchamiania.  

<br>W podanym programie przedstawione zostały transformacje ze współrzędnych:
<br> 1) geocentrycznych (XYZ) na elipsoidalne(BLH),
<br> 2) elipsoidalnych (BLH) na geocentryczne (XYZ); 
<br> 3) geocentrycznych (XYZ) na topocentryczne (NEU); 
<br> 4) BL (GRS80, Krasowski, WGS84) na układ 2000;
<br> 5) BL (GRS80, Krasowski, WGS84) na układ 1992; 
<br> Dodatkowo są obsługiwane elispoidy GRS80, Krasowski oraz WGS84.
<br> Elipsoidy charakteryzują się wartościami *a* oraz *e<sup>2</sup>*.
<br>Gdzie *a* jest to wielka półoś elipsy, a *e<sup>2</sup>* to mimośród.
<br> Przy elipsoidzie GRS80 te wartości wynoszą odpowiednio 6378137.000 oraz 0.00669438002290, przy elipsoidzie WGS84
6378137.000 oraz  0.00669437999014, a przy elipsoidzie Krasowskiego 6378245.000 oraz 0.00669342162297.
<br> Ponadto dodano zabezpieczenie dzięki któremu, przy wprowadzeniu elipsoidy niewymienionej wyżej, program informuje komunikatem "Nieobsługiwana elipsoida!"

***Funkcjonalność i posługiwanie się programami*** 
<br>1. Program transformujący współrzędne geocentryczne do elipsoidalnych:

<br>2. Program transformujący współrzędne elipsoidalne do geocentrycznych:

<br>3. Program transformujący współrzędne geocentryczne do topocentrycznych:

<br>4. Program transformujący współrzędne B,L do układu PL2000:
<br> ***Używanie programu - przykład***
<br> Program został napisany tak, aby mógł pracować na większej ilości danych - plikach. 
<br> W tym celu w programie Notatnik (plik .txt) zamieszczono dane o następującej charakterystyce:
<br> 1. pierwsza kolumna stanowi wartość stopniową kąta B,
<br> 2. druga kolumna stanowi wartość minutową kąta B,
<br> 3. trzecia kolumna - wartość minutową kąta B,
<br> 4. czwarta kolumna stanowi wartość stopniową L,
<br> 5. piąta kolumna stanowi wartość minutową L,
<br> 6. szósta kolumna - wartość minutową kąta L,
<br> 7. siódma kolumna - numer pasa odwzorowawczego w układzie PL2000 
(dla wartości lambdy z przedziału: 13.5-16.5 stopnia - pas 5;
<br> 16.5-19.5 stopnia - pas 6; 19.5-22.5 stopnia - pas 7; 22.5-25.5 - pas 8)
<br> 8. ósma kolumna - wartość stopniowa dla danego pasa odwzorowawczego (odpowiednio 15, 18, 21 lub 24 stopnie)
<br>Po uruchomieniu programu następuje proces zapisu do pliku tekstowego (.txt), 
w którym otrzymujemy wyniki podzielone na dwie kolumny:
<br> X oraz Y w układzie PL2000.
<br> Nadmienic należy, że każde kolumny rozdzielone są spacją.
<br> Program został przetestowany za pomocą wiersza poleceń, aby wprowadzić plik tekstowy do obliczenia wartości
należy posługiwać się wyżej ukazaną instrukcją. 

<br>*Przykład:* 
<br>52 16 17 17 56 49 GRS80 6 18 
<br>51 30 16 18 14 15 GRS80 6 18 
<br>50 25 36 18 58 47 GRS80 6 18
<br>50 15 00 15 40 00 GRS80 5 15 
<br>51 10 10 15 14 15 GRS80 5 15 

<br>*Wyniki:* 
<br>Xgk2000 = 5793095.196m
<br>Ygk2000 = 6496378.604m

<br>Xgk2000 = 5707793.947m
<br>Ygk2000 = 6516489.238m

<br>Xgk2000 = 5588335.008m
<br>Ygk2000 = 6569612.324m