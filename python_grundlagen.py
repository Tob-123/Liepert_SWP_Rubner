# Prompt an die KI: erstelle einen phyton code wo ganz einfach
# folgende funktionen in phyton dargestellt werden:
#   if, schleifen, break, pass, try except
#   so dass ich sie klar verstehe und mit der code anaylse
#   die schreibweise verstehe.

# Listendaten vorbereiten
eingaben = ["10", "0", "abc", "20", "STOP", "99"]

print("=== Start der Analyse ===")

# 1. FOR-SCHLEIFE: Geht das Array Element für Element durch
for text in eingaben:
    print(f"\nVerarbeite Eingabe: '{text}'")

    # 2. TRY / EXCEPT: Fehler abfangen, falls int() fehlschlägt
    try:
        zahl = int(text)  # Versucht den Text in eine Ganzzahl umzuwandeln

        # 3. IF / ELIF / ELSE: Bedingungen prüfen
        if zahl == 0:
            print("-> Hinweis: Zahl ist Null (wird übersprungen).")
            # 4. PASS: Tut absolut nichts (Platzhalter)
            pass

        elif zahl == 20:
            print("-> Zahl 20 erreicht! Abbruch der Schleife.")
            # 5. BREAK: Beendet die for-Schleife sofort
            break

        else:
            ergebnis = 100 / zahl
            print(f"-> Rechnung: 100 / {zahl} = {ergebnis}")

    except ValueError:
        # Wird ausgeführt, wenn int("abc") fehlschlägt
        print(f"-> Fehler: '{text}' ist keine Zahl!")

print("\n=== Ende des Programms ===")