from typing import Callable, Dict


def mage_counter() -> Callable:
    count = 0

    def inner_count() -> int:
        nonlocal count
        count += 1
        return count

    return inner_count


def spell_accumulator(initial_power: int) -> Callable:
    total = initial_power

    def accumulate_power(amount: int) -> int:
        nonlocal total
        total += amount
        return total

    return accumulate_power


def enchantment_factory(enchantment_type: str) -> Callable:

    def enchantment(item_name: str) -> str:
        return f"{enchantment_type} {item_name}"

    return enchantment


def memory_vault() -> Dict[str, Callable]:
    memory = {}

    def store(key: str, value: str) -> None:
        memory[key] = value

    def recall(key: str) -> str:
        v = memory.get(key)
        if v is not None:
            return v
        else:
            return "Memory not found"

    return {
            "store": store,
            "recall": recall
            }


def main() -> None:
    print("\nTesting mage counter...")
    counter = mage_counter()
    print("Call 1: ", counter())
    print("Call 2: ", counter())
    print("Call 3: ", counter())

    print("\nTesting enchantment factory...")
    fire_enchant = enchantment_factory("Flaming")
    ice_enchant = enchantment_factory("Frozen")
    print(fire_enchant("Sword"))
    print(ice_enchant("Shield"))


if __name__ == "__main__":
    try:
        main()
    except Exception as e:
        print(e)
