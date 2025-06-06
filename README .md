# Vizualizace fraktálů – Mandelbrot a Julia

Tento projekt umožňuje interaktivní vizualizaci fraktálů Mandelbrotovy a Juliovy množiny pomocí knihoven Matplotlib, NumPy a Numba.  
Uživatel má možnost přepínat mezi typy fraktálů, měnit parametry, přibližovat vybranou oblast a vrátit pohled zpět.

## Funkcionalita

- **Zobrazení Mandelbrotovy množiny** – standardní výchozí fraktál
- **Zobrazení Juliovy množiny** – podle volby komplexního parametru c
- **Přiblížení (zoom)** – výběr oblasti tažením myši
- **Reset Zoom** – návrat na výchozí zobrazení
- **Posuvníky Re(c), Im(c)** – určují hodnotu komplexního čísla c pro Juliovu množinu
- **Posuvník počtu iterací** – určuje kvalitu a hloubku výpočtu
- **Optimalizace pomocí knihovny Numba** – urychlení výpočtů paralelizací

## Jak spustit projekt

1. Ujistěte se, že máte nainstalované závislosti:
   ```
   pip install matplotlib numpy numba
   ```
2. V hlavní složce spusťte soubor `main.py`:
   ```
   python3 main.py
   ```

## Struktura projektu

```
vizualizace_fraktalu_final/
├── fraktaly/
│   ├── visualizer.py
│   ├── mandelbrot.py
│   └── julia.py
├── main.py
├── README.md
```

## Popis modulů

- **main.py** – vstupní bod aplikace, volá funkci `run_visualizer`
- **fraktaly/visualizer.py** – spravuje rozhraní, tlačítka, posuvníky a kreslení
- **fraktaly/mandelbrot.py** – obsahuje funkce pro výpočet Mandelbrotovy množiny
- **fraktaly/julia.py** – obsahuje funkce pro výpočet Juliovy množiny

## Ovládání

- Přepínání mezi fraktály: tlačítko **"Mandelbrot / Julia"**
- Změna parametrů Re(c), Im(c): pomocí posuvníků
- Zoom: výběrem oblasti tažením myši
- Reset zobrazení: tlačítko **"Reset Zoom"**

## Cíl projektu

Cílem projektu je umožnit snadnou a rychlou vizualizaci známých matematických fraktálů a zároveň si vyzkoušet práci s grafickým rozhraním v Pythonu, optimalizací výpočtů pomocí Numba a implementací základních interaktivních prvků (GUI).

