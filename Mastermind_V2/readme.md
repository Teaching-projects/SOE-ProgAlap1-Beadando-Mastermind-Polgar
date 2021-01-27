# mastermind_def

```python
def filecheck(filename):
```

Ez a függvény eldönti, hogy megnyitható - e a file `filename` változóban a megnyitandó file neve.

Eredmény:
`True` ha megnyitható (létezik).
`False` ha nem nyitható meg vagy nem létezik.


```python
def setup_game_E(cg):
```

Ez a függvény az egyéni szint működését mutatja be. A játékos döntheti el, hogy hány próbálkozása legyen, hány színt találjon ki, a 7 alapszínhez szeretne – e még hozzáadni színeket. Ezután azt is eldöntheti, hogy egy szín többször is szerepelhet – e a játékban, kér – e statisztikát, valamint azt is, hogy ezeket a beállításokat szeretné – e elmenteni. Ha igen, akkor azokat egy file-ba fogja elmenteni a program.


```python
def setup_game(filename):
```

A függvény alapján a játékos eldöntheti, hogy milyen nehézségi szinten szeretne játszana: kezdő vagy haladó. 
Ha a játékos a kezdő szintet választja, akkor 10 próbálkzása lesz, 4 színt kell kitalálnia az előre megadott 7 színből, 1 színt csak egyszer használhat fel, valamint a játék elején és végén is kap statisztikát. 

Ha a játékos a haladó szintet választja, akkor 15 próbálkozása lesz, 6 színt kell kitalálnia az előre megadott 7 színből, 1 színt többször is felhasználhat, valamint csak a játék végén kap statisztikát.


```python
def load_setup(beallitasok, adatbazis):
```

Ez a függvény ellenőrzi, hogy létezik - e a beallitsok file.
Ha létetik, akkor megnyitja a file-t és megkérdezi, hogy a játékos szeretné - e betölteni az elmentett beállításokat. 
Ha nem szeretné a játékos, akkor elíndítja a septup_game függvényt.
Ha szeretné a játékos, akkor kiírja: "Mentett beállítások betöltése."
Ha nem létezik, akkor elindul a setup_game függvény.

Eredmény: 
A `conf` listát adja vissza, azaz a programbeállítások listáját.


```python
def general(conf, adatbazis):
```

Ez a függvény véletlenszerűen kíválasztja azokat a színeket, amelyeket el kell találnia a játékosnak.

Eredmény:
`a feladvany` lista, amely a véletlenszerűen kiadott színek listája


```python
def check(bevitel, feladvany, conf):
```

Ez a függvény eldönti, hogy a játékos által megadott színek a véletlenszerűen kiválasztott színsorból eltalálta-e a színeket és azok jó helyen vannak-e (OK), 
     vagy eltalálta a színeket, de nem jó helyen vannak (RH), 
     vagy egyáltalan nem találta el a színeket (NO).
       
 Eredmény:
 `checktip` listát adja vissza, ha nyert a játékos
 `True`, ha a játékos vesztett


```python
def szinkod(bevitel, bevitel2, conf):
```

A játékosok által megadott színeket adja meg háttérszínnel és szöveggel.

Eredmény:
egyesíti a stringeket a listában


```python
def tipp(conf, feladvany):
```

Ez a függvény a tippelhető színeket adja meg. Bekéri a játékostól a színeket. 
Ha olyan szintet választott a játékos, ahol 1 színt csak egyszer lehet kiválasztani, akkor a program kiírja, hogy "ezt a színt már tippelted".
Ha olyan színt tippel a játékos, amely nem szerepel a választható színek között, akkor a program ezt írja ki: "Ez a szín nem szerepel a választható színek közt".

Eredmény:
visszaadja a `process` listát vagy
kiírja, hogy `True`


```python
def statisztika(conf, adatbazis):
```

Ez a függvény egy statisztikát készít: a színek hány %-ban forduktak elő.


```python
def mastermind():
```

Ez a függvény maga a játék.
