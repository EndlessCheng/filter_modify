# -*- coding:utf-8 -*-

DEBUG = False

# 'm2s' -> 's' (3 -> 1)
SKILL = ['m', 's', 'r', 'm2s'][3]  # melee spell range

# A1( 1-13), A2(13-23), A3(*23*-33), A4(33-40) N
# A1(40-44), A2(44-48), A3(*48*-54), A4(54-57) C
# A1(56-59), A2(59-63), A3(*63*-67), A4(67-70) M

# Essence = (1-46 12-66 30 48 68) = 12 30 47 48 67 68
# Socket = 2 25 35 50(A3C)
# Ex >= 35(A4N)
# Ring-Amulet-Belt's T1-Life >= 44(A2C), 54(A4C), 64(A3M)
# Resistance = 12x : Fire12-48, Lighting13-49, Cold14-50
# MS = 1 15 30 40 55

#
# 第一部分：1-64（按重要度排序）
#

SMALLS_MAGIC_CLASS = '' + ' "Amulets" ' + ' "Rings"  ' + ' "Belts" '

#  "Gold" (8)    Dex: "Citrine" "Jade" "Turquoise"    Int: "Agate" "Lapis" "Turquoise"   (5 16)
SSF_CRAFT_AMULET_BASE_TYPE = '' + ' "Gold" '  # + ' "Agate" "Lapis" "Turquoise" '  # + ' "Citrine" "Jade" "Turquoise"  '
# "Sapphire" "Topaz" "Ruby" "Two-Stone" (8 12 16 20)
SSF_CRAFT_RINGS_BASE_TYPE = '' + ' "Two-Stone" '
# "Rustic Sash" "Leather Belt" (1 8)
SSF_CRAFT_BELTS_BASE_TYPE = '' + ' "Leather Belt" '  # + ' "Rustic Sash" '

MAGIC_BOOTS_ITEM_LEVEL = ['>= 1', '< 1'][1]

CURRENCY_ALERT_BLACKSMITH = True
CURRENCY_ALERT_TRANSMUTATION = True
CURRENCY_PORTAL_SCROLL_FONT_SIZE = [33, 30, 18][0]
CURRENCY_WISDOM_SCROLL_FONT_SIZE = [33, 18][0]
CURRENCY_ARMOURER_SCRAP_FONT_SIZE = [33, 18][0]

HIDE_FLASK_MANA = False
HALLOWED_MAX_ITEM_LEVEL = [50, 41][1]
HIDE_FLASK_LIFE = False

# "Quicksilver Flask" "Silver Flask" "Bismuth Flask" "Basalt Flask" "Granite Flask" "Diamond Flask"
# "Stibnite Flask" "Sulphur Flask"  "Ruby Flask" "Sapphire Flask" "Topaz Flask" "Amethyst Flask"
ALERT_UTILITY_FLASK_BASE_TYPE = '' + ' "Quicksilver Flask" "Stibnite Flask" "Granite Flask" "Sulphur Flask" "Basalt Flask" "Silver Flask" '

# "Firestorm" "Scorching Ray" "Orb of Storms"  "Clarity" "Added Fire Damage" "Melee Splash"
# "Blasphemy" "Fortify" "Increased Duration"  "Vortex"
# "Immortal Call" "Cast when Damage Taken"
LEVELING_GEMS_BASE_TYPE = '' + ' "Cast when Damage Taken"     "Vortex" '  # + ' "Firestorm" "Scorching Ray" "Orb of Storms" ' + ' "Clarity" '

# >= 15
HIDE_LEVELING_RARE_CLASS = '"Bows" "Quivers" "One Hand" "Claws" "Two Hand Swords" '  # + '  "Staves" "Two Hand"  '
# >= 2
HIDE_NORMAL_MAGIC_CLASS = '"Shields" ' + ' "Two Hand Maces" "Staves" ' + ' "Two Hand" "One Hand" '
# >= 2 找到高pDPS武器就隐藏所有白武器
HIDE_NORMAL_CLASS = '"Two Hand Maces" "Staves" '  # + ' "Two Hand" "One Hand" '

#
# 第二部分：65+（按重要度排序）
#

NEED_MAP = True

NEED_RGB = True

CURRENCY_ALERT_AUGMENTATION = True
CURRENCY_ALERT_CHANCE = True

SHOW_ENDGAME_4L = True

# "Hubris Circlet" "Vaal Regalia"  "Astral Plate"
# *急需的话直接点金* "Opal Sceptre" "Void Sceptre"  "Fossilised Spirit Shield"  "Vaal Axe"
SSF_CRAFT_BASE_TYPE = '' + ' "Opal Sceptre" "Void Sceptre" ' + ' "Astral Plate" ' + ' "Crystal Sceptre" '

ALERT_T1_RARE_BASE_TYPE = ''  # + ' "Vaal Regalia" '

# 提升部分T2的到T1中（T2为特定角色的farm gears提供了一个很好的参考样例，可以将部分T2物品根据不同的角色需求放入T1中）
ALERT_T2_RARE_BASE_TYPE = '' + ' "Astral Plate" "Opal Sceptre" "Void Sceptre" "Opal Wand" "Tornado Wand" "Prophecy Wand" ' + ' "Crystal Sceptre" '
ALERT_RARE_BASE_TYPE = ALERT_T1_RARE_BASE_TYPE + ALERT_T2_RARE_BASE_TYPE

# HIGHLIGHT_T2_RARE_BASE_TYPE = '' + ' "Tornado Wand" "Opal Wand" "Prophecy Wand"  "Vaal Axe"  "Opal Sceptre" "Void Sceptre"    '

T2_BIG_WEAPON_BASE_TYPE = ''  # + ' "Vaal Axe" "Coronal Maul" "Harbinger Bow" '
T2_BIG_ARM_BASE_TYPE = '' + ' "Colossal Tower Shield" "Pinnacle Tower Shield" '  # + ' "Assassin\'s Garb" "Glorious Plate" "Astral Plate" "Spike-Point Arrow Quiver" '

# "Two Hand Swords"  "Body Armour"  "Boots" "Gloves" "Helmets"
HIDE_ENDGAME_BELOW_T2_RARE_CLASS = '"Bows" "Quivers" "One Hand" "Claws" "Two Hand" "Staves"   '  # + ' "Shields" ' + ' "Daggers" ' + ' "Sceptres" "Wands" '

# "Fencer Helm" "Lacquered Helmet" "Bascinet"
# "Sharkskin Gloves" "Shagreen Gloves" "Stealth Gloves" "Slink Gloves"
# "Sharkskin Boots" "Shagreen Boots" "Stealth Boots" "Slink Boots" "Wyrmscale Boots" "Hydrascale Boots" "Dragonscale Boots"
# ONLY_HIGHLIGHT_RARE_SMALL_ARMOUR_BASE_TYPE = '' + ' "Siege Helmet" "Samite Helmet" "Burgonet"   "Gauntlets"  "Greaves" '

# "General\'s Brigandine" "Triumphant Lamellar"
# ONLY_HIGHLIGHT_RARE_BODY_ARMOUR_BASE_TYPE = '' + ' "Plate" '

# ONLY_HIGHLIGHT_RARE_SHIELD_BASE_TYPE = ''

# 洗珠宝：没有废词缀就停手。注意近战/弓的元素系玩法
# "Cobalt"  "Crimson" "Viridian"
ALERT_JEWEL_BASE_TYPE = '' + ' "Cobalt"  "Crimson" "Viridian" '

# "Sorcerer Boots"  "Occultist\'s Vestment" "Prophecy Wand" "Goathide Boots"
# "Fiend Dagger"
CHANCING_ITEM_BASE_TYPE = '' + ' "Sorcerer Boots" '

#
# 第三部分：（大致）固定内容
#

RARE_BOOTS_ALERT = (MAGIC_BOOTS_ITEM_LEVEL == '>= 1')

HIDE_LEVELING_RARE_MIN_ITEM_LEVEL = 15

# 'RRR' 'BBB'
LINKED4_SOCKET_GROUP = ['RRR', 'BBB']
LINKED4_NORMAL_MAX_ITEM_LEVEL = 60  # >60的由0216负责
LINKED4_MAGIC_MAX_ITEM_LEVEL = 55  # 第三难度不再显示
LINKED4_RARE_MAX_ITEM_LEVEL = 64  # 0700隐藏了>=65的黄装
LINKED4_SIMPLE_MAX_ITEM_LEVEL = 40  # 覆盖第一难度
LINKED4_CLASS = '' + ' "Gloves" "Helmets" ' + ' "Boots" ' + ' "Body Armour" '

# 三小件
SMALLS_NORMAL_MAX_ITEM_LEVEL = 9  # 出监狱后     隐藏不需要的白色三小件
SMALLS_MAGIC_MAX_ITEM_LEVEL = 24  # 出瓦尔金字塔后隐藏不需要的蓝色三小件
