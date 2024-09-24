*[Název]*


[Název] je aplikace pro zpětné testování akcií na základě uživatelsky definovaných parametrů. Umožňuje uživatelům zvolit si klíčové finanční ukazatele a strategie, které chtějí otestovat na historických datech, a poskytuje přehledné výsledky, které jim pomohou zhodnotit výkonnost vybraných akcií v minulosti. Cílem aplikace je zefektivnit analýzu investičních strategií a nabídnout uživatelům jednoduchý nástroj pro simulaci jejich obchodních rozhodnutí.

Funkce:
Zpětné testování akcií na základě historických dat
Možnost volby různých ukazatelů (např. ROIC, P/E ratio)
Vizuální zobrazení výkonnosti strategie
Možnost úpravy a optimalizace vstupních parametrů
Úpráva váhy akcie v portfoliu (Scoring systém)
Generování reportů s výsledky zpětného testování
kalendář událostí
možnost stažení výsledků 
Sdílení portfolia/strategie s ostatními uživateli
Určit období backtestu
Historie všech ukazatelů dané společnosti

Co se tím naučím:
Práce s vekým množstvím finančních dat a jejich analýzou
Základy algoritmického obchodování a tvorba obchodních strategií
Použití knihoven pro práci s daty v Pythonu (např. pandas, matplotlib)
Vytvoření uživatelsky přívětivého rozhraní pro aplikaci
Jak provádět backtesting a interpretovat výsledky z pohledu investičních strategií


Cíl: 
-Sociální síť pro sdílení strategií
-Chci klást velký důraz na vzhled aplikace 
-Pomoct uživatelům se lépe rozhodovat díky historickým datům


Technologie:
Django
Python 
yfinance
PyTorch
randál dalších 

Konkurence, inspirace:
Simfin
Danelfin

ČASOVÝ HARMONOGRAM

Září:
Získání a implementace všech potřebných historických dat do backendu
Návrh struktury databáze pro uchování dat
Implementace základních funkcí pro správu a načítání dat
Testování správnosti a kompletnosti získaných dat
Říjen:
Výběr akcií do portfolia na základě zvolených ukazatelů (např. ROIC, P/E ratio)
Vývoj algoritmu pro zpětné testování vybraných akcií
Implementace funkcí pro zadávání uživatelských parametrů (časový horizont, typ strategie)
Návrh rozhraní pro vizualizaci výsledků zpětného testování
Listopad:
Optimalizace algoritmu zpětného testování pro rychlejší a přesnější výpočty
Testování aplikace s různými strategiemi a portfolii
Implementace generování reportů s výsledky testů
Průběžné ladění aplikace na základě testů a zpětné vazby
Prosinec:
Finalizace uživatelského rozhraní a přidání detailních grafů a přehledů
Dokončení dokumentace aplikace včetně uživatelského manuálu
Příprava finální prezentace projektu
Závěrečné testování a opravy případných chyb

Myšlenky, co mě napadaj o půl noci: 
V investicích jsou 2 strany, velcí hráči(instituce) a drobní investoři. Ten,kdo má lepší informovanost o společnostech není pochyb. 
Když už hledám já informace ohledně nějaké společnosti do které bych potenciálně mohl investovat, musím projít několik stránek.Věřím, že mě i ostatním investorům by pomohlo, kdyby alespoň část jejich procesu hledání informací byla na jednom místě, o to se chci pokusit.


Instalace
Klonování repozitáře
git clone https://github.com/Vojtik1/Rocnik.git
Přesun do adresáře webu
python -m venv .venv
Vytvoření virtuálního prostředí do složky .venv
python -m venv .venv
Aktivace virtuálního prostředí
.venv\Scripts\activate
Instalace závislostí
pip install -r requirements.txt
Spuštění aplikace
python manage.py runserver
Přístupové údaje do administrace
superuživatel: admin
heslo: admin
