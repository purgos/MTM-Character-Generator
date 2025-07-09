# MTM Character Sheet

A Python-based character sheet application for the MTM (Magic: The Gathering) tabletop roleplaying game.

## Features

- Character creation and management
- Aspect system with die assignments
- Gear die slot management
- Inventory tracking
- Special abilities management
- PDF export functionality
- Dice rolling with modifiers

## Usage

1. **Basic Information Tab:** Enter character name, player name, race, and other basic details
2. **Aspects Tab:** Assign die types to your character's aspects (melee, ranged, rogue, magic)
3. **Abilities Tab:** Select special abilities based on your d12 aspect
4. **Gear Die Tab:** Manage your gear die slots for spells and abilities
5. **Inventory Tab:** Track your character's equipment and items

## File Management

- **Save Character:** Use File → Save to save your character as a JSON file
- **Load Character:** Use File → Load to load a previously saved character
- **Print Character:** Use File → Print to export your character sheet as a PDF
- **Reset Character:** Use File → Reset to start with a fresh character

## Dependencies

- Python 3.8+
- tkinter (GUI framework)
- reportlab (PDF generation)
- pillow (Image processing for reportlab)

