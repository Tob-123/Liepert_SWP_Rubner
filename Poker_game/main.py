import random
from collections import Counter

SIMULATION_COUNT = 100_000
TOTAL_FIVE_CARD_HANDS = 2_598_960

RANK_NAMES = (
    "2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K", "A"
)
SUIT_NAMES = ("♣", "♦", "♥", "♠")

# Exakte Anzahlen aller 5-Karten-Kombinationen aus einem Standarddeck.
THEORETICAL_COUNTS = {
    "Royal Flush": 4,
    "Straight Flush": 36,
    "Vierling (Poker)": 624,
    "Full House": 3_744,
    "Flush": 5_108,
    "Strasse": 10_200,
    "Drilling": 54_912,
    "Zwei Paare": 123_552,
    "Ein Paar": 1_098_240,
    "High Card": 1_302_540,
}


def build_deck() -> list[int]:
    """Erstellt ein vollstaendiges 52-Karten-Deck (0 bis 51)."""
    return list(range(52))


def draw_hand(deck: list[int]) -> list[int]:
    """Zieht fuenf Karten ohne Zuruecklegen aus dem uebergebenen Deck."""
    hand = [0, 0, 0, 0, 0]

    for i in range(5):
        index = random.randrange(len(deck))
        hand[i] = deck[index]
        # Die gezogene Karte wird durch die letzte Karte ersetzt.
        # Danach wird das letzte Listenelement entfernt: O(1), ohne Verschieben.
        deck[index] = deck[-1]
        deck.pop()

    return hand


def card_rank(card: int) -> int:
    """Gibt den Rangwert (2 bis 14) einer Karte zurueck."""
    return card % 13 + 2


def card_suit(card: int) -> int:
    """Gibt die Farbe (0 bis 3) einer Karte zurueck."""
    return card // 13


def card_to_text(card: int) -> str:
    """Wandelt die kompakte Kartennummer in eine lesbare Karte um."""
    return f"{RANK_NAMES[card % 13]}{SUIT_NAMES[card // 13]}"


def extract_ranks(hand: list[int]) -> list[int]:
    """Extrahiert die Rangwerte einer Hand, aufsteigend sortiert."""
    return sorted(card_rank(card) for card in hand)


def extract_suits(hand: list[int]) -> list[int]:
    """Extrahiert die Farben einer Hand."""
    return [card_suit(card) for card in hand]


def rank_counts_desc(ranks: list[int]) -> list[int]:
    """Zaehlt, wie oft jeder Rangwert vorkommt, absteigend sortiert."""
    return sorted(Counter(ranks).values(), reverse=True)


def is_flush(suits: list[int]) -> bool:
    """Prueft, ob alle fuenf Karten dieselbe Farbe haben."""
    return suits.count(suits[0]) == 5


def is_wheel(ranks: list[int]) -> bool:
    """Prueft auf die Spezial-Strasse Ass-2-3-4-5 (Ass zaehlt niedrig)."""
    return ranks == [2, 3, 4, 5, 14]


def is_straight(ranks: list[int]) -> bool:
    """Prueft, ob die Rangwerte eine Strasse bilden."""
    is_sequential = ranks[4] - ranks[0] == 4 and len(set(ranks)) == 5
    return is_sequential or is_wheel(ranks)


def is_royal_flush(ranks: list[int]) -> bool:
    """Prueft, ob die Rangwerte 10 bis Ass ergeben."""
    return ranks == [10, 11, 12, 13, 14]


def classify_hand(hand: list[int]) -> str:
    """Ordnet eine 5-Karten-Hand genau einer Pokerkombination zu."""
    ranks = extract_ranks(hand)
    suits = extract_suits(hand)
    counts = rank_counts_desc(ranks)
    flush = is_flush(suits)
    straight = is_straight(ranks)

    if straight and flush:
        return "Royal Flush" if is_royal_flush(ranks) else "Straight Flush"
    if counts[0] == 4:
        return "Vierling (Poker)"
    if counts == [3, 2]:
        return "Full House"
    if flush:
        return "Flush"
    if straight:
        return "Strasse"
    if counts[0] == 3:
        return "Drilling"
    if counts == [2, 2, 1]:
        return "Zwei Paare"
    if counts[0] == 2:
        return "Ein Paar"
    return "High Card"


def format_hand(hand: list[int]) -> str:
    """Formatiert eine Hand als kommagetrennte Liste lesbarer Karten."""
    return ", ".join(map(card_to_text, hand))


def print_sample_hand(hand: list[int]) -> None:
    """Gibt eine Beispielhand und ihre Kombination auf der Konsole aus."""
    print("Zufaellige Beispielhand:", format_hand(hand))
    print("Kombination:", classify_hand(hand))


def run_simulation(deck: list[int], count: int) -> dict[str, int]:
    """Simuliert `count` Pokerhaende und zaehlt die Haeufigkeit jeder Kombination."""
    statistics = dict.fromkeys(THEORETICAL_COUNTS, 0)

    for _ in range(count):
        hand = draw_hand(deck)
        statistics[classify_hand(hand)] += 1
        deck.extend(hand)  # Deck wieder vervollstaendigen, ohne es neu aufzubauen.

    return statistics


def print_result(name: str, counts: dict[str, int]) -> None:
    """Gibt eine Statistikzeile fuer eine einzelne Kombination aus."""
    amount = counts[name]
    measured = amount * 100 / SIMULATION_COUNT
    expected = THEORETICAL_COUNTS[name] * 100 / TOTAL_FIVE_CARD_HANDS
    difference = measured - expected
    print(
        f"{name:<19} {amount:>8} "
        f"{measured:>10.5f}% {expected:>10.5f}% {difference:>+10.5f}%"
    )


def print_statistics_header() -> None:
    """Gibt die Tabellenueberschrift der Statistikausgabe aus."""
    print(
        f"{'Kombination':<19} {'Anzahl':>8} "
        f"{'Simulation':>11} {'Theorie':>11} {'Abweichung':>12}"
    )
    print("-" * 66)


def print_statistics_table(statistics: dict[str, int]) -> None:
    """Gibt die vollstaendige Statistiktabelle fuer alle Kombinationen aus."""
    print(f"\nStatistik nach {SIMULATION_COUNT:,} simulierten Haenden")
    print_statistics_header()
    for name in THEORETICAL_COUNTS:
        print_result(name, statistics)


def main() -> None:
    deck = build_deck()

    sample_hand = draw_hand(deck)
    deck.extend(sample_hand)  # Die fuenf Karten kommen zurueck ins Deck.
    print_sample_hand(sample_hand)

    statistics = run_simulation(deck, SIMULATION_COUNT)
    print_statistics_table(statistics)


if __name__ == "__main__":
    main()
