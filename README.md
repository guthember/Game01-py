# Game01-py
Python game for beginner school

## 1. Szöveges megjelenítés a játék menetéről
- Információk képernyőre írása (*szabaly.txt*)
    - "---> Üdvözöllek játékos <---"
    - "----------------------------"
    - A játék célja, hogy átjuss három szobán az ajtókon keresztül."
    - "Minden szobában két ajtó van. Választanod kell közülük!"
    - "Van olyan ajtó, ami mögött csapda van és ha azon belépsz 10 életpontot veszítesz."
    - "A játék célja, hogy átjuss mind a három szobán!" 
    - "Az ajtó választását az '1' vagy '2' gombbal teheted meg."
- **print** utasítás használata

## 2. Játékos életerejének nyilvántartása
- változó bevezetése
- egész típus, értékadás
- változó értékének kiíratása a képernyőre

## 3. A játék kezdete, az első szoba
- a játékos választása -> adatbekérés a felhasználótól
- feltételezzük, hogy helyes adatot ad meg (nem kell hibakezelés)
- szöveges típus
- konvertálás 

## 4. Melyik ajtó mögött van a csapda?
- véletlenszám generálás -> random modul használata
- **randint** használata
- ellenőrzésképpen a csapda helyének kiírása

## 5. Beleléptünk-e a csapdába vagy nem?
- feltételes szerkezet használat
- egyszerű feltétel, 2 lehetőség
- intendálás

## 6. Ha csapdába léptünk
- változó értékének változtatása
- életerő aktualizálása

## 7. További két szobán való áthaladás
- további játék a szobákon át