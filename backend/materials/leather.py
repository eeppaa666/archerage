from .materials import *
from .ingot import *
from .oil import *
class Leather(Meterial):
    item_id = GetNextGlobalId()
    def __init__(self) -> None:
        super().__init__(self.item_id, {
            Pelt(): 3
        }, 2)
        RegisterName(self.item_id, "Leather", "皮革")

class FineLeather(Meterial):
    item_id = GetNextGlobalId()
    def __init__(self) -> None:
        super().__init__(self.item_id, {
            Leather(): 10,
            SmallSeedOil(): 1
        }, 3)
        RegisterName(self.item_id, "Fine Leather", "优质皮革")

class WindSpiritLeather(Meterial):
    item_id = GetNextGlobalId()
    def __init__(self) -> None:
        super().__init__(self.item_id, {
            FineLeather(): 10,
            MysteriousGardenPowder(): 5,
            ViscousGlossyOil(): 1
        }, 4)
        RegisterName(self.item_id, "Wind Spirit Leather", "真皮皮革")

class BlazingWindSpiritLeather(Meterial):
    item_id = GetNextGlobalId()
    def __init__(self) -> None:
        super().__init__(self.item_id, {
            WindSpiritLeather(): 10,
            AnyaIngot(): 9,
            DragonEssenceStabilizer(): 25,
            FlamingLog(): 6
        }, 5)
        RegisterName(self.item_id, "Blazing Wind Spirit Leather", "柔韧真皮皮革")