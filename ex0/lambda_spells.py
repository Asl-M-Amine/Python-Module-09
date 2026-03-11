from typing import Dict, List


def artifact_sorter(artifacts: List[Dict]) -> List[Dict]:
    return sorted(artifacts, key=lambda x: x['power'], reverse=True)


def power_filter(mages: List[Dict], min_power: int) -> List[Dict]:
    return list(filter(lambda m: m['power'] >= min_power, mages))


def spell_transformer(spells: List[str]) -> List[str]:
    return list(map(lambda s: f"* {s} *", spells))


def mage_stats(mages: List[Dict]) -> Dict:
    if not mages:
        return {'max_power': 0, 'min_power': 0, 'avg_power': 0.0}

    max_p = max(mages, key=lambda m: m['power'])['power']
    min_p = min(mages, key=lambda m: m['power'])['power']
    total_power = sum(map(lambda m: m['power'], mages))
    avg_p = round(total_power / len(mages), 2)

    return {'max_power': max_p, 'min_power': min_p, 'avg_power': avg_p}


def main() -> None:
    artifacts = [
        {'name': "Fire Staff", 'power': 92, 'type': "Legendary"},
        {'name': "Crystal Orb", 'power': 85, 'type': "Epic"}
    ]
    sort_list = artifact_sorter(artifacts)

    print("\nTesting artifact sorter...")
    for i in range(len(sort_list) - 1):
        a = sort_list[i]
        b = sort_list[i + 1]
        print(f"{a['name']} ({a['power']} power) "
              f"comes before {b['name']} ({b['power']} power)")

    spells = ["fireball", "heal", "shield"]
    transformed_list = spell_transformer(spells)
    print("\nTesting spell transformer...")
    for spell in transformed_list:
        print(spell, end=" ")
    print()

    mages = [
        {'name': "Alex", 'power': 80, 'element': "fire"},
        {'name': "Lina", 'power': 40, 'element': "ice"},
        {'name': "Ryu", 'power': 95, 'element': "lightning"}
    ]
    filtered_mages = power_filter(mages, 70)
    print("\nTesting power_filter...")
    if filtered_mages:
        for mage in filtered_mages:
            print(f"{mage['name']} ({mage['power']} power)")
    else:
        print("No mages passed the filter.")

    print("\nTesting mage_stats...")
    stats = mage_stats(mages)
    print(f"Max power: {stats['max_power']}")
    print(f"Min power: {stats['min_power']}")
    print(f"Average power: {stats['avg_power']}")


if __name__ == "__main__":
    try:
        main()
    except Exception as e:
        print(f"Unexpected error: {e}")
