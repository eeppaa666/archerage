from .materials import *
from .oil import *
from .ingot import *

class Lumber(Meterial):
    item_id = GetNextGlobalId()
    def __init__(self) -> None:
        super().__init__(self.item_id, {Log():3}, 2)
        RegisterName(self.item_id, "Lumber", "木材")

class FineLumber(Meterial):
    item_id = GetNextGlobalId()
    def __init__(self) -> None:
        super().__init__(self.item_id, {
            Lumber(): 10,
            SmallSeedOil(): 1,
        }, 3)
        RegisterName(self.item_id, "FineLumber", "胶合木材")

class NuriForestLumber(Meterial):
    item_id = GetNextGlobalId()
    def __init__(self) -> None:
        super().__init__(self.item_id, {
            FineLumber(): 10,
            MysteriousGardenPowder(): 5,
            ViscousGlossyOil(): 1,
        }, 4)
        RegisterName(self.item_id, "Nuri Forest Lumber", "nuri 木材")

class BlazingNuriForestLumber(Meterial):
    item_id = GetNextGlobalId()
    def __init__(self) -> None:
        super().__init__(self.item_id, {
            NuriForestLumber(): 10,
            AnyaIngot(): 9,
            DragonEssenceStabilizer(): 25,
            FlamingLog(): 6
        }, 5)
        RegisterName(self.item_id, "Blazing Nuri Forest Lumber", "炽热的 nuri木材")