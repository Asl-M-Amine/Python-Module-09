from typing import Callable, Tuple


def spell_combiner(spell1: Callable, spell2: Callable) -> Callable:
    if not callable(spell1) or not callable(spell2):
        raise TypeError("spell1 and spell2 must be callable functions")

    def combined_spell(target: str) -> Tuple[str, str]:
        s1 = spell1(target)
        s2 = spell2(target)
        return s1, s2

    return combined_spell


def power_amplifier(base_spell: Callable, multiplier: int) -> Callable:
    if not callable(base_spell):
        raise TypeError("base_spell must be a callable function")
    if not isinstance(multiplier, int):
        raise TypeError("multiplier must be a integer")

    def amplified_spell(target: str) -> int:
        result = base_spell(target)
        return result * multiplier

    return amplified_spell


def conditional_caster(condition: Callable, spell: Callable) -> Callable:
    if not callable(condition) or not callable(spell):
        raise TypeError("condition and spell must be callable functions")

    def conditional_spell(target: str) -> str:
        if condition(target):
            return spell(target)
        return "Spell fizzled"

    return conditional_spell


def spell_sequence(spells: list[Callable]) -> Callable:
    if not all(callable(s) for s in spells):
        raise TypeError("All items in spells must be callable functions")

    def sequence(target: str) -> list[str]:
        results = [s(target) for s in spells]
        return results

    return sequence


def main() -> None:
    def fireball(target: str) -> str:
        return f"fireball hits {target}"

    def heal(target: str) -> str:
        return f"heal {target}"
    combined = spell_combiner(fireball, heal)
    res = combined("Dragon")
    print("\nTesting spell combiner...")
    print(f"Combined spell result: {res[0]}, {res[1]}\n")

    print("Testing power amplifier...")
    value = 10

    def fireball(target: str) -> int:
        return value

    mega_fireball = power_amplifier(fireball, 3)
    print(f"Original: {value}, Amplified: {mega_fireball('Dragon')}")


if __name__ == "__main__":
    try:
        main()
    except Exception as e:
        print(e)
