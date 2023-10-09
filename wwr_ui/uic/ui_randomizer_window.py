# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'randomizer_window.ui'
##
## Created by: Qt User Interface Compiler version 6.5.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QAbstractItemView, QAbstractSpinBox, QApplication, QCheckBox,
    QComboBox, QFrame, QGridLayout, QGroupBox,
    QHBoxLayout, QLabel, QLineEdit, QListView,
    QMainWindow, QPushButton, QScrollArea, QSizePolicy,
    QSpacerItem, QSpinBox, QTabWidget, QVBoxLayout,
    QWidget)

from wwr_ui.cosmetic_tab import CosmeticTab

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(905, 722)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.verticalLayout = QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.layoutS_for_0_primary = QScrollArea(self.centralwidget)
        self.layoutS_for_0_primary.setObjectName(u"layoutS_for_0_primary")
        self.layoutS_for_0_primary.setMinimumSize(QSize(600, 400))
        self.layoutS_for_0_primary.setFrameShape(QFrame.NoFrame)
        self.layoutS_for_0_primary.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOn)
        self.layoutS_for_0_primary.setWidgetResizable(True)
        self.scrollA_for_primary = QWidget()
        self.scrollA_for_primary.setObjectName(u"scrollA_for_primary")
        self.scrollA_for_primary.setGeometry(QRect(0, 0, 870, 608))
        self.verticalLayout_2 = QVBoxLayout(self.scrollA_for_primary)
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.tabs_for_primary = QTabWidget(self.scrollA_for_primary)
        self.tabs_for_primary.setObjectName(u"tabs_for_primary")
        self.tabs_for_primary.setEnabled(True)
        self.tab_randomizer_settings = QWidget()
        self.tab_randomizer_settings.setObjectName(u"tab_randomizer_settings")
        self.verticalLayout_3 = QVBoxLayout(self.tab_randomizer_settings)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.layoutG_for_0_paths = QGridLayout()
        self.layoutG_for_0_paths.setObjectName(u"layoutG_for_0_paths")
        self.seed = QLineEdit(self.tab_randomizer_settings)
        self.seed.setObjectName(u"seed")

        self.layoutG_for_0_paths.addWidget(self.seed, 2, 1, 1, 1)

        self.label_for_clean_iso_path = QLabel(self.tab_randomizer_settings)
        self.label_for_clean_iso_path.setObjectName(u"label_for_clean_iso_path")
        self.label_for_clean_iso_path.setTextFormat(Qt.MarkdownText)

        self.layoutG_for_0_paths.addWidget(self.label_for_clean_iso_path, 0, 0, 1, 1)

        self.clean_iso_path = QLineEdit(self.tab_randomizer_settings)
        self.clean_iso_path.setObjectName(u"clean_iso_path")

        self.layoutG_for_0_paths.addWidget(self.clean_iso_path, 0, 1, 1, 1)

        self.label_for_output_folder = QLabel(self.tab_randomizer_settings)
        self.label_for_output_folder.setObjectName(u"label_for_output_folder")

        self.layoutG_for_0_paths.addWidget(self.label_for_output_folder, 1, 0, 1, 1)

        self.output_folder = QLineEdit(self.tab_randomizer_settings)
        self.output_folder.setObjectName(u"output_folder")

        self.layoutG_for_0_paths.addWidget(self.output_folder, 1, 1, 1, 1)

        self.output_folder_browse_button = QPushButton(self.tab_randomizer_settings)
        self.output_folder_browse_button.setObjectName(u"output_folder_browse_button")

        self.layoutG_for_0_paths.addWidget(self.output_folder_browse_button, 1, 2, 1, 1)

        self.label_for_seed = QLabel(self.tab_randomizer_settings)
        self.label_for_seed.setObjectName(u"label_for_seed")

        self.layoutG_for_0_paths.addWidget(self.label_for_seed, 2, 0, 1, 1)

        self.generate_seed_button = QPushButton(self.tab_randomizer_settings)
        self.generate_seed_button.setObjectName(u"generate_seed_button")

        self.layoutG_for_0_paths.addWidget(self.generate_seed_button, 2, 2, 1, 1)

        self.clean_iso_path_browse_button = QPushButton(self.tab_randomizer_settings)
        self.clean_iso_path_browse_button.setObjectName(u"clean_iso_path_browse_button")

        self.layoutG_for_0_paths.addWidget(self.clean_iso_path_browse_button, 0, 2, 1, 1)


        self.verticalLayout_3.addLayout(self.layoutG_for_0_paths)

        self.progression_locations_groupbox = QGroupBox(self.tab_randomizer_settings)
        self.progression_locations_groupbox.setObjectName(u"progression_locations_groupbox")
        self.gridLayout_2 = QGridLayout(self.progression_locations_groupbox)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.progression_dungeons = QCheckBox(self.progression_locations_groupbox)
        self.progression_dungeons.setObjectName(u"progression_dungeons")
        self.progression_dungeons.setChecked(True)

        self.gridLayout_2.addWidget(self.progression_dungeons, 0, 0, 1, 1)

        self.progression_tingle_chests = QCheckBox(self.progression_locations_groupbox)
        self.progression_tingle_chests.setObjectName(u"progression_tingle_chests")

        self.gridLayout_2.addWidget(self.progression_tingle_chests, 0, 1, 1, 1)

        self.progression_long_sidequests = QCheckBox(self.progression_locations_groupbox)
        self.progression_long_sidequests.setObjectName(u"progression_long_sidequests")

        self.gridLayout_2.addWidget(self.progression_long_sidequests, 4, 1, 1, 1)

        self.progression_spoils_trading = QCheckBox(self.progression_locations_groupbox)
        self.progression_spoils_trading.setObjectName(u"progression_spoils_trading")

        self.gridLayout_2.addWidget(self.progression_spoils_trading, 4, 2, 1, 1)

        self.progression_short_sidequests = QCheckBox(self.progression_locations_groupbox)
        self.progression_short_sidequests.setObjectName(u"progression_short_sidequests")

        self.gridLayout_2.addWidget(self.progression_short_sidequests, 4, 0, 1, 1)

        self.progression_puzzle_secret_caves = QCheckBox(self.progression_locations_groupbox)
        self.progression_puzzle_secret_caves.setObjectName(u"progression_puzzle_secret_caves")
        self.progression_puzzle_secret_caves.setChecked(True)

        self.gridLayout_2.addWidget(self.progression_puzzle_secret_caves, 1, 0, 1, 1)

        self.progression_savage_labyrinth = QCheckBox(self.progression_locations_groupbox)
        self.progression_savage_labyrinth.setObjectName(u"progression_savage_labyrinth")

        self.gridLayout_2.addWidget(self.progression_savage_labyrinth, 1, 2, 1, 1)

        self.progression_combat_secret_caves = QCheckBox(self.progression_locations_groupbox)
        self.progression_combat_secret_caves.setObjectName(u"progression_combat_secret_caves")

        self.gridLayout_2.addWidget(self.progression_combat_secret_caves, 1, 1, 1, 1)

        self.progression_dungeon_secrets = QCheckBox(self.progression_locations_groupbox)
        self.progression_dungeon_secrets.setObjectName(u"progression_dungeon_secrets")

        self.gridLayout_2.addWidget(self.progression_dungeon_secrets, 0, 2, 1, 1)

        self.progression_battlesquid = QCheckBox(self.progression_locations_groupbox)
        self.progression_battlesquid.setObjectName(u"progression_battlesquid")

        self.gridLayout_2.addWidget(self.progression_battlesquid, 2, 3, 1, 1)

        self.progression_mail = QCheckBox(self.progression_locations_groupbox)
        self.progression_mail.setObjectName(u"progression_mail")

        self.gridLayout_2.addWidget(self.progression_mail, 2, 1, 1, 1)

        self.progression_great_fairies = QCheckBox(self.progression_locations_groupbox)
        self.progression_great_fairies.setObjectName(u"progression_great_fairies")
        self.progression_great_fairies.setChecked(True)

        self.gridLayout_2.addWidget(self.progression_great_fairies, 1, 3, 1, 1)

        self.z_layoutH_for_z_bottom = QHBoxLayout()
        self.z_layoutH_for_z_bottom.setObjectName(u"z_layoutH_for_z_bottom")
        self.progression_misc = QCheckBox(self.progression_locations_groupbox)
        self.progression_misc.setObjectName(u"progression_misc")
        self.progression_misc.setChecked(True)

        self.z_layoutH_for_z_bottom.addWidget(self.progression_misc)

        self.progression_treasure_charts = QCheckBox(self.progression_locations_groupbox)
        self.progression_treasure_charts.setObjectName(u"progression_treasure_charts")

        self.z_layoutH_for_z_bottom.addWidget(self.progression_treasure_charts)

        self.progression_triforce_charts = QCheckBox(self.progression_locations_groupbox)
        self.progression_triforce_charts.setObjectName(u"progression_triforce_charts")

        self.z_layoutH_for_z_bottom.addWidget(self.progression_triforce_charts)


        self.gridLayout_2.addLayout(self.z_layoutH_for_z_bottom, 7, 0, 1, 4)

        self.progression_expensive_purchases = QCheckBox(self.progression_locations_groupbox)
        self.progression_expensive_purchases.setObjectName(u"progression_expensive_purchases")
        self.progression_expensive_purchases.setChecked(True)

        self.gridLayout_2.addWidget(self.progression_expensive_purchases, 4, 3, 1, 1)

        self.progression_minigames = QCheckBox(self.progression_locations_groupbox)
        self.progression_minigames.setObjectName(u"progression_minigames")

        self.gridLayout_2.addWidget(self.progression_minigames, 2, 2, 1, 1)

        self.progression_submarines = QCheckBox(self.progression_locations_groupbox)
        self.progression_submarines.setObjectName(u"progression_submarines")
        self.progression_submarines.setChecked(False)

        self.gridLayout_2.addWidget(self.progression_submarines, 5, 0, 1, 1)

        self.progression_big_octos_gunboats = QCheckBox(self.progression_locations_groupbox)
        self.progression_big_octos_gunboats.setObjectName(u"progression_big_octos_gunboats")

        self.gridLayout_2.addWidget(self.progression_big_octos_gunboats, 5, 1, 1, 1)

        self.progression_platforms_rafts = QCheckBox(self.progression_locations_groupbox)
        self.progression_platforms_rafts.setObjectName(u"progression_platforms_rafts")

        self.gridLayout_2.addWidget(self.progression_platforms_rafts, 5, 2, 1, 1)

        self.progression_free_gifts = QCheckBox(self.progression_locations_groupbox)
        self.progression_free_gifts.setObjectName(u"progression_free_gifts")
        self.progression_free_gifts.setChecked(True)

        self.gridLayout_2.addWidget(self.progression_free_gifts, 0, 3, 1, 1)

        self.progression_island_puzzles = QCheckBox(self.progression_locations_groupbox)
        self.progression_island_puzzles.setObjectName(u"progression_island_puzzles")

        self.gridLayout_2.addWidget(self.progression_island_puzzles, 2, 0, 1, 1)

        self.progression_eye_reef_chests = QCheckBox(self.progression_locations_groupbox)
        self.progression_eye_reef_chests.setObjectName(u"progression_eye_reef_chests")

        self.gridLayout_2.addWidget(self.progression_eye_reef_chests, 5, 3, 1, 1)


        self.verticalLayout_3.addWidget(self.progression_locations_groupbox)

        self.layoutG_for_2_item_randomizers = QGroupBox(self.tab_randomizer_settings)
        self.layoutG_for_2_item_randomizers.setObjectName(u"layoutG_for_2_item_randomizers")
        self.gridLayout_3 = QGridLayout(self.layoutG_for_2_item_randomizers)
        self.gridLayout_3.setObjectName(u"gridLayout_3")
        self.layoutH_for_0_sword_mode = QHBoxLayout()
        self.layoutH_for_0_sword_mode.setObjectName(u"layoutH_for_0_sword_mode")
        self.label_for_sword_mode = QLabel(self.layoutG_for_2_item_randomizers)
        self.label_for_sword_mode.setObjectName(u"label_for_sword_mode")

        self.layoutH_for_0_sword_mode.addWidget(self.label_for_sword_mode)

        self.sword_mode = QComboBox(self.layoutG_for_2_item_randomizers)
        self.sword_mode.addItem("")
        self.sword_mode.addItem("")
        self.sword_mode.addItem("")
        self.sword_mode.setObjectName(u"sword_mode")
        sizePolicy = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(1)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.sword_mode.sizePolicy().hasHeightForWidth())
        self.sword_mode.setSizePolicy(sizePolicy)

        self.layoutH_for_0_sword_mode.addWidget(self.sword_mode)


        self.gridLayout_3.addLayout(self.layoutH_for_0_sword_mode, 0, 0, 1, 1)

        self.layoutH_for_1_triforce_shards = QHBoxLayout()
        self.layoutH_for_1_triforce_shards.setObjectName(u"layoutH_for_1_triforce_shards")
        self.label_for_num_starting_triforce_shards = QLabel(self.layoutG_for_2_item_randomizers)
        self.label_for_num_starting_triforce_shards.setObjectName(u"label_for_num_starting_triforce_shards")
        sizePolicy1 = QSizePolicy(QSizePolicy.Maximum, QSizePolicy.Preferred)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.label_for_num_starting_triforce_shards.sizePolicy().hasHeightForWidth())
        self.label_for_num_starting_triforce_shards.setSizePolicy(sizePolicy1)

        self.layoutH_for_1_triforce_shards.addWidget(self.label_for_num_starting_triforce_shards)

        self.num_starting_triforce_shards = QComboBox(self.layoutG_for_2_item_randomizers)
        self.num_starting_triforce_shards.addItem("")
        self.num_starting_triforce_shards.addItem("")
        self.num_starting_triforce_shards.addItem("")
        self.num_starting_triforce_shards.addItem("")
        self.num_starting_triforce_shards.addItem("")
        self.num_starting_triforce_shards.addItem("")
        self.num_starting_triforce_shards.addItem("")
        self.num_starting_triforce_shards.addItem("")
        self.num_starting_triforce_shards.addItem("")
        self.num_starting_triforce_shards.setObjectName(u"num_starting_triforce_shards")
        sizePolicy.setHeightForWidth(self.num_starting_triforce_shards.sizePolicy().hasHeightForWidth())
        self.num_starting_triforce_shards.setSizePolicy(sizePolicy)
        self.num_starting_triforce_shards.setMinimumSize(QSize(30, 0))
        self.num_starting_triforce_shards.setMaximumSize(QSize(40, 16777215))

        self.layoutH_for_1_triforce_shards.addWidget(self.num_starting_triforce_shards)

        self.widget = QWidget(self.layoutG_for_2_item_randomizers)
        self.widget.setObjectName(u"widget")

        self.layoutH_for_1_triforce_shards.addWidget(self.widget)


        self.gridLayout_3.addLayout(self.layoutH_for_1_triforce_shards, 0, 1, 1, 1)

        self.chest_type_matches_contents = QCheckBox(self.layoutG_for_2_item_randomizers)
        self.chest_type_matches_contents.setObjectName(u"chest_type_matches_contents")

        self.gridLayout_3.addWidget(self.chest_type_matches_contents, 0, 3, 1, 1)

        self.keylunacy = QCheckBox(self.layoutG_for_2_item_randomizers)
        self.keylunacy.setObjectName(u"keylunacy")

        self.gridLayout_3.addWidget(self.keylunacy, 0, 2, 1, 1)


        self.verticalLayout_3.addWidget(self.layoutG_for_2_item_randomizers)

        self.layoutH_for_3_randomizers = QHBoxLayout()
        self.layoutH_for_3_randomizers.setObjectName(u"layoutH_for_3_randomizers")
        self.layoutG_for_0_entrance = QGroupBox(self.tab_randomizer_settings)
        self.layoutG_for_0_entrance.setObjectName(u"layoutG_for_0_entrance")
        self.gridLayout_9 = QGridLayout(self.layoutG_for_0_entrance)
        self.gridLayout_9.setObjectName(u"gridLayout_9")
        self.randomize_boss_entrances = QCheckBox(self.layoutG_for_0_entrance)
        self.randomize_boss_entrances.setObjectName(u"randomize_boss_entrances")

        self.gridLayout_9.addWidget(self.randomize_boss_entrances, 0, 1, 1, 1)

        self.randomize_fairy_fountain_entrances = QCheckBox(self.layoutG_for_0_entrance)
        self.randomize_fairy_fountain_entrances.setObjectName(u"randomize_fairy_fountain_entrances")

        self.gridLayout_9.addWidget(self.randomize_fairy_fountain_entrances, 1, 2, 1, 1)

        self.randomize_secret_cave_inner_entrances = QCheckBox(self.layoutG_for_0_entrance)
        self.randomize_secret_cave_inner_entrances.setObjectName(u"randomize_secret_cave_inner_entrances")

        self.gridLayout_9.addWidget(self.randomize_secret_cave_inner_entrances, 1, 1, 1, 1)

        self.randomize_secret_cave_entrances = QCheckBox(self.layoutG_for_0_entrance)
        self.randomize_secret_cave_entrances.setObjectName(u"randomize_secret_cave_entrances")

        self.gridLayout_9.addWidget(self.randomize_secret_cave_entrances, 1, 0, 1, 1)

        self.randomize_dungeon_entrances = QCheckBox(self.layoutG_for_0_entrance)
        self.randomize_dungeon_entrances.setObjectName(u"randomize_dungeon_entrances")

        self.gridLayout_9.addWidget(self.randomize_dungeon_entrances, 0, 0, 1, 1)

        self.randomize_miniboss_entrances = QCheckBox(self.layoutG_for_0_entrance)
        self.randomize_miniboss_entrances.setObjectName(u"randomize_miniboss_entrances")

        self.gridLayout_9.addWidget(self.randomize_miniboss_entrances, 0, 2, 1, 1)

        self.layoutH_for_0_mix = QHBoxLayout()
        self.layoutH_for_0_mix.setObjectName(u"layoutH_for_0_mix")
        self.label_for_mix_entrances = QLabel(self.layoutG_for_0_entrance)
        self.label_for_mix_entrances.setObjectName(u"label_for_mix_entrances")

        self.layoutH_for_0_mix.addWidget(self.label_for_mix_entrances)

        self.mix_entrances = QComboBox(self.layoutG_for_0_entrance)
        self.mix_entrances.addItem("")
        self.mix_entrances.addItem("")
        self.mix_entrances.setObjectName(u"mix_entrances")
        sizePolicy.setHeightForWidth(self.mix_entrances.sizePolicy().hasHeightForWidth())
        self.mix_entrances.setSizePolicy(sizePolicy)

        self.layoutH_for_0_mix.addWidget(self.mix_entrances)


        self.gridLayout_9.addLayout(self.layoutH_for_0_mix, 2, 0, 1, 3)


        self.layoutH_for_3_randomizers.addWidget(self.layoutG_for_0_entrance)

        self.layoutG_for_1_other = QGroupBox(self.tab_randomizer_settings)
        self.layoutG_for_1_other.setObjectName(u"layoutG_for_1_other")
        self.gridLayout_10 = QGridLayout(self.layoutG_for_1_other)
        self.gridLayout_10.setObjectName(u"gridLayout_10")
        self.randomize_enemies = QCheckBox(self.layoutG_for_1_other)
        self.randomize_enemies.setObjectName(u"randomize_enemies")

        self.gridLayout_10.addWidget(self.randomize_enemies, 1, 1, 1, 1)

        self.randomize_charts = QCheckBox(self.layoutG_for_1_other)
        self.randomize_charts.setObjectName(u"randomize_charts")

        self.gridLayout_10.addWidget(self.randomize_charts, 0, 1, 1, 1)

        self.randomize_enemy_palettes = QCheckBox(self.layoutG_for_1_other)
        self.randomize_enemy_palettes.setObjectName(u"randomize_enemy_palettes")

        self.gridLayout_10.addWidget(self.randomize_enemy_palettes, 1, 0, 1, 1)

        self.randomize_starting_island = QCheckBox(self.layoutG_for_1_other)
        self.randomize_starting_island.setObjectName(u"randomize_starting_island")

        self.gridLayout_10.addWidget(self.randomize_starting_island, 0, 0, 1, 1)

        self.widget_2 = QWidget(self.layoutG_for_1_other)
        self.widget_2.setObjectName(u"widget_2")

        self.gridLayout_10.addWidget(self.widget_2, 2, 0, 1, 1)


        self.layoutH_for_3_randomizers.addWidget(self.layoutG_for_1_other)


        self.verticalLayout_3.addLayout(self.layoutH_for_3_randomizers)

        self.layoutG_for_4_convenience = QGroupBox(self.tab_randomizer_settings)
        self.layoutG_for_4_convenience.setObjectName(u"layoutG_for_4_convenience")
        self.gridLayout_4 = QGridLayout(self.layoutG_for_4_convenience)
        self.gridLayout_4.setObjectName(u"gridLayout_4")
        self.invert_sea_compass_x_axis = QCheckBox(self.layoutG_for_4_convenience)
        self.invert_sea_compass_x_axis.setObjectName(u"invert_sea_compass_x_axis")

        self.gridLayout_4.addWidget(self.invert_sea_compass_x_axis, 0, 4, 1, 1)

        self.invert_camera_x_axis = QCheckBox(self.layoutG_for_4_convenience)
        self.invert_camera_x_axis.setObjectName(u"invert_camera_x_axis")

        self.gridLayout_4.addWidget(self.invert_camera_x_axis, 1, 4, 1, 1)

        self.instant_text_boxes = QCheckBox(self.layoutG_for_4_convenience)
        self.instant_text_boxes.setObjectName(u"instant_text_boxes")
        self.instant_text_boxes.setChecked(True)

        self.gridLayout_4.addWidget(self.instant_text_boxes, 0, 1, 1, 1)

        self.reveal_full_sea_chart = QCheckBox(self.layoutG_for_4_convenience)
        self.reveal_full_sea_chart.setObjectName(u"reveal_full_sea_chart")
        self.reveal_full_sea_chart.setChecked(True)

        self.gridLayout_4.addWidget(self.reveal_full_sea_chart, 0, 3, 1, 1)

        self.swift_sail = QCheckBox(self.layoutG_for_4_convenience)
        self.swift_sail.setObjectName(u"swift_sail")
        self.swift_sail.setChecked(True)

        self.gridLayout_4.addWidget(self.swift_sail, 0, 0, 1, 1)

        self.remove_title_and_ending_videos = QCheckBox(self.layoutG_for_4_convenience)
        self.remove_title_and_ending_videos.setObjectName(u"remove_title_and_ending_videos")
        self.remove_title_and_ending_videos.setChecked(True)

        self.gridLayout_4.addWidget(self.remove_title_and_ending_videos, 1, 3, 1, 1)

        self.skip_rematch_bosses = QCheckBox(self.layoutG_for_4_convenience)
        self.skip_rematch_bosses.setObjectName(u"skip_rematch_bosses")
        self.skip_rematch_bosses.setChecked(True)

        self.gridLayout_4.addWidget(self.skip_rematch_bosses, 1, 0, 1, 1)

        self.remove_music = QCheckBox(self.layoutG_for_4_convenience)
        self.remove_music.setObjectName(u"remove_music")

        self.gridLayout_4.addWidget(self.remove_music, 0, 2, 1, 1)

        self.add_shortcut_warps_between_dungeons = QCheckBox(self.layoutG_for_4_convenience)
        self.add_shortcut_warps_between_dungeons.setObjectName(u"add_shortcut_warps_between_dungeons")

        self.gridLayout_4.addWidget(self.add_shortcut_warps_between_dungeons, 1, 1, 1, 2)


        self.verticalLayout_3.addWidget(self.layoutG_for_4_convenience)

        self.zzzz_spacerV_for_randomizer_settings = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_3.addItem(self.zzzz_spacerV_for_randomizer_settings)

        self.tabs_for_primary.addTab(self.tab_randomizer_settings, "")
        self.tab_starting_items = QWidget()
        self.tab_starting_items.setObjectName(u"tab_starting_items")
        self.tab_starting_items.setEnabled(True)
        self.verticalLayout_4 = QVBoxLayout(self.tab_starting_items)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.layoutH_for_0_gear = QHBoxLayout()
        self.layoutH_for_0_gear.setObjectName(u"layoutH_for_0_gear")
        self.layoutV_for_0_randomized_gear = QVBoxLayout()
        self.layoutV_for_0_randomized_gear.setObjectName(u"layoutV_for_0_randomized_gear")
        self.label_for_randomized_gear = QLabel(self.tab_starting_items)
        self.label_for_randomized_gear.setObjectName(u"label_for_randomized_gear")

        self.layoutV_for_0_randomized_gear.addWidget(self.label_for_randomized_gear)

        self.randomized_gear = QListView(self.tab_starting_items)
        self.randomized_gear.setObjectName(u"randomized_gear")
        self.randomized_gear.setEditTriggers(QAbstractItemView.NoEditTriggers)
        self.randomized_gear.setSelectionMode(QAbstractItemView.ExtendedSelection)

        self.layoutV_for_0_randomized_gear.addWidget(self.randomized_gear)


        self.layoutH_for_0_gear.addLayout(self.layoutV_for_0_randomized_gear)

        self.layoutV_for_1_gear_buttons = QVBoxLayout()
        self.layoutV_for_1_gear_buttons.setObjectName(u"layoutV_for_1_gear_buttons")
        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.layoutV_for_1_gear_buttons.addItem(self.verticalSpacer)

        self.remove_gear = QPushButton(self.tab_starting_items)
        self.remove_gear.setObjectName(u"remove_gear")
        self.remove_gear.setMinimumSize(QSize(0, 80))

        self.layoutV_for_1_gear_buttons.addWidget(self.remove_gear)

        self.add_gear = QPushButton(self.tab_starting_items)
        self.add_gear.setObjectName(u"add_gear")
        self.add_gear.setMinimumSize(QSize(0, 80))

        self.layoutV_for_1_gear_buttons.addWidget(self.add_gear)

        self.verticalSpacer_2 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.layoutV_for_1_gear_buttons.addItem(self.verticalSpacer_2)


        self.layoutH_for_0_gear.addLayout(self.layoutV_for_1_gear_buttons)

        self.layoutV_for_2_starting_gear = QVBoxLayout()
        self.layoutV_for_2_starting_gear.setObjectName(u"layoutV_for_2_starting_gear")
        self.label_for_starting_gear = QLabel(self.tab_starting_items)
        self.label_for_starting_gear.setObjectName(u"label_for_starting_gear")

        self.layoutV_for_2_starting_gear.addWidget(self.label_for_starting_gear)

        self.starting_gear = QListView(self.tab_starting_items)
        self.starting_gear.setObjectName(u"starting_gear")
        self.starting_gear.setEditTriggers(QAbstractItemView.NoEditTriggers)
        self.starting_gear.setSelectionMode(QAbstractItemView.ExtendedSelection)

        self.layoutV_for_2_starting_gear.addWidget(self.starting_gear)


        self.layoutH_for_0_gear.addLayout(self.layoutV_for_2_starting_gear)


        self.verticalLayout_4.addLayout(self.layoutH_for_0_gear)

        self.layoutH_for_1_health = QHBoxLayout()
        self.layoutH_for_1_health.setObjectName(u"layoutH_for_1_health")
        self.label_for_starting_hcs = QLabel(self.tab_starting_items)
        self.label_for_starting_hcs.setObjectName(u"label_for_starting_hcs")

        self.layoutH_for_1_health.addWidget(self.label_for_starting_hcs)

        self.starting_hcs = QSpinBox(self.tab_starting_items)
        self.starting_hcs.setObjectName(u"starting_hcs")
        self.starting_hcs.setLayoutDirection(Qt.LeftToRight)
        self.starting_hcs.setMaximum(6)
        self.starting_hcs.setValue(0)
        self.starting_hcs.setDisplayIntegerBase(10)

        self.layoutH_for_1_health.addWidget(self.starting_hcs)

        self.label_for_starting_pohs = QLabel(self.tab_starting_items)
        self.label_for_starting_pohs.setObjectName(u"label_for_starting_pohs")

        self.layoutH_for_1_health.addWidget(self.label_for_starting_pohs)

        self.starting_pohs = QSpinBox(self.tab_starting_items)
        self.starting_pohs.setObjectName(u"starting_pohs")
        self.starting_pohs.setMaximum(44)
        self.starting_pohs.setValue(0)
        self.starting_pohs.setDisplayIntegerBase(10)

        self.layoutH_for_1_health.addWidget(self.starting_pohs)

        self.current_health = QLabel(self.tab_starting_items)
        self.current_health.setObjectName(u"current_health")

        self.layoutH_for_1_health.addWidget(self.current_health)

        self.zzzz_spacerH_for_health = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.layoutH_for_1_health.addItem(self.zzzz_spacerH_for_health)


        self.verticalLayout_4.addLayout(self.layoutH_for_1_health)

        self.tabs_for_primary.addTab(self.tab_starting_items, "")
        self.tab_advanced = QWidget()
        self.tab_advanced.setObjectName(u"tab_advanced")
        self.verticalLayout_8 = QVBoxLayout(self.tab_advanced)
        self.verticalLayout_8.setObjectName(u"verticalLayout_8")
        self.layoutG_for_0_bosses = QGroupBox(self.tab_advanced)
        self.layoutG_for_0_bosses.setObjectName(u"layoutG_for_0_bosses")
        self.gridLayout_6 = QGridLayout(self.layoutG_for_0_bosses)
        self.gridLayout_6.setObjectName(u"gridLayout_6")
        self.required_bosses = QCheckBox(self.layoutG_for_0_bosses)
        self.required_bosses.setObjectName(u"required_bosses")

        self.gridLayout_6.addWidget(self.required_bosses, 0, 0, 1, 1)

        self.layoutH_for_0_bosses = QHBoxLayout()
        self.layoutH_for_0_bosses.setObjectName(u"layoutH_for_0_bosses")
        self.label_for_num_required_bosses = QLabel(self.layoutG_for_0_bosses)
        self.label_for_num_required_bosses.setObjectName(u"label_for_num_required_bosses")
        sizePolicy1.setHeightForWidth(self.label_for_num_required_bosses.sizePolicy().hasHeightForWidth())
        self.label_for_num_required_bosses.setSizePolicy(sizePolicy1)

        self.layoutH_for_0_bosses.addWidget(self.label_for_num_required_bosses)

        self.num_required_bosses = QComboBox(self.layoutG_for_0_bosses)
        self.num_required_bosses.addItem("")
        self.num_required_bosses.addItem("")
        self.num_required_bosses.addItem("")
        self.num_required_bosses.addItem("")
        self.num_required_bosses.addItem("")
        self.num_required_bosses.addItem("")
        self.num_required_bosses.setObjectName(u"num_required_bosses")
        sizePolicy.setHeightForWidth(self.num_required_bosses.sizePolicy().hasHeightForWidth())
        self.num_required_bosses.setSizePolicy(sizePolicy)
        self.num_required_bosses.setMaximumSize(QSize(40, 16777215))

        self.layoutH_for_0_bosses.addWidget(self.num_required_bosses)

        self.widget_3 = QWidget(self.layoutG_for_0_bosses)
        self.widget_3.setObjectName(u"widget_3")

        self.layoutH_for_0_bosses.addWidget(self.widget_3)


        self.gridLayout_6.addLayout(self.layoutH_for_0_bosses, 0, 1, 1, 1)

        self.widget_4 = QWidget(self.layoutG_for_0_bosses)
        self.widget_4.setObjectName(u"widget_4")

        self.gridLayout_6.addWidget(self.widget_4, 0, 2, 1, 1)

        self.widget_5 = QWidget(self.layoutG_for_0_bosses)
        self.widget_5.setObjectName(u"widget_5")

        self.gridLayout_6.addWidget(self.widget_5, 0, 3, 1, 1)


        self.verticalLayout_8.addWidget(self.layoutG_for_0_bosses)

        self.layoutG_for_1_logic = QGroupBox(self.tab_advanced)
        self.layoutG_for_1_logic.setObjectName(u"layoutG_for_1_logic")
        self.horizontalLayout_22 = QHBoxLayout(self.layoutG_for_1_logic)
        self.horizontalLayout_22.setObjectName(u"horizontalLayout_22")
        self.layoutH_for_0_obscurity = QHBoxLayout()
        self.layoutH_for_0_obscurity.setObjectName(u"layoutH_for_0_obscurity")
        self.label_for_logic_obscurity = QLabel(self.layoutG_for_1_logic)
        self.label_for_logic_obscurity.setObjectName(u"label_for_logic_obscurity")

        self.layoutH_for_0_obscurity.addWidget(self.label_for_logic_obscurity)

        self.logic_obscurity = QComboBox(self.layoutG_for_1_logic)
        self.logic_obscurity.addItem("")
        self.logic_obscurity.addItem("")
        self.logic_obscurity.addItem("")
        self.logic_obscurity.addItem("")
        self.logic_obscurity.setObjectName(u"logic_obscurity")

        self.layoutH_for_0_obscurity.addWidget(self.logic_obscurity)


        self.horizontalLayout_22.addLayout(self.layoutH_for_0_obscurity)

        self.layoutH_for_1_precision = QHBoxLayout()
        self.layoutH_for_1_precision.setObjectName(u"layoutH_for_1_precision")
        self.label_for_logic_precision = QLabel(self.layoutG_for_1_logic)
        self.label_for_logic_precision.setObjectName(u"label_for_logic_precision")

        self.layoutH_for_1_precision.addWidget(self.label_for_logic_precision)

        self.logic_precision = QComboBox(self.layoutG_for_1_logic)
        self.logic_precision.addItem("")
        self.logic_precision.addItem("")
        self.logic_precision.addItem("")
        self.logic_precision.addItem("")
        self.logic_precision.setObjectName(u"logic_precision")

        self.layoutH_for_1_precision.addWidget(self.logic_precision)


        self.horizontalLayout_22.addLayout(self.layoutH_for_1_precision)

        self.widget_10 = QWidget(self.layoutG_for_1_logic)
        self.widget_10.setObjectName(u"widget_10")

        self.horizontalLayout_22.addWidget(self.widget_10)

        self.widget_13 = QWidget(self.layoutG_for_1_logic)
        self.widget_13.setObjectName(u"widget_13")

        self.horizontalLayout_22.addWidget(self.widget_13)


        self.verticalLayout_8.addWidget(self.layoutG_for_1_logic)

        self.layoutG_for_2_hints = QGroupBox(self.tab_advanced)
        self.layoutG_for_2_hints.setObjectName(u"layoutG_for_2_hints")
        self.gridLayout_7 = QGridLayout(self.layoutG_for_2_hints)
        self.gridLayout_7.setObjectName(u"gridLayout_7")
        self.hoho_hints = QCheckBox(self.layoutG_for_2_hints)
        self.hoho_hints.setObjectName(u"hoho_hints")
        self.hoho_hints.setChecked(True)

        self.gridLayout_7.addWidget(self.hoho_hints, 4, 0, 1, 1)

        self.prioritize_remote_hints = QCheckBox(self.layoutG_for_2_hints)
        self.prioritize_remote_hints.setObjectName(u"prioritize_remote_hints")

        self.gridLayout_7.addWidget(self.prioritize_remote_hints, 6, 1, 1, 1)

        self.korl_hints = QCheckBox(self.layoutG_for_2_hints)
        self.korl_hints.setObjectName(u"korl_hints")

        self.gridLayout_7.addWidget(self.korl_hints, 4, 2, 1, 1)

        self.layoutH_for_2_barren_hints = QHBoxLayout()
        self.layoutH_for_2_barren_hints.setObjectName(u"layoutH_for_2_barren_hints")
        self.label_for_num_barren_hints = QLabel(self.layoutG_for_2_hints)
        self.label_for_num_barren_hints.setObjectName(u"label_for_num_barren_hints")

        self.layoutH_for_2_barren_hints.addWidget(self.label_for_num_barren_hints)

        self.num_barren_hints = QSpinBox(self.layoutG_for_2_hints)
        self.num_barren_hints.setObjectName(u"num_barren_hints")
        self.num_barren_hints.setCorrectionMode(QAbstractSpinBox.CorrectToNearestValue)
        self.num_barren_hints.setMinimum(0)
        self.num_barren_hints.setMaximum(15)
        self.num_barren_hints.setValue(0)

        self.layoutH_for_2_barren_hints.addWidget(self.num_barren_hints)

        self.widget_7 = QWidget(self.layoutG_for_2_hints)
        self.widget_7.setObjectName(u"widget_7")

        self.layoutH_for_2_barren_hints.addWidget(self.widget_7)


        self.gridLayout_7.addLayout(self.layoutH_for_2_barren_hints, 5, 2, 1, 1)

        self.cryptic_hints = QCheckBox(self.layoutG_for_2_hints)
        self.cryptic_hints.setObjectName(u"cryptic_hints")
        self.cryptic_hints.setChecked(True)

        self.gridLayout_7.addWidget(self.cryptic_hints, 6, 0, 1, 1)

        self.fishmen_hints = QCheckBox(self.layoutG_for_2_hints)
        self.fishmen_hints.setObjectName(u"fishmen_hints")
        self.fishmen_hints.setChecked(True)

        self.gridLayout_7.addWidget(self.fishmen_hints, 4, 1, 1, 1)

        self.layoutH_for_1_location_hints = QHBoxLayout()
        self.layoutH_for_1_location_hints.setObjectName(u"layoutH_for_1_location_hints")
        self.label_for_num_location_hints = QLabel(self.layoutG_for_2_hints)
        self.label_for_num_location_hints.setObjectName(u"label_for_num_location_hints")

        self.layoutH_for_1_location_hints.addWidget(self.label_for_num_location_hints)

        self.num_location_hints = QSpinBox(self.layoutG_for_2_hints)
        self.num_location_hints.setObjectName(u"num_location_hints")
        self.num_location_hints.setCorrectionMode(QAbstractSpinBox.CorrectToNearestValue)
        self.num_location_hints.setMinimum(0)
        self.num_location_hints.setMaximum(15)
        self.num_location_hints.setValue(5)

        self.layoutH_for_1_location_hints.addWidget(self.num_location_hints)

        self.widget_8 = QWidget(self.layoutG_for_2_hints)
        self.widget_8.setObjectName(u"widget_8")

        self.layoutH_for_1_location_hints.addWidget(self.widget_8)


        self.gridLayout_7.addLayout(self.layoutH_for_1_location_hints, 5, 1, 1, 1)

        self.layoutH_for_0_item_hints = QHBoxLayout()
        self.layoutH_for_0_item_hints.setObjectName(u"layoutH_for_0_item_hints")
        self.label_for_num_item_hints = QLabel(self.layoutG_for_2_hints)
        self.label_for_num_item_hints.setObjectName(u"label_for_num_item_hints")

        self.layoutH_for_0_item_hints.addWidget(self.label_for_num_item_hints)

        self.num_item_hints = QSpinBox(self.layoutG_for_2_hints)
        self.num_item_hints.setObjectName(u"num_item_hints")
        self.num_item_hints.setCorrectionMode(QAbstractSpinBox.CorrectToNearestValue)
        self.num_item_hints.setMinimum(0)
        self.num_item_hints.setMaximum(15)
        self.num_item_hints.setValue(15)

        self.layoutH_for_0_item_hints.addWidget(self.num_item_hints)

        self.widget_9 = QWidget(self.layoutG_for_2_hints)
        self.widget_9.setObjectName(u"widget_9")

        self.layoutH_for_0_item_hints.addWidget(self.widget_9)


        self.gridLayout_7.addLayout(self.layoutH_for_0_item_hints, 5, 0, 1, 1)

        self.layoutH_for_3_path_hints = QHBoxLayout()
        self.layoutH_for_3_path_hints.setObjectName(u"layoutH_for_3_path_hints")
        self.label_for_num_path_hints = QLabel(self.layoutG_for_2_hints)
        self.label_for_num_path_hints.setObjectName(u"label_for_num_path_hints")

        self.layoutH_for_3_path_hints.addWidget(self.label_for_num_path_hints)

        self.num_path_hints = QSpinBox(self.layoutG_for_2_hints)
        self.num_path_hints.setObjectName(u"num_path_hints")
        self.num_path_hints.setCorrectionMode(QAbstractSpinBox.CorrectToNearestValue)
        self.num_path_hints.setMinimum(0)
        self.num_path_hints.setMaximum(15)
        self.num_path_hints.setValue(0)

        self.layoutH_for_3_path_hints.addWidget(self.num_path_hints)

        self.widget_6 = QWidget(self.layoutG_for_2_hints)
        self.widget_6.setObjectName(u"widget_6")

        self.layoutH_for_3_path_hints.addWidget(self.widget_6)


        self.gridLayout_7.addLayout(self.layoutH_for_3_path_hints, 5, 3, 1, 1)


        self.verticalLayout_8.addWidget(self.layoutG_for_2_hints)

        self.layoutG_for_3_advanced = QGroupBox(self.tab_advanced)
        self.layoutG_for_3_advanced.setObjectName(u"layoutG_for_3_advanced")
        self.gridLayout_8 = QGridLayout(self.layoutG_for_3_advanced)
        self.gridLayout_8.setObjectName(u"gridLayout_8")
        self.do_not_generate_spoiler_log = QCheckBox(self.layoutG_for_3_advanced)
        self.do_not_generate_spoiler_log.setObjectName(u"do_not_generate_spoiler_log")

        self.gridLayout_8.addWidget(self.do_not_generate_spoiler_log, 0, 0, 1, 1)

        self.widget_11 = QWidget(self.layoutG_for_3_advanced)
        self.widget_11.setObjectName(u"widget_11")

        self.gridLayout_8.addWidget(self.widget_11, 0, 2, 1, 1)

        self.widget_12 = QWidget(self.layoutG_for_3_advanced)
        self.widget_12.setObjectName(u"widget_12")

        self.gridLayout_8.addWidget(self.widget_12, 0, 3, 1, 1)

        self.dry_run = QCheckBox(self.layoutG_for_3_advanced)
        self.dry_run.setObjectName(u"dry_run")

        self.gridLayout_8.addWidget(self.dry_run, 0, 1, 1, 1)


        self.verticalLayout_8.addWidget(self.layoutG_for_3_advanced)

        self.zzzz_spacerV_for_advanced = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_8.addItem(self.zzzz_spacerV_for_advanced)

        self.tabs_for_primary.addTab(self.tab_advanced, "")
        self.tab_player_customization = CosmeticTab()
        self.tab_player_customization.setObjectName(u"tab_player_customization")
        self.tabs_for_primary.addTab(self.tab_player_customization, "")

        self.verticalLayout_2.addWidget(self.tabs_for_primary)

        self.layoutS_for_0_primary.setWidget(self.scrollA_for_primary)

        self.verticalLayout.addWidget(self.layoutS_for_0_primary)

        self.option_description = QLabel(self.centralwidget)
        self.option_description.setObjectName(u"option_description")
        self.option_description.setMinimumSize(QSize(0, 32))
        self.option_description.setTextFormat(Qt.RichText)
        self.option_description.setWordWrap(True)

        self.verticalLayout.addWidget(self.option_description)

        self.layoutH_for_2_permalink = QHBoxLayout()
        self.layoutH_for_2_permalink.setObjectName(u"layoutH_for_2_permalink")
        self.label_for_permalink = QLabel(self.centralwidget)
        self.label_for_permalink.setObjectName(u"label_for_permalink")

        self.layoutH_for_2_permalink.addWidget(self.label_for_permalink)

        self.permalink = QLineEdit(self.centralwidget)
        self.permalink.setObjectName(u"permalink")

        self.layoutH_for_2_permalink.addWidget(self.permalink)


        self.verticalLayout.addLayout(self.layoutH_for_2_permalink)

        self.update_checker_label = QLabel(self.centralwidget)
        self.update_checker_label.setObjectName(u"update_checker_label")
        self.update_checker_label.setOpenExternalLinks(True)

        self.verticalLayout.addWidget(self.update_checker_label)

        self.layoutH_for_4_buttons = QHBoxLayout()
        self.layoutH_for_4_buttons.setObjectName(u"layoutH_for_4_buttons")
        self.about_button = QPushButton(self.centralwidget)
        self.about_button.setObjectName(u"about_button")

        self.layoutH_for_4_buttons.addWidget(self.about_button)

        self.zzzz_spacerH_for_about = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.layoutH_for_4_buttons.addItem(self.zzzz_spacerH_for_about)

        self.reset_settings_to_default = QPushButton(self.centralwidget)
        self.reset_settings_to_default.setObjectName(u"reset_settings_to_default")
        self.reset_settings_to_default.setMinimumSize(QSize(180, 0))

        self.layoutH_for_4_buttons.addWidget(self.reset_settings_to_default)

        self.zzzz_spacerH_for_default = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.layoutH_for_4_buttons.addItem(self.zzzz_spacerH_for_default)

        self.randomize_button = QPushButton(self.centralwidget)
        self.randomize_button.setObjectName(u"randomize_button")

        self.layoutH_for_4_buttons.addWidget(self.randomize_button)


        self.verticalLayout.addLayout(self.layoutH_for_4_buttons)

        MainWindow.setCentralWidget(self.centralwidget)
        QWidget.setTabOrder(self.layoutS_for_0_primary, self.clean_iso_path)
        QWidget.setTabOrder(self.clean_iso_path, self.clean_iso_path_browse_button)
        QWidget.setTabOrder(self.clean_iso_path_browse_button, self.output_folder)
        QWidget.setTabOrder(self.output_folder, self.output_folder_browse_button)
        QWidget.setTabOrder(self.output_folder_browse_button, self.seed)
        QWidget.setTabOrder(self.seed, self.generate_seed_button)
        QWidget.setTabOrder(self.generate_seed_button, self.sword_mode)
        QWidget.setTabOrder(self.sword_mode, self.num_starting_triforce_shards)
        QWidget.setTabOrder(self.num_starting_triforce_shards, self.mix_entrances)
        QWidget.setTabOrder(self.mix_entrances, self.swift_sail)
        QWidget.setTabOrder(self.swift_sail, self.instant_text_boxes)
        QWidget.setTabOrder(self.instant_text_boxes, self.reveal_full_sea_chart)
        QWidget.setTabOrder(self.reveal_full_sea_chart, self.skip_rematch_bosses)
        QWidget.setTabOrder(self.skip_rematch_bosses, self.add_shortcut_warps_between_dungeons)
        QWidget.setTabOrder(self.add_shortcut_warps_between_dungeons, self.remove_title_and_ending_videos)
        QWidget.setTabOrder(self.remove_title_and_ending_videos, self.randomize_button)
        QWidget.setTabOrder(self.randomize_button, self.randomized_gear)
        QWidget.setTabOrder(self.randomized_gear, self.remove_gear)
        QWidget.setTabOrder(self.remove_gear, self.add_gear)
        QWidget.setTabOrder(self.add_gear, self.starting_gear)
        QWidget.setTabOrder(self.starting_gear, self.starting_hcs)
        QWidget.setTabOrder(self.starting_hcs, self.starting_pohs)
        QWidget.setTabOrder(self.starting_pohs, self.required_bosses)
        QWidget.setTabOrder(self.required_bosses, self.num_required_bosses)
        QWidget.setTabOrder(self.num_required_bosses, self.hoho_hints)
        QWidget.setTabOrder(self.hoho_hints, self.fishmen_hints)
        QWidget.setTabOrder(self.fishmen_hints, self.korl_hints)
        QWidget.setTabOrder(self.korl_hints, self.num_item_hints)
        QWidget.setTabOrder(self.num_item_hints, self.num_location_hints)
        QWidget.setTabOrder(self.num_location_hints, self.num_barren_hints)
        QWidget.setTabOrder(self.num_barren_hints, self.num_path_hints)
        QWidget.setTabOrder(self.num_path_hints, self.cryptic_hints)
        QWidget.setTabOrder(self.cryptic_hints, self.prioritize_remote_hints)
        QWidget.setTabOrder(self.prioritize_remote_hints, self.do_not_generate_spoiler_log)
        QWidget.setTabOrder(self.do_not_generate_spoiler_log, self.permalink)
        QWidget.setTabOrder(self.permalink, self.about_button)
        QWidget.setTabOrder(self.about_button, self.reset_settings_to_default)

        self.retranslateUi(MainWindow)

        self.tabs_for_primary.setCurrentIndex(0)
        self.num_required_bosses.setCurrentIndex(3)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"Wind Waker Randomizer", None))
        self.label_for_clean_iso_path.setText(QCoreApplication.translate("MainWindow", u"Vanilla Wind Waker ISO [[?]](help)", None))
        self.label_for_output_folder.setText(QCoreApplication.translate("MainWindow", u"Randomized Output Folder", None))
        self.output_folder_browse_button.setText(QCoreApplication.translate("MainWindow", u"Browse", None))
        self.label_for_seed.setText(QCoreApplication.translate("MainWindow", u"Random Seed (optional)", None))
        self.generate_seed_button.setText(QCoreApplication.translate("MainWindow", u"New seed", None))
        self.clean_iso_path_browse_button.setText(QCoreApplication.translate("MainWindow", u"Browse", None))
        self.progression_locations_groupbox.setTitle(QCoreApplication.translate("MainWindow", u"Progression Locations: Where Should Progress Items Be Placed?", None))
        self.progression_dungeons.setText(QCoreApplication.translate("MainWindow", u"Dungeons", None))
        self.progression_tingle_chests.setText(QCoreApplication.translate("MainWindow", u"Tingle Chests", None))
        self.progression_long_sidequests.setText(QCoreApplication.translate("MainWindow", u"Long Sidequests", None))
        self.progression_spoils_trading.setText(QCoreApplication.translate("MainWindow", u"Spoils Trading", None))
        self.progression_short_sidequests.setText(QCoreApplication.translate("MainWindow", u"Short Sidequests", None))
        self.progression_puzzle_secret_caves.setText(QCoreApplication.translate("MainWindow", u"Puzzle Secret Caves", None))
        self.progression_savage_labyrinth.setText(QCoreApplication.translate("MainWindow", u"Savage Labyrinth", None))
        self.progression_combat_secret_caves.setText(QCoreApplication.translate("MainWindow", u"Combat Secret Caves", None))
        self.progression_dungeon_secrets.setText(QCoreApplication.translate("MainWindow", u"Dungeon Secrets", None))
        self.progression_battlesquid.setText(QCoreApplication.translate("MainWindow", u"Battlesquid Minigame", None))
        self.progression_mail.setText(QCoreApplication.translate("MainWindow", u"Mail", None))
        self.progression_great_fairies.setText(QCoreApplication.translate("MainWindow", u"Great Fairies", None))
        self.progression_misc.setText(QCoreApplication.translate("MainWindow", u"Miscellaneous", None))
        self.progression_treasure_charts.setText(QCoreApplication.translate("MainWindow", u"Sunken Treasure (From Treasure Charts)", None))
        self.progression_triforce_charts.setText(QCoreApplication.translate("MainWindow", u"Sunken Treasure (From Triforce Charts)", None))
        self.progression_expensive_purchases.setText(QCoreApplication.translate("MainWindow", u"Expensive Purchases", None))
        self.progression_minigames.setText(QCoreApplication.translate("MainWindow", u"Minigames", None))
        self.progression_submarines.setText(QCoreApplication.translate("MainWindow", u"Submarines", None))
        self.progression_big_octos_gunboats.setText(QCoreApplication.translate("MainWindow", u"Big Octos and Gunboats", None))
        self.progression_platforms_rafts.setText(QCoreApplication.translate("MainWindow", u"Lookout Platforms and Rafts", None))
        self.progression_free_gifts.setText(QCoreApplication.translate("MainWindow", u"Free Gifts", None))
        self.progression_island_puzzles.setText(QCoreApplication.translate("MainWindow", u"Island Puzzles", None))
        self.progression_eye_reef_chests.setText(QCoreApplication.translate("MainWindow", u"Eye Reef Chests", None))
        self.layoutG_for_2_item_randomizers.setTitle(QCoreApplication.translate("MainWindow", u"Item Randomizer Modes", None))
        self.label_for_sword_mode.setText(QCoreApplication.translate("MainWindow", u"Sword Mode", None))
        self.sword_mode.setItemText(0, QCoreApplication.translate("MainWindow", u"Start with Hero's Sword", None))
        self.sword_mode.setItemText(1, QCoreApplication.translate("MainWindow", u"No Starting Sword", None))
        self.sword_mode.setItemText(2, QCoreApplication.translate("MainWindow", u"Swordless", None))

        self.label_for_num_starting_triforce_shards.setText(QCoreApplication.translate("MainWindow", u"Triforce Shards to Start With", None))
        self.num_starting_triforce_shards.setItemText(0, QCoreApplication.translate("MainWindow", u"0", None))
        self.num_starting_triforce_shards.setItemText(1, QCoreApplication.translate("MainWindow", u"1", None))
        self.num_starting_triforce_shards.setItemText(2, QCoreApplication.translate("MainWindow", u"2", None))
        self.num_starting_triforce_shards.setItemText(3, QCoreApplication.translate("MainWindow", u"3", None))
        self.num_starting_triforce_shards.setItemText(4, QCoreApplication.translate("MainWindow", u"4", None))
        self.num_starting_triforce_shards.setItemText(5, QCoreApplication.translate("MainWindow", u"5", None))
        self.num_starting_triforce_shards.setItemText(6, QCoreApplication.translate("MainWindow", u"6", None))
        self.num_starting_triforce_shards.setItemText(7, QCoreApplication.translate("MainWindow", u"7", None))
        self.num_starting_triforce_shards.setItemText(8, QCoreApplication.translate("MainWindow", u"8", None))

        self.chest_type_matches_contents.setText(QCoreApplication.translate("MainWindow", u"Chest Type Matches Contents", None))
        self.keylunacy.setText(QCoreApplication.translate("MainWindow", u"Key-Lunacy", None))
        self.layoutG_for_0_entrance.setTitle(QCoreApplication.translate("MainWindow", u"Entrance Randomizer Options", None))
        self.randomize_boss_entrances.setText(QCoreApplication.translate("MainWindow", u"Nested Bosses", None))
        self.randomize_fairy_fountain_entrances.setText(QCoreApplication.translate("MainWindow", u"Fairy Fountains", None))
        self.randomize_secret_cave_inner_entrances.setText(QCoreApplication.translate("MainWindow", u"Inner Secret Caves", None))
        self.randomize_secret_cave_entrances.setText(QCoreApplication.translate("MainWindow", u"Secret Caves", None))
        self.randomize_dungeon_entrances.setText(QCoreApplication.translate("MainWindow", u"Dungeons", None))
        self.randomize_miniboss_entrances.setText(QCoreApplication.translate("MainWindow", u"Nested Minibosses", None))
        self.label_for_mix_entrances.setText(QCoreApplication.translate("MainWindow", u"Mixing", None))
        self.mix_entrances.setItemText(0, QCoreApplication.translate("MainWindow", u"Separate Dungeons From Caves & Fountains", None))
        self.mix_entrances.setItemText(1, QCoreApplication.translate("MainWindow", u"Mix Dungeons & Caves & Fountains", None))

        self.layoutG_for_1_other.setTitle(QCoreApplication.translate("MainWindow", u"Other Randomizers", None))
        self.randomize_enemies.setText(QCoreApplication.translate("MainWindow", u"Randomize Enemy Locations", None))
        self.randomize_charts.setText(QCoreApplication.translate("MainWindow", u"Randomize Charts", None))
        self.randomize_enemy_palettes.setText(QCoreApplication.translate("MainWindow", u"Randomize Enemy Palettes", None))
        self.randomize_starting_island.setText(QCoreApplication.translate("MainWindow", u"Randomize Starting Island", None))
        self.layoutG_for_4_convenience.setTitle(QCoreApplication.translate("MainWindow", u"Convenience Tweaks", None))
        self.invert_sea_compass_x_axis.setText(QCoreApplication.translate("MainWindow", u"Invert Sea Compass X-Axis", None))
        self.invert_camera_x_axis.setText(QCoreApplication.translate("MainWindow", u"Invert Camera X-Axis", None))
        self.instant_text_boxes.setText(QCoreApplication.translate("MainWindow", u"Instant Text Boxes", None))
        self.reveal_full_sea_chart.setText(QCoreApplication.translate("MainWindow", u"Reveal Full Sea Chart", None))
        self.swift_sail.setText(QCoreApplication.translate("MainWindow", u"Swift Sail", None))
        self.remove_title_and_ending_videos.setText(QCoreApplication.translate("MainWindow", u"Remove Title and Ending Videos", None))
        self.skip_rematch_bosses.setText(QCoreApplication.translate("MainWindow", u"Skip Boss Rematches", None))
        self.remove_music.setText(QCoreApplication.translate("MainWindow", u"Remove Music", None))
        self.add_shortcut_warps_between_dungeons.setText(QCoreApplication.translate("MainWindow", u"Add Shortcut Warps Between Dungeons", None))
        self.tabs_for_primary.setTabText(self.tabs_for_primary.indexOf(self.tab_randomizer_settings), QCoreApplication.translate("MainWindow", u"Randomizer Settings", None))
        self.label_for_randomized_gear.setText(QCoreApplication.translate("MainWindow", u"Randomized Gear", None))
        self.remove_gear.setText(QCoreApplication.translate("MainWindow", u"<-", None))
        self.add_gear.setText(QCoreApplication.translate("MainWindow", u"->", None))
        self.label_for_starting_gear.setText(QCoreApplication.translate("MainWindow", u"Starting Gear", None))
        self.label_for_starting_hcs.setText(QCoreApplication.translate("MainWindow", u"Heart Containers", None))
        self.label_for_starting_pohs.setText(QCoreApplication.translate("MainWindow", u"Heart Pieces", None))
        self.current_health.setText(QCoreApplication.translate("MainWindow", u"Current Starting Health: 3 hearts", None))
        self.tabs_for_primary.setTabText(self.tabs_for_primary.indexOf(self.tab_starting_items), QCoreApplication.translate("MainWindow", u"Starting Items", None))
        self.layoutG_for_0_bosses.setTitle(QCoreApplication.translate("MainWindow", u"Required Bosses", None))
        self.required_bosses.setText(QCoreApplication.translate("MainWindow", u"Required Bosses Mode", None))
        self.label_for_num_required_bosses.setText(QCoreApplication.translate("MainWindow", u"Number of Required Bosses", None))
        self.num_required_bosses.setItemText(0, QCoreApplication.translate("MainWindow", u"1", None))
        self.num_required_bosses.setItemText(1, QCoreApplication.translate("MainWindow", u"2", None))
        self.num_required_bosses.setItemText(2, QCoreApplication.translate("MainWindow", u"3", None))
        self.num_required_bosses.setItemText(3, QCoreApplication.translate("MainWindow", u"4", None))
        self.num_required_bosses.setItemText(4, QCoreApplication.translate("MainWindow", u"5", None))
        self.num_required_bosses.setItemText(5, QCoreApplication.translate("MainWindow", u"6", None))

        self.layoutG_for_1_logic.setTitle(QCoreApplication.translate("MainWindow", u"Logic Difficulty", None))
        self.label_for_logic_obscurity.setText(QCoreApplication.translate("MainWindow", u"Obscure Tricks Required", None))
        self.logic_obscurity.setItemText(0, QCoreApplication.translate("MainWindow", u"None", None))
        self.logic_obscurity.setItemText(1, QCoreApplication.translate("MainWindow", u"Normal", None))
        self.logic_obscurity.setItemText(2, QCoreApplication.translate("MainWindow", u"Hard", None))
        self.logic_obscurity.setItemText(3, QCoreApplication.translate("MainWindow", u"Very Hard", None))

        self.label_for_logic_precision.setText(QCoreApplication.translate("MainWindow", u"Precise Tricks Required", None))
        self.logic_precision.setItemText(0, QCoreApplication.translate("MainWindow", u"None", None))
        self.logic_precision.setItemText(1, QCoreApplication.translate("MainWindow", u"Normal", None))
        self.logic_precision.setItemText(2, QCoreApplication.translate("MainWindow", u"Hard", None))
        self.logic_precision.setItemText(3, QCoreApplication.translate("MainWindow", u"Very Hard", None))

        self.layoutG_for_2_hints.setTitle(QCoreApplication.translate("MainWindow", u"Hint Options", None))
        self.hoho_hints.setText(QCoreApplication.translate("MainWindow", u"Place Hints on Old Man Ho Ho", None))
        self.prioritize_remote_hints.setText(QCoreApplication.translate("MainWindow", u"Prioritize Remote Location Hints", None))
        self.korl_hints.setText(QCoreApplication.translate("MainWindow", u"Place Hints on King of Red Lions", None))
        self.label_for_num_barren_hints.setText(QCoreApplication.translate("MainWindow", u"Barren Hints", None))
        self.cryptic_hints.setText(QCoreApplication.translate("MainWindow", u"Use Cryptic Text for Hints", None))
        self.fishmen_hints.setText(QCoreApplication.translate("MainWindow", u"Place Hints on Fishmen", None))
        self.label_for_num_location_hints.setText(QCoreApplication.translate("MainWindow", u"Location Hints", None))
        self.label_for_num_item_hints.setText(QCoreApplication.translate("MainWindow", u"Item Hints", None))
        self.label_for_num_path_hints.setText(QCoreApplication.translate("MainWindow", u"Path Hints", None))
        self.layoutG_for_3_advanced.setTitle(QCoreApplication.translate("MainWindow", u"Additional Advanced Options", None))
        self.do_not_generate_spoiler_log.setText(QCoreApplication.translate("MainWindow", u"Do Not Generate Spoiler Log", None))
        self.dry_run.setText(QCoreApplication.translate("MainWindow", u"Dry Run", None))
        self.tabs_for_primary.setTabText(self.tabs_for_primary.indexOf(self.tab_advanced), QCoreApplication.translate("MainWindow", u"Advanced Options", None))
        self.tabs_for_primary.setTabText(self.tabs_for_primary.indexOf(self.tab_player_customization), QCoreApplication.translate("MainWindow", u"Player Customization", None))
        self.option_description.setText("")
        self.label_for_permalink.setText(QCoreApplication.translate("MainWindow", u"Permalink (copy paste to share your settings):", None))
        self.update_checker_label.setText(QCoreApplication.translate("MainWindow", u"Checking for updates to the randomizer...", None))
        self.about_button.setText(QCoreApplication.translate("MainWindow", u"About", None))
        self.reset_settings_to_default.setText(QCoreApplication.translate("MainWindow", u"Reset All Settings to Default", None))
        self.randomize_button.setText(QCoreApplication.translate("MainWindow", u"Randomize", None))
    # retranslateUi

