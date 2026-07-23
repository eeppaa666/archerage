from .materials import *
from .polish import *

class IronIngot(Meterial):
    item_id = GetNextGlobalId()
    def __init__(self) -> None:
        super().__init__(self.item_id, {IronOre():3}, 2)
        RegisterName(self.item_id, "Iron Ingot", "铁锭")

class CopperIngot(Meterial):
    item_id = GetNextGlobalId()
    def __init__(self) -> None:
        super().__init__(self.item_id, {CopperOre():3}, 2)
        RegisterName(self.item_id, "Copper Ingot", "铜锭")

class SliverIngot(Meterial):
    item_id = GetNextGlobalId()
    def __init__(self) -> None:
        super().__init__(self.item_id, {SliverOre():3}, 2)
        RegisterName(self.item_id, "Sliver Ingot", "银锭")

class GoldIngot(Meterial):
    item_id = GetNextGlobalId()
    def __init__(self) -> None:
        super().__init__(self.item_id, {GoldOre():3}, 2)
        RegisterName(self.item_id, "Gold Ingot", "金锭")

class AnyaIngot(Meterial):
    item_id = GetNextGlobalId()
    def __init__(self) -> None:
        super().__init__(self.item_id, {AnyaPebble():3}, 2)
        RegisterName(self.item_id, "Anya Ingot", "Anya 锭")

class ArcheumIngot(Meterial):
    item_id = GetNextGlobalId()
    def __init__(self) -> None:
        super().__init__(self.item_id, {ArcheumOre():3}, 2)
        RegisterName(self.item_id, "Archeum Ingot", "源晶锭")

class SturdyIngot(Meterial):
    item_id = GetNextGlobalId()
    def __init__(self) -> None:
        super().__init__(self.item_id,
        {
            IronIngot():8,
            CopperIngot():1,
            SliverIngot():1,
            OpaquePolish():1,
        }, 3)
        RegisterName(self.item_id, "Sturdy Ingot", "合金锭")

class SunridgeIngot(Meterial):
    item_id = GetNextGlobalId()
    def __init__(self)->None:
        super().__init__(self.item_id,
        {
            SturdyIngot():10,
            MysteriousGardenPowder():5,
            RoughPolish():1
        }, 4)
        RegisterName(self.item_id, "Sunridge Ingot", "阳光之锭")

class BlazingSunridgeIngot(Meterial):
    item_id = GetNextGlobalId()
    def __init__(self) -> None:
        super().__init__(self.item_id, {
            SunridgeIngot(): 10,
            AnyaIngot(): 9,
            DragonEssenceStabilizer(): 25,
            FlamingLog(): 6
        }, 5)
        RegisterName(self.item_id, "Blazing Sunridge Ingot", "炙热的阳光之锭")