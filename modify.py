# -*- coding:utf-8 -*-

import time
import os
import platform

import shutil

from utils import FilterBlock, FilterManager
import settings

SHOW = 'Show'
HIDE = 'Hide'
DEBUG = SHOW if settings.DEBUG else HIDE

CLASS_WEAPON = '"Bows" "Quivers" "Two Hand" "Staves" "Shields" "Claws" "Sceptres" "Daggers" "Wands" "One Hand"'
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

BLOCK_5L = 401
BLOCK_6S = 402
BLOCK_HIDE_RARES_65 = 900
BLOCK_ACT_1 = 2606
BLOCK_HIDE_REMAINING = 2800  # SetFontSize=FONT_SIZE_MIN


# [[0100 - 0400]]
def modify_endgame_mix(filter_manager):
    # 8
    blocks = filter_manager.add_comment(100, 'OVERRIDE AREA 1 - Override ALL rules here')
    blocks[0].PlayAlertSound = SOUND_TOP_VALUE
    filter_manager.extend_blocks(blocks)

    # blocks_5l
    blocks_5l = filter_manager.get_blocks(BLOCK_5L)
    blocks_5l[0].PlayAlertSound = SOUND_TOP_VALUE
    blocks_5l[1].PlayAlertSound = SOUND_TOP_VALUE
    filter_manager.extend_blocks(blocks_5l)

    # block_6s_body
    if not settings.TENCENT:
        block_6s_body = filter_manager.get_blocks(BLOCK_6S)[0]
        block_6s_body.modify(ItemLevel=None, BaseType='"Astral Plate" "Glorious Plate" "Gladiator Plate"',
                             PlayAlertSound=SOUND_TOP_VALUE, **STYLE_TOP)
        filter_manager.extend_blocks(block_6s_body)

    filter_manager.add_comment(200, 'SHAPER ITEMS', ignored=True)

    # 8 10 10
    blocks = filter_manager.add_comment(201, 'Exception Handling - Rings, Amulets, Belts')
    blocks[0].PlayAlertSound = SOUND_TOP_VALUE
    blocks[0].PlayAlertSound = SOUND_SHAPER_ELDER
    blocks[0].PlayAlertSound = SOUND_SHAPER_ELDER
    filter_manager.extend_blocks(blocks)

    # 8
    blocks = filter_manager.add_comment(202, 'Shaper Item Layers - T1')
    for block in blocks:
        block.PlayAlertSound = SOUND_TOP_VALUE
    filter_manager.extend_blocks(blocks)

    blocks = filter_manager.add_comment(203, 'Shaper Item Layers - T2')
    filter_manager.extend_blocks(blocks)

    # 10
    blocks = filter_manager.add_comment(204, 'Shaper Item Layers - T3')
    for block in blocks:
        block.PlayAlertSound = SOUND_SHAPER_ELDER
    filter_manager.extend_blocks(blocks)

    filter_manager.add_comment(300, 'ELDER ITEMS', ignored=True)

    # 8 10 10
    blocks = filter_manager.add_comment(301, 'Exception Handling - Rings, Amulets, Belts')
    blocks[0].PlayAlertSound = SOUND_TOP_VALUE
    blocks[0].PlayAlertSound = SOUND_SHAPER_ELDER
    blocks[0].PlayAlertSound = SOUND_SHAPER_ELDER
    filter_manager.extend_blocks(blocks)

    # 8
    blocks = filter_manager.add_comment(302, 'Elder Item Layers - T1')
    for block in blocks:
        block.PlayAlertSound = SOUND_TOP_VALUE
    filter_manager.extend_blocks(blocks)

    blocks = filter_manager.add_comment(303, 'Elder Item Layers - T2')
    filter_manager.extend_blocks(blocks)

    # 10
    blocks = filter_manager.add_comment(304, 'Elder Item Layers - T3')
    for block in blocks:
        block.PlayAlertSound = SOUND_SHAPER_ELDER
    filter_manager.extend_blocks(blocks)

    filter_manager.add_comment(400, 'Recipes, Magic and Normal items (endgame!)', ignored=True)

    filter_manager.add_comment(BLOCK_5L, '5-Linked items', ignored=True)

    # 8 样式改掉
    blocks = filter_manager.add_comment(BLOCK_6S, '6-Socket Items')
    blocks[0].modify(PlayAlertSound=SOUND_TOP_VALUE, **STYLE_TOP)
    blocks[1].modify(PlayAlertSound=SOUND_TOP_VALUE, **STYLE_TOP)
    del blocks[2]  # 移除不需要的提示
    blocks[-1].modify(SetTextColor=COLOR_WHITE, SetBorderColor=COLOR_BLACK, SetBackgroundColor=COLOR_TANGERINE)
    filter_manager.extend_blocks(blocks)

    # 8 2 12
    blocks = filter_manager.add_comment(403, 'Exclusive bases: Stygian Vise')
    blocks[0].PlayAlertSound = SOUND_TOP_VALUE
    blocks[1].modify(SetBorderColor='25 235 25', PlayAlertSound=SOUND_LOW_VALUE)
    blocks[2].modify(SetBorderColor='25 235 25', PlayAlertSound=SOUND_LEVELING)
    filter_manager.extend_blocks(blocks)

    # 8 8 2 去掉最后一个
    blocks = filter_manager.add_comment(404, 'Abyss Jewels (Rare and Magic)')
    blocks[0].PlayAlertSound = SOUND_TOP_VALUE
    blocks[1].PlayAlertSound = SOUND_TOP_VALUE
    blocks[2].PlayAlertSound = SOUND_LOW_VALUE
    filter_manager.extend_blocks(blocks[:3])

    # 8 1 2 ALERT_ATLAS_BASE_TYPE
    blocks = filter_manager.add_comment(405, 'Exclusive bases: Atlas bases, talismans (includes Rare rarity)')
    blocks[0].modify(PlayAlertSound=SOUND_TOP_VALUE, **STYLE_TOP)
    blocks[1].modify(PlayAlertSound=SOUND_TOP_VALUE, **STYLE_TOP)
    blocks[2].modify(PlayAlertSound=SOUND_MID_VALUE, **STYLE_TOP_RARE)
    blocks[3].modify(ItemLevel=None, SetTextColor=None, PlayAlertSound=SOUND_MID_VALUE, **STYLE_TOP_RARE)
    blocks[4].modify(BaseType=settings.ALERT_ATLAS_BASE_TYPE, PlayAlertSound=SOUND_LOW_VALUE, **STYLE_TOP_RARE)

    filter_manager.extend_blocks(blocks)

    # 改稀有度
    # 项链：+1诅咒，+1球，抗性上限；  腰带：+1球
    # 手：击中附加诅咒；  脚：+1球；  箭袋：+1箭；  爪匕剑：3-6%格挡
    filter_manager.add_comment(406, 'Corrupted items', ignored=True)
    accessories = FilterBlock(Corrupted=True, Class='"Amulets" "Belts"', Rarity=RARITY_N2R,
                              SetFontSize=36, SetBorderColor=COLOR_MAGENTA_DARK)
    others = accessories.copy_modify(Class='"Gloves" "Boots" "Quivers" "Claws" "Daggers" "One Hand Swords"',
                                     SetFontSize=None)
    filter_manager.extend_blocks([accessories, others])

    # 参考模板 CHANCING_BASE_TYPE
    filter_manager.add_comment(407, 'Chancing items', ignored=True)
    if settings.CHANCING_BASE_TYPE != '':
        block = FilterBlock(Corrupted=False, BaseType=settings.CHANCING_BASE_TYPE, Rarity=RARITY_NORMAL,
                            SetFontSize=42, SetTextColor=COLOR_WHITE, SetBorderColor=COLOR_LIME_LIGHT)
        filter_manager.append_block(block)

    # ALERT_UTILITY_FLASK_BASE_TYPE
    # CURRENCY_ALERT_BLACKSMITH
    blocks = filter_manager.add_comment(408, 'FLASKS (Endgame rules)')
    for block in blocks:
        block.SetFontSize = FONT_SIZE_MAX
    if settings.ALERT_UTILITY_FLASK_BASE_TYPE != '':
        utility_flasks = blocks[-1].copy_modify(BaseType=settings.ALERT_UTILITY_FLASK_BASE_TYPE,
                                                PlayAlertSound=SOUND_LEVELING)
        filter_manager.append_block(utility_flasks)
    if settings.CURRENCY_ALERT_BLACKSMITH:
        blocks[0].PlayAlertSound = SOUND_LOW_VALUE
        blocks[1].PlayAlertSound = SOUND_LOW_VALUE
        filter_manager.extend_blocks(blocks[:2])

    filter_manager.add_comment(409, 'Add your own crafting rules here', ignored=True)

    # 8
    blocks = filter_manager.add_comment(410, '86+ Endgame crafting rules')
    blocks[0].PlayAlertSound = SOUND_TOP_VALUE
    filter_manager.extend_blocks(blocks)

    blocks = filter_manager.add_comment(411, '83/84+ Endgame crafting rules')
    filter_manager.append_block(blocks[0])
    blocks[2].BaseType = '"Siege Axe"'
    filter_manager.append_block(blocks[2])

    # 12
    blocks = filter_manager.add_comment(412, 'Magic jewel and others')
    if settings.ALERT_JEWEL_BASE_TYPE != '':
        magic_jewels = blocks[0].copy_modify(BaseType=settings.ALERT_JEWEL_BASE_TYPE, PlayAlertSound=SOUND_LEVELING)
        filter_manager.append_block(magic_jewels)
        filter_manager.append_block(blocks[0])

    filter_manager.add_comment(413, 'Warband items', ignored=True)

    # ALERT_NORMAL_BASE_TYPE, SSF_CRAFT_AMULETS_BASE_TYPE, SSF_CRAFT_RINGS_BASE_TYPE, SSF_CRAFT_BELTS_BASE_TYPE
    # ALERT_MAGIC_BASE_TYPE
    filter_manager.add_comment(414, 'Remaining crafting rules - add your own bases here!', ignored=True)
    if settings.ALERT_NORMAL_BASE_TYPE != '':
        normals = filter_manager.get_blocks(BLOCK_ACT_1)[0]
        normals.modify(BaseType=settings.ALERT_NORMAL_BASE_TYPE, ItemLevel=None,
                       SetFontSize=40, PlayAlertSound=SOUND_LEVELING)
        str_n = normals.copy_modify(BaseType='"Amber Amulet" "Heavy Belt"', ItemLevel='<= 12')
        filter_manager.extend_blocks([str_n, normals])

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
    blocks = filter_manager.add_comment(415, 'Chisel recipe items')
    for block in blocks:
        block.PlayAlertSound = SOUND_MID_VALUE
    blocks[0].SetFontSize = FONT_SIZE_MAX
    blocks[1].Quality = '>= 10' if settings.NEED_CHISEL else '>= 14'
    blocks[2].Quality = '>= 0' if settings.NEED_CHISEL else '>= 5'
    filter_manager.extend_blocks(blocks[:3])

    # 8
    blocks = filter_manager.add_comment(416, 'Fishing Rod')
    blocks[0].PlayAlertSound = SOUND_TOP_VALUE
    filter_manager.extend_blocks(blocks)

    filter_manager.add_comment(417, 'SRS Crude Bow', ignored=True)

    # NEED_RGB
    blocks = filter_manager.add_comment(418, 'Chromatic recipe items ("RGB Recipe")')
    if settings.NEED_RGB:
        filter_manager.extend_blocks(blocks)

    filter_manager.add_comment(419, 'Endgame-start 4-links', ignored=True)

    filter_manager.add_comment(420, 'Animate Weapon script - deactivated by default', ignored=True)

    # 8，改稀有度，高亮边框
    blocks = filter_manager.add_comment(421, 'W-soc offhand weapons')
    for block in blocks:
        block.Class = '"Wands" "Daggers" "One Hand" "Shields" "Sceptres" "Claws"'
    blocks[0].modify(SetFontSize=FONT_SIZE_MAX, PlayAlertSound=SOUND_TOP_VALUE)
    blocks[1].modify(Rarity=RARITY_N2R, SetFontSize=38, SetBorderColor=COLOR_WHITE)
    filter_manager.extend_blocks(blocks)

    blocks = filter_manager.add_comment(422, 'Sacrificial Garb')
    filter_manager.extend_blocks(blocks)


# [[0800]]
def modify_endgame_rare(filter_manager):
    filter_manager.add_comment(800, 'RARE ITEMS (ENDGAME)', ignored=True)

    # 8 1
    blocks = filter_manager.add_comment(801, 'Rare crafting bases')
    blocks[0].PlayAlertSound = SOUND_TOP_VALUE
    blocks[1].PlayAlertSound = SOUND_MID_VALUE
    filter_manager.extend_blocks(blocks)

    # T1_RARE_BASE_TYPE
    # HIDE_BELOW_T1_RARE_CLASS
    blocks = filter_manager.add_comment(802, 'T1 rare items')
    if settings.T1_RARE_BASE_TYPE != '':
        filter_manager.append_block(blocks[0].copy_modify(BaseType=settings.T1_RARE_BASE_TYPE,
                                                          PlayAlertSound=SOUND_MID_VALUE, **STYLE_T1_RARE))
        filter_manager.append_block(blocks[1].copy_modify(BaseType=settings.T1_RARE_BASE_TYPE, ItemLevel=None,
                                                          PlayAlertSound=SOUND_MID_VALUE, **STYLE_T1_RARE))

    hide_blocks = filter_manager.get_blocks(BLOCK_HIDE_RARES_65)
    for block in hide_blocks[-2:]:
        block.modify(status=DEBUG, Identified=False, Class='"Bows" "Quivers" "Two Hand" "Staves" "Shields"',
                     SetFontSize=26)
    if settings.NEED_REGAL:
        hide_blocks[-1].ItemLevel = '<= 74'
    filter_manager.extend_blocks(hide_blocks[-1 if settings.NEED_REGAL else -2:])
    if settings.HIDE_BELOW_T1_RARE_CLASS != '':
        hide_blocks[-2].Class = settings.HIDE_BELOW_T1_RARE_CLASS
        hide_blocks[-1].Class = settings.HIDE_BELOW_T1_RARE_CLASS
        filter_manager.extend_blocks(hide_blocks[-1 if settings.NEED_REGAL else -2:])

    filter_manager.extend_blocks(blocks)

    blocks = filter_manager.add_comment(803, 'T2 rare items')
    filter_manager.extend_blocks(blocks)

    blocks = filter_manager.add_comment(804, 'Breach Rings')
    filter_manager.extend_blocks(blocks)

    # ALERT_RARE_ACCESSORY
    # 2
    blocks = filter_manager.add_comment(805, 'Amulets, Jewels, Rings, Belts')
    blocks[0].PlayAlertSound = SOUND_LOW_VALUE  # rare jewel
    blocks[1].SetFontSize = 36
    blocks[2].SetFontSize = 36
    if settings.SHOW_RARE_ACCESSORY != '':
        for block in blocks[1:]:
            block.Class = settings.SHOW_RARE_ACCESSORY
    if settings.NEED_REGAL:
        blocks[1].modify(Class=CLASS_ACCESSORY, PlayAlertSound=SOUND_MID_VALUE)
        blocks[3].modify(Class=CLASS_ACCESSORY, PlayAlertSound=SOUND_MID_VALUE)
    if settings.NEED_CHAOS:
        blocks[2].modify(Class=CLASS_ACCESSORY, PlayAlertSound=SOUND_MID_VALUE)
        blocks[4].modify(Class=CLASS_ACCESSORY, PlayAlertSound=SOUND_MID_VALUE)
    filter_manager.extend_blocks(blocks)

    blocks = filter_manager.add_comment(806, '1H Daggers', ignored=settings.IGNORE_RARE_UNDER_T2)
    filter_manager.extend_blocks(blocks)

    blocks = filter_manager.add_comment(807, '1H Claws', ignored=settings.IGNORE_RARE_UNDER_T2)
    filter_manager.extend_blocks(blocks)

    blocks = filter_manager.add_comment(808, '1H Wands', ignored=settings.IGNORE_RARE_UNDER_T2)
    filter_manager.extend_blocks(blocks)

    blocks = filter_manager.add_comment(809, '1H Foils', ignored=settings.IGNORE_RARE_UNDER_T2)
    filter_manager.extend_blocks(blocks)

    blocks = filter_manager.add_comment(810, '1H Swords', ignored=settings.IGNORE_RARE_UNDER_T2)
    filter_manager.extend_blocks(blocks)

    blocks = filter_manager.add_comment(811, '1H Maces', ignored=settings.IGNORE_RARE_UNDER_T2)
    filter_manager.extend_blocks(blocks)

    blocks = filter_manager.add_comment(812, '1H Axes', ignored=settings.IGNORE_RARE_UNDER_T2)
    filter_manager.extend_blocks(blocks)

    blocks = filter_manager.add_comment(813, '1H Sceptres', ignored=settings.IGNORE_RARE_UNDER_T2)
    filter_manager.extend_blocks(blocks)

    blocks = filter_manager.add_comment(814, '2H Staves', ignored=settings.IGNORE_RARE_UNDER_T2)
    filter_manager.extend_blocks(blocks)

    blocks = filter_manager.add_comment(815, '2H Swords, Axes, Maces', ignored=settings.IGNORE_RARE_UNDER_T2)
    filter_manager.extend_blocks(blocks)

    blocks = filter_manager.add_comment(816, '2H Bows', ignored=settings.IGNORE_RARE_UNDER_T2)
    filter_manager.extend_blocks(blocks)

    blocks = filter_manager.add_comment(817, 'AR: Gloves, Boots, Helmets', ignored=settings.IGNORE_RARE_UNDER_T2)
    filter_manager.extend_blocks(blocks)

    blocks = filter_manager.add_comment(818, 'AR: Body Armors', ignored=settings.IGNORE_RARE_UNDER_T2)
    filter_manager.extend_blocks(blocks)

    blocks = filter_manager.add_comment(819, 'OH: Shields', ignored=settings.IGNORE_RARE_UNDER_T2)
    filter_manager.extend_blocks(blocks)

    blocks = filter_manager.add_comment(820, 'OH: Quivers', ignored=settings.IGNORE_RARE_UNDER_T2)
    filter_manager.extend_blocks(blocks)


# [[1000]]-[[1400]]
def modify_gem_flask_map(filter_manager):
    filter_manager.add_comment(1000, 'OVERRIDE AREA 3 - Override Map, Gem and Flask drops here', ignored=True)

    filter_manager.add_comment(1100, 'Gems', ignored=True)

    # 8 LEVELING_GEMS_BASE_TYPE 1
    blocks = filter_manager.add_comment(1101, 'Value gems')
    blocks[0].PlayAlertSound = SOUND_TOP_VALUE
    blocks[1].PlayAlertSound = SOUND_TOP_VALUE
    blocks[2].modify(SetBackgroundColor=COLOR_WHITE, PlayAlertSound=SOUND_TOP_VALUE)
    blocks[2].BaseType += ' "Vaal Summon Skeletons" "Vaal Lightning Trap" ' + settings.LEVELING_GEMS_BASE_TYPE
    blocks[3].PlayAlertSound = SOUND_MID_VALUE
    filter_manager.extend_blocks(blocks)

    # 前两个换位，改成1和2   LEVELING_GEMS_BASE_TYPE
    blocks = filter_manager.add_comment(1102, 'Other gems')
    blocks[0], blocks[1] = blocks[1], blocks[0]
    blocks[0].modify(SetFontSize=FONT_SIZE_MAX, PlayAlertSound=SOUND_MID_VALUE)
    blocks[1].modify(SetFontSize=FONT_SIZE_MAX, PlayAlertSound=SOUND_LOW_VALUE)
    if '"Immortal Call"' not in settings.LEVELING_GEMS_BASE_TYPE:
        blocks[-1].status = DEBUG
    filter_manager.extend_blocks(blocks)

    # ALERT_UTILITY_FLASK_BASE_TYPE
    blocks = filter_manager.add_comment(1200, 'UTILITY FLASKS (Levelling Rules)')
    if settings.ALERT_UTILITY_FLASK_BASE_TYPE != '':
        blocks[1].modify(Class='"Utility Flasks"', BaseType=settings.ALERT_UTILITY_FLASK_BASE_TYPE)
        filter_manager.append_block(blocks[1])

    blocks = filter_manager.add_comment(1300, 'HIDE LAYER 3: Random Endgame Flasks')
    filter_manager.extend_blocks(blocks)

    filter_manager.add_comment(1400, 'Maps, fragments and labyrinth items', ignored=True)

    # 8
    blocks = filter_manager.add_comment(1401, 'Unique Maps')
    blocks[0].modify(BaseType=None, PlayAlertSound=SOUND_TOP_VALUE)
    filter_manager.append_block(blocks[0])

    blocks = filter_manager.add_comment(1402, 'Labyrinth items, Offerings')
    filter_manager.extend_blocks(blocks)

    blocks = filter_manager.add_comment(1403, 'Shaped Maps')
    blocks[0].modify(SetBorderColor=COLOR_RED, PlayAlertSound=SOUND_TOP_VALUE)
    blocks[1].modify(PlayAlertSound=SOUND_TOP_VALUE, **STYLE_MAP_HIGH_11_14)
    blocks[2].modify(DropLevel='>= 71', **STYLE_MAP_MID_9_10)
    blocks.append(blocks[2].copy_modify(DropLevel=None, **STYLE_MAP_MID_6_8))
    filter_manager.extend_blocks(blocks)

    # T15加红边
    blocks = filter_manager.add_comment(1404, 'Top tier maps (T15-16)')
    blocks[0].PlayAlertSound = SOUND_TOP_VALUE
    blocks[1].modify(SetBorderColor=COLOR_RED, PlayAlertSound=SOUND_TOP_VALUE)
    filter_manager.extend_blocks(blocks)

    # 加红边
    blocks = filter_manager.add_comment(1405, 'High tier maps(T11-14)')
    for block in blocks:
        block.modify(PlayAlertSound=SOUND_TOP_VALUE, **STYLE_MAP_HIGH_11_14)
    filter_manager.extend_blocks(blocks)

    # 加黄边/橙边，不显示稀有度
    blocks = filter_manager.add_comment(1406, 'Mid tier maps (T6-10)')
    for block in blocks[:3]:
        block.modify(PlayAlertSound=SOUND_MAP, **STYLE_MAP_MID_9_10)
    for block in blocks[3:]:
        block.modify(PlayAlertSound=SOUND_MAP, **STYLE_MAP_MID_6_8)
    filter_manager.extend_blocks(blocks)

    # 加蓝边/黑边，不显示稀有度
    blocks = filter_manager.add_comment(1407, 'Low tier maps (T1-T5)')
    for block in blocks[:6]:
        block.modify(PlayAlertSound=SOUND_MAP, **STYLE_MAP_LOW_3_5)
    for block in blocks[6:-1]:
        block.modify(PlayAlertSound=SOUND_MAP, **STYLE_MAP_LOW_1_2)
    filter_manager.extend_blocks(blocks)

    # 8, 4
    blocks = filter_manager.add_comment(1408, 'Map fragments')
    for block in blocks[:-2]:
        block.PlayAlertSound = SOUND_TOP_VALUE
    blocks[-2].modify(SetFontSize=FONT_SIZE_MAX, PlayAlertSound=SOUND_MAP)
    blocks[-1].PlayAlertSound = SOUND_TOP_VALUE
    filter_manager.extend_blocks(blocks)


# [[2100]]-[[2700]]
def modify_leveling(filter_manager):
    # 后期只要42和60级的血瓶
    filter_manager.add_comment(2100, 'OVERRIDE AREA 4 - Insert your custom leveling adjustments here', ignored=True)
    hide_some_life_flasks = FilterBlock(status=DEBUG, Quality='= 0', Class='"Life Flask"',
                                        BaseType='Sanctified Eternal', SetFontSize=FONT_SIZE_MIN)
    filter_manager.append_block(hide_some_life_flasks)

    filter_manager.add_comment(2200, 'Leveling - Flasks', ignored=True)

    blocks = filter_manager.add_comment(2201, 'Hide outdated flasks')
    filter_manager.extend_blocks(blocks)

    filter_manager.add_comment(2202, 'Hybrid flasks', ignored=True)

    # SHOW_FLASK_HALLOWED 42, 60   SHOW_FLASK_LIFE
    blocks = filter_manager.add_comment(2203, 'Life Flasks')
    if settings.SHOW_FLASK_LIFE:
        blocks[-4].ItemLevel = None if settings.SHOW_FLASK_HALLOWED else '<= 1'
        blocks[-2].ItemLevel = None
        filter_manager.extend_blocks(blocks)

    # SHOW_FLASK_MANA
    blocks = filter_manager.add_comment(2204, 'Mana Flasks')
    if settings.SHOW_FLASK_MANA:
        filter_manager.extend_blocks(blocks)

    # 15改成10  CURRENCY_ALERT_BLACKSMITH
    blocks = filter_manager.add_comment(2205, 'Show remaining flasks')
    blocks[0].SetFontSize = FONT_SIZE_MAX
    blocks[1].modify(SetFontSize=FONT_SIZE_MAX, Quality='>= 10')
    if settings.CURRENCY_ALERT_BLACKSMITH:
        filter_manager.extend_blocks(blocks[:2])

    # LINKED_CLASS
    blocks = filter_manager.add_comment(2300, 'Leveling - Merged Rules')
    if settings.LINKED_CLASS != '':
        for block in blocks:  # 4L RGB
            block.Class = settings.LINKED_CLASS
        filter_manager.extend_blocks(blocks)

    # NEED_RGB
    blocks = filter_manager.add_comment(2400, 'Leveling - RGB Recipes')
    if settings.NEED_RGB:
        filter_manager.extend_blocks(blocks)

    # hide_leveling_rares hide_some_body_rares  HIDE_BELOW_T1_RARE_CLASS
    filter_manager.add_comment(2500, 'Leveling - RARES', ignored=True)
    hide_big_rares = filter_manager.get_blocks(BLOCK_HIDE_RARES_65)[-1]
    hide_big_rares.modify(status=DEBUG, Identified=False, ItemLevel='>= 13',
                          Class='"Bows" "Quivers" "Two Hand" "Staves" "Shields" "Wands"', SetFontSize=26)
    hide_some_body_rares = hide_big_rares.copy_modify(
        ItemLevel='>= 23', Class='"Body Armour"',
        BaseType=' '.join([BASE_TYPE_BODY_EVA, BASE_TYPE_BODY_ES, BASE_TYPE_BODY_EE]))
    filter_manager.extend_blocks([hide_big_rares, hide_some_body_rares])
    if settings.HIDE_BELOW_T1_RARE_CLASS != '':
        hide_rares = hide_big_rares.copy_modify(Class=settings.HIDE_BELOW_T1_RARE_CLASS, ItemLevel=None)
        filter_manager.append_block(hide_rares)

    # Rare: 4L RRG RRR L3_MAX_IL   ALERT_RARE_ACCESSORY   提醒下跑鞋
    blocks = filter_manager.add_comment(2501, 'Leveling rares - specific items')
    if settings.LINKED_CLASS != '':
        blocks[0].modify(Class=settings.LINKED_CLASS, **STYLE_LINKS)
        rare_rrg = blocks[0].copy_modify(LinkedSockets='>= 3', SocketGroup='RRG',
                                         ItemLevel='<= ' + str(settings.L3_MAX_IL))
        rare_rrr = rare_rrg.copy_modify(SocketGroup='RRR')
        filter_manager.extend_blocks([blocks[0], rare_rrg, rare_rrr])
    if settings.SHOW_RARE_ACCESSORY == '':
        blocks[1].PlayAlertSound = None
    blocks[2].PlayAlertSound = SOUND_LEVELING
    blocks[3].modify(Height=None, Class='"Boots" "Helmets" "Gloves"')
    filter_manager.extend_blocks(blocks[1:-1])

    blocks = filter_manager.add_comment(2502, 'Leveling rares - Progression')
    filter_manager.extend_blocks(blocks)

    blocks = filter_manager.add_comment(2503, 'Leveling rares - remaining rules')
    filter_manager.extend_blocks(blocks)

    filter_manager.add_comment(2600, 'Leveling - Useful items', ignored=True)

    # RR**
    blocks = filter_manager.add_comment(2601, 'Linked gear - 4links')
    if settings.LINKED_CLASS != '':
        for block in blocks:
            block.modify(Class=settings.LINKED_CLASS, SocketGroup='RR', **STYLE_LINKS)
            filter_manager.append_block(block)

    filter_manager.add_comment(2602, 'Linked gear - Caster Weapon Configuration', ignored=True)

    # RR RG RRG RRR L2_MAX_IL L3_MAX_IL
    blocks = filter_manager.add_comment(2603, 'Linked gear - 3links')
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

    filter_manager.add_comment(2604, 'Extra Highlight: Boots', ignored=True)

    filter_manager.add_comment(2605, 'Optional Recipes', ignored=True)

    # 注意，后续(13+)需要高亮的蓝白装已经在 [02xx] 里面了
    blocks = filter_manager.add_comment(BLOCK_ACT_1, 'Act 1')
    blocks[0].BaseType = '"Rustic Sash" "Amulet"' if settings.TENCENT else '"Iron Ring" "Rustic Sash" "Amulet"'
    blocks[1].BaseType = '"Iron Ring" "Rustic Sash" "Amulet"'
    filter_manager.extend_blocks(blocks[:2])

    filter_manager.add_comment(2607, 'Act 2+3', ignored=True)

    filter_manager.add_comment(2608, 'Act 4+5+6', ignored=True)

    filter_manager.add_comment(2609, 'Jewellery - Regular Highlight', ignored=True)

    filter_manager.add_comment(2610, 'Quivers - Progression', ignored=True)

    filter_manager.add_comment(2611, 'Magic Gear', ignored=True)

    filter_manager.add_comment(2612, '20% quality items for those strange people who want them', ignored=True)

    filter_manager.add_comment(2700, 'Levelling - normal and magic item progression', ignored=True)

    # 蓝白武器  HIDE_NORMAL_MAGIC_CLASS
    filter_manager.add_comment(2701, 'Progression - Part 1 1-30', ignored=True)
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
    hide_m_2.modify(Class=' '.join([CLASS_WEAPON, '"Flasks"', CLASS_ACCESSORY]), Rarity=RARITY_MAGIC,
                    ItemLevel='>= {}'.format(2 if settings.TENCENT else 6))
    hide_m_5 = hide_m_2.copy_modify(Class='"Helmets" "Gloves" "Boots" "Body Armour"',
                                    ItemLevel='>= {}'.format(5 if settings.TENCENT else 6))
    hide_n_2 = hide_m_2.copy_modify(Rarity=None, ItemLevel='>= 2', SetFontSize=FONT_SIZE_MIN)
    filter_manager.extend_blocks([hide_m_2, hide_m_5, hide_n_2])

    filter_manager.add_comment(2702, 'Progression - Part 2 30-40', ignored=True)

    filter_manager.add_comment(2703, 'Progression - Part 4 40-65', ignored=True)

    blocks = filter_manager.add_comment(2704, 'Normal items - First 4 levels - exceptions')
    filter_manager.extend_blocks(blocks)

    blocks = filter_manager.add_comment(2705, 'Magic items - general highlight')
    filter_manager.extend_blocks(blocks)


def modify_filter(filter_manager):
    # [[0100 - 0400]]
    modify_endgame_mix(filter_manager)

    blocks = filter_manager.add_comment(500, 'HIDE LAYER 1 - MAGIC AND NORMAL ITEMS')
    blocks[0].status = DEBUG
    filter_manager.extend_blocks(blocks)

    # CURRENCY_ALERT_XXX
    # CURRENCY_XXX_FONT_SIZE
    blocks = filter_manager.add_comment(600, 'Currency - PART 1 - Common currency')
    blocks[0].BaseType = '"Orb of Alteration" "Chromatic Orb" "Jeweller\'s Orb" '
    if settings.CURRENCY_ALERT_TRANSMUTATION:
        blocks[0].BaseType += ' "Orb of Transmutation" '
    if settings.CURRENCY_ALERT_BLACKSMITH:
        blocks[0].BaseType += ' "Blacksmith\'s Whetstone"'
    if settings.CURRENCY_ALERT_AUGMENTATION:
        blocks[0].BaseType += ' "Orb of Augmentation" '
    if not settings.CURRENCY_ALERT_CHANCE:
        blocks[0].BaseType += ' "Orb of Chance" '
    if settings.ALERT_LOW_CURRENCY:
        blocks[0].PlayAlertSound = SOUND_LOW_VALUE
    blocks[1].BaseType += ' "Orb of Augmentation"'
    blocks[2].SetFontSize = settings.CURRENCY_PORTAL_FONT_SIZE
    blocks[3].BaseType = blocks[3].BaseType.replace('"Transmutation Shard"', '')
    blocks[3].SetFontSize = settings.CURRENCY_ARMOURER_SCRAP_FONT_SIZE
    blocks[4].SetFontSize = settings.CURRENCY_WISDOM_FONT_SIZE
    filter_manager.extend_blocks(blocks)

    filter_manager.add_comment(700, 'OVERRIDE AREA 2 - Override the default rare rulesets here', ignored=True)

    # [[0800]]
    modify_endgame_rare(filter_manager)

    blocks = filter_manager.add_comment(BLOCK_HIDE_RARES_65, 'HIDE LAYER 2 - RARE ITEMS (65+)')
    for block in blocks:
        block.status = DEBUG
    filter_manager.extend_blocks(blocks)

    # [[1000]]-[[1400]]
    modify_gem_flask_map(filter_manager)

    filter_manager.add_comment(1500, 'Currency - PART 2 - Rare currency', ignored=True)

    # 8
    blocks = filter_manager.add_comment(1502, 'Top Currency')
    blocks[0].BaseType += ' "Master Cartographer\'s Sextant" "Orb of Annulment" "Stacked Deck" '
    blocks[0].PlayAlertSound = SOUND_TOP_VALUE
    filter_manager.extend_blocks(blocks)

    # CURRENCY_ALERT_CHANCE
    blocks = filter_manager.add_comment(1501, 'Regular Rare Currency')
    if settings.TENCENT:
        blocks[1].BaseType = blocks[1].BaseType.replace('"Orb of Regret"', '')
    if settings.CURRENCY_ALERT_CHANCE:
        blocks[1].BaseType += ' "Orb of Chance"'
    blocks[0].BaseType += ' ' + blocks[1].BaseType
    blocks[0].PlayAlertSound = SOUND_MID_VALUE
    blocks[1].PlayAlertSound = SOUND_MID_VALUE
    if settings.TENCENT:
        blocks[2].BaseType += ' "Orb of Regret"'
    blocks[2].BaseType += ' "Glassblower\'s Bauble"'
    blocks[2].PlayAlertSound = SOUND_MID_VALUE
    blocks.insert(3, blocks[2].copy_modify(BaseType='"Silver Coin"', SetBackgroundColor='190 178 135'))  # Pavlova
    blocks[-2].BaseType += ' "Horizon Shard"'
    blocks[-2].PlayAlertSound = SOUND_MID_VALUE
    filter_manager.extend_blocks(blocks)

    # ALERT_ESSENCE_BASE_TYPE, 8, 1
    blocks = filter_manager.add_comment(1503, 'Essence Tier List')
    blocks[0].PlayAlertSound = SOUND_TOP_VALUE
    blocks[0].BaseType += settings.ALERT_ESSENCE_BASE_TYPE
    blocks[1].PlayAlertSound = SOUND_MID_VALUE
    filter_manager.extend_blocks(blocks)

    # alert "Splinter of Chayula"
    blocks = filter_manager.add_comment(1504, 'Special items')
    blocks[0].PlayAlertSound = SOUND_TOP_VALUE
    blocks[1].PlayAlertSound = SOUND_MID_VALUE
    blocks[2].modify(PlayAlertSound=SOUND_TOP_VALUE, **STYLE_TOP)
    blocks[3].PlayAlertSound = None
    blocks[-1].modify(SetFontSize=FONT_SIZE_MAX, PlayAlertSound=SOUND_TOP_VALUE)
    filter_manager.extend_blocks(blocks)

    filter_manager.add_comment(1600, 'Currency - PART 3 - Divination cards', ignored=True)

    blocks = filter_manager.add_comment(1601, 'Exceptions to prevent ident. mistakes')
    blocks[0].SetFontSize = FONT_SIZE_MAX  # T4
    filter_manager.extend_blocks(blocks)

    # 8
    blocks = filter_manager.add_comment(1602, 'T1 - Top tier cards', ignored=settings.TEMP)
    if blocks:
        blocks[0].PlayAlertSound = SOUND_TOP_VALUE
        filter_manager.extend_blocks(blocks)

    # 8
    blocks = filter_manager.add_comment(1603, 'T2 - Great cards', ignored=settings.TEMP)
    if blocks:
        blocks[0].PlayAlertSound = SOUND_TOP_VALUE
        blocks[0].BaseType += ' "The Encroaching Darkness" "The Throne" '
        filter_manager.extend_blocks(blocks)

    # 1
    blocks = filter_manager.add_comment(1604, 'T3 - Decent cards', ignored=settings.TEMP)
    if blocks:
        blocks[0].modify(SetFontSize=FONT_SIZE_MAX, PlayAlertSound=SOUND_MID_VALUE)
        filter_manager.extend_blocks(blocks)

    # 2
    blocks = filter_manager.add_comment(1605, 'T5 - Format trash tier cards... before', ignored=settings.TEMP)
    if blocks:
        hide_cards = blocks[0].copy_modify(status=DEBUG, BaseType='"Carrion Crow" '  # Shit
                                                                  '"King\'s Blade" '  # (110-134)% 物理 永恒之剑
                                                                  '"Prosperity" '  # T1 稀有度 金光戒指
                                                                  '"Struck by Lightning" '  # 点电伤 宝石
                                                                  '"The Inoculated " '  # T1 混合 ES% 护甲
                                                                  '"The Rabid Rhoa" '  # 混沌伤 双子战爪
                                                                  '"The Sigil" '  # T1 ES% 项链
                                                                  '"The Surgeon" '  # 暴击充能 药剂
                                                                  '"The Twins"',  # T1 攻速 双子战爪
                                           SetFontSize=FONT_SIZE_MIN)
        filter_manager.append_block(hide_cards)
        blocks[0].modify(SetFontSize=40, PlayAlertSound=SOUND_LOW_VALUE)
        filter_manager.extend_blocks(blocks)

    blocks = filter_manager.add_comment(1606, 'T4 - ...showing the remaining cards')
    blocks[0].SetFontSize = FONT_SIZE_MAX
    filter_manager.extend_blocks(blocks)

    # CATCHALL
    blocks = filter_manager.add_comment(1700, 'Currency - PART 4 - remaining items')
    blocks[0].BaseType += ' "Transmutation Shard" '
    blocks[0].SetFontSize = FONT_SIZE_MIN
    blocks[1].modify(PlayAlertSound=SOUND_TOP_VALUE, **STYLE_TOP)
    filter_manager.extend_blocks(blocks)

    blocks = filter_manager.add_comment(1800, 'Leaguestones - Tierlists')
    for block in blocks[:-1]:
        block.PlayAlertSound = SOUND_MID_VALUE
    filter_manager.extend_blocks(blocks)

    filter_manager.add_comment(1900, 'Uniques!', ignored=True)

    # 改成T1
    blocks = filter_manager.add_comment(1901, 'Exceptions')
    for block in blocks:
        block.PlayAlertSound = SOUND_TOP_VALUE
    blocks[0].modify(**STYLE_TOP_UNIQUE)
    filter_manager.extend_blocks(blocks)

    # 6
    blocks = filter_manager.add_comment(1902, 'Harbinger - Pieces')
    blocks[0].PlayAlertSound = SOUND_UNIQUE
    filter_manager.extend_blocks(blocks)

    # 8
    blocks = filter_manager.add_comment(1903, 'Tier 1 uniques')
    for block in blocks:
        block.PlayAlertSound = SOUND_TOP_VALUE
    blocks[0].BaseType += ' "Basket Rapier" "Twilight Blade"'
    filter_manager.extend_blocks(blocks)

    # 改成T1
    blocks = filter_manager.add_comment(1904, 'Tier 2 uniques')
    for block in blocks:
        block.modify(PlayAlertSound=SOUND_TOP_VALUE, **STYLE_TOP_UNIQUE)
    filter_manager.extend_blocks(blocks)

    # 6
    blocks = filter_manager.add_comment(1905, 'Multi-Unique bases')
    blocks[0].modify(SetFontSize=FONT_SIZE_MAX, PlayAlertSound=SOUND_UNIQUE)
    filter_manager.extend_blocks(blocks)

    # 6
    blocks = filter_manager.add_comment(1906, 'Prophecy-Material Uniques')
    blocks[0].modify(SetFontSize=FONT_SIZE_MAX, PlayAlertSound=SOUND_UNIQUE)
    filter_manager.extend_blocks(blocks)

    # 6
    blocks = filter_manager.add_comment(1907, 'Random Uniques')
    blocks[0].modify(SetFontSize=FONT_SIZE_MAX, PlayAlertSound=SOUND_UNIQUE)
    filter_manager.extend_blocks(blocks)

    blocks = filter_manager.add_comment(2000, 'Quest Items and Shaper Orbs')
    filter_manager.extend_blocks(blocks)

    # [[2100]]-[[2700]]
    modify_leveling(filter_manager)

    blocks = filter_manager.add_comment(BLOCK_HIDE_REMAINING, 'HIDE LAYER 5 - Remaining Items')
    blocks[0].modify(status=DEBUG, SetFontSize=FONT_SIZE_MIN)
    filter_manager.extend_blocks(blocks)

    # 8
    blocks = filter_manager.add_comment(2900, 'CATCHALL')
    blocks[0].PlayAlertSound = SOUND_TOP_VALUE
    filter_manager.extend_blocks(blocks)


def main():
    filter_name = 'res' + os.sep + 'NeverSink\'s filter - 1-REGULAR.filter'
    with open(filter_name) as f:
        fm = FilterManager(f.readlines())

    modify_filter(fm)

    out_file_path = 'out' + os.sep + 'MODIFY.filter'
    with open(out_file_path, 'w') as f:
        f.writelines(fm.new_text)
    if platform.system() == 'Windows':
        shutil.copyfile(out_file_path, os.path.expanduser('~') + "\Documents\My Games\Path of Exile\MODIFY.filter")


if __name__ == '__main__':
    start_time = time.time()
    main()
    print("Modify success, time cost: {:.0f}ms".format(1000 * (time.time() - start_time)))
