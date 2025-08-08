# MTM Character Sheet - Modular Version

This is the modular, tab-based MTM Character Sheet app. The UI is split into focused tabs, all sharing a single character_data dictionary for a clean, maintainable design.

## 📁 Project Structure

```
MTM-Character-Generator/
├── requirements.txt
├── README.md
└── src/
    ├── character_sheet_modular.py  # Main application (tabs notebook)
    ├── README_MODULAR.md           # This file
    ├── DAMAGE TABLES.md            # Reference tables (doc only)
    ├── spells.py                   # Reference data
    ├── magic_items.py              # Reference data
    ├── aspect_abilities.py         # Reference data
    └── tabs/
        ├── __init__.py
        ├── basic_info_tab.py       # Character info & core settings
        ├── aspects_tab.py          # Aspect dice (d4…d12), locks, increases
        ├── gear_die_tab.py         # Gear die slots & allocations
        ├── inventory_tab.py        # Inventory management
        ├── abilities_tab.py        # Special abilities
        ├── encyclopedia_tab.py     # Read-only rules/reference browser
        └── dice_roller_tab.py      # Dice roller & saves (history)
```

## 🔧 Modular Architecture

### Main Application (`character_sheet_modular.py`)
- Initializes the main window and the tabbed notebook
- Wires tab-to-tab callbacks (rank updates, aspect changes, HP updates)
- Manages save/load/lock/reset and PDF export (ReportLab)
- Keeps a single source-of-truth `character_data` shared by all tabs

### Tab Modules (`tabs/`)

1) Basic Info Tab (`basic_info_tab.py`)
- Names, race, profession, specialization (type), Unarmed Combat toggle
- Rank and rank point tracking (drives slot/aspect availability)
- Combat stats (HP, initiative, speeds, hero points) and resources
- Exposes variables/callbacks used by other tabs

2) Aspects Tab (`aspects_tab.py`)
- Four aspects: Melee, Ranged, Rogue, Magic
- Die assignment (d4, d6, d8, d10, d12) with computed modifiers
- Locking/unlocking based on specialization choices
- Tracks level-one D12 selection and available die increases by rank
- Applies Unarmed Combat effects when relevant

3) Gear Die Tab (`gear_die_tab.py`)
- Rank-driven gear slot counts and allocation widgets
- Syncs slot changes and can lock allocations (HP/Dodge/Parry, etc.)
- Notifies Basic Info tab to refresh Max HP display

4) Inventory Tab (`inventory_tab.py`)
- Four categories: Stored, Magic, Stored Magic, Elsewhere
- Add/remove/edit with quantities and location tracking

5) Abilities Tab (`abilities_tab.py`)
- Rank-based ability visibility/availability
- Dropdown reacts to which aspect is D12 at level one
- Space for custom/special abilities (e.g., race-based)

6) Encyclopedia Tab (`encyclopedia_tab.py`)
- In-app reference for spells, magic items, aspect abilities, and damage tables
- Read-only documentation; not read by the dice roller for calculations

7) Dice Roller Tab (`dice_roller_tab.py`)
- General dice rolls (die, count, modifier) with advantage/disadvantage
- Quick-roll buttons for aspects; skill checks with profession bonus
- Armor/Dodge saves (melee table), Magic save (spells table)
- Damage helper (normal/critical), result history with rich formatting
- Uses character_data for aspects and relevant bonuses

## 🚀 Benefits of Modular Design

- Maintainable: each feature area is in its own file
- Reusable: easy to extend or swap tabs
- Testable: units can be exercised in isolation
- Parallel-friendly: multiple contributors can work safely

## 🔄 Data Flow

All tabs read/write a shared `character_data` dictionary, e.g.:

```python
{
  'name': str,
  'playerName': str,
  'rank': int,
  'rankPoints': int,
  'race': str,
  'profession': str,
  'type': str,                 # specialization
  'unarmedCombat': bool,
  'aspects': {                 # e.g., {'melee': 'd6', ...}
    'melee': str,
    'ranged': str,
    'rogue': str,
    'magic': str
  },
  'aspectIncreases': {'allowed': int, 'used': int, 'history': dict},
  'levelOneD12Aspect': str|None,
  'gearDieSlots': dict,
  'gearDieAllocations': dict,
  'gearDieEntries': dict,
  'combatStats': dict,
  'resources': dict,
  'magicItems': list,
  'inventory': dict,
  'specialAbilities': dict,
  'selectedAbilities': list
}
```

Note on damage tables: `src/DAMAGE TABLES.md` documents outcomes; the dice roller uses logic in code and does not read the markdown at runtime.

## 🛠️ Usage

Install dependencies and run from the `src/` folder so relative imports work.

```bash
pip install -r requirements.txt
cd MTM-Character-Generator/src
python3 character_sheet_modular.py
```

PDF export uses ReportLab and writes to a user-chosen path via a file dialog.

## 📝 Adding New Tabs

1) Create `src/tabs/new_tab.py` with a class exposing a `.tab` Frame.

```python
class NewTab:
    def __init__(self, parent, character_data):
        self.parent = parent
        self.character_data = character_data
        self.tab = ttk.Frame(parent)
        self._build_ui()

    def _build_ui(self):
        # create UI widgets
        pass
```

2) Import and add it in `create_notebook` (in `character_sheet_modular.py`):

```python
from tabs.new_tab import NewTab

self.new_tab = NewTab(self.notebook, self.character_data)
self.notebook.add(self.new_tab.tab, text="New Tab")
```

3) Optionally export helper methods or callbacks if other tabs need to react.

## 🔧 Dependencies

- tkinter (bundled with Python; on Linux you may need `python3-tk`)
- reportlab (PDF export)

## 📋 Migration Notes

- Dice rolling is now in its own tab (`dice_roller_tab.py`), not in Basic Info
- Two new tabs: Encyclopedia (reference) and Dice Roller (tools & history)
- The damage tables markdown is documentation-only

## 🐛 Troubleshooting

Import errors
- Run the app from `src/` so `tabs/` imports resolve
- Ensure `tabs/__init__.py` exists (it does in this repo)

Missing tkinter
- Linux: `sudo apt install python3-tk`

Missing Python packages
- `pip install -r requirements.txt`