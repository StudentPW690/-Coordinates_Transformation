# Informacje dotyczące projektu 

***Program transformujący dane - wymagania do jego uruchomienia***
<br> Przedstawiony program, należy uruchomić za pomocą Python 3.10, został on napisany na systemie operacyjnym Windows 10, 64-bitowym.
Jeden z komputerów jest wyposażony w kartę graficzną NVIDIA GEFORCE GTX 1660Ti, procesor AMD Ryzen 7 4800H with Radeon Graphics oraz
pamięć RAM o wielkości 16 GB.
<br> Drugi komputer wykorzystany do napisania projektu posiada system operacyjny Windows 10, 64-bitowy, pamięć RAM 16 GB,
procesor Intel CORE i7 oraz kartę graficzną NVIDIA GEFORCE GTX 1660Ti.
<br> Użytkowanie programu jest możliwe, jedynie po uprzednim zainstalowaniu języka programowania Python w jednej z najnowszysch wersji, np. 3.10.
<br>Aby skorzystać z jednego z programów należy uruchomić "Wiersz polecenia" na komputerze użytkownika, przejść do odpowiedniego folderu, w 
którym znajduje się plik programu (.py) oraz pliki z danymi (.txt) i uruchomić program. Wpisać w wiersz polecenia komendę np. ***python projinfa.py -f dane_f_l_h.txt -t flh2xyz*** . 
<br> Po uruchomieniu programu python: ```projinfa.py```, należy zapoznać się z jego wymaganiami, tzn. : zainstalowaniem biblioteki numpy oraz biblioteki argparse. 
<br>Biblioteka numpy zawiera wiele funkcji i narzędzi do przetwarzania,
analizy i manipulacji dużych danych numerycznych, co pozwala na łatwiejsze posługiwanie się funkcjami matematycznymi. 
Zaś biblioteka argparse pozwala na łatwe parsowanie argumentów wywołania programu z wiersza poleceń, 
umożliwia definiowanie zestawu argumentów, które użytkownik może przekazać do programu podczas jego uruchamiania.  

<br>W podanym programie przedstawione zostały transformacje ze współrzędnych wraz z ich odpowiednikami do wpisania w wiersz polecenia
za flagą "-t" oraz "-f". Należy dodać, że elipsoida odniesienia zawarta jest w pliku z danymi:
<br> 1) geocentrycznych (XYZ) na elipsoidalne(BLH) - xyz2blh - dane_xyz.txt,
<br> 2) elipsoidalnych (BLH) na geocentryczne (XYZ) - blh2xyz - dane_f_l_h.txt; 
<br> 3) geocentrycznych (XYZ) na topocentryczne (NEU) - xyz-neu - neu_1.txt; 
<br> 4) BL (GRS80, Krasowski, WGS84) na układ 2000 - fl22000 - dane_2000.txt;
<br> 5) BL (GRS80, Krasowski, WGS84) na układ 1992 - fl21992 - dane_1992.txt; 
<br> Każdy z programów obsługuje elispoidy GRS80, Krasowski oraz WGS84.
<br> Elipsoidy charakteryzują się wartościami *a* oraz *e<sup>2</sup>*.
<br>Gdzie *a* jest to wielka półoś elipsy, a *e<sup>2</sup>* to mimośród.
<br> Przy elipsoidzie GRS80 te wartości wynoszą odpowiednio 6378137.000 oraz 0.00669438002290, przy elipsoidzie WGS84
6378137.000 oraz  0.00669437999014, a przy elipsoidzie Krasowskiego 6378245.000 oraz 0.00669342162297.
<br> Ponadto dodano zabezpieczenie dzięki któremu, przy wprowadzeniu elipsoidy niewymienionej wyżej, program informuje komunikatem "Nieobsługiwana elipsoida!"
<br>
<br> Wszystkie rogramy zostały napisane tak, aby mogły pracować na większej ilości danych - plikach.
<br>
***Funkcjonalność i posługiwanie się programami*** 
<br>
<br>1. Program transformujący współrzędne geocentryczne do elipsoidalnych:
<br> Struktura danych:
<br> plik z danymi geocentrycznymi charakteryzuje się następującym ułożeniem danych:
<br> 1. pierwsza kolumna to wszpółrzędna X - w metrach
<br> 2. druga kolumna to współrzędna Y - w metrach
<br> 3. trzecia kolumna to współrzędna Z - w metrach
<br> 4. czwarta kolumna to rodzaj elipsoidy GRS80, WGS84 lub Krasowski
<br> Kolumny są od siebie oddzielone spacjami.
<br> Plik wynikowy zawiera podpisane współrzędne jedna pod drugą, każdy punkt jest odseparowany od poprzedniego linijką odstępu.

<br>2. Program transformujący współrzędne elipsoidalne do geocentrycznych:
<br> Struktura danych:
<br> plik z danymi elipsoidalnymi charakteryzuje się następującym ułożeniem danych:
<br> 1. pierwsza kolumna to wszpółrzędna stopniowa phi
<br> 2. druga kolumna to współrzędna minutowa phi
<br> 3. trzecia kolumna to współrzędna sekundowa phi
<br> 4. czwarta to wszpółrzędna stopniowa lambdy
<br> 5. piąta to współrzędna minutowa lambdy
<br> 6. szósta to współrzędna sekundowa lambdy
<br> 7. siódma to wysokość punktu w metrach
<br> 8. ósma kolumna to rodzaj elipsoidy GRS80, WGS84 lub Krasowski
<br> Kolumny są od siebie oddzielone spacjami.
<br> Plik wynikowy zawiera podpisane współrzędne jedna pod drugą, każdy punkt jest odseparowany od poprzedniego linijką odstępu.

<br>3. Program transformujący współrzędne geocentryczne do topocentrycznych:
<br> Struktura danych:
<br> plik z danymi współrzędnymi geocentrycznymi charakteryzuje się następującym ułożeniem danych:
<br> 1. pierwsza kolumna to wszpółrzędna X - w metrach
<br> 2. druga kolumna to współrzędna Y - w metrach
<br> 3. trzecia kolumna to współrzędna Z - w metrach
<br> 4. czwarta kolumna to odległość między punktami w metrach.
<br> 5. piąta kolumna to rodzaj elipsoidy GRS80, WGS84 lub Krasowski
<br> 6. szósta kolumna to wszpółrzędna stopniowa azymutu danego punktu
<br> 7. siódma kolumna to współrzędna minutowa azymutu danego punktu
<br> 8. ósma kolumna to współrzędna sekundowa azymutu danego punktu
<br> 9. dziewiąta to wszpółrzędna stopniowa kąta zenitalnego danego punktu
<br> 10. dziesiąta to współrzędna minutowa kąta zenitalnego danego punktu
<br> 11. jedenasta to współrzędna sekundowa kąta zenitalnego danego punktu
<br> Kolumny są od siebie oddzielone spacjami.
<br> Plik wynikowy zawiera podpisane współrzędne jedna pod drugą, każdy punkt jest odseparowany od poprzedniego linijką odstępu.

<br>4. Program transformujący współrzędne B,L do układu PL2000:
<br> Struktura danych:
<br> plik z danymi współrzędnymi B, L charakteryzuje się następującym ułożeniem danych:
<br> 1. pierwsza kolumna stanowi wartość stopniową kąta B,
<br> 2. druga kolumna stanowi wartość minutową kąta B,
<br> 3. trzecia kolumna - wartość sekundową kąta B,
<br> 4. czwarta kolumna stanowi wartość stopniową L,
<br> 5. piąta kolumna stanowi wartość minutową L,
<br> 6. szósta kolumna - wartość sekundową kąta L,
<br> 7. siódma kolumna - elipsoida odniesienia
<br> 7. ósma kolumna - numer pasa odwzorowawczego w układzie PL2000 
(dla wartości lambdy z przedziału: 13.5-16.5 stopnia - pas 5;
<br> 16.5-19.5 stopnia - pas 6; 19.5-22.5 stopnia - pas 7; 22.5-25.5 - pas 8)
<br> 8. dziewiąta kolumna - wartość stopniowa dla danego pasa odwzorowawczego (odpowiednio 15, 18, 21 lub 24 stopnie)
<br>Po uruchomieniu programu następuje proces zapisu do pliku tekstowego (.txt), 
w którym otrzymujemy wyniki podzielone na dwie kolumny:
<br> X oraz Y w układzie PL2000.
<br> Nadmienic należy, że każde kolumny rozdzielone są spacją.
<br> Program został przetestowany za pomocą wiersza poleceń, aby wprowadzić plik tekstowy do obliczenia wartości
należy posługiwać się wyżej ukazaną instrukcją. 
<br> Plik wynikowy zawiera podpisane współrzędne jedna pod drugą, każdy punkt jest odseparowany od poprzedniego linijką odstępu.

<br>5. Program transformujący współrzędne B,L do układu PL1992:
Struktura danych:
<br> plik z danymi współrzędnymi B, L charakteryzuje się następującym ułożeniem danych:
<br> 1. pierwsza kolumna stanowi wartość stopniową kąta B,
<br> 2. druga kolumna stanowi wartość minutową kąta B,
<br> 3. trzecia kolumna - wartość minutową kąta B,
<br> 4. czwarta kolumna stanowi wartość stopniową L,
<br> 5. piąta kolumna stanowi wartość minutową L,
<br> 6. szósta kolumna - wartość minutową kąta L,
<br> 7. siódma kolumna - to rodzaj elipsoidy GRS80, WGS84 lub Krasowski
<br> Kolumny rozdzielone są spacją.
<br> Po uruchomieniu programu następuje proces zapisu do pliku tekstowego (.txt), 
<br> X oraz Y w układzie PL1992.
<br> Program został przetestowany za pomocą wiersza poleceń, aby wprowadzić plik tekstowy do obliczenia wartości
należy posługiwać się wyżej ukazaną instrukcją. 
<br> Plik wynikowy zawiera podpisane współrzędne jedna pod drugą, każdy punkt jest odseparowany od poprzedniego linijką odstępu.
<br>
<br>Poniżej prezentowany jest przykładowy format danych wejściowych i wyjściowych na podstawie transformacji współrzędnych geocentrycznych 
do układu PL2000

<br>*Przykład danych dla układu flh:* 
<br>3966086.489 1305184.14 4807557.867 GRS8
<br>2594756.458 1258912.127 5988562.236 GRS80
<br>4662213.222 2465664.45 4635321.796 GRS80
<br>3565612.777 2565640.556 6461121.55 GRS80

<br>*Przykład danych dla układu xyz:*
<br>52 16 17 17 56 49 1380 GRS80
<br>51 30 16 18 14 15 1100 GRS80
<br>50 25 36 18 58 47 1120 GRS80
<br>48 73 0 17 73 0 1380 GRS80
<br>47 58 11 18 39 0 1000 GRS80 

<br>*Przykład danych dla układu neu:*
<br>3966086.489 1305184.14 4807557.867 45000 GRS80 140 12 11 90 21 36
<br>2594756.458 1258912.127 5988562.236 39000 GRS80 136 21 22 74 45 36
<br>4662213.222 2465664.45 4635321.796 12000 GRS80 98 52 56 31 13 25
<br>3565612.777 2565640.556 6461121.55 19000 GRS80 54 58 56 25 36 54
<br>3712175.133 1195423.468 5030233.372 45000 GRS80 145 0 0 90 0 0

<br>*Przykład danych dla układu 2000:* 
<br>52 16 17 17 56 49 GRS80 6 18 
<br>51 30 16 18 14 15 GRS80 6 18 
<br>50 25 36 18 58 47 GRS80 6 18
<br>50 15 00 15 40 00 GRS80 5 15 
<br>51 10 10 15 14 15 GRS80 5 15 

<br>*Przykład danych dla układu 1992:*
<br>52 16 17 17 56 49 GRS80
<br>51 30 16 18 14 15 GRS80
<br>50 25 36 18 58 47 GRS80
<br>50 0 0 17 0 0 GRS80

<br> Wszystkie wyniki zostały zaokrąglone do trzeciego miejsca po przecinku w przypadku metrów, zaś w przypadku miar stopniowych - do pięciu. 
<br>
***Znane błędy*** 
<br>
<br> Transformacja BL Krasowski - PL2000/PL1992 da błędne wyniki, gdyż algorytm przejścia został zapisany niepoprawnie. Z tego powodu należy unikać tej transformacji.
<br>
<br> ***Program został przetestowany i nie prezentuje innych nietypowych zachowań, o ile jest użytkowany zgodnie z powyższą instrukcją.***