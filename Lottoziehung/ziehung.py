import random

def lottoziehung(anzahl=6, max_zahl=45):
    """Zieht 'anzahl' verschiedene Zahlen aus 1..max_zahl."""
    ziehtrommel = list(range(1, max_zahl + 1))
    ende = max_zahl - 1

    for _ in range(anzahl):
        index = random.randint(0, ende)

        # vertauschen der gezogenen Zahl ans Ende des gültigen Bereichs
        ziehtrommel[index], ziehtrommel[ende] = ziehtrommel[ende], ziehtrommel[index]
        ende = ende - 1
    return ziehtrommel[max_zahl - anzahl:]


def statistik (gezogen, stat):
    """Erhöht den Zähler für jede gezogene Zahl im Dictionary"""
    for zahl in gezogen:
        stat[zahl] += 1

def lotto_statistik (anzahl_ziehungen):
    stat = {zahl: 0 for zahl in range(1, 46)}
    for _ in range(anzahl_ziehungen):
        gezogen = lottoziehung()
        statistik(gezogen,stat)
    return stat


if __name__ == "__main__":

    zahlen = lottoziehung()
    print ("Gezogene Zahlen: ", zahlen)

    for n in [1000, 10000, 100000]:
        stat = lotto_statistik(n)
        print(f"\n--- {n} Ziehungen ---")
        for zahl, haeufigkeit in stat.items():
            print(f"{zahl:2d}: {haeufigkeit}")

