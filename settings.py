DEBUG = False
TEMP = False

# Small different on leveling
TENCENT = True or TEMP
SSF = False

#
# Part 1 - A1-A10
#

SHOW_FLASK_HALLOWED = True
SHOW_FLASK_LIFE = True

ALERT_MAGIC_BASE_TYPE = ' '.join([
    '"Leather Belt"' if SHOW_FLASK_LIFE else '',
    '"Lapis Amulet" "Turquoise Amulet" "Onyx Amulet"',  # 点伤抗性
    '"Ruby Ring" "Topaz Ring" "Sapphire Ring" "Two-Stone Ring"',  # 点伤抗性
    '"Siege Axe"',  # ~100%
]).strip()

# Life: 70+(Rings), 80+(Amulets, Gloves, Boots), 90+(Helmets, Belts, Body Armour), 100+(Body Armour, IL 73+)
HIDE_BELOW_T1_RARE_CLASS = ' '.join([
    # '"Sceptres" "Claws" "One Hand"',  # 抗性/智力
    # '"Body Armour"',  # 血量精华

    # '"Boots"',  # 80+血
    # '"Helmets"',  # 90+血
    # '"Gloves"',  # 80+血，有点伤/攻速更好
])

ALERT_NORMAL_BASE_TYPE = ' '.join([
    '"Siege Axe"',  # 59 73

    '"Titan Greaves" "Vaal Greaves"' if '"Boots"' not in HIDE_BELOW_T1_RARE_CLASS else '',  # 62 68
    '"Royal Burgonet" "Eternal Burgonet"' if '"Helmets"' not in HIDE_BELOW_T1_RARE_CLASS else '',  # 65 69
]).strip()

ALERT_UTILITY_FLASK_BASE_TYPE = ' '.join([
    '"Silver"',  # if SHOW_FLASK_LIFE else '',
    '"Basalt"',  # if SHOW_FLASK_LIFE else '',
    '"Diamond"',
    '"Granite"',
    '"Jade" "Quartz" "Sulphur" "Quicksilver" "Stibnite"' if SHOW_FLASK_HALLOWED else '',
]).strip()

#
# Part 2 - Atlas
#

MAP_WHITE = False
MAP_YELLOW = False
MAP_RED = False  # or SHAPED

T1_RARE_BASE_TYPE = ' '.join([
    '"Nightmare Mace" "Pernarch" "Legion Hammer" "Tenderizer" "Dragon Mace"',  # 等一个过3.0分的武器
    '"Infernal Axe" "Butcher Axe" "Karui Axe" "Engraved Hatchet" "Wraith Axe"',
    '"Behemoth Mace" "Vaal Hatchet" "Runic Hatchet"',

    '"Royal Burgonet" "Eternal Burgonet" "Ezomyte Burgonet"',  # 差不多就行
    '"Titan Greaves" "Vaal Greaves"',
    '"Titan Gauntlets" "Vaal Gauntlets"',

    '"Siege Axe"',  # 开膛斧
]).strip()

CURRENCY_PORTAL_FONT_SIZE = [40, 18][0]  # Portal skill

#
# Part 3 - Others
#

L3_MAX_IL = 19  # RRG 头/脚

LINKED_CLASS = ' '.join([
    '"Body Armour"',
    '"Boots"' if '"Boots"' not in HIDE_BELOW_T1_RARE_CLASS else '',
    '"Helmets"' if '"Helmets"' not in HIDE_BELOW_T1_RARE_CLASS else '',
    '"Gloves"' if '"Gloves"' not in HIDE_BELOW_T1_RARE_CLASS else '',
]).strip() if SHOW_FLASK_LIFE else ''
SHOW_N2M_ONE_HAND = True and SHOW_FLASK_LIFE

CURRENCY_WISDOM_FONT_SIZE = [40, 33, 18][max(0, 0 if SHOW_FLASK_LIFE else 2)]
CURRENCY_ARMOURER_SCRAP_FONT_SIZE = [40, 36, 18][max(0, 0 if SHOW_FLASK_LIFE else 1, 0 if any(
    class_ not in HIDE_BELOW_T1_RARE_CLASS for class_ in ['"Boots"', '"Helmets"']) else 2)]

NEED_RGB = True and SHOW_FLASK_LIFE
CURRENCY_ALERT_TRANSMUTATION = True and SHOW_FLASK_LIFE
CURRENCY_ALERT_BLACKSMITH = True and '"Siege Axe"' in ALERT_NORMAL_BASE_TYPE  # Trade 8 for 1 glass
CURRENCY_ALERT_AUGMENTATION = True and not MAP_YELLOW
CURRENCY_ALERT_CHANCE = True and not MAP_YELLOW
ALERT_LOW_CURRENCY = True and SHOW_FLASK_LIFE
NEED_CHISEL = False

SSF_CRAFT_AMULETS_BASE_TYPE = ' '.join(
    ['"Turquoise"', '"Lapis"']
    [max(0, 0 if SHOW_FLASK_LIFE else 1, 0 if '"Lapis Amulet"' in ALERT_MAGIC_BASE_TYPE else 2):])
SSF_CRAFT_RINGS_BASE_TYPE = '"Two-Stone"' if '"Two-Stone Ring"' in ALERT_MAGIC_BASE_TYPE else ''
SSF_CRAFT_BELTS_BASE_TYPE = '"Leather Belt"' if SHOW_FLASK_LIFE else ''  # ' '.join(['"Leather Belt"'][0:])

ALERT_ESSENCE_BASE_TYPE = ' "Essence of Greed" "Essence of Contempt" "Essence of Zeal" ' \
                          ' "Essence of Loathing" "Essence of Scorn" '

IGNORE_RARE_UNDER_T2 = False
L2_MAX_IL = min(4, L3_MAX_IL)
SHOW_FLASK_MANA = True and SHOW_FLASK_HALLOWED and SHOW_FLASK_LIFE
CHANCING_BASE_TYPE = '' if CURRENCY_ALERT_CHANCE else ''

ALERT_MAGIC_JEWEL_BASE_TYPE = ' '.join([
    '"Crimson" "Viridian" "Cobalt" "Eye"',
    '"Murderous Eye"',  # 找血，抗性，点伤  >=74：36–45血
]).strip() if not MAP_YELLOW else ''

# TODO： 备注地图八向分类
ALERT_ATLAS_BASE_TYPE = ' '.join([
    # '"Two-Toned Boots"',
    '"Spiked Gloves"',  # 攻速精华
]).strip()

HIDE_NETS = ''
if MAP_WHITE:
    HIDE_NETS += '"Simple Steel Net"'
if MAP_YELLOW:
    HIDE_NETS += ' "Reinforced Steel Net"'
if MAP_RED:
    HIDE_NETS += ' "Strong Steel Net"'

# SHOW_FLASK_HALLOWED = True
# SHOW_FLASK_LIFE = True
