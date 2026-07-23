from .materials import *

class SmallSeedOil(Meterial):
    item_id = GetNextGlobalId()
    def __init__(self) -> None:
        super().__init__(self.item_id,
                        {
                            Rice():20,
                            Corn():20,
                            OnyxArcheumEssence():3,
                        }, 2)
        RegisterName(self.item_id, "Small Seed Oil", "胚芽皮革油")

class ViscousGlossyOil(Meterial):
    item_id = GetNextGlobalId()
    def __init__(self) -> None:
        super().__init__(self.item_id, {
            OnyxArcheumEssence(): 5,
            Peanut(): 30,
            Wheat(): 30,
            RedCoral(): 20,
        }, 2)
        RegisterName(self.item_id, "Viscous Glossy Oil", "杂质皮革油")

class EmulsifiedOil(Meterial):
    item_id = GetNextGlobalId()
    def __init__(self) -> None:
        super().__init__(self.item_id, {
            OnyxArcheumEssence(): 9,
            Bean(): 40,
            Rye(): 40,
            Pearl(): 20,
            Vanilla(): 5,
        }, 2)
        RegisterName(self.item_id, "Emulsified Oil", "透明皮革油")

class DeeplyColoredOil(Meterial):
    item_id = GetNextGlobalId()
    def __init__(self) -> None:
        super().__init__(self.item_id, {
            DragonEssenceStabilizer(): 3,
            Quinoa(): 50,
            CultivatedGinseng(): 50,
            SparklingShellDust(): 10,
            Coconut(): 10
        }, 2)
        RegisterName(self.item_id, "Deeply Colored Oil", "五彩皮革油")