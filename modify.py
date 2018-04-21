import os
import platform
import shutil
import time

from utils import FilterBlock, FilterManager
import settings

SHOW = 'Show'
HIDE = 'Hide'
DEBUG = SHOW if settings.DEBUG else HIDE

CLASS_TWO_HAND = '"Bows" "Two Hand" "Staves"'
CLASS_HAND = CLASS_TWO_HAND + ' "Quivers" "Shields" "Claws" "Sceptres" "Daggers" "Wands" "One Hand"'
CLASS_ACCESSORY = '"Belts" "Amulets" "Rings"'

BASE_TYPE_BODY_EVA = '"Shabby Jerkin" "Leather" "Buckskin Tunic" "Eelskin Tunic" "Sharkskin Tunic" ' \
                     '"Thief\'s Garb" "Cutthroat\'s Garb" "Assassin\'s Garb"'
BASE_TYPE_BODY_ES = '"Robe" "Silken Vest" "Silken Garb" "Vestment" "Regalia" "Silken Wrap" "Necromancer Silks"'
BASE_TYPE_BODY_EE = '"Padded Vest" "Oiled Vest" "Jacket" "Oiled Coat" "Sleek Coat" "Varnished Coat" "Raiment" ' \
                    '"Waxed Garb" "Lacquered Garb" "Sadist Garb" "Bone Armour" "Crypt Armour" "Carnal Armour"'

RARITY_NORMAL = 'Normal'
RARITY_MAGIC = 'Magic'
RARITY_RARE = 'Rare'
RARITY_UNIQUE = 'Unique'
RARITY_N2M = '<= Magic'
RARITY_N2R = '<= Rare'

ITEM_LEVEL_REGAL = '>= 75'
ITEM_LEVEL_CHAOS = '>= 60'

FONT_SIZE_MAX = 45
FONT_SIZE_MIN = 18

COLOR_WHITE = '255 255 255'
COLOR_SILVER = '200 200 200'
COLOR_GRAY = '150 150 150'
COLOR_BLACK = '0 0 0'
COLOR_RED = '255 0 0'
COLOR_YELLOW = '255 255 0'
COLOR_TANGERINE = '213 159 0'
COLOR_ORANGE = '255 125 0'
COLOR_UNIQUE = '175 96 37'  # Rich Gold
COLOR_OLIVE = '100 75 0'
COLOR_LIME = '0 255 0'
COLOR_LIME_LIGHT = '0 210 0 210'
COLOR_SPRING_BUD = '180 255 0'
COLOR_AQUA = '0 255 255'
COLOR_BLUE = '0 0 255'
COLOR_MAGENTA = '255 0 255'
COLOR_MAGENTA_DARK = '129 15 213 200'

_SOUND_1 = '1 300'  # 重敲锣声
_SOUND_2 = '2 300'
_SOUND_3 = '3 300'  # 沉闷地敲锣
_SOUND_4 = '4 300'
_SOUND_5 = '5 300'  # 摩托快速驶过
_SOUND_6 = '6 300'
_SOUND_7 = '7 300'  # 类似8，废弃
_SOUND_8 = '8 300'
_SOUND_9 = '9 300'  # 类似8，废弃
_SOUND_10 = '10 300'  # 重锤铁板
_SOUND_11 = '11 300'  # 重锤石板
_SOUND_12 = '12 300'
_SOUND_13 = '13 300'  # 敲锣声
_SOUND_14 = '14 300'  # 类似8，废弃
_SOUND_15 = '15 300'  # 类似8，废弃
_SOUND_16 = '16 300'  # 锤石板

SOUND_TOP_VALUE = _SOUND_8
SOUND_MID_VALUE = _SOUND_1
SOUND_LOW_VALUE = _SOUND_2
SOUND_SHAPER_ELDER_T2 = _SOUND_3
SOUND_SHAPER_ELDER = _SOUND_10
SOUND_MAP = _SOUND_4
SOUND_UNIQUE = _SOUND_6
SOUND_LEVELING = _SOUND_12

STYLE_TOP = {'SetFontSize': FONT_SIZE_MAX,
             'SetTextColor': COLOR_RED, 'SetBorderColor': COLOR_RED, 'SetBackgroundColor': COLOR_WHITE}
STYLE_TOP_RARE = {'SetFontSize': FONT_SIZE_MAX, 'SetBorderColor': COLOR_ORANGE, 'SetBackgroundColor': COLOR_OLIVE}
STYLE_T1_RARE = {'SetBorderColor': COLOR_ORANGE, 'SetBackgroundColor': COLOR_OLIVE + ' 225'}
STYLE_TOP_UNIQUE = {'SetTextColor': COLOR_UNIQUE, 'SetBorderColor': COLOR_UNIQUE, 'SetBackgroundColor': COLOR_WHITE}
_STYLE_MAP_BASE = {'SetFontSize': FONT_SIZE_MAX, 'SetTextColor': COLOR_BLACK, 'SetBackgroundColor': COLOR_SILVER}
STYLE_MAP_HIGH_11_14 = {**_STYLE_MAP_BASE, 'SetBorderColor': COLOR_RED}
STYLE_MAP_MID_9_10 = {**_STYLE_MAP_BASE, 'SetBorderColor': COLOR_YELLOW}
STYLE_MAP_MID_6_8 = {**_STYLE_MAP_BASE, 'SetBorderColor': COLOR_SPRING_BUD}
STYLE_MAP_LOW_3_5 = {**_STYLE_MAP_BASE, 'SetBorderColor': COLOR_BLUE}
STYLE_MAP_LOW_1_2 = {**_STYLE_MAP_BASE, 'SetBorderColor': COLOR_WHITE}
STYLE_LINKS = {'SetBorderColor': COLOR_AQUA}
STYLE_NONE = {'SetFontSize': None, 'SetTextColor': None, 'SetBorderColor': None, 'SetBackgroundColor': None}

BLOCK_5L = 501
BLOCK_6S = 502
BLOCK_HIDE_RARES_65 = 1000
BLOCK_ACT_1 = 2706
BLOCK_HIDE_REMAINING = 2900  # SetFontSize=FONT_SIZE_MIN


def modify_endgame_mix(filter_manager):
    filter_manager.add_comment(100, 'OVERRIDE AREA 1 - Override ALL rules here', ignored=True)

    # 8
    blocks = filter_manager.add_comment(200, '6 LINKS')
    blocks[0].PlayAlertSound = SOUND_TOP_VALUE
    filter_manager.extend_blocks(blocks)

    # BLOCK_5L 8
    blocks_5l = filter_manager.get_blocks(BLOCK_5L)
    for block in blocks_5l:
        block.PlayAlertSound = SOUND_TOP_VALUE
    filter_manager.extend_blocks(blocks_5l)

    filter_manager.add_comment(300, 'SHAPER ITEMS', ignored=True)

    # 8
    blocks = filter_manager.add_comment(301, 'Exception Handling - Rings, Amulets, Belts')
    blocks[0].PlayAlertSound = SOUND_TOP_VALUE
    filter_manager.extend_blocks(blocks)

    # 8
    blocks = filter_manager.add_comment(302, 'Shaper Item Layers - T1')
    for block in blocks:
        block.PlayAlertSound = SOUND_TOP_VALUE
    filter_manager.extend_blocks(blocks)

    blocks = filter_manager.add_comment(303, 'Shaper Item Layers - T2')
    filter_manager.extend_blocks(blocks)

    # 10
    blocks = filter_manager.add_comment(304, 'Shaper Item Layers - T3')
    for block in blocks:
        block.PlayAlertSound = SOUND_SHAPER_ELDER
    filter_manager.extend_blocks(blocks)

    filter_manager.add_comment(400, 'ELDER ITEMS', ignored=True)

    # 8
    blocks = filter_manager.add_comment(401, 'Exception Handling - Rings, Amulets, Belts')
    blocks[0].PlayAlertSound = SOUND_TOP_VALUE
    filter_manager.extend_blocks(blocks)

    # 8
    blocks = filter_manager.add_comment(402, 'Elder Item Layers - T1')
    for block in blocks:
        block.PlayAlertSound = SOUND_TOP_VALUE
    filter_manager.extend_blocks(blocks)

    blocks = filter_manager.add_comment(403, 'Elder Item Layers - T2')
    filter_manager.extend_blocks(blocks)

    # 10
    blocks = filter_manager.add_comment(404, 'Elder Item Layers - T3')
    for block in blocks:
        block.PlayAlertSound = SOUND_SHAPER_ELDER
    filter_manager.extend_blocks(blocks)

    filter_manager.add_comment(500, 'Recipes, Magic and Normal items (endgame!)', ignored=True)

    # 移到 6L 之后
    filter_manager.add_comment(BLOCK_5L, '5-Linked items', ignored=True)

    # 8 样式改掉
    blocks = filter_manager.add_comment(BLOCK_6S, '6-Socket Items')
    blocks[0].modify(PlayAlertSound=SOUND_TOP_VALUE, **STYLE_TOP)
    blocks[1].modify(PlayAlertSound=SOUND_TOP_VALUE, **STYLE_TOP)
    del blocks[2]  # 移除不需要的提示

    # TODO: SetBorderColor????
    blocks[-1].modify(SetTextColor=COLOR_WHITE, SetBorderColor=COLOR_BLACK, SetBackgroundColor=COLOR_TANGERINE)
    filter_manager.extend_blocks(blocks)

    # 8 1 1
    blocks = filter_manager.add_comment(503, 'Exclusive bases: Stygian Vise')
    blocks[0].PlayAlertSound = SOUND_TOP_VALUE
    blocks[1].PlayAlertSound = SOUND_MID_VALUE
    blocks[2].PlayAlertSound = SOUND_MID_VALUE
    filter_manager.extend_blocks(blocks)

    # 8 8 1 去掉最后一个
    blocks = filter_manager.add_comment(504, 'Abyss Jewels (Rare and Magic)')
    blocks[0].PlayAlertSound = SOUND_TOP_VALUE
    blocks[1].PlayAlertSound = SOUND_TOP_VALUE
    blocks[2].PlayAlertSound = SOUND_MID_VALUE
    filter_manager.extend_blocks(blocks[:3])

    # 8 1 1 2 ALERT_ATLAS_BASE_TYPE
    blocks = filter_manager.add_comment(505, 'Exclusive bases: Atlas bases, talismans (includes Rare rarity)')
    for block in blocks[:2]:
        block.BaseType += ' "Marble Amulet" '
        block.modify(PlayAlertSound=SOUND_TOP_VALUE, **STYLE_TOP)
    blocks[2].PlayAlertSound = SOUND_MID_VALUE
    blocks[3].PlayAlertSound = SOUND_MID_VALUE
    blocks[4].modify(PlayAlertSound=SOUND_MID_VALUE, **STYLE_TOP_RARE)
    blocks[5].modify(PlayAlertSound=SOUND_MID_VALUE, **STYLE_TOP_RARE)
    blocks[-3].modify(BaseType=settings.ALERT_ATLAS_BASE_TYPE, PlayAlertSound=SOUND_LOW_VALUE, **STYLE_TOP_RARE)
    del blocks[-2]
    filter_manager.extend_blocks(blocks)

    # RARITY_MAGIC
    # 项链：+1诅咒，+1球，抗性上限；  腰带：+1球
    # 手：击中附加诅咒；  脚：+1球；  箭袋：+1箭
    filter_manager.add_comment(506, 'Corrupted Amulets', ignored=True)
    accessories = FilterBlock(Corrupted=True, Class='"Amulets" "Belts"', Rarity=RARITY_MAGIC,
                              SetFontSize=36, SetBorderColor=COLOR_ORANGE)
    others = accessories.copy_modify(Class='"Gloves" "Boots" "Quivers"')
    filter_manager.extend_blocks([accessories, others])

    # CHANCING_BASE_TYPE
    filter_manager.add_comment(507, 'Chancing items', ignored=True)
    if settings.CHANCING_BASE_TYPE != '':
        block = FilterBlock(Corrupted=False, BaseType=settings.CHANCING_BASE_TYPE, Rarity=RARITY_NORMAL,
                            SetFontSize=42, SetTextColor=COLOR_WHITE, SetBorderColor=COLOR_LIME_LIGHT)
        filter_manager.append_block(block)

    # ALERT_UTILITY_FLASK_BASE_TYPE 12
    blocks = filter_manager.add_comment(508, 'FLASKS (Endgame rules)')
    if settings.ALERT_UTILITY_FLASK_BASE_TYPE != '':
        utility_flasks = blocks[-1].copy_modify(BaseType=settings.ALERT_UTILITY_FLASK_BASE_TYPE,
                                                SetFontSize=FONT_SIZE_MAX, PlayAlertSound=SOUND_LEVELING)
        filter_manager.append_block(utility_flasks)

    filter_manager.add_comment(509, 'Add your own crafting rules here', ignored=True)

    # 8
    blocks = filter_manager.add_comment(510, '86+ Endgame crafting rules')
    for block in blocks:
        block.PlayAlertSound = SOUND_TOP_VALUE
    filter_manager.extend_blocks(blocks)

    # 前三个 & Siege Axe
    blocks = filter_manager.add_comment(511, '83/84+ Endgame crafting rules')
    filter_manager.extend_blocks(blocks[:3])
    blocks[3].BaseType = '"Siege Axe"'
    filter_manager.append_block(blocks[3])

    # ALERT_JEWEL_BASE_TYPE 12
    blocks = filter_manager.add_comment(512, '60+ Crafting rules for 60++ trinkets')
    if settings.ALERT_JEWEL_BASE_TYPE != '':
        magic_jewels = blocks[0].copy_modify(BaseType=settings.ALERT_JEWEL_BASE_TYPE, PlayAlertSound=SOUND_LEVELING)
        filter_manager.append_block(magic_jewels)
        filter_manager.append_block(blocks[0])

    filter_manager.add_comment(513, 'Warband items', ignored=True)

    # ALERT_NORMAL_BASE_TYPE, SSF_CRAFT_AMULETS_BASE_TYPE, SSF_CRAFT_RINGS_BASE_TYPE, SSF_CRAFT_BELTS_BASE_TYPE
    # ALERT_MAGIC_BASE_TYPE
    filter_manager.add_comment(514, 'Remaining crafting rules - add your own bases here!', ignored=True)
    if settings.ALERT_NORMAL_BASE_TYPE != '':
        normals = filter_manager.get_blocks(BLOCK_ACT_1)[0]
        normals.modify(BaseType=settings.ALERT_NORMAL_BASE_TYPE, ItemLevel=None,
                       SetFontSize=40, PlayAlertSound=SOUND_LEVELING)
        # str_n = normals.copy_modify(BaseType='"Amber Amulet" "Heavy Belt"', ItemLevel='<= 12')
        filter_manager.extend_blocks([normals])

    if settings.SSF_CRAFT_BELTS_BASE_TYPE != '':
        hide_normals = filter_manager.get_blocks(BLOCK_HIDE_REMAINING)[0]
        hide_normals.modify(Class=None, Rarity=RARITY_NORMAL, SetFontSize=FONT_SIZE_MIN)
        hide_n_leather_belt = hide_normals.copy_modify(BaseType='"Leather Belt"', ItemLevel='<= 29')
        hide_n_rustic_sash = hide_normals.copy_modify(BaseType='"Rustic Sash"', ItemLevel='>= 30')
        filter_manager.extend_blocks([hide_n_leather_belt, hide_n_rustic_sash])  # A4左右开始堆血(T5血从30开始)

        filter_manager.append_block(FilterBlock(
            Class='Belts', BaseType=settings.SSF_CRAFT_BELTS_BASE_TYPE, Rarity=RARITY_NORMAL, ItemLevel='>= 13',
            SetTextColor=COLOR_WHITE))
    if settings.SSF_CRAFT_AMULETS_BASE_TYPE != '':
        filter_manager.append_block(FilterBlock(
            Class='Amulets', BaseType=settings.SSF_CRAFT_AMULETS_BASE_TYPE, Rarity=RARITY_NORMAL, ItemLevel='>= 13',
            SetTextColor=COLOR_WHITE))
    if settings.SSF_CRAFT_RINGS_BASE_TYPE != '':
        filter_manager.append_block(FilterBlock(
            Class='Rings', BaseType=settings.SSF_CRAFT_RINGS_BASE_TYPE, Rarity=RARITY_NORMAL, ItemLevel='>= 13',
            SetTextColor=COLOR_WHITE))

    if settings.ALERT_MAGIC_BASE_TYPE != '':
        hide_magics = filter_manager.get_blocks(BLOCK_HIDE_REMAINING)[0]
        hide_magics.modify(Class=None, Rarity=RARITY_MAGIC, SetFontSize=FONT_SIZE_MIN)
        hide_m_rustic_sash = hide_magics.copy_modify(BaseType='"Rustic Sash"', ItemLevel='>= 30')
        hide_m_iron_ring = hide_magics.copy_modify(BaseType='"Iron Ring"', ItemLevel='>= 20')
        filter_manager.extend_blocks([hide_m_rustic_sash, hide_m_iron_ring])

        alert_magics = filter_manager.get_blocks(BLOCK_ACT_1)[1]
        alert_magics.PlayAlertSound = SOUND_LEVELING
        if '"Amulet"' in settings.ALERT_MAGIC_BASE_TYPE:
            settings.ALERT_MAGIC_BASE_TYPE = settings.ALERT_MAGIC_BASE_TYPE.replace('"Amulet"', '')
            alert_magic_amulets = alert_magics.copy_modify(Class='"Amulets"', BaseType=None, ItemLevel='<= 19')
            filter_manager.append_block(alert_magic_amulets)
        if '"Gloves"' in settings.ALERT_MAGIC_BASE_TYPE:
            settings.ALERT_MAGIC_BASE_TYPE = settings.ALERT_MAGIC_BASE_TYPE.replace('"Gloves"', '')
            alert_magic_gloves = alert_magics.copy_modify(Class='"Gloves"', BaseType=None, ItemLevel='<= 24')
            filter_manager.append_block(alert_magic_gloves)
        alert_magics.modify(BaseType=settings.ALERT_MAGIC_BASE_TYPE, ItemLevel=None)
        filter_manager.append_block(alert_magics)

    # NEED_CHISEL
    blocks = filter_manager.add_comment(515, 'Chisel recipe items')
    for block in blocks:
        block.PlayAlertSound = SOUND_MID_VALUE
    blocks[1].Quality = '>= 10' if settings.NEED_CHISEL else '>= 14'
    blocks[2].Quality = '>= 0' if settings.NEED_CHISEL else '>= 5'
    filter_manager.extend_blocks(blocks[:3])

    # 8
    blocks = filter_manager.add_comment(516, 'Fishing Rod')
    blocks[0].PlayAlertSound = SOUND_TOP_VALUE
    filter_manager.extend_blocks(blocks)

    filter_manager.add_comment(517, 'SRS Crude Bow', ignored=True)

    # NEED_RGB
    blocks = filter_manager.add_comment(518, 'Chromatic recipe items ("RGB Recipe")')
    if settings.NEED_RGB:
        filter_manager.extend_blocks(blocks)

    filter_manager.add_comment(519, 'Endgame-start 4-links', ignored=True)

    filter_manager.add_comment(520, 'Animate Weapon script - deactivated by default', ignored=True)

    # 8 高亮边框
    blocks = filter_manager.add_comment(521, 'W-soc offhand weapons')
    for block in blocks:
        block.Class = '"Wands" "Daggers" "Sceptres" "Claws" "One Hand" "Shields"'
    blocks[0].modify(SetFontSize=FONT_SIZE_MAX, PlayAlertSound=SOUND_TOP_VALUE)
    blocks[1].SetBorderColor = COLOR_WHITE
    filter_manager.extend_blocks(blocks)

    blocks = filter_manager.add_comment(522, 'Sacrificial Garb')
    filter_manager.extend_blocks(blocks)


def modify_endgame_rare(filter_manager, show_rare_class=''):
    filter_manager.add_comment(900, 'RARE ITEMS (ENDGAME)', ignored=True)

    # 8
    blocks = filter_manager.add_comment(901, 'Rare crafting bases 86+')
    for block in blocks:
        block.PlayAlertSound = SOUND_TOP_VALUE
    filter_manager.extend_blocks(blocks)

    blocks = filter_manager.add_comment(902, 'Rare crafting bases 83+')
    filter_manager.extend_blocks(blocks)

    # T1_RARE_BASE_TYPE
    # block_1_3
    # HIDE_BELOW_T1_RARE_CLASS with Identified=False and show_rare_class
    blocks = filter_manager.add_comment(903, 'T1 rare items')
    if settings.T1_RARE_BASE_TYPE != '':
        filter_manager.append_block(blocks[0].copy_modify(BaseType=settings.T1_RARE_BASE_TYPE,
                                                          PlayAlertSound=SOUND_MID_VALUE, **STYLE_T1_RARE))
        filter_manager.append_block(blocks[1].copy_modify(BaseType=settings.T1_RARE_BASE_TYPE, ItemLevel=None,
                                                          PlayAlertSound=SOUND_MID_VALUE, **STYLE_T1_RARE))

    filter_manager.append_block(blocks[0].copy_modify(BaseType=None, Width='= 1', Height='= 3'))
    filter_manager.append_block(blocks[1].copy_modify(BaseType=None, Width='= 1', Height='= 3'))

    hide_blocks = filter_manager.get_blocks(BLOCK_HIDE_RARES_65)
    hide_rare_classes = ' '.join(['"Quivers"', '"Shields"', CLASS_TWO_HAND, settings.HIDE_BELOW_T1_RARE_CLASS])
    if show_rare_class:
        hide_rare_classes = hide_rare_classes.replace(show_rare_class, '')
    for block in hide_blocks:
        block.modify(status=DEBUG, Identified=False, Class=hide_rare_classes)
    filter_manager.extend_blocks(hide_blocks)

    filter_manager.extend_blocks(blocks)

    blocks = filter_manager.add_comment(904, 'T2 rare items')
    filter_manager.extend_blocks(blocks)

    blocks = filter_manager.add_comment(905, 'Breach Rings')
    filter_manager.extend_blocks(blocks)

    # 2  移除中间两个 1
    blocks = filter_manager.add_comment(906, 'Amulets, Jewels, Rings, Belts')
    blocks[0].PlayAlertSound = SOUND_LOW_VALUE  # rare jewel
    filter_manager.append_block(blocks[0])
    for block in blocks[3:]:
        block.modify(SetBorderColor=COLOR_YELLOW, PlayAlertSound=SOUND_MID_VALUE)
    blocks[4].ItemLevel = ITEM_LEVEL_CHAOS
    filter_manager.extend_blocks(blocks[3:])

    blocks = filter_manager.add_comment(907, '1H Daggers', ignored=settings.IGNORE_RARE_UNDER_T2)
    filter_manager.extend_blocks(blocks)

    blocks = filter_manager.add_comment(908, '1H Claws', ignored=settings.IGNORE_RARE_UNDER_T2)
    filter_manager.extend_blocks(blocks)

    blocks = filter_manager.add_comment(909, '1H Wands', ignored=settings.IGNORE_RARE_UNDER_T2)
    filter_manager.extend_blocks(blocks)

    blocks = filter_manager.add_comment(910, '1H Foils', ignored=settings.IGNORE_RARE_UNDER_T2)
    filter_manager.extend_blocks(blocks)

    blocks = filter_manager.add_comment(911, '1H Swords', ignored=settings.IGNORE_RARE_UNDER_T2)
    filter_manager.extend_blocks(blocks)

    blocks = filter_manager.add_comment(912, '1H Maces', ignored=settings.IGNORE_RARE_UNDER_T2)
    filter_manager.extend_blocks(blocks)

    blocks = filter_manager.add_comment(913, '1H Axes', ignored=settings.IGNORE_RARE_UNDER_T2)
    filter_manager.extend_blocks(blocks)

    blocks = filter_manager.add_comment(914, '1H Sceptres', ignored=settings.IGNORE_RARE_UNDER_T2)
    filter_manager.extend_blocks(blocks)

    blocks = filter_manager.add_comment(915, '2H Staves', ignored=settings.IGNORE_RARE_UNDER_T2)
    filter_manager.extend_blocks(blocks)

    blocks = filter_manager.add_comment(916, '2H Swords, Axes, Maces', ignored=settings.IGNORE_RARE_UNDER_T2)
    filter_manager.extend_blocks(blocks)

    blocks = filter_manager.add_comment(917, '2H Bows', ignored=settings.IGNORE_RARE_UNDER_T2)
    filter_manager.extend_blocks(blocks)

    blocks = filter_manager.add_comment(918, 'AR: Gloves, Boots, Helmets', ignored=settings.IGNORE_RARE_UNDER_T2)
    filter_manager.extend_blocks(blocks)

    blocks = filter_manager.add_comment(919, 'AR: Body Armors', ignored=settings.IGNORE_RARE_UNDER_T2)
    filter_manager.extend_blocks(blocks)

    blocks = filter_manager.add_comment(920, 'OH: Shields', ignored=settings.IGNORE_RARE_UNDER_T2)
    filter_manager.extend_blocks(blocks)

    blocks = filter_manager.add_comment(921, 'OH: Quivers', ignored=settings.IGNORE_RARE_UNDER_T2)
    filter_manager.extend_blocks(blocks)

    # NEED_RGB
    blocks = filter_manager.add_comment(922, 'Other Conditions', ignored=settings.IGNORE_RARE_UNDER_T2)
    if settings.NEED_RGB:
        filter_manager.extend_blocks(blocks)


def modify_gem_flask_map(filter_manager):
    filter_manager.add_comment(1100, 'OVERRIDE AREA 3 - Override Map, Gem and Flask drops here', ignored=True)

    filter_manager.add_comment(1200, 'Gems', ignored=True)

    # 8 8 8 1
    blocks = filter_manager.add_comment(1201, 'Value gems')
    blocks[0].PlayAlertSound = SOUND_TOP_VALUE
    blocks[1].PlayAlertSound = SOUND_TOP_VALUE
    blocks[2].modify(SetBackgroundColor=COLOR_WHITE, PlayAlertSound=SOUND_TOP_VALUE)
    blocks[2].BaseType += ' "Vaal Summon Skeletons" "Vaal Lightning Trap"'
    blocks[3].PlayAlertSound = SOUND_MID_VALUE
    filter_manager.extend_blocks(blocks)

    # 前两个换位 1   hide
    blocks = filter_manager.add_comment(1202, 'Other gems')
    blocks[0], blocks[1] = blocks[1], blocks[0]
    blocks[0].modify(SetFontSize=FONT_SIZE_MAX, PlayAlertSound=SOUND_MID_VALUE)
    blocks[-1].modify(status=DEBUG, SetFontSize=26)
    filter_manager.extend_blocks(blocks)

    # ALERT_UTILITY_FLASK_BASE_TYPE
    blocks = filter_manager.add_comment(1300, 'UTILITY FLASKS (Levelling Rules)')
    if settings.ALERT_UTILITY_FLASK_BASE_TYPE != '':
        blocks[1].modify(Class='"Utility Flasks"', BaseType=settings.ALERT_UTILITY_FLASK_BASE_TYPE)
        filter_manager.append_block(blocks[1])

    blocks = filter_manager.add_comment(1400, 'HIDE LAYER 3: Random Endgame Flasks')
    filter_manager.extend_blocks(blocks)

    filter_manager.add_comment(1500, 'Maps, fragments and labyrinth items', ignored=True)

    # 8
    blocks = filter_manager.add_comment(1501, 'Unique Maps')
    blocks[0].modify(BaseType=None, PlayAlertSound=SOUND_TOP_VALUE)
    filter_manager.append_block(blocks[0])

    blocks = filter_manager.add_comment(1502, 'Labyrinth items, Offerings')
    filter_manager.extend_blocks(blocks)

    # 8 STYLE_MAP_XXX
    blocks = filter_manager.add_comment(1503, 'Shaped Maps')
    blocks[0].PlayAlertSound = SOUND_TOP_VALUE
    blocks[1].modify(SetBorderColor=COLOR_RED, PlayAlertSound=SOUND_TOP_VALUE)
    blocks[2].modify(PlayAlertSound=SOUND_TOP_VALUE, **STYLE_MAP_HIGH_11_14)
    blocks[3].modify(DropLevel='>= 71', **STYLE_MAP_MID_9_10)
    blocks.append(blocks[3].copy_modify(DropLevel=None, **STYLE_MAP_MID_6_8))
    filter_manager.extend_blocks(blocks)

    # T15加红边
    blocks = filter_manager.add_comment(1504, 'Top tier maps (T15-16)')
    blocks[0].PlayAlertSound = SOUND_TOP_VALUE
    blocks[1].modify(SetBorderColor=COLOR_RED, PlayAlertSound=SOUND_TOP_VALUE)
    filter_manager.extend_blocks(blocks)

    # 加红边
    blocks = filter_manager.add_comment(1505, 'High tier maps(T11-14)')
    for block in blocks:
        block.modify(PlayAlertSound=SOUND_TOP_VALUE, **STYLE_MAP_HIGH_11_14)
    filter_manager.extend_blocks(blocks)

    # 加黄边/橙边，不显示稀有度
    blocks = filter_manager.add_comment(1506, 'Mid tier maps (T6-10)')
    for block in blocks[:3]:
        block.modify(PlayAlertSound=SOUND_MAP, **STYLE_MAP_MID_9_10)
    for block in blocks[3:]:
        block.modify(PlayAlertSound=SOUND_MAP, **STYLE_MAP_MID_6_8)
    filter_manager.extend_blocks(blocks)

    # 加蓝边/黑边，不显示稀有度
    blocks = filter_manager.add_comment(1507, 'Low tier maps (T1-T5)')
    for block in blocks[:6]:
        block.modify(PlayAlertSound=SOUND_MAP, **STYLE_MAP_LOW_3_5)
    for block in blocks[6:-1]:
        block.modify(PlayAlertSound=SOUND_MAP, **STYLE_MAP_LOW_1_2)
    filter_manager.extend_blocks(blocks)

    # 8 4
    blocks = filter_manager.add_comment(1508, 'Map fragments')
    for block in blocks[:-2]:
        block.PlayAlertSound = SOUND_TOP_VALUE
    blocks[-2].PlayAlertSound = SOUND_MAP
    blocks[-1].PlayAlertSound = SOUND_TOP_VALUE
    filter_manager.extend_blocks(blocks)


def modify_leveling(filter_manager):
    # 后期只要42和60级的血瓶
    filter_manager.add_comment(2200, 'OVERRIDE AREA 4 - Insert your custom Leveling adjustments here', ignored=True)
    hide_some_life_flasks = FilterBlock(status=DEBUG, Quality='= 0', Class='"Life Flask"',
                                        BaseType='Sanctified Eternal', SetFontSize=FONT_SIZE_MIN)
    filter_manager.append_block(hide_some_life_flasks)

    filter_manager.add_comment(2300, 'Leveling - Flasks', ignored=True)

    blocks = filter_manager.add_comment(2301, 'Hide outdated flasks')
    filter_manager.extend_blocks(blocks)

    filter_manager.add_comment(2302, 'Hybrid flasks (normal)', ignored=True)

    # SHOW_FLASK_HALLOWED 42, 60   SHOW_FLASK_LIFE
    blocks = filter_manager.add_comment(2303, 'Life Flasks - Normal (Kudos to Antnee)')
    if settings.SHOW_FLASK_LIFE:
        blocks[-4].ItemLevel = None if settings.SHOW_FLASK_HALLOWED else '<= 1'
        blocks[-2].ItemLevel = None
        filter_manager.extend_blocks(blocks)

    # SHOW_FLASK_MANA
    blocks = filter_manager.add_comment(2304, 'Mana Flasks - Magic (Kudos to Antnee)')
    if settings.SHOW_FLASK_MANA:
        filter_manager.extend_blocks(blocks)

    filter_manager.add_comment(2305, 'Show remaining flasks', ignored=True)

    # LINKED_CLASS
    blocks = filter_manager.add_comment(2400, 'Leveling - Merged Rules')
    if settings.LINKED_CLASS != '':
        for block in blocks:  # 4L RGB
            block.Class = settings.LINKED_CLASS
        filter_manager.extend_blocks(blocks)

    # NEED_RGB
    blocks = filter_manager.add_comment(2500, 'Leveling - RGB Recipes')
    if settings.NEED_RGB:
        filter_manager.extend_blocks(blocks)

    # hide_leveling_rares hide_some_body_rares  HIDE_BELOW_T1_RARE_CLASS
    filter_manager.add_comment(2600, 'Leveling - RARES', ignored=True)
    hide_leveling_rares = filter_manager.get_blocks(BLOCK_HIDE_RARES_65)[-1]
    hide_leveling_rares.modify(status=DEBUG, Identified=False, ItemLevel='>= 13',
                               Class='"Bows" "Quivers" "Two Hand" "Staves" "Shields" "Wands"', SetFontSize=26)
    hide_some_body_rares = hide_leveling_rares.copy_modify(
        ItemLevel='>= 23', Class='"Body Armour"',
        BaseType=' '.join([BASE_TYPE_BODY_EVA, BASE_TYPE_BODY_ES, BASE_TYPE_BODY_EE]))
    filter_manager.extend_blocks([hide_leveling_rares, hide_some_body_rares])
    if settings.HIDE_BELOW_T1_RARE_CLASS != '':
        hide_rares = hide_leveling_rares.copy_modify(Class=settings.HIDE_BELOW_T1_RARE_CLASS, ItemLevel=None)
        filter_manager.append_block(hide_rares)

    # Rare: 4L RRG RRR L3_MAX_IL   ALERT_RARE_ACCESSORY   提醒下(跑)鞋
    blocks = filter_manager.add_comment(2601, 'Leveling rares - specific items')
    if settings.LINKED_CLASS != '':
        blocks[0].modify(Class=settings.LINKED_CLASS, **STYLE_LINKS)
        rare_rrg = blocks[0].copy_modify(LinkedSockets='>= 3', SocketGroup='RRG',
                                         ItemLevel='<= ' + str(settings.L3_MAX_IL))
        rare_rrr = rare_rrg.copy_modify(SocketGroup='RRR')
        filter_manager.extend_blocks([blocks[0], rare_rrg, rare_rrr])
    blocks[2].PlayAlertSound = SOUND_LEVELING
    blocks[3].modify(Height=None, Class='"Boots" "Helmets" "Gloves"')
    filter_manager.extend_blocks(blocks[1:-1])

    blocks = filter_manager.add_comment(2602, 'Leveling rares - Progression')
    filter_manager.extend_blocks(blocks)

    blocks = filter_manager.add_comment(2603, 'Leveling rares - remaining rules')
    filter_manager.extend_blocks(blocks)

    filter_manager.add_comment(2700, 'Leveling - Useful items', ignored=True)

    # RR**
    blocks = filter_manager.add_comment(2701, 'Linked gear - 4links')
    if settings.LINKED_CLASS != '':
        for block in blocks:
            block.modify(Class=settings.LINKED_CLASS, SocketGroup='RR', **STYLE_LINKS)
            filter_manager.append_block(block)

    filter_manager.add_comment(2702, 'Linked gear - Caster Weapon Configuration', ignored=True)

    # RR RG RRG RRR L2_MAX_IL L3_MAX_IL
    blocks = filter_manager.add_comment(2703, 'Linked gear - 3links')
    if settings.LINKED_CLASS != '':
        for block in blocks[:2]:
            block.modify(LinkedSockets=None, Class=settings.LINKED_CLASS, **STYLE_LINKS)
            links_rr = block.copy_modify(SocketGroup='RR', ItemLevel='<= ' + str(settings.L2_MAX_IL),
                                         PlayAlertSound=SOUND_LEVELING)
            links_rg = block.copy_modify(SocketGroup='RG', ItemLevel='<= ' + str(settings.L2_MAX_IL),
                                         PlayAlertSound=SOUND_LEVELING)
            links_rrg = links_rg.copy_modify(SocketGroup='RRG', ItemLevel='<= ' + str(settings.L3_MAX_IL))
            links_rrr = links_rg.copy_modify(SocketGroup='RRR', ItemLevel='<= ' + str(settings.L3_MAX_IL))
            filter_manager.extend_blocks([links_rr, links_rg, links_rrg, links_rrr])

    filter_manager.add_comment(2704, 'Extra Highlight: Boots', ignored=True)

    filter_manager.add_comment(2705, 'Optional Recipes', ignored=True)

    # 注意，后续(13+)需要高亮的蓝白装已经在 "Remaining crafting rules" 里面了
    blocks = filter_manager.add_comment(BLOCK_ACT_1, 'Act 1')
    blocks[0].BaseType = '"Rustic Sash" "Amulet"' if settings.TENCENT else '"Iron Ring" "Rustic Sash" "Amulet"'
    blocks[1].BaseType = '"Iron Ring" "Rustic Sash" "Amulet"'
    filter_manager.extend_blocks(blocks[:2])

    filter_manager.add_comment(2707, 'Act 2+3', ignored=True)

    filter_manager.add_comment(2708, 'Act 4+5+6', ignored=True)

    filter_manager.add_comment(2709, 'Jewellery - Regular Highlight', ignored=True)

    filter_manager.add_comment(2710, 'Quivers - Progression', ignored=True)

    filter_manager.add_comment(2711, 'Magic Gear', ignored=True)

    filter_manager.add_comment(2712, '20% quality items for those strange people who want them', ignored=True)

    filter_manager.add_comment(2800, 'Leveling - normal and magic item progression', ignored=True)

    # 蓝白武器  HIDE_NORMAL_MAGIC_CLASS
    filter_manager.add_comment(2801, 'Progression - Part 1 1-30', ignored=True)
    if settings.SHOW_N2M_ONE_HAND:
        _LEVELING_BASE = [('"Rusted Sword"', 1 - 1), ('"Rusted Spike"', 3), ('"Copper Sword"', 5),
                          ('"Whalebone Rapier"', 7), ('"Sabre"', 10), ('"Jade Hatchet"', 6), ('"Boarding Axe"', 11),
                          ('"Broad Axe"', 21), ('"Wraith Axe"', 54), ]  # ('"Arming Axe"', 25 + 1),
        if not settings.TENCENT:
            _LEVELING_BASE.extend([('"Spectral Axe"', 33), ('"War Axe"', 45)])
        _LEVELING_BASE_IL_GAP = 3
        for weapon_template in filter_manager.get_blocks(BLOCK_ACT_1)[:2]:
            weapon_template.FontSize = 42
            weapons = [weapon_template.copy_modify(BaseType=leveling_base[0],
                                                   ItemLevel='<= ' + str(leveling_base[1] + _LEVELING_BASE_IL_GAP))
                       for leveling_base in _LEVELING_BASE]
            filter_manager.extend_blocks(weapons)

    hide_m_2 = filter_manager.get_blocks(BLOCK_HIDE_REMAINING)[0]
    hide_m_2.modify(Class=' '.join([CLASS_HAND, '"Flasks"', CLASS_ACCESSORY]), Rarity=RARITY_MAGIC,
                    ItemLevel='>= {}'.format(2 if settings.TENCENT else 6))
    hide_m_5 = hide_m_2.copy_modify(Class='"Helmets" "Gloves" "Boots" "Body Armour"',
                                    ItemLevel='>= {}'.format(5 if settings.TENCENT else 6))
    hide_n_2 = hide_m_2.copy_modify(Rarity=None, ItemLevel='>= 2', SetFontSize=FONT_SIZE_MIN)
    filter_manager.extend_blocks([hide_m_2, hide_m_5, hide_n_2])

    filter_manager.add_comment(2802, 'Progression - Part 2 30-40', ignored=True)

    filter_manager.add_comment(2803, 'Progression - Part 4 40-65', ignored=True)

    blocks = filter_manager.add_comment(2804, 'Normal items - First 12 levels - exceptions')
    filter_manager.extend_blocks(blocks)

    blocks = filter_manager.add_comment(2805, 'Magic items - general highlight')
    filter_manager.extend_blocks(blocks)


def modify_filter(filter_manager, show_rare_class=''):
    modify_endgame_mix(filter_manager)

    blocks = filter_manager.add_comment(600, 'HIDE LAYER 1 - MAGIC AND NORMAL ITEMS')
    blocks[0].status = DEBUG
    filter_manager.extend_blocks(blocks)

    # CURRENCY_ALERT_XXX CURRENCY_XXX_FONT_SIZE
    blocks = filter_manager.add_comment(700, 'Currency - PART 1 - Common currency')
    blocks[0].PlayAlertSound = SOUND_MID_VALUE
    blocks[1].BaseType = '"Orb of Alteration" "Chromatic Orb" "Jeweller\'s Orb" '
    if settings.CURRENCY_ALERT_TRANSMUTATION:
        blocks[1].BaseType += ' "Orb of Transmutation" '
    if settings.CURRENCY_ALERT_BLACKSMITH:
        blocks[1].BaseType += ' "Blacksmith\'s Whetstone" '
    if settings.CURRENCY_ALERT_AUGMENTATION:
        blocks[1].BaseType += ' "Orb of Augmentation" '
    if not settings.CURRENCY_ALERT_CHANCE:
        blocks[1].BaseType += ' "Orb of Chance" '
    if settings.ALERT_LOW_CURRENCY:
        blocks[1].PlayAlertSound = SOUND_LOW_VALUE
    blocks[2].BaseType = '"Orb of Transmutation" "Alchemy Shard" "Orb of Augmentation"'
    blocks[-3].SetFontSize = settings.CURRENCY_PORTAL_FONT_SIZE
    blocks[-2].BaseType += ' "Blacksmith\'s Whetstone" '
    blocks[-2].BaseType = blocks[-2].BaseType.replace('"Transmutation Shard"', '')
    blocks[-2].SetFontSize = settings.CURRENCY_ARMOURER_SCRAP_FONT_SIZE
    blocks[-1].SetFontSize = settings.CURRENCY_WISDOM_FONT_SIZE
    filter_manager.extend_blocks(blocks)

    filter_manager.add_comment(800, 'OVERRIDE AREA 2 - Override the default rare rulesets here', ignored=True)

    modify_endgame_rare(filter_manager, show_rare_class)

    blocks = filter_manager.add_comment(BLOCK_HIDE_RARES_65, 'HIDE LAYER 2 - RARE ITEMS (65+)')
    for block in blocks:
        block.status = DEBUG
    filter_manager.extend_blocks(blocks)

    modify_gem_flask_map(filter_manager)

    filter_manager.add_comment(1600, 'Currency - PART 2 - Rare currency', ignored=True)

    # 1 CURRENCY_ALERT_CHANCE
    blocks = filter_manager.add_comment(1601, 'Regular Rare Currency')
    for block in blocks:
        block.PlayAlertSound = SOUND_MID_VALUE
    if settings.CURRENCY_ALERT_CHANCE:
        blocks[1].BaseType += ' "Orb of Chance"'
    blocks[0].BaseType += ' ' + blocks[1].BaseType
    blocks[2].BaseType += ' "Glassblower\'s Bauble"'
    filter_manager.extend_blocks(blocks)

    # 1
    blocks = filter_manager.add_comment(1602, 'Harbinger Currency')
    blocks[0].BaseType += ' "Horizon Shard"'
    blocks[0].PlayAlertSound = SOUND_MID_VALUE
    filter_manager.extend_blocks(blocks)

    # 1 2 HIDE_NETS
    blocks = filter_manager.add_comment(1603, 'Bestiary Currency')
    blocks[0].PlayAlertSound = SOUND_MID_VALUE
    blocks[1].modify(PlayAlertSound=SOUND_LOW_VALUE, DisableDropSound=None)
    for block in blocks[3:]:
        block.status = HIDE
    if settings.HIDE_NETS:
        hide_nets = blocks[2].copy_modify(status=HIDE, BaseType=settings.HIDE_NETS)
        blocks.insert(2, hide_nets)
    filter_manager.extend_blocks(blocks)

    # 8
    blocks = filter_manager.add_comment(1604, 'Top Currency')
    blocks[0].PlayAlertSound = SOUND_TOP_VALUE
    filter_manager.extend_blocks(blocks)

    # ALERT_ESSENCE_BASE_TYPE 8 1
    blocks = filter_manager.add_comment(1605, 'Essence Tier List')
    blocks[0].PlayAlertSound = SOUND_TOP_VALUE
    blocks[0].BaseType += settings.ALERT_ESSENCE_BASE_TYPE
    blocks[1].PlayAlertSound = SOUND_MID_VALUE
    filter_manager.extend_blocks(blocks)

    # 8 1 8 X 8
    blocks = filter_manager.add_comment(1606, 'Special items')
    blocks[0].PlayAlertSound = SOUND_TOP_VALUE
    blocks[1].PlayAlertSound = SOUND_MID_VALUE
    blocks[2].modify(PlayAlertSound=SOUND_TOP_VALUE, **STYLE_TOP)
    blocks[3].PlayAlertSound = None
    blocks[-1].PlayAlertSound = SOUND_TOP_VALUE
    filter_manager.extend_blocks(blocks)

    filter_manager.add_comment(1700, 'Currency - PART 3 - Divination cards (yes the strange sorting is intended)',
                               ignored=True)

    blocks = filter_manager.add_comment(1701, 'Exceptions to prevent ident. mistakes')
    filter_manager.extend_blocks(blocks)  # T4

    # 8
    blocks = filter_manager.add_comment(1702, 'T1 - Top tier cards', ignored=settings.TEMP)
    if blocks:
        blocks[0].PlayAlertSound = SOUND_TOP_VALUE
        filter_manager.extend_blocks(blocks)

    # 8
    blocks = filter_manager.add_comment(1703, 'T2 - Great cards', ignored=settings.TEMP)
    if blocks:
        blocks[0].PlayAlertSound = SOUND_TOP_VALUE
        blocks[0].BaseType += ' "The Encroaching Darkness" "The Throne" '
        filter_manager.extend_blocks(blocks)

    # 1
    blocks = filter_manager.add_comment(1704, 'T3 - Decent cards', ignored=settings.TEMP)
    if blocks:
        blocks[0].PlayAlertSound = SOUND_MID_VALUE
        filter_manager.extend_blocks(blocks)

    # FONT_SIZE_MIN or 2
    blocks = filter_manager.add_comment(1705, 'T5 - Format trash tier cards... before', ignored=settings.TEMP)
    if blocks:
        hide_cards = blocks[0].copy_modify(status=DEBUG, BaseType='"Carrion Crow" '  # Shit
                                                                  '"King\'s Blade" '  # (110-134)% 物理 永恒之剑
                                                                  '"Prosperity" '  # T1 稀有度 金光戒指
                                                                  '"Struck by Lightning" '  # 点电伤 宝石
                                                                  '"The Inoculated" '  # T1 混合 ES% 护甲
                                                                  '"The Rabid Rhoa" '  # 混沌伤 双子战爪
                                                                  '"The Sigil" '  # T1 ES% 项链
                                                                  '"The Surgeon" '  # 暴击充能 药剂
                                                                  '"The Twins"',  # T1 攻速 双子战爪
                                           SetFontSize=FONT_SIZE_MIN)
        filter_manager.append_block(hide_cards)
        blocks[0].SetFontSize = FONT_SIZE_MIN
        if settings.SSF:
            blocks[0].modify(SetFontSize=40, PlayAlertSound=SOUND_LOW_VALUE)
        filter_manager.extend_blocks(blocks)

    blocks = filter_manager.add_comment(1706, 'T4 - ...showing the remaining cards')
    filter_manager.extend_blocks(blocks)

    # CATCHALL
    blocks = filter_manager.add_comment(1800, 'Currency - PART 4 - remaining items')
    blocks[0].BaseType += ' "Transmutation Shard" '
    blocks[0].SetFontSize = FONT_SIZE_MIN
    blocks[1].modify(PlayAlertSound=SOUND_TOP_VALUE, **STYLE_TOP)
    filter_manager.extend_blocks(blocks)

    blocks = filter_manager.add_comment(1900, 'Leaguestones - Tierlists')
    for block in blocks[:-1]:
        block.PlayAlertSound = SOUND_MID_VALUE
    filter_manager.extend_blocks(blocks)

    filter_manager.add_comment(2000, 'Uniques!', ignored=True)

    # 同T1
    blocks = filter_manager.add_comment(2001, 'Exceptions')
    for block in blocks:
        block.PlayAlertSound = SOUND_TOP_VALUE
    blocks[0].modify(**STYLE_TOP_UNIQUE)
    filter_manager.extend_blocks(blocks)

    # 6
    blocks = filter_manager.add_comment(2002, 'Harbinger - Pieces')
    blocks[0].PlayAlertSound = SOUND_UNIQUE
    filter_manager.extend_blocks(blocks)

    # 8
    blocks = filter_manager.add_comment(2003, 'Tier 1 uniques')
    for block in blocks:
        block.PlayAlertSound = SOUND_TOP_VALUE
    blocks[0].BaseType += ' "Basket Rapier" "Twilight Blade" '
    filter_manager.extend_blocks(blocks)

    # 同T1
    blocks = filter_manager.add_comment(2004, 'Tier 2 uniques')
    for block in blocks:
        block.modify(PlayAlertSound=SOUND_TOP_VALUE, **STYLE_TOP_UNIQUE)
    filter_manager.extend_blocks(blocks)

    # 6
    blocks = filter_manager.add_comment(2005, 'Multi-Unique bases.')
    blocks[0].PlayAlertSound = SOUND_UNIQUE
    filter_manager.extend_blocks(blocks)

    # 6
    blocks = filter_manager.add_comment(2006, 'Prophecy-Material Uniques')
    blocks[0].modify(SetFontSize=FONT_SIZE_MAX, PlayAlertSound=SOUND_UNIQUE)
    filter_manager.extend_blocks(blocks)

    # 6
    blocks = filter_manager.add_comment(2007, 'Random Uniques')
    blocks[0].modify(SetFontSize=FONT_SIZE_MAX, PlayAlertSound=SOUND_UNIQUE)
    filter_manager.extend_blocks(blocks)

    blocks = filter_manager.add_comment(2100, 'Quest Items and Shaper Orbs')
    filter_manager.extend_blocks(blocks)

    modify_leveling(filter_manager)

    blocks = filter_manager.add_comment(BLOCK_HIDE_REMAINING, 'HIDE LAYER 5 - Remaining Items')
    blocks[0].modify(status=DEBUG, SetFontSize=FONT_SIZE_MIN)
    filter_manager.extend_blocks(blocks)

    # 8
    blocks = filter_manager.add_comment(3000, 'CATCHALL')
    blocks[0].PlayAlertSound = SOUND_TOP_VALUE
    filter_manager.extend_blocks(blocks)

    filter_manager.add_comment(3100, 'Special thanks to!', ignored=True)


def main():
    filter_name = 'res' + os.sep + 'NeverSink\'s filter - 1-REGULAR.filter'
    with open(filter_name) as f:
        fm = FilterManager(f.readlines())

    show_rare_classes = [
        ('', 'MODIFY'),
        ('"Helmets"', '头'),
        ('"Gloves"', '手'),
        ('"Boots"', '脚'),
        ('"Body Armour"', '胸'),
        (CLASS_TWO_HAND, '双手'),
    ]

    for clazz, gen_filter_name in show_rare_classes:
        fm.clear()
        modify_filter(fm, clazz)

        gen_filter_name += '.filter'
        out_file_path = 'out' + os.sep + gen_filter_name
        with open(out_file_path, 'w') as f:
            f.writelines(fm.new_text)
        if platform.system() == 'Windows':
            shutil.copyfile(out_file_path,
                            os.path.expanduser('~') + f'\Documents\My Games\Path of Exile\{gen_filter_name}')


if __name__ == '__main__':
    start_time = time.time()
    main()
    print("Modify success, time cost: {:.0f}ms".format(1000 * (time.time() - start_time)))
