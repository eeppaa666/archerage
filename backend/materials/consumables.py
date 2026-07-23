from .materials import *
from .ingot import *

class MoonRedStone(Meterial):
    item_id = GetNextGlobalId()
    def __init__(self) -> None:
        super().__init__(self.item_id, None, 1)
        RegisterName(self.item_id, "", "新月赤石")

class DepthMoonRedStone(Meterial):
    item_id = GetNextGlobalId()
    def __init__(self) -> None:
        super().__init__(self.item_id, {
            MoonRedStone(): 1,
            MoonStoneCrystal(): 20,
            SturdyIngot(): 10,
        }, 1)
        RegisterName(self.item_id, "", " 深邃的新月赤石")

class GracefulMoonRedStone(Meterial):
    item_id = GetNextGlobalId()
    def __init__(self) -> None:
        super().__init__(self.item_id, {
            DepthMoonRedStone(): 1,
            MoonStoneCrystal(): 30,
            SturdyIngot(): 30,
        }, 2)
        RegisterName(self.item_id, "", "秀丽的新月赤石")

class MoonGreenStone(Meterial):
    item_id = GetNextGlobalId()
    def __init__(self) -> None:
        super().__init__(self.item_id, None, 1)
        RegisterName(self.item_id, "", "新月碧石")

class DepthMoonGreenStone(Meterial):
    item_id = GetNextGlobalId()
    def __init__(self) -> None:
        super().__init__(self.item_id, {
            MoonGreenStone(): 1,
            MoonStoneCrystal(): 20,
            SturdyIngot(): 10,
        }, 1)
        RegisterName(self.item_id, "", "深邃的新月碧石")

class GracefulMoonGreenStone(Meterial):
    item_id = GetNextGlobalId()
    def __init__(self) -> None:
        super().__init__(self.item_id, {
            DepthMoonGreenStone(): 1,
            MoonStoneCrystal(): 30,
            SturdyIngot(): 30,
        }, 2)
        RegisterName(self.item_id, "", "秀丽的新月碧石")

class MoonBrownStone(Meterial):
    item_id = GetNextGlobalId()
    def __init__(self) -> None:
        super().__init__(self.item_id, None, 1)
        RegisterName(self.item_id, "", "新月褐石")

class DepthMoonBrownStone(Meterial):
    item_id = GetNextGlobalId()
    def __init__(self) -> None:
        super().__init__(self.item_id, {
            MoonBrownStone(): 1,
            MoonStoneCrystal(): 20,
            SturdyIngot(): 10,
        }, 1)
        RegisterName(self.item_id, "", "深邃的新月褐石")

class GracefulMoonBrownStone(Meterial):
    item_id = GetNextGlobalId()
    def __init__(self) -> None:
        super().__init__(self.item_id, {
            DepthMoonBrownStone(): 1,
            MoonStoneCrystal(): 30,
            SturdyIngot(): 30,
        }, 2)
        RegisterName(self.item_id, "", "秀丽的新月褐石")

class MoonCyanStone(Meterial):
    item_id = GetNextGlobalId()
    def __init__(self) -> None:
        super().__init__(self.item_id, None, 1)
        RegisterName(self.item_id, "", "新月青石")

class DepthMoonCyanStone(Meterial):
    item_id = GetNextGlobalId()
    def __init__(self) -> None:
        super().__init__(self.item_id, {
            MoonCyanStone(): 1,
            MoonStoneCrystal(): 20,
            SturdyIngot(): 10,
        }, 1)
        RegisterName(self.item_id, "", "深邃的新月青石")

class GracefulMoonCyanStone(Meterial):
    item_id = GetNextGlobalId()
    def __init__(self) -> None:
        super().__init__(self.item_id, {
            DepthMoonCyanStone(): 1,
            MoonStoneCrystal(): 30,
            SturdyIngot(): 30,
        }, 2)
        RegisterName(self.item_id, "", "秀丽的新月青石")

class MoonYellowStone(Meterial):
    item_id = GetNextGlobalId()
    def __init__(self) -> None:
        super().__init__(self.item_id, None, 1)
        RegisterName(self.item_id, "", "新月黄石")

class DepthMoonYellowStone(Meterial):
    item_id = GetNextGlobalId()
    def __init__(self) -> None:
        super().__init__(self.item_id, {
            MoonYellowStone(): 1,
            MoonStoneCrystal(): 20,
            SturdyIngot(): 10,
        }, 1)
        RegisterName(self.item_id, "", "深邃的新月黄石")

class GracefulMoonYellowStone(Meterial):
    item_id = GetNextGlobalId()
    def __init__(self) -> None:
        super().__init__(self.item_id, {
            DepthMoonYellowStone(): 1,
            MoonStoneCrystal(): 30,
            SturdyIngot(): 30,
        }, 2)
        RegisterName(self.item_id, "", "秀丽的新月黄石")

class MoonBloodStone(Meterial):
    item_id = GetNextGlobalId()
    def __init__(self) -> None:
        super().__init__(self.item_id, None, 1)
        RegisterName(self.item_id, "", "新月血石")

class DepthMoonBloodStone(Meterial):
    item_id = GetNextGlobalId()
    def __init__(self) -> None:
        super().__init__(self.item_id, {
            MoonBloodStone(): 1,
            MoonStoneCrystal(): 20,
            SturdyIngot(): 10,
        }, 1)
        RegisterName(self.item_id, "", "深邃的新月血石")

class GracefulMoonBloodStone(Meterial):
    item_id = GetNextGlobalId()
    def __init__(self) -> None:
        super().__init__(self.item_id, {
            DepthMoonBloodStone(): 1,
            MoonStoneCrystal(): 30,
            SturdyIngot(): 30,
        }, 2)
        RegisterName(self.item_id, "", "秀丽的新月血石")