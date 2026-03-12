from typing import List, Dict, Callable
import functools
import operator
from functools import singledispatch


def spell_reducer(spells: List[int], operation: str) -> int:
    ops = {
        "add": operator.add,
        "multiply": operator.mul,
        "max": max,
        "min": min
    }

    if operation not in ops:
        raise ValueError(f"Unsupported operation: {operation}")

    return functools.reduce(ops[operation], spells)


def partial_enchanter(base_enchantment: Callable) -> Dict[str, Callable]:
    return {
        "fire_enchant": functools.partial(base_enchantment, 50, "fire"),
        "ice_enchant": functools.partial(base_enchantment, 50, "ice"),
        "lightning_enchant": functools.partial(base_enchantment, 50, "lightning"),
    }


@functools.lru_cache(maxsize=None)
def memoized_fibonacci(n: int) -> int:
    if n <= 0:
        return 0
    elif n == 1:
        return 1
    return memoized_fibonacci(n - 1) + memoized_fibonacci(n - 2)


def spell_dispatcher() -> Callable:
    @singledispatch
    def cast(spell):
        return f"Unknown spell type: {spell}"

    @cast.register
    def _(spell: int):
        return f"Damage spell deals {spell} points!"

    @cast.register
    def _(spell: str):
        return f"Enchantment spell: {spell}"

    @cast.register
    def _(spell: list):
        results = [cast(s) for s in spell]
        return f"Multi-cast: {results}"

    return cast


def main() -> None:
    print("\nTesting spell reducer...")
    spells = [10, 20, 30, 40]
    sum_result = spell_reducer(spells, "add")
    product_result = spell_reducer(spells, "multiply")
    max_result = spell_reducer(spells, "max")
    print(f"Sum: {sum_result}")
    print(f"Product: {product_result}")
    print(f"Max: {max_result}")

    print("\nTesting memoized fibonacci...")
    fib1 = 10
    fib2 = 15
    print(f"Fib({fib1}): {memoized_fibonacci(fib1)}")
    print(f"Fib({fib2}): {memoized_fibonacci(fib2)}")


if __name__ == "__main__":
    try:
        main()
    except Exception as e:
        print(e)
