import sys, os
this_file = os.path.abspath(__file__)
project_root = os.path.abspath(os.path.join(os.path.dirname(this_file), '..'))
if project_root not in sys.path:
    sys.path.insert(0, project_root)

import backend.materials.ingot as ingot
import backend.materials.polish as polish
import backend.materials.pigment as pigment
import backend.materials.materials as materials
import backend.materials.oil as oil
import backend.materials.lumber as lumber
import backend.materials.fabric as fabric
import backend.materials.machine as machine
import backend.materials.scroll as scroll
import backend.materials.equip as equip
import backend.materials.glider as glider

global_price = {
    materials.OnyxArcheumEssence() : 2.3,
    materials.IronOre() : 0.35,
    materials.CopperOre() : 2,
    materials.SliverOre() : 0.28,
    materials.OnyxArcheumEssence() : 2.75,
    materials.Azalea() : 0.10,
    materials.Narcissus() : 0.11,
    materials.MysteriousGardenPowder() : 2.6,
    materials.Lotus() : 0.20,
    materials.Oats() : 0.18,
    materials.AntlerCoral() : 0.80
}

global_use_en = False

def CalculatePrice(items:list):
    price = 0
    for item in items:
        price += CalculateSinglePrice(item)
    return int(price)

def CalculateSinglePrice(item:tuple):
    price = float(0)
    if item[0] in global_price:
        price += global_price[item[0]] * item[1]
    return round(price, 2)

def PrintNeededAndPrice(input:dict):
    output = dict()
    for key, val in input.items():
        output.setdefault(key.level, list()).append((key, val))
    for line in sorted(output.items()):
        print(line[0],
                [(lambda x:f"{materials.GetItemNameFromId(x[0].id, global_use_en)}:{x[1]}({CalculateSinglePrice(x)}g)")(item) for item in line[1]],
                f"{CalculatePrice(line[1])}g\n")

def PrintTopology(input:dict):
    for line in sorted(input.items()):
        # print(line[0], [(lambda x : f"{materials.GetItemNameFromId(x[0].id, global_use_en)}({materials.GetItemNameFromId(x[0].id)}):{x[1]}({CalculateSinglePrice(x)}g)")(item) for item in line[1].items()],
        # f"{CalculatePrice(line[1].items())}g\n")
        items = {k: line[1][k] for k in sorted(line[1])}
        print(line[0], [(lambda x : f"{materials.GetItemNameFromId(x[0].id, global_use_en)}:{x[1]}({CalculateSinglePrice(x)}g)")(item) for item in items.items()],
        f"{CalculatePrice(line[1].items())}g\n")

def CombineItem(needed:dict):
    class Tmp(materials.Meterial):
        item_id = materials.GetNextGlobalId()
        def __init__(self) -> None:
            super().__init__(self.item_id, needed, 10)
            materials.RegisterName(self.item_id, "tmp", "tmp")

    return Tmp()

if __name__ == '__main__':
    # oil=oil.SmallSeedOil()
    # ret = oil.Calculate(2, not_need=[])
    # item = ingot.BlazingSunridgeIngot()
    # item = machine.HighPowerEngine()
    # item = scroll.ScrollSeawhipSpeedboat()
    # item = polish.OpaquePolish()
    # item = ingot.SturdyIngot()
    # item = scroll.ScrollS200Lite()
    item = scroll.ScrollToothedEdgeSkateboard()
    # item = equip.RadiantDawnsdropBoots()
    # item = glider.HeighGliderFramework()
    topology = item.TopologyV2(1, not_need={glider.SummerWindGlider()})
    PrintTopology(topology)
    print("-----------------TopologyV2-------------------------")

    topology = item.TopologyV3(1, not_need={glider.SummerWindGlider()})
    PrintTopology(topology)
    print("-----------------TopologyV3-------------------------")

    # combine = CombineItem({lumber.FineLumber(): 150,
    #                         fabric.BeautifullyColoredFabric(): 200,
    #                         pigment.SoftStemPigment(): 10})
    # PrintTopology(combine.TopologyV2(1))