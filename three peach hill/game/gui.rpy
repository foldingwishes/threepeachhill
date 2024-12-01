﻿################################################################################
## Initialization
################################################################################

## The init offset statement causes the initialization statements in this file
## to run before init statements in any other file.
init offset = -2

## Calling gui.init resets the styles to sensible default values, and sets the
## width and height of the game.
init python:
    gui.init(2560, 1440)

## Enable checks for invalid or unstable properties in screens or transforms
define config.check_conflicting_properties = True


################################################################################
## GUI Configuration Variables
################################################################################


## Colors ######################################################################
##
## The colors of text in the interface.

## An accent color used throughout the interface to label and highlight text.
define gui.accent_color = '#ff6e2f'

## The color used for a text button when it is neither selected nor hovered.
define gui.idle_color = '#aeaeae'

## The small color is used for small text, which needs to be brighter/darker to
## achieve the same effect.
define gui.idle_small_color = '#606060'

## The color that is used for buttons and bars that are hovered.
define gui.hover_color = '#ff6e2f'

## The color used for a text button when it is selected but not focused. A
## button is selected if it is the current screen or preference value.
define gui.selected_color = '#ffffff'

## The color used for a text button when it cannot be selected.
define gui.insensitive_color = '#7070707f'

## Colors used for the portions of bars that are not filled in. These are not
## used directly, but are used when re-generating bar image files.
define gui.muted_color = '#e0a366'
define gui.hover_muted_color = '#eac199'

## The colors used for dialogue and menu choice text.
define gui.text_color = '#292525'
define gui.interface_text_color = '#404040'


## Fonts and Font Sizes ########################################################

## The font used for in-game text.
define gui.text_font = "fonts/AutumnInSeptember-G3ZoD.ttf"

## The font used for character names.
define gui.name_text_font = "fonts/Wildy-Sans.ttf"

## The font used for out-of-game text.
define gui.interface_text_font = "fonts/AutumnInSeptember-G3ZoD.ttf"

## The size of normal dialogue text.
define gui.text_size = 56

## The size of character names.
define gui.name_text_size = 80

## The size of text in the game's user interface.
define gui.interface_text_size = 66

## The size of labels in the game's user interface.
define gui.label_text_size = 66

## The size of text on the notify screen.
define gui.notify_text_size = 50

## The size of the game's title.
define gui.title_text_size = 100

define gui.name_text_outlines = [(absolute(2), '#74301e', absolute(2), absolute(2))]


## Main and Game Menus #########################################################

## The images used for the main and game menus.
define gui.main_menu_background = "main_menu_animated"
define gui.game_menu_background = "gui/menu/game_menu.png"


## Dialogue ####################################################################
##
## These variables control how dialogue is displayed on the screen one line at a
## time.

## The height of the textbox containing dialogue.
define gui.textbox_height = 530 # default: 370

## The placement of the textbox vertically on the screen. 0.0 is the top, 0.5 is
## center, and 1.0 is the bottom.
define gui.textbox_yalign = 1.0


## The placement of the speaking character's name, relative to the textbox.
## These can be a whole number of pixels from the left or top, or 0.5 to center.
define gui.name_xpos = 900
define gui.name_ypos = -8 # default: -0.4

## The horizontal alignment of the character's name. This can be 0.0 for left-
## aligned, 0.5 for centered, and 1.0 for right-aligned.
define gui.name_xalign = 0.025

## The width, height, and borders of the box containing the character's name, or
## None to automatically size it.
define gui.namebox_width = 680
define gui.namebox_height = None

## The borders of the box containing the character's name, in left, top, right,
## bottom order.
define gui.namebox_borders = Borders(0, -5, 5, 5)

## If True, the background of the namebox will be tiled, if False, the
## background of the namebox will be scaled.
define gui.namebox_tile = False


## The placement of dialogue relative to the textbox. These can be a whole
## number of pixels relative to the left or top side of the textbox, or 0.5 to
## center.
define gui.dialogue_xpos = 780
define gui.dialogue_ypos = 160 # default: 0

## The maximum width of dialogue text, in pixels.
define gui.dialogue_width = 1488

## The horizontal alignment of the dialogue text. This can be 0.0 for left-
## aligned, 0.5 for centered, and 1.0 for right-aligned.
define gui.dialogue_text_xalign = 0.0


## Night colors.
define gui.dialogue_night_accent_color = '#377FCC'
define gui.dialogue_night_hover_color = '#377FCC'
define gui.dialogue_night_text_color = '#ffffff'


## Buttons #####################################################################
##
## These variables, along with the image files in gui/button, control aspects of
## how buttons are displayed.

## The width and height of a button, in pixels. If None, Ren'Py computes a size.
define gui.button_width = None
define gui.button_height = None

## The borders on each side of the button, in left, top, right, bottom order.
define gui.button_borders = Borders(8, 8, 8, 8)

## If True, the background image will be tiled. If False, the background image
## will be linearly scaled.
define gui.button_tile = False

## The font used by the button.
define gui.button_text_font = gui.interface_text_font

## The size of the text used by the button.
define gui.button_text_size = gui.interface_text_size

## The color of button text in various states.
define gui.button_text_idle_color = gui.idle_color
define gui.button_text_hover_color = gui.hover_color
define gui.button_text_selected_color = gui.selected_color
define gui.button_text_insensitive_color = gui.insensitive_color

## The horizontal alignment of the button text. (0.0 is left, 0.5 is center, 1.0
## is right).
define gui.button_text_xalign = 0.5


## These variables override settings for different kinds of buttons. Please see
## the gui documentation for the kinds of buttons available, and what each is
## used for.
##
## These customizations are used by the default interface:

define gui.radio_button_borders = Borders(36, 8, 8, 8)

define gui.check_button_borders = Borders(36, 8, 8, 8)

define gui.confirm_button_text_xalign = 0.5

define gui.page_button_borders = Borders(20, 8, 20, 8)

define gui.quick_button_borders = Borders(20, 8, 20, 0)
define gui.quick_button_text_size = 28
define gui.quick_button_text_idle_color = gui.idle_small_color
define gui.quick_button_text_selected_color = gui.accent_color


## Choice Buttons ##############################################################
##
## Choice buttons are used in the in-game menus.

define gui.choice_button_width = 1180
define gui.choice_button_height = 120
define gui.choice_button_tile = False
#define gui.choice_button_borders = Borders(200, 10, 200, 10)
define gui.choice_button_text_font = gui.text_font
define gui.choice_button_text_size = gui.text_size
define gui.choice_button_text_xalign = 0.5
define gui.choice_button_text_yalign = 0.35
define gui.choice_button_text_idle_color = '#ffffff'
define gui.choice_button_text_hover_color = "#e05b33"
define gui.choice_button_text_insensitive_color = '#ffffff'

# Night mode styling.
define gui.choice_night_button_text_idle_color = '#5984CC'
define gui.choice_night_button_text_hover_color = "#ffffff"
define gui.choice_night_button_text_insensitive_color = '#5984CC'

## File Slot Buttons ###########################################################
##
## A file slot button is a special kind of button. It contains a thumbnail
## image, and text describing the contents of the save slot. A save slot uses
## image files in gui/button, like the other kinds of buttons.

## The save slot button.
define gui.slot_button_width = 552
define gui.slot_button_height = 412
define gui.slot_button_borders = Borders(20, 20, 20, 20)
define gui.slot_button_text_size = 28
define gui.slot_button_text_xalign = 0.5
define gui.slot_button_text_idle_color = gui.idle_small_color
define gui.slot_button_text_selected_idle_color = gui.selected_color
define gui.slot_button_text_selected_hover_color = gui.hover_color

## The width and height of thumbnails used by the save slots.
define config.thumbnail_width = 512
define config.thumbnail_height = 288

## The number of columns and rows in the grid of save slots.
define gui.file_slot_cols = 2
define gui.file_slot_rows = 2


## Positioning and Spacing #####################################################
##
## These variables control the positioning and spacing of various user interface
## elements.

## The vertical position of the skip indicator.
define gui.skip_ypos = 20

## The vertical position of the notify screen.
define gui.notify_ypos = 90

## The spacing between menu choices.
define gui.choice_spacing = 44

## Controls the amount of spacing between preferences.
define gui.pref_spacing = 20

## Controls the amount of spacing between preference buttons.
define gui.pref_button_spacing = 0

## The spacing between file page buttons.
define gui.page_spacing = 0

## The spacing between file slots.
define gui.slot_spacing = 20

## The position of the main menu text.
define gui.main_menu_text_xalign = 1.0


## Frames ######################################################################
##
## These variables control the look of frames that can contain user interface
## components when an overlay or window is not present.

## Generic frames.
define gui.frame_borders = Borders(8, 8, 8, 8)

## The frame that is used as part of the confirm screen.
define gui.confirm_frame_borders = Borders(80, 80, 80, 80)

## The frame that is used as part of the skip screen.
define gui.skip_frame_borders = Borders(32, 10, 100, 10)

## The frame that is used as part of the notify screen.
define gui.notify_frame_borders = Borders(32, 10, 80, 10)

## Should frame backgrounds be tiled?
define gui.frame_tile = False


## Bars, Scrollbars, and Sliders ###############################################
##
## These control the look and size of bars, scrollbars, and sliders.
##
## The default GUI only uses sliders and vertical scrollbars. All of the other
## bars are only used in creator-written screens.

## The height of horizontal bars, scrollbars, and sliders. The width of vertical
## bars, scrollbars, and sliders.
define gui.bar_size = 50
define gui.scrollbar_size = 24
define gui.slider_size = 50

## True if bar images should be tiled. False if they should be linearly scaled.
define gui.bar_tile = False
define gui.scrollbar_tile = False
define gui.slider_tile = False

## Horizontal borders.
define gui.bar_borders = Borders(8, 8, 8, 8)
define gui.scrollbar_borders = Borders(8, 8, 8, 8)
define gui.slider_borders = Borders(8, 8, 8, 8)

## Vertical borders.
define gui.vbar_borders = Borders(8, 8, 8, 8)
define gui.vscrollbar_borders = Borders(8, 8, 8, 8)
define gui.vslider_borders = Borders(8, 8, 8, 8)

## What to do with unscrollable scrollbars in the gui. "hide" hides them, while
## None shows them.
define gui.unscrollable = "hide"


## Menu Navigation #############################################################

define menu_font_color = '#CA613F'

define gui.menu_navigation_button_text_size = 80

define gui.menu_navigation_button_text_idle_color = menu_font_color
define gui.menu_navigation_button_text_hover_color = menu_font_color
define gui.menu_navigation_button_text_insensitive_color = menu_font_color
define gui.menu_navigation_button_text_outlines = [(absolute(.85), menu_font_color, 0, 0)]

define gui.menu_navigation_button_text_kerning = 1.25
define gui.menu_navigation_button_text_line_spacing = 1.12
define gui.menu_navigation_button_text_yalign = 0.55

define gui.menu_navigation_button_text_xmargin = 72
define gui.menu_navigation_button_ypadding = 10

define gui.menu_navigation_xalign = 0.5
define gui.menu_navigation_yalign = 0.9

define gui.menu_navigation_spacing = 20
define gui.menu_navigation_button_ysize = 110
define gui.menu_navigation_button_height = 110


## Game Menu Navigation ########################################################

## The position of the left side of the navigation buttons, relative to the left
## side of the screen.
define gui.navigation_xpos = 80

define gui.navigation_spacing = 40


## History #####################################################################
##
## The history screen displays dialogue that the player has already dismissed.

## The number of blocks of dialogue history Ren'Py will keep.
define config.history_length = 250

## The height of a history screen entry, or None to make the height variable at
## the cost of performance.
define gui.history_height = 280

## Additional space to add between history screen entries.
define gui.history_spacing = 0

## The position, width, and alignment of the label giving the name of the
## speaking character.
define gui.history_name_xpos = 310
define gui.history_name_ypos = 0
define gui.history_name_width = 310
define gui.history_name_xalign = 1.0

## The position, width, and alignment of the dialogue text.
define gui.history_text_xpos = 340
define gui.history_text_ypos = 4
define gui.history_text_width = 1480
define gui.history_text_xalign = 0.0


## NVL-Mode ####################################################################
##
## The NVL-mode screen displays the dialogue spoken by NVL-mode characters.

## The borders of the background of the NVL-mode background window.
define gui.nvl_borders = Borders(0, 20, 0, 40)

## The maximum number of NVL-mode entries Ren'Py will display. When more entries
## than this are to be show, the oldest entry will be removed.
define gui.nvl_list_length = 6

## The height of an NVL-mode entry. Set this to None to have the entries
## dynamically adjust height.
define gui.nvl_height = 230

## The spacing between NVL-mode entries when gui.nvl_height is None, and between
## NVL-mode entries and an NVL-mode menu.
define gui.nvl_spacing = 20

## The position, width, and alignment of the label giving the name of the
## speaking character.
define gui.nvl_name_xpos = 860
define gui.nvl_name_ypos = 0
define gui.nvl_name_width = 300
define gui.nvl_name_xalign = 1.0

## The position, width, and alignment of the dialogue text.
define gui.nvl_text_xpos = 900
define gui.nvl_text_ypos = 16
define gui.nvl_text_width = 1180
define gui.nvl_text_xalign = 0.0

## The position, width, and alignment of nvl_thought text (the text said by the
## nvl_narrator character.)
define gui.nvl_thought_xpos = 480
define gui.nvl_thought_ypos = 0
define gui.nvl_thought_width = 1560
define gui.nvl_thought_xalign = 0.0

## The position of nvl menu_buttons.
define gui.nvl_button_xpos = 900
define gui.nvl_button_xalign = 0.0


## Localization ################################################################

## This controls where a line break is permitted. The default is suitable
## for most languages. A list of available values can be found at https://
## www.renpy.org/doc/html/style_properties.html#style-property-language

define gui.language = "unicode"


################################################################################
## Mobile devices
################################################################################

init python:

    ## This increases the size of the quick buttons to make them easier to touch
    ## on tablets and phones.
    @gui.variant
    def touch():

        gui.quick_button_borders = Borders(80, 28, 80, 0)

    ## This changes the size and spacing of various GUI elements to ensure they
    ## are easily visible on phones.
    @gui.variant
    def small():

        ## Font sizes.
        gui.text_size = 60
        gui.name_text_size = 72
        gui.notify_text_size = 50
        gui.interface_text_size = 60
        gui.button_text_size = 60
        gui.label_text_size = 68

        ## Adjust the location of the textbox.
        gui.textbox_height = 480
        gui.name_xpos = 160
        gui.dialogue_xpos = 180
        gui.dialogue_width = 2200

        ## Change the size and spacing of various things.
        gui.slider_size = 72

        gui.choice_button_width = 2480
        gui.choice_button_text_size = 60

        gui.navigation_spacing = 40
        gui.pref_button_spacing = 20

        gui.history_height = 380
        gui.history_text_width = 1380

        gui.quick_button_text_size = 40

        ## File button layout.
        gui.file_slot_cols = 2
        gui.file_slot_rows = 2

        ## NVL-mode.
        gui.nvl_height = 340

        gui.nvl_name_width = 610
        gui.nvl_name_xpos = 650

        gui.nvl_text_width = 1830
        gui.nvl_text_xpos = 690
        gui.nvl_text_ypos = 10

        gui.nvl_thought_width = 2480
        gui.nvl_thought_xpos = 40

        gui.nvl_button_width = 2480
        gui.nvl_button_xpos = 40
