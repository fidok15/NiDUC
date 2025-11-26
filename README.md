# Sensor Voting & Fault Tolerance Simulator

Projekt symuluje system tolerancji bledow w ukladach wieloczujnikowych. Aplikacja generuje sygnal wzorcowy, wprowadza zroznicowane zaklocenia i awarie do czujnikow, a nastepnie przetwarza te dane za pomoca algorytmow glosujacych (Voters), aby odtworzyc poprawny sygnal.

Calosc jest zarzadzana i uruchamiana przy uzyciu menedzera pakietow uv.

## Wymagania

- Python 3.x
- uv (narzedzie do zarzadzania projektem i zaleznosciami)

## Uruchomienie projektu

Projekt wykorzystuje uv do automatycznego zarzadzania srodowiskiem wirtualnym i bibliotekami. Aby uruchomic symulacje, wpisz w terminalu:

uv run main.py

Skrypt automatycznie:
1. Zainstaluje wymagane zaleznosci (jesli ich brakuje, np. numpy, matplotlib).
2. Wygeneruje sygnaly i szum.
3. Przeliczy wyniki dla zaimplementowanych algorytmow (Majority, Weighted, Smoothing).
4. Wyswietli wykresy z wynikami i tabelami statystyk.

## Struktura projektu

Glowna logika programu znajduje sie w katalogu src/, a punktem wejscia jest main.py.

- main.py: Glowny plik sterujacy przeplywem symulacji.
- config.py: Plik konfiguracyjny (liczba czujnikow, parametry szumu, progi bledow).
- src/noise.py: Klasa SensorArray odpowiedzialna za generowanie szumu gaussowskiego oraz wstrzykiwanie awarii.
- src/deafult.py: Generator sygnalu bazowego (funkcja sinus).
- src/calculations.py: Obliczanie metryk niezawodnosci (dostepnosc, bezpieczenstwo, detekcja).
- src/plots.py: Generowanie wykresow przy uzyciu matplotlib.
- src/voters/: Katalog zawierajacy implementacje algorytmow glosujacych (Majority, Weighted, Smoothing).

## Konfiguracja (config.py)

Mozesz dostosowac dzialanie symulacji edytujac zmienne w pliku config.py. Kluczowe parametry:

- NUM_SENSORS: Calkowita liczba czujnikow w systemie.
- NUM_FAULT_SENSORS: Liczba czujnikow, ktore maja ulec awarii.
- EPSILON: Prog tolerancji bledu (decyduje o tym, czy wynik glosowania jest uznany za poprawny wzgledem sygnalu bazowego).
- NORMAL_NOISE_STD: Odchylenie standardowe dla normalnego szumu operacyjnego.
- LARGE_ERROR_BASE: Amplituda duzych bledow (awarii).

## Typy symulowanych awarii

W pliku src/noise.py zaimplementowano trzy rodzaje uszkodzen czujnikow:

1. Ramp: Stopniowy wzrost bledu w czasie (liniowy).
2. Drift: Blad losowy z tendencja do dryfowania w jednym kierunku.
3. Flatten: Wyplaszczenie dynamiki sygnalu (utrata czulosci czujnika).

## Metryki oceny

Dla kazdego votera obliczane sa nastepujace wskazniki statystyczne:

- Dostepnosc (nc/n): Stosunek liczby poprawnych decyzji do wszystkich probek.
- Bezpieczenstwo (nic/n): Stosunek liczby blednych decyzji do wszystkich probek (bledy niewykryte).
- Detekcja (nd/n): Stosunek cykli, w ktorych system nie podjal decyzji (wykryto niespojnosc/brak zaufania).