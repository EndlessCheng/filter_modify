DEBUG = False
TEMP = False

# Small different on leveling
TENCENT = False or TEMP
SSF = False

AW = False
AW_RANGE = False and AW

SPELL = True
BOW = False

RICH_LEVELING = False

#
# Part 1 - A1-A10
#

SHOW_FLASK_HALLOWED = True  # True
SHOW_FLASK_LIFE = True  # True

ALERT_MAGIC_BASE_TYPE = ' '.join([
    '"Jade Amulet" "Turquoise Amulet" "Citrine Amulet"' if SPELL else '',  # 血抗
    '"Lapis Amulet" "Turquoise Amulet" "Onyx Amulet"' if not SPELL else '',  # 点伤，血抗
    '"Ruby Ring" "Topaz Ring" "Sapphire Ring" "Two-Stone Ring"',  # 点伤，血抗
]).strip() if not RICH_LEVELING else ''

# Life: 70+(Rings), 80+(Amulets, Gloves, Boots), 90+(Helmets, Belts, Body Armour), 100+(Body Armour, IL 73+)
HIDE_BELOW_T1_RARE_CLASS = ' '.join([
    '"Claws" "One Hand"',
    # '"Body Armour"',  # 有血就行

    # '"Boots"',  # 80+血，有移速更好
    # '"Helmets"',  # 90+血，有命中更好
    # '"Gloves"',  # 80+血，有攻速/点伤更好

    # '"Shields"',  # 爆率
    # '"Sceptres"',  # 爆率
    # '"Daggers" "Wands"',
])

ALERT_UTILITY_FLASK_BASE_TYPE = ' '.join([
    '"Quicksilver"',
    '"Diamond"',
    '"Jade"',
    '"Quartz"',
    '"Basalt"',

    '"Ruby"',
    '"Topaz"',

    '"Stibnite"',
    '"Silver"',
    '"Granite"',

    '"Bismuth" "Amethyst" "Sapphire" "Aquamarine" "Sulphur"' if SHOW_FLASK_HALLOWED else '',
]).strip() if not RICH_LEVELING else ''

#
# Part 2 - Atlas
#

MAP_WHITE = False  # False
MAP_YELLOW = False  # False
MAP_RED = False  # False

MAGIC_JEWEL_BASE_TYPE = ' '.join([
    '"Crimson"',
    '"Viridian" "Cobalt"',
]).strip()  # if not MAP_YELLOW else ''

CURRENCY_PORTAL_FONT_SIZE = [40, 18][0]  # Portal skill
NEED_CHISEL = False

ALERT_ATLAS_NORMAL_BASE_TYPE = ' '.join([
    '"Bone Helmet"',  # +2/+3，血，召唤血
    '"Two-Toned Boots"',  # 血抗（移速）
    '"Spiked Gloves"',  # 攻速精华
    '"Gripped Gloves"',  # 攻速精华
    '"Fingerless Silk Gloves"',  # TODO: ???
]).strip()

#
# Part 3 - Others
#

SSF_CRAFT_AMULETS_BASE_TYPE = ' '.join(
    ['"Turquoise"', '"Lapis"']
    [max(0, 0 if SHOW_FLASK_LIFE else 1, 0 if '"Lapis Amulet"' in ALERT_MAGIC_BASE_TYPE else 2):])
if SPELL:
    SSF_CRAFT_AMULETS_BASE_TYPE = ' '.join(['"Citrine"'][0:])
SSF_CRAFT_RINGS_BASE_TYPE = '"Two-Stone"' if '"Two-Stone Ring"' in ALERT_MAGIC_BASE_TYPE else ''
SSF_CRAFT_BELTS_BASE_TYPE = ' '.join(['"Leather Belt"'][0:])

L3_MAX_IL = 19  # RRG 头/脚

ALERT_NORMAL_BASE_TYPE = ' '.join([
    # '"Engraved Wand"',  # essence of anger/wrath/hatred
    # '"Siege Axe"',  # 59 73

    # TODO: other bases?
    # '"Titan Greaves" "Vaal Greaves"' if '"Boots"' not in HIDE_BELOW_T1_RARE_CLASS else '',  # 62 68
    # '"Royal Burgonet" "Eternal Burgonet"' if '"Helmets"' not in HIDE_BELOW_T1_RARE_CLASS else '',  # 65 69
]).strip()

T1_RARE_BASE_TYPE = ' '.join([
    # '"Nightmare Mace" "Pernarch" "Legion Hammer" "Tenderizer" "Dragon Mace"',  # 等一个过3.0分的武器
    # '"Infernal Axe" "Butcher Axe" "Karui Axe" "Engraved Hatchet" "Wraith Axe"',
    # '"Behemoth Mace" "Vaal Hatchet" "Runic Hatchet"',

    # TODO: other bases?
    # '"Royal Burgonet" "Eternal Burgonet" "Ezomyte Burgonet"',  # 差不多就行
    # '"Titan Greaves" "Vaal Greaves"',
    # '"Titan Gauntlets" "Vaal Gauntlets"',  # 血友病

    # '"Siege Axe"',  # 开膛斧

    # '"Imbued Wand" "Carved Wand" "Engraved Wand"'  # 皮斯卡托的慧眼
    # '"Lion Pelt"',  # 斯塔空加之首
    # '"Crusader Buckler"',  # 艾许之镜
]).strip() if not MAP_RED else ''

LINKED_CLASS = ' '.join([
    '"Body Armour"',
    '"Boots"' if '"Boots"' not in HIDE_BELOW_T1_RARE_CLASS else '',
    '"Helmets"' if '"Helmets"' not in HIDE_BELOW_T1_RARE_CLASS else '',
    '"Gloves"' if '"Gloves"' not in HIDE_BELOW_T1_RARE_CLASS else '',
]).strip() if SHOW_FLASK_HALLOWED else ''
SHOW_N2M_ONE_HAND_MELEE = True and SHOW_FLASK_LIFE and not SPELL and not BOW

CURRENCY_WISDOM_FONT_SIZE = [40, 33, 18][max(0, 0 if SHOW_FLASK_LIFE else 2)]
CURRENCY_ARMOURER_SCRAP_FONT_SIZE = [40, 36, 18][max(0, 0 if SHOW_FLASK_LIFE else 1, 0 if any(
    class_ not in HIDE_BELOW_T1_RARE_CLASS for class_ in ['"Boots"', '"Helmets"']) else 2)]

NEED_RGB = True and SHOW_FLASK_LIFE
CURRENCY_ALERT_TRANSMUTATION = True and SHOW_FLASK_LIFE
CURRENCY_ALERT_BLACKSMITH = True and '"Siege Axe"' in ALERT_NORMAL_BASE_TYPE and not SPELL  # Trade 8 for 1 glass
CURRENCY_ALERT_AUGMENTATION = True and not MAP_YELLOW
# CURRENCY_ALERT_CHANCE = True and not MAP_YELLOW
ALERT_LOW_CURRENCY = True and SHOW_FLASK_LIFE

SSF_UNIQUE = '"Siege Axe" "Basket Rapier" "Twilight Blade" "Sadist Garb" "Destiny Leather" "Tornado Wand"'

ALERT_ESSENCE_BASE_TYPE = ''

IGNORE_RARE_UNDER_T2 = False
L2_MAX_IL = min(4, L3_MAX_IL)
SHOW_FLASK_MANA = True and SHOW_FLASK_HALLOWED and SHOW_FLASK_LIFE
if SPELL:
    SHOW_FLASK_MANA = True and SHOW_FLASK_LIFE
CHANCING_BASE_TYPE = ''  # if CURRENCY_ALERT_CHANCE else ''

# SHOW_FLASK_HALLOWED = True
# SHOW_FLASK_LIFE = True
