import sys
import math


def produce(quantity, chemical, reactions, unused):
    if quantity == 0:
        return 0
    if chemical == "ORE":
        return quantity
    else:
        total = 0
        output_quantity, reactants = reactions[chemical]
        times = math.ceil(quantity / output_quantity)
        wasted = times * output_quantity - quantity
        if wasted > 0:
            unused.setdefault(chemical, 0)
            unused[chemical] += wasted
        for quantity, chemical in reactants:
            required = times * quantity
            if chemical in unused:
                if unused[chemical] > required:
                    unused[chemical] -= required
                    required = 0
                else:
                    required -= unused[chemical]
                    del unused[chemical]
            total += produce(required, chemical, reactions, unused)
        return total


def main():
    reactions = {}
    for line in sys.stdin:
        sources, target = line.strip().split(" => ")
        sources = sources.strip().split(", ")
        output_quantity, target = target.strip().split(" ")
        reactants = []
        for source in sources:
            input_quantity, chemical = source.strip().split(" ")
            reactants.append((int(input_quantity), chemical))
        reactions[target] = (int(output_quantity), reactants)
    print(produce(1, 'FUEL', reactions, {}))


if __name__ == "__main__":
    main()
