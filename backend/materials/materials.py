from typing import List, Tuple, Dict, Set, Optional, Union, Any

global_item_ch_name = dict()

global_item_en_name = dict()

global_item_id = 0

def GetNextGlobalId() ->int:
    global global_item_id
    ret = global_item_id
    global_item_id += 1
    return ret

def RegisterName(id:int, en_name:str, ch_name:str):
    global_item_en_name[id] = en_name
    global_item_ch_name[id] = ch_name

def GetItemNameFromId(id:int, is_en:bool = True):
    if is_en:
        if id in global_item_en_name:
            return global_item_en_name[id]
    else:
        if id in global_item_ch_name:
            return global_item_ch_name[id]
    return "unknow"

class Meterial:
    # item_id = int()
    def __init__(self, id:int, neededs: Dict[Any, int], level:int) -> None:
        self.neededs = neededs
        self.level = level
        self.id = id

    def _Topology(need:Dict[Any, int], cur_layer: int = 0, not_need=set(), ouput: Dict[int, Dict[Any, int]]=dict()):
        cur_needed = ouput.setdefault(cur_layer, dict())
        for material, cnt in need.items():
            if material in not_need: continue

            cur_needed.setdefault(material, 0)
            cur_needed[material] += cnt
            if material.neededs is None:
                continue
            new_neededs = {k: v * cnt for k, v in material.neededs.items()}
            Meterial._Topology(new_neededs, cur_layer + 1, ouput=ouput)

    def TopologyV2(self, cnt:int, not_need=set(), cur_layer=0)->Dict[int, Dict[Any, int]]:
        output = dict()
        # new_neededs = {k: v * cnt for k, v in self.neededs.items()}
        Meterial._Topology({self: cnt}, 0, not_need, output)

        final_need = dict()
        for layer, materials in output.items():
            for material, cnt in materials.items():
                if material.neededs is not None:
                    continue
                final_need.setdefault(material, 0)
                final_need[material] += cnt
        output[len(output)]={k: final_need[k] for k in sorted(final_need)}
        return output

    def TopologyV3(self, cnt:int, not_need=set(), cur_layer=0)->Dict[int, Dict[Any, int]]:
        output:Dict[int, Dict[Meterial, int]] = {}
        # new_neededs = {k: v * cnt for k, v in self.neededs.items()}
        Meterial._Topology({self: cnt}, 0, not_need, output)

        last_layer = dict()
        for layer, materials in output.items():
            for material, cnt in last_layer.items():
                if material in materials:
                    materials[material] += cnt
                else:
                    materials[material] = cnt
            materials = {k: materials[k] for k in sorted(materials)}
            last_layer.clear()
            for material, cnt in materials.items():
                if material.neededs is None:
                    last_layer[material] = cnt

        return output

    def __hash__(self):
        return hash(self.id)

    def __eq__(self, other):
        if isinstance(other, Meterial):
            return self.id == other.id
        return False

    def __lt__(self, other):
        if isinstance(other, Meterial):
            return self.id < other.id
        return False

class Template(Meterial):
    item_id = GetNextGlobalId()
    def __init__(self) -> None:
        super().__init__(self.item_id, None, 1)
        RegisterName(self.item_id, "tmp", "tmp")

class IronOre(Meterial):
    item_id = GetNextGlobalId()
    def __init__(self) -> None:
        super().__init__(self.item_id, None, 1)
        RegisterName(self.item_id, "Iron Ore", "铁矿石")

class CopperOre(Meterial):
    item_id = GetNextGlobalId()
    def __init__(self) -> None:
        super().__init__(self.item_id, None, 1)
        RegisterName(self.item_id, "Copper Ore", "铜矿石")

class SliverOre(Meterial):
    item_id = GetNextGlobalId()
    def __init__(self) -> None:
        super().__init__(self.item_id, None, 1)
        RegisterName(self.item_id, "Sliver Ore", "银矿石")

class GoldOre(Meterial):
    item_id = GetNextGlobalId()
    def __init__(self) -> None:
        super().__init__(self.item_id, None, 1)
        RegisterName(self.item_id, "Gold Ore", "金矿石")

class ArcheumOre(Meterial):
    item_id = GetNextGlobalId()
    def __init__(self) -> None:
        super().__init__(self.item_id, None, 1)
        RegisterName(self.item_id, "Archeum Ore", "源晶矿")

class Log(Meterial):
    item_id = GetNextGlobalId()
    def __init__(self) -> None:
        super().__init__(self.item_id, None, 1)
        RegisterName(self.item_id, "Log", "原木")

class Rice(Meterial):
    item_id = GetNextGlobalId()
    def __init__(self) -> None:
        super().__init__(self.item_id, None, 1)
        RegisterName(self.item_id, "Rice", "大米")

class Corn(Meterial):
    item_id = GetNextGlobalId()
    def __init__(self) -> None:
        super().__init__(self.item_id, None, 1)
        RegisterName(self.item_id, "Corn", "玉米")

class OnyxArcheumEssence(Meterial):
    item_id = GetNextGlobalId()
    def __init__(self) -> None:
        super().__init__(self.item_id, None, 1)
        RegisterName(self.item_id, "Onyx Archeum Essence", "黑色源晶精华")

class ThunderStruckTree(Meterial):
    item_id = GetNextGlobalId()
    def __init__(self) -> None:
        super().__init__(self.item_id, None, 1)
        RegisterName(self.item_id, "Thunder Struck Tree", "雷击木")

class ThunderStruckLog(Meterial):
    item_id = GetNextGlobalId()
    def __init__(self) -> None:
        super().__init__(self.item_id, None, 1)
        RegisterName(self.item_id, "Thunder Struck Log", "雷击树杈")

class FlamingLog(Meterial):
    item_id = GetNextGlobalId()
    def __init__(self) -> None:
        super().__init__(self.item_id, None, 1)
        RegisterName(self.item_id, "Flaming Log", "烈火原木")

class MysteriousGardenPowder(Meterial):
    item_id = GetNextGlobalId()
    def __init__(self) -> None:
        super().__init__(self.item_id, None, 1)
        RegisterName(self.item_id, "Mysterious Garden Powder", "庭院神秘粉末")

class Azalea(Meterial):
    item_id = GetNextGlobalId()
    def __init__(self) -> None:
        super().__init__(self.item_id, None, 1)
        RegisterName(self.item_id, "Azalea", "映山红")

class Narcissus(Meterial):
    item_id = GetNextGlobalId()
    def __init__(self) -> None:
        super().__init__(self.item_id, None, 1)
        RegisterName(self.item_id, "Narcissus", "水仙花")

class Lotus(Meterial):
    item_id = GetNextGlobalId()
    def __init__(self) -> None:
        super().__init__(self.item_id, None, 1)
        RegisterName(self.item_id, "Lotus", "莲花")

class Oats(Meterial):
    item_id = GetNextGlobalId()
    def __init__(self) -> None:
        super().__init__(self.item_id, None, 1)
        RegisterName(self.item_id, "Oats", "燕麦")

class AntlerCoral(Meterial):
    item_id = GetNextGlobalId()
    def __init__(self) -> None:
        super().__init__(self.item_id, None, 1)
        RegisterName(self.item_id, "Antler Coral", "鹿角型珊瑚草")

class ChiliPepper(Meterial):
    item_id = GetNextGlobalId()
    def __init__(self) -> None:
        super().__init__(self.item_id, None, 1)
        RegisterName(self.item_id, "Chili Pepper", "红辣椒")

class Rosemary(Meterial):
    item_id = GetNextGlobalId()
    def __init__(self) -> None:
        super().__init__(self.item_id, None, 1)
        RegisterName(self.item_id, "Rosemary", "迷迭香")

class Pearl(Meterial):
    item_id = GetNextGlobalId()
    def __init__(self) -> None:
        super().__init__(self.item_id, None, 1)
        RegisterName(self.item_id, "Pearl", "黑珍珠")

class BlueBerry(Meterial):
    item_id = GetNextGlobalId()
    def __init__(self) -> None:
        super().__init__(self.item_id, None, 1)
        RegisterName(self.item_id, "Blue Berry", "蓝莓")

class DragonEssenceStabilizer(Meterial):
    item_id = GetNextGlobalId()
    def __init__(self) -> None:
        super().__init__(self.item_id, None, 1)
        RegisterName(self.item_id, "Dragon Essence Stabilizer", "龙骨精华")

class Turmeric(Meterial):
    item_id = GetNextGlobalId()
    def __init__(self) -> None:
        super().__init__(self.item_id, None, 1)
        RegisterName(self.item_id, "Turmeric", "姜黄")

class Cactus(Meterial):
    item_id = GetNextGlobalId()
    def __init__(self) -> None:
        super().__init__(self.item_id, None, 1)
        RegisterName(self.item_id, "Cactus", "仙人掌")

class SparklingShellDust(Meterial):
    item_id = GetNextGlobalId()
    def __init__(self) -> None:
        super().__init__(self.item_id, None, 1)
        RegisterName(self.item_id, "Sparkling Shell Dust", "浪花结晶")

class BeeChnut(Meterial):
    item_id = GetNextGlobalId()
    def __init__(self) -> None:
        super().__init__(self.item_id, None, 1)
        RegisterName(self.item_id, "BeeChnut", "山毛榉")

class Peanut(Meterial):
    item_id = GetNextGlobalId()
    def __init__(self) -> None:
        super().__init__(self.item_id, None, 1)
        RegisterName(self.item_id, "Peanut", "花生")

class Wheat(Meterial):
    item_id = GetNextGlobalId()
    def __init__(self) -> None:
        super().__init__(self.item_id, None, 1)
        RegisterName(self.item_id, "Wheat", "小麦")

class RedCoral(Meterial):
    item_id = GetNextGlobalId()
    def __init__(self) -> None:
        super().__init__(self.item_id, None, 1)
        RegisterName(self.item_id, "Red Coral", "红色珊瑚")

class Bean(Meterial):
    item_id = GetNextGlobalId()
    def __init__(self) -> None:
        super().__init__(self.item_id, None, 1)
        RegisterName(self.item_id, "Bean", "大豆")

class Rye(Meterial):
    item_id = GetNextGlobalId()
    def __init__(self) -> None:
        super().__init__(self.item_id, None, 1)
        RegisterName(self.item_id, "Rye", "黑麦")

class Vanilla(Meterial):
    item_id = GetNextGlobalId()
    def __init__(self) -> None:
        super().__init__(self.item_id, None, 1)
        RegisterName(self.item_id, "Vanilla", "香草")

class Quinoa(Meterial):
    item_id = GetNextGlobalId()
    def __init__(self) -> None:
        super().__init__(self.item_id, None, 1)
        RegisterName(self.item_id, "Quinoa", "?麦")

class CultivatedGinseng(Meterial):
    item_id = GetNextGlobalId()
    def __init__(self) -> None:
        super().__init__(self.item_id, None, 1)
        RegisterName(self.item_id, "Gultivated Ginseng", "长脑人参")

class Coconut(Meterial):
    item_id = GetNextGlobalId()
    def __init__(self) -> None:
        super().__init__(self.item_id, None, 1)
        RegisterName(self.item_id, "Coconut", "椰子")

class Clover(Meterial):
    item_id = GetNextGlobalId()
    def __init__(self) -> None:
        super().__init__(self.item_id, None, 1)
        RegisterName(self.item_id, "Clover", "四叶草")

class Rose(Meterial):
    item_id = GetNextGlobalId()
    def __init__(self) -> None:
        super().__init__(self.item_id, None, 1)
        RegisterName(self.item_id, "Rose", "玫瑰")

class CornFlower(Meterial):
    item_id = GetNextGlobalId()
    def __init__(self) -> None:
        super().__init__(self.item_id, None, 1)
        RegisterName(self.item_id, "Corn Flower", "矢车菊")

class Lily(Meterial):
    item_id = GetNextGlobalId()
    def __init__(self) -> None:
        super().__init__(self.item_id, None, 1)
        RegisterName(self.item_id, "Lily", "百合")

class GreenCoral(Meterial):
    item_id = GetNextGlobalId()
    def __init__(self) -> None:
        super().__init__(self.item_id, None, 1)
        RegisterName(self.item_id, "Green Coral", "绿色珊瑚草")

class Mint(Meterial):
    item_id = GetNextGlobalId()
    def __init__(self) -> None:
        super().__init__(self.item_id, None, 1)
        RegisterName(self.item_id, "Mint", "薄荷")

class Pepper(Meterial):
    item_id = GetNextGlobalId()
    def __init__(self) -> None:
        super().__init__(self.item_id, None, 1)
        RegisterName(self.item_id, "Pepper", "胡椒")

class Poppy(Meterial):
    item_id = GetNextGlobalId()
    def __init__(self) -> None:
        super().__init__(self.item_id, None, 1)
        RegisterName(self.item_id, "Poppy", "罂粟")

class Saffron(Meterial):
    item_id = GetNextGlobalId()
    def __init__(self) -> None:
        super().__init__(self.item_id, None, 1)
        RegisterName(self.item_id, "Saffron", "藏红花")

class Chestnut(Meterial):
    item_id = GetNextGlobalId()
    def __init__(self) -> None:
        super().__init__(self.item_id, None, 1)
        RegisterName(self.item_id, "Chestnut", "板栗")

class AnyaPebble(Meterial):
    item_id = GetNextGlobalId()
    def __init__(self) -> None:
        super().__init__(self.item_id, None, 1)
        RegisterName(self.item_id, "Anya Pebble", "Anya 卵石")

class Wool(Meterial):
    item_id = GetNextGlobalId()
    def __init__(self) -> None:
        super().__init__(self.item_id, None, 1)
        RegisterName(self.item_id, "Wool", "绵羊毛")

class Pelt(Meterial):
    item_id = GetNextGlobalId()
    def __init__(self) -> None:
        super().__init__(self.item_id, None, 1)
        RegisterName(self.item_id, "Pelt", "原皮")

class Diamond(Meterial):
    item_id = GetNextGlobalId()
    def __init__(self) -> None:
        super().__init__(self.item_id, None, 1)
        RegisterName(self.item_id, "Diamond", "钻石")

class MoonlightArcheumCrystal(Meterial):
    item_id = GetNextGlobalId()
    def __init__(self) -> None:
        super().__init__(self.item_id, None, 1)
        RegisterName(self.item_id, "Moonlight Archeum Crystal", "防具源晶精华")

class Eel(Meterial):
    item_id = GetNextGlobalId()
    def __init__(self) -> None:
        super().__init__(self.item_id, None, 1)
        RegisterName(self.item_id, "Eel", "鳗鱼")

class HandicraftYarn(Meterial):
    item_id = GetNextGlobalId()
    def __init__(self) -> None:
        super().__init__(self.item_id, None, 1)
        RegisterName(self.item_id, "Handicraft Yarn", "手工绒线")

class Stingray(Meterial):
    item_id = GetNextGlobalId()
    def __init__(self) -> None:
        super().__init__(self.item_id, None, 1)
        RegisterName(self.item_id, "Stingray", "黄貂鱼")

class GlacierGrayfish(Meterial):
    item_id = GetNextGlobalId()
    def __init__(self) -> None:
        super().__init__(self.item_id, None, 1)
        RegisterName(self.item_id, "Glacier Grayfish", "冰川灰鱼")

class Bamboo(Meterial):
    item_id = GetNextGlobalId()
    def __init__(self) -> None:
        super().__init__(self.item_id, None, 1)
        RegisterName(self.item_id, "Bamboo", "竹子")

class FloatingStones(Meterial):
    item_id = GetNextGlobalId()
    def __init__(self) -> None:
        super().__init__(self.item_id, None, 1)
        RegisterName(self.item_id, "FloatingStones", "浮游石")

class FishOil(Meterial):
    item_id = GetNextGlobalId()
    def __init__(self) -> None:
        super().__init__(self.item_id, None, 1)
        RegisterName(self.item_id, "fish oil", "水银色鱼油")

class NaturalRubber(Meterial):
    item_id = GetNextGlobalId()
    def __init__(self) -> None:
        super().__init__(self.item_id, None, 1)
        RegisterName(self.item_id, "Natural rubber", "天然橡胶")

class YuanJingmu(Meterial):
    item_id = GetNextGlobalId()
    def __init__(self) -> None:
        super().__init__(self.item_id, None, 1)
        RegisterName(self.item_id, "", "原晶木")

class OceanWarm(Meterial):
    item_id = GetNextGlobalId()
    def __init__(self) -> None:
        super().__init__(self.item_id, None, 1)
        RegisterName(self.item_id, "", "大海温暖之息")

class MoonStoneCrystal(Meterial):
    item_id = GetNextGlobalId()
    def __init__(self) -> None:
        super().__init__(self.item_id, None, 1)
        RegisterName(self.item_id, "", "新月石晶")