from .materials import *



class DawnsdropBoots(Meterial):
    item_id = GetNextGlobalId()
    def __init__(self) -> None:
        super().__init__(self.item_id, None, 1)
        RegisterName(self.item_id, "Dawnsdrop Boots", "晨露双脚")


class DewyDawnsdropBoots(Meterial):
    item_id = GetNextGlobalId()
    def __init__(self) -> None:
        super().__init__(self.item_id, {
            DawnsdropBoots(): 1,
            MoonlightArcheumCrystal(): 8,
            Eel(): 10,
            HandicraftYarn(): 110
        }, 2)
        RegisterName(self.item_id, "Dewy Dawnsdrop Boots", "德威的晨露双脚")

class DazzlingDawnsdropBoots(Meterial):
    item_id = GetNextGlobalId()
    def __init__(self) -> None:
        super().__init__(self.item_id, {
            DewyDawnsdropBoots(): 1,
            MoonlightArcheumCrystal(): 16,
            Stingray(): 10,
            HandicraftYarn(): 130,
        }, 3)
        RegisterName(self.item_id, "Dazzling Dawnsdrop Boots", "耀眼的晨露双脚")

class RadiantDawnsdropBoots(Meterial):
    item_id = GetNextGlobalId()
    def __init__(self) -> None:
        super().__init__(self.item_id, {
            DazzlingDawnsdropBoots(): 1,
            MoonlightArcheumCrystal(): 38,
            GlacierGrayfish(): 10,
            HandicraftYarn(): 150
        }, 1)
        RegisterName(self.item_id, "Radiant Dawnsdrop Boots", "灿烂的晨露双脚")
