from .materials import *

class OpaquePolish(Meterial):
    item_id = GetNextGlobalId()
    def __init__(self) -> None:
        super().__init__(self.item_id, {
            Azalea():20,
            Narcissus():20,
            OnyxArcheumEssence():3,
        }, 2)
        RegisterName(self.item_id, "Opaque Polish", "双花翻新剂")

class RoughPolish(Meterial):
    item_id = GetNextGlobalId()
    def __init__(self) -> None:
        super().__init__(self.item_id, {
            OnyxArcheumEssence():5,
            Lotus():30,
            Oats():30,
            AntlerCoral():20
        }, 2)
        RegisterName(self.item_id, "Rough Polish", "浊体翻新剂")

class NonStickPolish(Meterial):
    item_id = GetNextGlobalId()
    def __init__(self) -> None:
        super().__init__(self.item_id, {
            OnyxArcheumEssence(): 9,
            ChiliPepper(): 40,
            Rosemary(): 40,
            Pearl(): 20,
            BlueBerry(): 5
        }, 2)
        RegisterName(self.item_id, "Non-Stick Polish", "珍珠翻新剂")

class RainbowPolish(Meterial):
    item_id = GetNextGlobalId()
    def __init__(self) -> None:
        super().__init__(self.item_id, {
            DragonEssenceStabilizer(): 3,
            Turmeric(): 50,
            Cactus(): 50,
            SparklingShellDust(): 10,
            BeeChnut(): 10
        }, 2)
        RegisterName(self.item_id, "Non-Stick Polish", "彩虹翻新剂")