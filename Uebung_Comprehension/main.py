# --- Vorbereitung ---
# Wir definieren eine Liste mit Zahlen für die Beispiele
zahlen = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# --- 1. List Comprehension mit if-else ---
# Ziel: Eine neue Liste erstellen, die "gerade" für gerade Zahlen und "ungerade" für ungerade Zahlen enthält.

# Klassischer Ansatz (for-Schleife):
liste_klassisch = []
for x in zahlen:
    if x % 2 == 0:
        liste_klassisch.append("gerade")
    else:
        liste_klassisch.append("ungerade")
print("Klassische Liste:", liste_klassisch)

# List Comprehension Ansatz:
# Die Syntax ist: [ausdruck_wenn_wahr if bedingung else ausdruck_wenn_falsch for element in iterierbar]
liste_comprehension = ["gerade" if x % 2 == 0 else "ungerade" for x in zahlen]
print("List Comprehension:", liste_comprehension)
print("-" * 20)


# --- 2. Set Comprehension mit if-else ---
# Ziel: Ein Set (Menge) erstellen, das die quadrierten Werte enthält, aber nur für Zahlen, die größer als 5 sind.
#      Zahlen <= 5 sollen ignoriert werden (was kein echtes else-Szenario im Resultat ist, aber die if-Struktur zeigt).
#      Set-Comprehensions nutzen geschweifte Klammern {}.

# Hinweis: Ein echtes 'else' in einer Set/Dict Comprehension, das *kein* Element hinzufügt, ist nicht direkt möglich.
# Meistens wird 'if-else' in Set/Dict Comprehensions genutzt, um den *Wert* zu transformieren, nicht um das Hinzufügen zu steuern.
# Wenn man nur filtern will (wie hier), nutzt man ein einfaches 'if' am Ende.

# Set-Comprehension (nur Filtern):
set_comprehension = {x**2 for x in zahlen if x > 5}
print("Set Comprehension (nur Filter):", set_comprehension) # Ausgabe: {36, 49, 64, 81, 100}

# Wenn man *unbedingt* ein if-else in der Wert-Transformation möchte (z.B. für Duplikate-Handling):
# Beispiel: Quadrat von x, wenn x > 5, sonst '0' (und 0 wird nur einmal im Set sein)
set_comprehension_else = {x**2 if x > 5 else 0 for x in zahlen}
print("Set Comprehension mit if-else Wert:", set_comprehension_else) # Ausgabe: {0, 64, 36, 100, 49, 81}
print("-" * 20)


# --- 3. Dictionary Comprehension mit if-else ---
# Ziel: Ein Dictionary erstellen, wo der Schlüssel die Zahl ist und der Wert "positiv", wenn x > 5, sonst "klein".
#      Dict-Comprehensions nutzen geschweifte Klammern {} und die key:value Notation.
#      Die Syntax ist ähnlich wie bei List-Comprehension, aber für key:value Paare.

# Dictionary Comprehension Ansatz:
# {key: (wert_wenn_wahr if bedingung else wert_wenn_falsch) for element in iterierbar}
dict_comprehension = {x: ("positiv" if x > 5 else "klein") for x in zahlen}
print("Dict Comprehension:")
for key, value in dict_comprehension.items():
    print(f"  {key}: {value}")

# Ein weiteres Beispiel: Transformierter Schlüssel und Wert
# Ziel: Schlüssel ist "gerade_<zahl>" oder "ungerade_<zahl>", Wert ist das Quadrat
dict_comprehension_2 = {
    (f"gerade_{x}" if x % 2 == 0 else f"ungerade_{x}"): x**2
    for x in zahlen
}
print("\nKomplexere Dict Comprehension:")
for key, value in dict_comprehension_2.items():
    print(f"  {key}: {value}")
print("-" * 20)

print("\nAlle Beispiele erfolgreich ausgeführt!")