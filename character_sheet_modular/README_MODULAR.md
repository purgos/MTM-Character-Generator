# MTM Character Sheet - Modular Version

This is a refactored version of the MTM Character Sheet application that has been split into modular components for better maintainability and organization.

## 📁 Project Structure

```
mtm-character-sheet-python/
├── src/
│   ├── tabs/
│   │   ├── __init__.py
│   │   ├── basic_info_tab.py      # Character info and dice roller
│   │   ├── aspects_tab.py         # Character aspects management
│   │   ├── gear_die_tab.py        # Gear die slots
│   │   ├── inventory_tab.py       # Inventory management
│   │   └── abilities_tab.py       # Special abilities
│   ├── character_sheet_modular.py # Main application
│   └── MTM-Character-Generator-0.1.py # Original monolithic version
├── requirements.txt
└── README_MODULAR.md
```

## 🔧 Modular Architecture

### Main Application (`character_sheet_modular.py`)
- **Purpose**: Main entry point and coordination
- **Responsibilities**:
  - Initialize the GUI window
  - Create and manage the notebook with tabs
  - Handle file operations (save/load)
  - Coordinate data flow between tabs
  - Generate PDF exports

### Tab Modules (`tabs/`)

#### 1. Basic Info Tab (`basic_info_tab.py`)
- **Purpose**: Character basic information and dice rolling
- **Features**:
  - Character name, player name, race, profession
  - Rank and rank points management
  - Magic items tracking
  - Combat statistics (HP, initiative, hero points)
  - Resources (money, magic dust)
  - Dice roller with history
  - Aspect modifiers for dice rolls

#### 2. Aspects Tab (`aspects_tab.py`)
- **Purpose**: Character aspect management
- **Features**:
  - Four aspects: Melee, Ranged, Rogue, Magic
  - Die type assignment (d4, d6, d8, d10, d12)
  - Modifier calculations
  - Aspect locking system
  - Increase/decrease die value buttons

#### 3. Gear Die Tab (`gear_die_tab.py`)
- **Purpose**: Gear die slot management
- **Features**:
  - Dynamic slot allocation based on rank
  - Text entries for each gear die slot
  - Rank-based slot increases
  - Automatic slot recalculation

#### 4. Inventory Tab (`inventory_tab.py`)
- **Purpose**: Comprehensive inventory management
- **Features**:
  - Four inventory categories: Stored, Magic, Stored Magic, Elsewhere
  - Add/remove items with quantities
  - Location tracking for "elsewhere" items
  - Quantity adjustment controls
  - Edit location functionality

#### 5. Abilities Tab (`abilities_tab.py`)
- **Purpose**: Special abilities management
- **Features**:
  - Rank-based ability visibility
  - Dragon's Breath ability (Half-Dragon race)
  - Dynamic ability scaling with rank
  - Text areas for custom abilities

## 🚀 Benefits of Modular Design

### 1. **Maintainability**
- Each tab is self-contained and easier to modify
- Clear separation of concerns
- Reduced code complexity

### 2. **Reusability**
- Tab modules can be reused in other applications
- Easy to add new tabs or modify existing ones
- Consistent interface across all tabs

### 3. **Testing**
- Individual tabs can be tested in isolation
- Easier to write unit tests for specific functionality
- Better error isolation

### 4. **Development**
- Multiple developers can work on different tabs simultaneously
- Reduced merge conflicts
- Clearer code ownership

## 🔄 Data Flow

### Character Data Structure
All tabs share a common `character_data` dictionary that contains:
```python
{
    'name': str,
    'playerName': str,
    'rank': int,
    'rankPoints': int,
    'race': str,
    'profession': str,
    'aspects': dict,
    'gearDieSlots': dict,
    'gearDieEntries': dict,
    'combatStats': dict,
    'resources': dict,
    'magicItems': list,
    'inventory': dict,
    'specialAbilities': dict
}
```

### Tab Interface
Each tab implements a consistent interface:
- `get_data()`: Returns the tab's data as a dictionary
- `set_data(data)`: Updates the tab with new data
- `create_tab()`: Creates the tab's GUI elements

## 🛠️ Usage

### Running the Modular Version
```bash
cd mtm-character-sheet-python/src
python character_sheet_modular.py
```

### Running the Original Version
```bash
cd mtm-character-sheet-python/src
python MTM-Character-Generator-0.1.py
```

## 📝 Adding New Tabs

To add a new tab:

1. Create a new file in `src/tabs/` (e.g., `new_tab.py`)
2. Implement the tab class with the required interface:
   ```python
   class NewTab:
       def __init__(self, parent, character_data):
           self.parent = parent
           self.character_data = character_data
           self.tab = ttk.Frame(parent)
           self.create_tab()
       
       def create_tab(self):
           # Create GUI elements
           pass
       
       def get_data(self):
           # Return tab data
           pass
       
       def set_data(self, data):
           # Update tab with data
           pass
   ```

3. Import and add the tab in `character_sheet_modular.py`:
   ```python
   from tabs.new_tab import NewTab
   
   # In create_notebook method:
   self.new_tab = NewTab(self.notebook, self.character_data)
   self.notebook.add(self.new_tab.tab, text="New Tab")
   ```

4. Update the `__init__.py` file in the tabs package

## 🔧 Dependencies

The modular version uses the same dependencies as the original:
- `tkinter` (built-in)
- `reportlab` (for PDF generation)
- `json` (built-in)

## 📋 Migration Notes

- The modular version maintains full compatibility with the original
- All functionality has been preserved
- File formats (JSON save/load) are identical
- PDF export functionality is maintained

## 🐛 Troubleshooting

### Import Errors
If you get import errors, make sure:
1. You're running from the correct directory (`src/`)
2. The `tabs/` directory contains `__init__.py`
3. All tab modules are present

### Missing Dependencies
Install required packages:
```bash
pip install reportlab
```

### GUI Issues
- Ensure tkinter is available on your system
- On Linux: `sudo apt install python3-tk`
- On Windows: Usually included with Python installation 
