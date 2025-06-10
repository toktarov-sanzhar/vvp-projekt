# Fraktální vizualizace (Projekt pro Vědecké výpočty v Pythonu)

Tento projekt slouží jako interaktivní nástroj pro vizualizaci fraktálů – konkrétně Mandelbrotovy množiny a Juliiho množin.

## Struktura projektu

```
vvp_projekt/
├── fraktaly/
│   ├── __init__.py
│   ├── julia.py
│   ├── mandelbrot.py
│   └── visualizer.py
├── example_fractals.ipynb
├── setup.py
└── README.md
```

## Popis

- `julia.py`: obsahuje výpočet Juliiho množin
- `mandelbrot.py`: obsahuje výpočet Mandelbrotovy množiny
- `visualizer.py`: interaktivní rozhraní s posuvníky a tlačítky
- `example_fractals.ipynb`: ukázkový Jupyter notebook s interaktivním GUI a statickými obrázky
- `setup.py`: soubor pro instalaci balíčku pomocí `pip install -e .`

## Spuštění

Tento projekt je určen k použití v prostředí Jupyter Notebook. Není určen k přímému spouštění přes terminál.

### Doporučený způsob:

1. V kořenové složce projektu spusťte příkaz:

```
pip install -e .
```

2. Poté spusťte Jupyter Notebook:

```
jupyter notebook
```

3. Otevřete soubor `example_fractals.ipynb` a spusťte jednotlivé buňky pro zobrazení fraktálů a spuštění interaktivního nástroje.