from .materials import *

class SmallRootPigment(Meterial):
    item_id = GetNextGlobalId()
    def __init__(self) -> None:
        super().__init__(self.item_id, {
            OnyxArcheumEssence(): 3,
            Clover(): 20,
            Rose(): 20,
        }, 2)
        RegisterName(self.item_id, "Small Root Pigment", "细须柔顺剂")

class SmallLeafPigment(Meterial):
    item_id = GetNextGlobalId()
    def __init__(self) -> None:
        super().__init__(self.item_id, {
            OnyxArcheumEssence(): 5,
            CornFlower(): 30,
            Lily(): 30,
            GreenCoral(): 20
        }, 2)
        RegisterName(self.item_id, "Small Leaf Pigment", "叶片柔顺剂")

class SoftStemPigment(Meterial):
    item_id = GetNextGlobalId()
    def __init__(self) -> None:
        super().__init__(self.item_id, {
            OnyxArcheumEssence(): 9,
            Cactus(): 40,
            Mint(): 40,
            Pearl(): 20,
            Pepper(): 5
        }, 2)
        RegisterName(self.item_id, "Soft Stem Pigment", "根茎柔顺剂")

class ScentedPetalPigment(Meterial):
    item_id = GetNextGlobalId()
    def __init__(self) -> None:
        super().__init__(self.item_id, {
            DragonEssenceStabilizer(): 3,
            Poppy(): 50,
            Saffron(): 50,
            SparklingShellDust(): 10,
            Chestnut(): 10
        }, 2)
        RegisterName(self.item_id, "Scented Petal Pigment", "香花柔顺剂")