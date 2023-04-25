# Informacje dotyczące projektu 

***Program - wymagania do jego uruchomienia***
<br> Przedstawiony program, należy uruchomić za pomocą Python 3.10, został on napisany na systemie operacyjnym Windows 10,
komputer jest wyposażony w kartę graficzną NVIDIA GEFORCE GTX oraz procesor intel CORE i5. 
<br> Po uruchomieniu programu pythonowego: ```projinfa.py```, należy zapoznać się z jego wymaganiami, tzn. : zainstalowaniem biblioteki numpy oraz biblioteki argparse. 
<br>Biblioteka numpy zawiera wiele funkcji i narzędzi do przetwarzania,
analizy i manipulacji dużych danych numerycznych, co pozwala na łatwiejsze posługiwanie się funkcjami matematycznymi. 
Zaś biblioteka argparse pozwala na łatwe parsowanie argumentów wywołania programu z wiersza poleceń, 
umożliwia definiowanie zestawu argumentów, które użytkownik może przekazać do programu podczas jego uruchamiania.  

***Funkcjonalność i posługiwanie się programem*** 
<br>Program służy do transforamcji współrzędnych punktów z jednego układu współrzędnych geodezyjnych na inny. 
<br>W podanym programie przedstawione zostały transformacje ze współrzędnych:
<br> 1) geocentrycznych (XYZ) na elipsoidalne(BLH),
<br> 2) elipsoidalnych (BLH) na geocentryczne (XYZ); 
<br> 3) geocentrycznych (XYZ) na topocentryczne (NEU); 
<br> 4) BL (GRS80, Krasowski, WGS84) na układ 2000;
<br> 5) BL (GRS80, Krasowski, WGS84) na układ 1992; 
<br> Dodatkowo są obsługiwane elispoidy GRS80, Krasowski oraz WGS84.
<br> Elipsoidy charakteryzują się wartościami a oraz e2.
<br> Przy elipsoidzie GRS80 te wartości wynoszą odpowiednio 6378137.000 oraz 0.00669438002290, przy elipsoidzie WGS84
6378137.000 oraz  0.00669437999014, a przy elipsoidzie Krasowskiego 6378245.000 oraz 0.00669342162297.
<br> Przy wprowadzeniu elipsoidy nie wymienionej wyżej program informuje komunikatem "Nieobsługiwana elipsoida!"


<br> ***Używanie programu - przykład***
<br> Program został przetestowany za pomocą wiersza poleceń, aby wprowadzić plik tekstowy do obliczenia wartości
należy posługiwać się nastepującą instrukcją. W pliku tekstowym wartości powinny być oddzielone spacją, w pierwszej 
kolumnie muszą znaleźć się wartości stopniowe kąta phi, w drugiej lambdy, kolejno wysokość oraz nazwa elipsoidy
*Przykład* 
<br>3966086.489 1305184.14 4807557.867 GRS80
<br>2594756.458 1258912.127 5988562.236 GRS80
<br>4662213.222 2465664.45 4635321.796 GRS80
<br>3565612.777 2565640.556 6461121.55 GRS80

<br> Wyniki: 
<br> x = 3721617.690m
<br> y = 1205418.013m
<br> z = 5022429.776m

<br> Wyniki podane są w metrach oraz zostały zaokrąglone do trzeciego miejsca po przecinku. 