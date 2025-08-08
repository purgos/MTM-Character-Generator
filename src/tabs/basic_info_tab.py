import tkinter as tk
from tkinter import ttk
import re
# Robust import for MAGIC_ITEMS to support running this file directly or via package
try:
    from magic_items import MAGIC_ITEMS  # when src/ is on sys.path
except ModuleNotFoundError:
    try:
        from ..magic_items import MAGIC_ITEMS  # when using package relative import
    except Exception:
        import os, sys as _sys
        _base_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
        if _base_dir not in _sys.path:
            _sys.path.insert(0, _base_dir)
        from magic_items import MAGIC_ITEMS

class BasicInfoTab:
    CUSTOM_ITEM_LABEL = 'Custom Item...'
    CUSTOM_PROFESSION_LABEL = 'Custom Profession...'
    PROFESSION_OPTIONS = [
        'Alchemist', 'Architect', 'Armorsmith', 'Barrister', 'Basketweaver', 'Blacksmith',
        'Boatman/Sailor', 'Bookbinder', 'Bookkeeper', 'Bowyer/Fletcher', 'Brewer',
        'Calligrapher', 'Carpenter', 'Cobbler', 'Cook', 'Driver', 'Engineer', 'Farmer',
        'Fisherman', 'Forgerer/Scribe', 'Gambler', 'Gardener', 'Gemcutter', 'Guide',
        'Herder', 'Historian', 'Hunter', 'Leatherworker', 'Lip Reader', 'Lumberjack',
        'Miller', 'Miner', 'Musician', 'Naturalist/Survivalist', 'Painter', 'Potter',
        'Rancher', 'Sculptor', 'Shipbuilder', 'Stablehand', 'Stonemason',
        'Street Performer (Actor, Dancer, Singer, etc)', 'Tanner', 'Taxidermist',
        'Weaponsmith', 'Weaver', 'Writer'
    ]
    def __init__(self, parent, character_data, type_callback=None, gear_die_tab=None):
        self.parent = parent
        self.character_data = character_data
        self.type_callback = type_callback
        self.gear_die_tab = gear_die_tab
        self.tab = ttk.Frame(parent)
        # Provide instance attribute for MAGIC_ITEMS
        self.MAGIC_ITEMS = MAGIC_ITEMS
        # Guard for preventing duplicate custom item dialogs
        self._custom_item_dialog = None
        # Guard for preventing duplicate custom profession dialog
        self._custom_profession_dialog = None
        self.create_tab()
        
    def on_magic_item_selected(self, event=None):
        # Sync from listbox selection if event originated there
        if event and hasattr(event, 'widget') and event.widget is getattr(self, 'magic_items_listbox', None):
            sel = self.magic_items_listbox.curselection()
            if sel:
                idx = sel[0]
                if 0 <= idx < len(self.selected_magic_items):
                    self.magic_item_var.set(self.selected_magic_items[idx]['name'])
        item_name = self.magic_item_var.get() if hasattr(self, 'magic_item_var') else ''
        if not item_name:
            if hasattr(self, 'update_use_charge_state'):
                self.update_use_charge_state()
            return
        if item_name == self.CUSTOM_ITEM_LABEL:
            if hasattr(self, 'open_custom_item_dialog'):
                self.open_custom_item_dialog()
            return
        item_data = self.magic_item_lookup.get(item_name, {}) if hasattr(self, 'magic_item_lookup') else {}
        # Variants handling
        if hasattr(self, 'variant_combo') and hasattr(self, 'variant_var'):
            if 'variants' in item_data:
                self.variant_combo['values'] = item_data['variants']
                current_variant = self.variant_var.get()
                if current_variant not in item_data['variants']:
                    self.variant_combo.set(item_data['variants'][0])
            else:
                self.variant_combo['values'] = []
                self.variant_combo.set('')
        # Charges default
        if hasattr(self, 'charges_var'):
            if 'charges' in item_data:
                self.charges_var.set(str(item_data['charges']))
            else:
                self.charges_var.set('')
        if hasattr(self, 'update_magic_item_description'):
            self.update_magic_item_description(item_data)
        if hasattr(self, 'update_use_charge_state'):
            self.update_use_charge_state()

    def sanitize_item_name(self, name: str) -> str:
        if not name:
            return name
        # Remove common apostrophe-like characters
        name = re.sub(r"[\u2018\u2019\u02BC\u2032`']", "", name)
        # Collapse multiple whitespace into single spaces
        name = re.sub(r"\s+", " ", name).strip()
        return name

    def sanitize_text(self, text: str) -> str:
        if not text:
            return text
        text = re.sub(r"[\u2018\u2019\u02BC\u2032`']", "", text)
        text = re.sub(r"\s+", " ", text)
        return text.strip()

    def create_tab(self):
        """Create the basic info tab with character information and dice roller"""
        # Main container frame
        main_frame = ttk.Frame(self.tab)
        main_frame.pack(fill='both', expand=True, padx=5, pady=5)

        # Left side frame for character info
        left_frame = ttk.Frame(main_frame)
        left_frame.pack(side='left', fill='both', expand=True, padx=5, pady=5)

        # Basic Info Frame
        frame = ttk.LabelFrame(left_frame, text="Character Information")
        frame.pack(fill='both', expand=True, padx=5, pady=5)

        # Name and Player Name
        ttk.Label(frame, text="Character Name:").grid(row=0, column=0, padx=5, pady=2)
        self.name_entry = ttk.Entry(frame)
        self.name_entry.grid(row=0, column=1, padx=5, pady=2)

        ttk.Label(frame, text="Player Name:").grid(row=1, column=0, padx=5, pady=2)
        self.player_name_entry = ttk.Entry(frame)
        self.player_name_entry.grid(row=1, column=1, padx=5, pady=2)

        # Race Selection
        ttk.Label(frame, text="Race:").grid(row=2, column=0, padx=5, pady=2)
        self.race_var = tk.StringVar()
        self.race_combo = ttk.Combobox(frame, textvariable=self.race_var)
        self.race_combo['values'] = ('Half-Dragon', 'Human', 'Elf', 'Half Elf', 'Galdur', 
                                   'Gnome', 'Halfling', 'Dwarf', 'Minotaur', 'Half Giant')
        self.race_combo.grid(row=2, column=1, padx=5, pady=2)
        
        # Add trace to monitor race changes
        self.race_var.trace_add('write', lambda *args: self.on_race_change())

        # Profession Selection (dropdown with custom option)
        ttk.Label(frame, text="Profession:").grid(row=3, column=0, padx=5, pady=2)
        self.profession_var = tk.StringVar()
        # Sort the profession options alphabetically (case-insensitive), custom option stays on top
        prof_values = [self.CUSTOM_PROFESSION_LABEL] + sorted(self.PROFESSION_OPTIONS, key=str.lower)
        # Compute a width that fits the longest entry (characters), with small padding
        prof_width = max((len(v) for v in prof_values), default=20) + 2
        self.profession_combo = ttk.Combobox(frame, textvariable=self.profession_var, state='readonly', values=prof_values, width=prof_width)
        self.profession_combo.grid(row=3, column=1, padx=5, pady=2)
        self.profession_combo.bind('<<ComboboxSelected>>', self.on_profession_selected)

        # Character Type/Specialization Selection
        ttk.Label(frame, text="Specialization:").grid(row=4, column=0, padx=5, pady=2)
        self.type_var = tk.StringVar(value="Non-Specialized")
        self.type_combo = ttk.Combobox(frame, textvariable=self.type_var, state='readonly')
        self.type_combo['values'] = ('Non-Specialized', 'Specialized Rogue', 'Specialized Warrior Melee',
                                   'Specialized Warrior Ranged', 'Specialized Caster', 'Shield Master')
        self.type_combo.grid(row=4, column=1, padx=5, pady=2)
        
        # Add trace to monitor type changes
        self.type_var.trace_add('write', self.on_type_change)

        # Unarmed Combat Checkbox
        self.unarmed_combat_var = tk.BooleanVar(value=False)
        self.unarmed_combat_check = ttk.Checkbutton(frame, text="Unarmed Combat", 
                                                   variable=self.unarmed_combat_var)
        self.unarmed_combat_check.grid(row=4, column=2, padx=5, pady=2)
        
        # Add trace to monitor unarmed combat changes
        self.unarmed_combat_var.trace_add('write', self.on_unarmed_combat_change)

        # Rank and Rank Points
        rank_frame = ttk.Frame(frame)
        rank_frame.grid(row=5, column=0, columnspan=2, padx=5, pady=2, sticky='w')
        
        ttk.Label(rank_frame, text="Rank:").pack(side='left', padx=5)
        self.rank_var = tk.StringVar(value="1")
        self.rank_label = ttk.Label(rank_frame, textvariable=self.rank_var)
        self.rank_label.pack(side='left', padx=5)
        
        # Add trace to monitor total rank points changes
        self.total_rank_points_var = tk.StringVar(value="0")
        self.total_rank_points_var.trace_add('write', self.update_rank)
        
        # Add trace to monitor rank changes for speed calculation
        self.rank_var.trace_add('write', self.on_rank_change_for_speed)

        # Display total points
        ttk.Label(rank_frame, text="Total Points:").pack(side='left', padx=5)
        self.total_points_label = ttk.Label(rank_frame, textvariable=self.total_rank_points_var)
        self.total_points_label.pack(side='left', padx=5)
        
        # Display current rank points (modulo 25)
        ttk.Label(rank_frame, text="Current Rank Points:").pack(side='left', padx=5)
        self.current_rank_points_var = tk.StringVar(value="0")
        self.current_rank_points_label = ttk.Label(rank_frame, textvariable=self.current_rank_points_var)
        self.current_rank_points_label.pack(side='left', padx=5)
        
        # Add points frame
        add_points_frame = ttk.Frame(rank_frame)
        add_points_frame.pack(side='left', padx=5)
        
        ttk.Label(add_points_frame, text="Add Points:").pack(side='left', padx=5)
        self.add_points_var = tk.StringVar(value="0")
        self.add_points_entry = ttk.Entry(add_points_frame, textvariable=self.add_points_var, width=5)
        self.add_points_entry.pack(side='left', padx=5)
        
        add_button = ttk.Button(add_points_frame, text="Add", command=self.add_rank_points)
        add_button.pack(side='left', padx=5)

        # Magic Items + Description Bottom Frame
        bottom_frame = ttk.Frame(self.tab)
        bottom_frame.pack(side='bottom', fill='x', padx=5, pady=5)

        # Magic Items Frame now on the left
        magic_items_frame = ttk.LabelFrame(bottom_frame, text="Magic Items")
        magic_items_frame.pack(side='left', fill='y', padx=5, pady=5)

        # Description frame now on the right
        desc_frame = ttk.LabelFrame(bottom_frame, text="Magic Item Description")
        desc_frame.pack(side='right', fill='both', expand=True, padx=5, pady=5)
        self.magic_item_description_text = tk.Text(desc_frame, wrap='word', height=10, width=80, state='disabled')
        self.magic_item_description_text.pack(fill='both', expand=True, padx=5, pady=5)

        # Dropdown for selecting magic item
        self.magic_item_var = tk.StringVar()
        # Build list from each item's internal 'name' field (fallback to key) and create lookup
        all_items = []
        self.magic_item_lookup = {}
        for group, group_dict in self.MAGIC_ITEMS.items():
            for key, item_data in group_dict.items():
                raw_name = item_data.get('name', key)
                display_name = self.sanitize_item_name(raw_name)
                if display_name not in self.magic_item_lookup:  # avoid duplicates
                    # Store cleaned name inside a shallow copy to preserve description etc.
                    stored = dict(item_data)
                    stored['name'] = display_name
                    if 'description' in stored:
                        stored['description'] = self.sanitize_text(stored['description'])
                    self.magic_item_lookup[display_name] = stored
                    all_items.append(display_name)
        # Prepend custom item label
        values_list = [self.CUSTOM_ITEM_LABEL] + sorted(all_items)
        self.magic_item_combo = ttk.Combobox(magic_items_frame, textvariable=self.magic_item_var, values=values_list, state='readonly', width=40)
        self.magic_item_combo.pack(padx=5, pady=2)
        self.magic_item_combo.bind('<<ComboboxSelected>>', self.on_magic_item_selected)  # unchanged binding

        # Variant selection and charges input
        self.variant_var = tk.StringVar()
        self.variant_combo = ttk.Combobox(magic_items_frame, textvariable=self.variant_var, state='readonly', width=10)
        self.variant_combo.pack(padx=5, pady=2)
        self.charges_var = tk.StringVar(value="")
        self.charges_entry = ttk.Entry(magic_items_frame, textvariable=self.charges_var, width=5)
        self.charges_entry.pack(padx=5, pady=2)

        # Add button
        self.add_magic_item_btn = ttk.Button(magic_items_frame, text="Add Item", command=self.add_magic_item)
        self.add_magic_item_btn.pack(padx=5, pady=2)

        # Listbox for selected items
        self.selected_magic_items = []
        self.magic_items_listbox = tk.Listbox(magic_items_frame, height=7, width=60)
        self.magic_items_listbox.pack(padx=5, pady=2)
        # Correct the binding to use the existing handler name
        self.magic_items_listbox.bind('<<ListboxSelect>>', self.on_magic_item_selected)

        # Remove button
        self.remove_magic_item_btn = ttk.Button(magic_items_frame, text="Remove Item", command=self.remove_magic_item)
        self.remove_magic_item_btn.pack(padx=5, pady=2)
        # Use Charge button
        self.use_charge_btn = ttk.Button(magic_items_frame, text="Use Charge", command=self.use_magic_item_charge)
        self.use_charge_btn.pack(padx=5, pady=2)
        # Recharge buttons
        self.recharge_item_btn = ttk.Button(magic_items_frame, text="Recharge Item", command=self.recharge_magic_item)
        self.recharge_item_btn.pack(padx=5, pady=2)

        # Combat Stats Frame
        combat_frame = ttk.LabelFrame(frame, text="Combat Statistics")
        combat_frame.grid(row=7, column=0, columnspan=2, padx=5, pady=5, sticky='ew')

        # Current / Max HP with step controls and Heal Full button
        ttk.Label(combat_frame, text="Current HP:").grid(row=0, column=0, padx=5, pady=2)
        hp_ctrl = ttk.Frame(combat_frame)
        hp_ctrl.grid(row=0, column=1, padx=5, pady=2, sticky='w')
        self.current_hp_var = tk.IntVar(value=0)
        # Default HP step to 0 (treated as 1 when applied)
        self.hp_step_var = tk.IntVar(value=0)
        # Non-editable current HP display placed before controls
        self.current_hp_label = ttk.Label(hp_ctrl, textvariable=self.current_hp_var, width=6, anchor='e')
        self.current_hp_label.pack(side='left', padx=(0, 6))
        # Buttons and step entry to modify current HP
        ttk.Button(hp_ctrl, text="-", width=2,
                   command=lambda: self._apply_step_and_reset(self.current_hp_var, self.hp_step_var, -1)).pack(side='left')
        self.hp_step_entry = ttk.Entry(
            hp_ctrl,
            textvariable=self.hp_step_var,
            width=6,
            validate='key',
            validatecommand=(self.tab.register(self._validate_nonnegative_int), '%P')
        )
        self.hp_step_entry.pack(side='left', padx=3)
        ttk.Button(hp_ctrl, text="+", width=2,
                   command=lambda: self._apply_step_and_reset(self.current_hp_var, self.hp_step_var, +1)).pack(side='left')

        ttk.Label(combat_frame, text="/").grid(row=0, column=2, padx=5, pady=2)
        ttk.Label(combat_frame, text="Max HP:").grid(row=0, column=3, padx=5, pady=2)
        self.max_hp_entry = ttk.Entry(combat_frame)
        self.max_hp_entry.grid(row=0, column=4, padx=5, pady=2)
        ttk.Button(combat_frame, text="Heal Full", command=self.heal_to_full).grid(row=0, column=5, padx=5, pady=2)

        # Indoor Speed
        ttk.Label(combat_frame, text="Indoor Speed:").grid(row=1, column=0, padx=5, pady=2)
        self.indoor_speed_label = ttk.Label(combat_frame, text="30 feet")
        self.indoor_speed_label.grid(row=1, column=1, padx=5, pady=2)
        
        # Outside Speed (calculated)
        ttk.Label(combat_frame, text="Outside Speed:").grid(row=1, column=2, padx=5, pady=2)
        self.outside_speed_label = ttk.Label(combat_frame, text="60 feet")
        self.outside_speed_label.grid(row=1, column=3, padx=5, pady=2)

        # Initiative
        ttk.Label(combat_frame, text="Initiative:").grid(row=2, column=0, padx=5, pady=2)
        self.initiative_label = ttk.Label(combat_frame, text="+0")
        self.initiative_label.grid(row=2, column=1, padx=5, pady=2)

        # Hero Points (integer entry with +/-)
        ttk.Label(combat_frame, text="Hero Points:").grid(row=3, column=0, padx=5, pady=2)
        hp_ctrl = ttk.Frame(combat_frame)
        hp_ctrl.grid(row=3, column=1, padx=5, pady=2, sticky='w')
        self.hero_points_var = tk.IntVar(value=0)
        ttk.Button(hp_ctrl, text="-", width=2, command=lambda: self._inc_var(self.hero_points_var, -1)).pack(side='left')
        self.hero_points_entry = ttk.Entry(
            hp_ctrl,
            textvariable=self.hero_points_var,
            width=6,
            validate='key',
            validatecommand=(self.tab.register(self._validate_nonnegative_int), '%P')
        )
        self.hero_points_entry.pack(side='left', padx=3)
        ttk.Button(hp_ctrl, text="+", width=2, command=lambda: self._inc_var(self.hero_points_var, +1)).pack(side='left')

        # Resources
        resources_frame = ttk.LabelFrame(frame, text="Resources")
        resources_frame.grid(row=8, column=0, columnspan=2, padx=5, pady=5, sticky='ew')

        ttk.Label(resources_frame, text="Gold:").grid(row=0, column=0, padx=5, pady=2)
        money_ctrl = ttk.Frame(resources_frame)
        money_ctrl.grid(row=0, column=1, padx=5, pady=2, sticky='w')
        self.money_var = tk.IntVar(value=50)
        # Non-editable display for current Gold value
        self.money_label = ttk.Label(money_ctrl, textvariable=self.money_var, width=8, anchor='e')
        self.money_label.pack(side='left', padx=(0, 6))
        # Step controls for add/subtract (default visually 0 and reset after use)
        self.money_step_var = tk.IntVar(value=0)
        ttk.Button(money_ctrl, text="-", width=2,
                   command=lambda: self._apply_step_and_reset(self.money_var, self.money_step_var, -1)).pack(side='left')
        self.money_step_entry = ttk.Entry(
            money_ctrl,
            textvariable=self.money_step_var,
            width=6,
            validate='key',
            validatecommand=(self.tab.register(self._validate_nonnegative_int), '%P')
        )
        self.money_step_entry.pack(side='left', padx=3)
        ttk.Button(money_ctrl, text="+", width=2,
                   command=lambda: self._apply_step_and_reset(self.money_var, self.money_step_var, +1)).pack(side='left')

        ttk.Label(resources_frame, text="Magic Dust:").grid(row=1, column=0, padx=5, pady=2)
        dust_ctrl = ttk.Frame(resources_frame)
        dust_ctrl.grid(row=1, column=1, padx=5, pady=2, sticky='w')
        self.magic_dust_var = tk.IntVar(value=0)
        # Non-editable display for current Magic Dust value
        self.magic_dust_label = ttk.Label(dust_ctrl, textvariable=self.magic_dust_var, width=8, anchor='e')
        self.magic_dust_label.pack(side='left', padx=(0, 6))
        # Step controls for add/subtract (default visually 0 and reset after use)
        self.magic_dust_step_var = tk.IntVar(value=0)
        ttk.Button(dust_ctrl, text="-", width=2,
                   command=lambda: self._apply_step_and_reset(self.magic_dust_var, self.magic_dust_step_var, -1)).pack(side='left')
        self.magic_dust_step_entry = ttk.Entry(
            dust_ctrl,
            textvariable=self.magic_dust_step_var,
            width=6,
            validate='key',
            validatecommand=(self.tab.register(self._validate_nonnegative_int), '%P')
        )
        self.magic_dust_step_entry.pack(side='left', padx=3)
        ttk.Button(dust_ctrl, text="+", width=2,
                   command=lambda: self._apply_step_and_reset(self.magic_dust_var, self.magic_dust_step_var, +1)).pack(side='left')

        # Initialize initiative display
        self.update_initiative_display()

    def calculate_max_hp(self):
        """Calculate max HP based on race, rank, and gear die allocations.
        New base HP formulas by race:
        - Human / Half-Dragon: 11 + 7 * rank
        - Elf / Half Elf / Galdur / Gnome / Halfling: 10 + 5 * rank
        - Dwarf / Minotaur: 12 + 8 * rank
        - Half Giant: 15 + 10 * rank
        """
        try:
            rank = int(self.rank_var.get())
        except Exception:
            rank = 1
        race = (self.race_var.get() or '').strip()
        race_key = race.lower()

        group_a = {"human", "half-dragon"}
        group_b = {"elf", "half elf", "galdur", "gnome", "halfling"}
        group_c = {"dwarf", "minotaur"}
        group_d = {"half giant"}

        if race_key in group_a:
            base_hp = 11 + 7 * rank
        elif race_key in group_b:
            base_hp = 10 + 5 * rank
        elif race_key in group_c:
            base_hp = 12 + 8 * rank
        elif race_key in group_d:
            base_hp = 15 + 10 * rank
        else:
            # Sensible default if race isn't selected or unrecognized
            base_hp = 10 + 5 * rank

        max_hp = base_hp

        # Add gear die hitpoints if gear die tab is available
        if hasattr(self, 'gear_die_tab') and self.gear_die_tab:
            try:
                gear_die_hp = self.gear_die_tab.calculate_gear_die_hitpoints()
                max_hp += gear_die_hp
            except Exception:
                pass
        return max_hp

    def update_rank(self, *args):
        """Update rank based on total points"""
        try:
            total_points = int(self.total_rank_points_var.get())
            rank = min(12, 1 + (total_points // 25))  # 25 points per rank
            self.rank_var.set(str(rank))
            
            # Update max HP
            self.update_max_hp_display()
            
            # Update current rank points (modulo 25)
            current_rank_points = total_points % 25
            self.current_rank_points_var.set(str(current_rank_points))
            
        except ValueError:
            pass

    def add_rank_points(self):
        """Add points to total rank points"""
        try:
            current_total = int(self.total_rank_points_var.get())
            points_to_add = int(self.add_points_var.get())
            new_total = current_total + points_to_add
            print(f"Adding {points_to_add} points to {current_total} = {new_total}")
            self.total_rank_points_var.set(str(new_total))
            self.add_points_var.set("0")
            print(f"Total points after update: {self.total_rank_points_var.get()}")
        except ValueError as e:
            print(f"Error adding rank points: {e}")
            pass

    def on_race_change(self):
        """Handle race change - update max HP"""
        self.update_max_hp_display()
    
    def update_max_hp_display(self):
        """Update the max HP display with current calculation, and default current HP to max on first calc."""
        max_hp = self.calculate_max_hp()
        self.max_hp_entry.delete(0, tk.END)
        self.max_hp_entry.insert(0, str(max_hp))
        # Initialize or clamp current HP
        try:
            cur = int(self.current_hp_var.get()) if hasattr(self, 'current_hp_var') else 0
        except Exception:
            cur = 0
        if not getattr(self, '_hp_initialized', False):
            if hasattr(self, 'current_hp_var'):
                self.current_hp_var.set(max_hp)
            self._hp_initialized = True
        else:
            if hasattr(self, 'current_hp_var') and cur > max_hp:
                self.current_hp_var.set(max_hp)

    def heal_to_full(self):
        """Set current HP to the latest Max HP."""
        # Ensure max HP is up to date
        self.update_max_hp_display()
        try:
            max_hp = int(self.max_hp_entry.get() or 0)
        except Exception:
            max_hp = self.calculate_max_hp()
        if hasattr(self, 'current_hp_var'):
            self.current_hp_var.set(max_hp)

    def on_type_change(self, *args):
        """Handle type change - call the callback if it exists"""
        if self.type_callback:
            self.type_callback(self.type_var.get())

    def on_unarmed_combat_change(self, *args):
        """Handle unarmed combat change - update indoor speed and initiative"""
        self.calculate_indoor_speed()
        self.update_initiative_display()

    def on_rank_change_for_speed(self, *args):
        """Handle rank change - update indoor speed and initiative"""
        self.calculate_indoor_speed()
        self.update_initiative_display()


    def get_data(self):
        """Get all data from the tab"""
        rank = int(self.rank_var.get())
        unarmed_combat = self.unarmed_combat_var.get()
        if unarmed_combat:
            indoor_speed = 35 + (5 * rank)
        else:
            indoor_speed = 30
        # Prepare magic items data
        magic_items_export = []
        for item in self.selected_magic_items:
            exported = {'name': self.sanitize_item_name(item['name'])}
            if item.get('variant'):
                exported['variant'] = item['variant']
            if 'current_charges' in item and 'max_charges' in item:
                exported['current_charges'] = item['current_charges']
                exported['max_charges'] = item['max_charges']
            if 'charges_note' in item:
                exported['charges_note'] = item['charges_note']
            if 'description' in item:
                exported['description'] = self.sanitize_text(item['description'])
            magic_items_export.append(exported)
        return {
            'name': self.name_entry.get(),
            'playerName': self.player_name_entry.get(),
            'race': self.race_var.get(),
            'profession': self.profession_var.get(),
            'type': self.type_var.get(),
            'unarmedCombat': self.unarmed_combat_var.get(),
            'rank': int(self.rank_var.get()),
            'rankPoints': int(self.total_rank_points_var.get()),
            'magicItems': magic_items_export,
            'combatStats': {
                'hp': self._get_int(self.current_hp_var),
                'maxHp': int(self.max_hp_entry.get() or 0),
                'indoorSpeed': indoor_speed,
                'initiative': self.calculate_initiative(),
                'heroPoints': self._get_int(self.hero_points_var)
            },
            'resources': {
                'money': self._get_int(self.money_var),
                'magicDust': self._get_int(self.magic_dust_var)
            }
        }

    def set_data(self, data):
        """Set data in the tab"""
        self.name_entry.delete(0, tk.END)
        self.name_entry.insert(0, data.get('name', ''))
        
        self.player_name_entry.delete(0, tk.END)
        self.player_name_entry.insert(0, data.get('playerName', ''))
        
        self.race_var.set(data.get('race', ''))
        
        # Profession: set var, and add to values if not present (keep list alphabetically sorted)
        saved_prof = data.get('profession', '')
        current_vals = list(self.profession_combo['values']) if hasattr(self, 'profession_combo') else []
        if saved_prof:
            base = [v for v in current_vals if v and v != self.CUSTOM_PROFESSION_LABEL]
            if saved_prof not in base:
                base.append(saved_prof)
            new_vals = [self.CUSTOM_PROFESSION_LABEL] + sorted(base, key=str.lower)
            self.profession_combo['values'] = new_vals
            # Recompute width to accommodate any longer custom value
            try:
                new_width = max((len(v) for v in new_vals), default=20) + 2
                self.profession_combo.config(width=new_width)
            except Exception:
                pass
        self.profession_var.set(saved_prof)
        
        self.type_var.set(data.get('type', 'Non-Specialized'))
        
        self.unarmed_combat_var.set(data.get('unarmedCombat', False))
        
        self.total_rank_points_var.set(str(data.get('rankPoints', 0)))
        
        # Calculate and display indoor speed based on loaded data
        self.calculate_indoor_speed()
        
        # Set magic items
        magic_items = data.get('magicItems', [])
        self.selected_magic_items = []
        for saved in magic_items:
            item_entry = {'name': self.sanitize_item_name(saved.get('name',''))}
            if saved.get('variant'):
                item_entry['variant'] = saved['variant']
            if 'current_charges' in saved and 'max_charges' in saved:
                item_entry['current_charges'] = saved['current_charges']
                item_entry['max_charges'] = saved['max_charges']
            if 'charges_note' in saved:
                item_entry['charges_note'] = saved['charges_note']
            if 'description' in saved and saved['description']:
                clean_desc = self.sanitize_text(saved['description'])
                item_entry['description'] = clean_desc
                if saved.get('name') and item_entry['name'] not in self.magic_item_lookup:
                    self.magic_item_lookup[item_entry['name']] = {
                        'name': item_entry['name'],
                        'description': clean_desc
                    }
            self.selected_magic_items.append(item_entry)
        self.refresh_magic_items_listbox()
        
        # Set combat stats
        combat_stats = data.get('combatStats', {})
        # Current HP via IntVar (default to calculated max if not provided)
        try:
            saved_hp = int(combat_stats.get('hp', 0))
        except Exception:
            saved_hp = 0
        calc_max = self.calculate_max_hp()
        if saved_hp > 0:
            self.current_hp_var.set(saved_hp)
            self._hp_initialized = True
        else:
            self.current_hp_var.set(calc_max)
            self._hp_initialized = True
        
        # Max HP entry uses saved if provided, else calculate
        self.max_hp_entry.delete(0, tk.END)
        try:
            saved_max = int(combat_stats.get('maxHp', 0))
        except Exception:
            saved_max = 0
        self.max_hp_entry.insert(0, str(saved_max if saved_max > 0 else calc_max))
        
        # Initiative is calculated automatically, so we just update the display
        self.update_initiative_display()
        
        # Hero Points via IntVar
        try:
            self.hero_points_var.set(int(combat_stats.get('heroPoints', 0)))
        except Exception:
            self.hero_points_var.set(0)
        
        # Set resources via IntVars
        resources = data.get('resources', {})
        try:
            self.money_var.set(int(resources.get('money', 0)))
        except Exception:
            self.money_var.set(0)
        try:
            self.magic_dust_var.set(int(resources.get('magicDust', 0)))
        except Exception:
            self.magic_dust_var.set(0)

    def lock_fields(self):
        """Disable editing of key character info fields."""
        try:
            self.name_entry.config(state='disabled')
            self.player_name_entry.config(state='disabled')
            self.race_combo.config(state='disabled')
            self.profession_combo.config(state='disabled')
            self.type_combo.config(state='disabled')
            self.unarmed_combat_check.config(state='disabled')
        except Exception as e:
            print(f"Error locking fields: {e}")

    def unlock_fields(self):
        """Enable editing of key character info fields."""
        try:
            self.name_entry.config(state='normal')
            self.player_name_entry.config(state='normal')
            self.race_combo.config(state='readonly')
            self.profession_combo.config(state='readonly')
            self.profession_combo.configure(state='readonly')
            self.type_combo.config(state='readonly')
            self.unarmed_combat_check.config(state='normal')
        except Exception as e:
            print(f"Error unlocking fields: {e}")

    def calculate_indoor_speed(self):
        """Calculate indoor speed based on unarmed combat and rank"""
        rank = int(self.rank_var.get())
        unarmed_combat = self.unarmed_combat_var.get()
        
        if unarmed_combat:
            speed = 35 + (5 * rank)
        else:
            speed = 30
        
        # Update the label text directly
        self.indoor_speed_label.config(text=f"{speed} feet")
        
        # Update outside speed as well (2 * indoor speed)
        self.outside_speed_label.config(text=f"{speed * 2} feet")
    
    def calculate_initiative(self):
        """Calculate initiative based on unarmed combat and rank"""
        current_rank = int(self.rank_var.get())
        unarmed_combat = self.unarmed_combat_var.get()
        
        # Initiative is +0 by default
        initiative = 0
        
        # If unarmed combat is selected, add +1 for every odd level attained
        if unarmed_combat:
            # Count odd levels from 1 to current rank
            for level in range(1, current_rank + 1):
                if level % 2 == 1:  # Odd level
                    initiative += 1
        
        return initiative
    
    def update_initiative_display(self):
        """Update the initiative display"""
        initiative = self.calculate_initiative()
        self.initiative_label.config(text=f"+{initiative}")
        
        # Also update character data
        self.character_data['combatStats']['initiative'] = initiative
        
        print(f"[DEBUG] Initiative calculated: rank={int(self.rank_var.get())}, unarmed={self.unarmed_combat_var.get()}, initiative={initiative}")

    def update_magic_item_description(self, item_data):
        """Populate the description text widget with the selected item's info."""
        if not hasattr(self, 'magic_item_description_text'):
            return
        self.magic_item_description_text.config(state='normal')
        self.magic_item_description_text.delete('1.0', tk.END)
        if item_data:
            desc = self.sanitize_text(item_data.get('description', '(No description available)'))
            if 'variants' in item_data:
                desc += "\n\nVariants: " + ", ".join(item_data['variants'])
            if 'charges' in item_data:
                desc += f"\nDefault Charges: {item_data['charges']}"
        else:
            desc = "Select a magic item to view its description."
        desc = re.sub(r"\s+", " ", desc).strip()
        self.magic_item_description_text.insert('1.0', desc)
        self.magic_item_description_text.config(state='disabled')

    def open_custom_item_dialog(self):
        # If a dialog is already open, just focus it
        try:
            if self._custom_item_dialog is not None and self._custom_item_dialog.winfo_exists():
                self._custom_item_dialog.lift()
                self._custom_item_dialog.focus_set()
                return
        except Exception:
            self._custom_item_dialog = None
        dialog = tk.Toplevel(self.tab)
        self._custom_item_dialog = dialog
        dialog.title('Create Custom Magic Item')
        dialog.transient(self.tab)
        dialog.grab_set()

        tk.Label(dialog, text='Name:').grid(row=0, column=0, sticky='e', padx=5, pady=5)
        name_var = tk.StringVar()
        name_entry = ttk.Entry(dialog, textvariable=name_var, width=40)
        name_entry.grid(row=0, column=1, padx=5, pady=5)

        tk.Label(dialog, text='Max Charges (optional):').grid(row=1, column=0, sticky='e', padx=5, pady=5)
        charges_var = tk.StringVar()
        charges_entry = ttk.Entry(dialog, textvariable=charges_var, width=10)
        charges_entry.grid(row=1, column=1, sticky='w', padx=5, pady=5)

        tk.Label(dialog, text='Description:').grid(row=2, column=0, sticky='ne', padx=5, pady=5)
        desc_text = tk.Text(dialog, width=50, height=10, wrap='word')
        desc_text.grid(row=2, column=1, padx=5, pady=5)

        button_frame = ttk.Frame(dialog)
        button_frame.grid(row=3, column=0, columnspan=2, pady=10)

        def close_dialog():
            try:
                dialog.destroy()
            finally:
                self._custom_item_dialog = None

        def confirm():
            name = self.sanitize_item_name(name_var.get().strip())
            if not name:
                close_dialog()
                return
            if name in self.magic_item_lookup:
                # Prevent overwriting existing items
                close_dialog()
                return
            description = self.sanitize_text(desc_text.get('1.0', tk.END).strip())
            charges_input = charges_var.get().strip()
            item_def = {'name': name, 'description': description}
            if charges_input:
                try:
                    ch = int(charges_input)
                    item_def['charges'] = ch
                except ValueError:
                    pass
            self.magic_item_lookup[name] = item_def
            # Update combobox values keeping custom label at top
            current_vals = list(self.magic_item_combo['values'])
            if name not in current_vals:
                base = [v for v in current_vals if v not in (self.CUSTOM_ITEM_LABEL, name) and v]
                self.magic_item_combo['values'] = [self.CUSTOM_ITEM_LABEL] + sorted(base + [name])
            self.magic_item_var.set(name)
            # Set charges entry for add_magic_item to pick up
            if 'charges' in item_def:
                self.charges_var.set(str(item_def['charges']))
            else:
                self.charges_var.set('')
            self.variant_combo['values'] = []
            self.variant_var.set('')
            self.update_magic_item_description(item_def)
            close_dialog()

        ttk.Button(button_frame, text='Add Item', command=confirm).pack(side='left', padx=5)
        ttk.Button(button_frame, text='Cancel', command=close_dialog).pack(side='left', padx=5)
        dialog.protocol("WM_DELETE_WINDOW", close_dialog)
        name_entry.focus_set()

    def on_profession_selected(self, event=None):
        """Handle profession selection; open custom dialog if needed."""
        choice = self.profession_var.get()
        if choice == self.CUSTOM_PROFESSION_LABEL:
            self.open_custom_profession_dialog()

    def open_custom_profession_dialog(self):
        # Prevent duplicates
        try:
            if self._custom_profession_dialog is not None and self._custom_profession_dialog.winfo_exists():
                self._custom_profession_dialog.lift()
                self._custom_profession_dialog.focus_set()
                return
        except Exception:
            self._custom_profession_dialog = None
        dialog = tk.Toplevel(self.tab)
        self._custom_profession_dialog = dialog
        dialog.title('Add Custom Profession')
        dialog.transient(self.tab)
        dialog.grab_set()

        ttk.Label(dialog, text='Profession Name:').grid(row=0, column=0, padx=8, pady=8, sticky='e')
        name_var = tk.StringVar()
        name_entry = ttk.Entry(dialog, textvariable=name_var, width=32)
        name_entry.grid(row=0, column=1, padx=8, pady=8, sticky='w')

        btns = ttk.Frame(dialog)
        btns.grid(row=1, column=0, columnspan=2, pady=8)

        def close_dialog():
            try:
                dialog.destroy()
            except Exception:
                pass
            finally:
                self._custom_profession_dialog = None

        def confirm():
            raw = name_var.get().strip()
            name = self.sanitize_item_name(raw)
            if not name:
                close_dialog()
                return
            # Add to combobox values keeping alphabetical order (case-insensitive)
            current_vals = list(self.profession_combo['values'])
            base = [v for v in current_vals if v and v != self.CUSTOM_PROFESSION_LABEL]
            if name not in base:
                base.append(name)
            new_vals = [self.CUSTOM_PROFESSION_LABEL] + sorted(base, key=str.lower)
            self.profession_combo['values'] = new_vals
            # Recompute width to accommodate potentially longer custom value
            try:
                new_width = max((len(v) for v in new_vals), default=20) + 2
                self.profession_combo.config(width=new_width)
            except Exception:
                pass
            self.profession_var.set(name)
            close_dialog()

        ttk.Button(btns, text='Add', command=confirm).pack(side='left', padx=6)
        ttk.Button(btns, text='Cancel', command=close_dialog).pack(side='left', padx=6)
        dialog.protocol("WM_DELETE_WINDOW", close_dialog)
        name_entry.focus_set()

    def refresh_magic_items_listbox(self):
        """Refresh listbox display of selected magic items."""
        if not hasattr(self, 'magic_items_listbox'):
            return
        self.magic_items_listbox.delete(0, tk.END)
        for item in self.selected_magic_items:
            parts = [item.get('name', '')]
            if item.get('variant'):
                parts.append(f"({item['variant']})")
            if 'current_charges' in item and 'max_charges' in item:
                parts.append(f"Charges {item['current_charges']}/{item['max_charges']}")
            elif 'charges_note' in item:
                parts.append(item['charges_note'])
            display = ' - '.join([p for p in parts if p])
            self.magic_items_listbox.insert(tk.END, display)
        self.update_use_charge_state()

    # --- Missing methods re-added ---
    def update_use_charge_state(self, event=None):
        if not hasattr(self, 'magic_items_listbox'):
            return
        selection = self.magic_items_listbox.curselection()
        # Safely disable if buttons exist
        def disable(btn):
            try:
                btn.state(['disabled'])
            except Exception:
                btn.configure(state='disabled')
        def enable(btn):
            try:
                btn.state(['!disabled'])
            except Exception:
                btn.configure(state='normal')
        if not selection:
            if hasattr(self, 'use_charge_btn'): disable(self.use_charge_btn)
            if hasattr(self, 'recharge_item_btn'): disable(self.recharge_item_btn)
            return
        idx = selection[0]
        if idx >= len(self.selected_magic_items):
            if hasattr(self, 'use_charge_btn'): disable(self.use_charge_btn)
            if hasattr(self, 'recharge_item_btn'): disable(self.recharge_item_btn)
            return
        item = self.selected_magic_items[idx]
        # Use charge enabled only if current_charges > 0
        if 'current_charges' in item and item.get('current_charges', 0) > 0:
            if hasattr(self, 'use_charge_btn'): enable(self.use_charge_btn)
        else:
            if hasattr(self, 'use_charge_btn'): disable(self.use_charge_btn)
        # Recharge enabled if has max and not already full
        if 'current_charges' in item and 'max_charges' in item and item['current_charges'] < item['max_charges']:
            if hasattr(self, 'recharge_item_btn'): enable(self.recharge_item_btn)
        else:
            if hasattr(self, 'recharge_item_btn'): disable(self.recharge_item_btn)

    def use_magic_item_charge(self):
        if not hasattr(self, 'magic_items_listbox'):
            return
        selection = self.magic_items_listbox.curselection()
        if not selection:
            return
        idx = selection[0]
        if idx >= len(self.selected_magic_items):
            return
        item = self.selected_magic_items[idx]
        if 'current_charges' in item and item['current_charges'] > 0:
            item['current_charges'] -= 1
            if item['current_charges'] < 0:
                item['current_charges'] = 0
            self.refresh_magic_items_listbox()
            self.magic_items_listbox.select_set(idx)
            self.magic_items_listbox.event_generate('<<ListboxSelect>>')

    def recharge_magic_item(self):
        if not hasattr(self, 'magic_items_listbox'):
            return
        selection = self.magic_items_listbox.curselection()
        if not selection:
            return
        idx = selection[0]
        if idx >= len(self.selected_magic_items):
            return
        item = self.selected_magic_items[idx]
        if 'current_charges' in item and 'max_charges' in item:
            item['current_charges'] = item['max_charges']
            self.refresh_magic_items_listbox()
            self.magic_items_listbox.select_set(idx)
            self.magic_items_listbox.event_generate('<<ListboxSelect>>')

    def remove_magic_item(self):
        if not hasattr(self, 'magic_items_listbox'):
            return
        selection = self.magic_items_listbox.curselection()
        if not selection:
            return
        idx = selection[0]
        if idx >= len(self.selected_magic_items):
            return
        del self.selected_magic_items[idx]
        self.refresh_magic_items_listbox()
        # Select nearest remaining item
        if self.selected_magic_items:
            new_index = min(idx, len(self.selected_magic_items) - 1)
            self.magic_items_listbox.select_set(new_index)
            self.magic_items_listbox.event_generate('<<ListboxSelect>>')
        else:
            self.update_use_charge_state()

    # --- Newly added methods ---
    def add_magic_item(self):
        """Add the currently selected magic item (or open custom dialog)."""
        if not hasattr(self, 'magic_item_var'):
            return
        name = self.magic_item_var.get().strip()
        if not name:
            return
        if name == self.CUSTOM_ITEM_LABEL:
            self.open_custom_item_dialog()
            return
        item_def = self.magic_item_lookup.get(name)
        if not item_def:
            return
        # Build new entry
        entry = {
            'name': item_def.get('name', name)
        }
        # Variant
        if hasattr(self, 'variant_var'):
            variant = self.variant_var.get().strip()
            if variant:
                entry['variant'] = variant
        # Description
        if 'description' in item_def:
            entry['description'] = self.sanitize_text(item_def['description'])
        # Charges
        max_charges = None
        if hasattr(self, 'charges_var'):
            raw_ch = self.charges_var.get().strip()
            if raw_ch:
                try:
                    max_charges = int(raw_ch)
                except ValueError:
                    max_charges = None
        if max_charges is None and 'charges' in item_def:
            try:
                max_charges = int(item_def['charges'])
            except Exception:
                max_charges = None
        if max_charges is not None:
            entry['max_charges'] = max_charges
            entry['current_charges'] = max_charges
        self.selected_magic_items.append(entry)
        self.refresh_magic_items_listbox()
        # Select the newly added item
        if hasattr(self, 'magic_items_listbox'):
            self.magic_items_listbox.select_clear(0, tk.END)
            self.magic_items_listbox.select_set(tk.END)
            self.magic_items_listbox.event_generate('<<ListboxSelect>>')
        self.update_use_charge_state()

    # --- Helpers for integer fields ---
    def _validate_nonnegative_int(self, proposed: str) -> bool:
        """Allow only empty or non-negative integers in entries."""
        return proposed == '' or proposed.isdigit()

    def _get_int(self, var: tk.Variable) -> int:
        try:
            return int(var.get())
        except Exception:
            return 0

    def _get_step(self, var: tk.Variable) -> int:
        """Return a positive step (defaults to 1 if empty/0)."""
        step = self._get_int(var)
        return step if step > 0 else 1

    def _inc_var(self, var: tk.Variable, delta: int, min_value: int = 0):
        current = self._get_int(var)
        new_val = current + delta
        if new_val < min_value:
            new_val = min_value
        try:
            var.set(new_val)
        except Exception:
            # For safety if var is not an IntVar
            try:
                var.set(int(new_val))
            except Exception:
                pass

    def _apply_step_and_reset(self, target_var: tk.Variable, step_var: tk.Variable, sign: int = 1, min_value: int = 0):
        """Apply +/- using step_var (0/empty treated as 1), then reset step_var to 0."""
        delta = sign * self._get_step(step_var)
        self._inc_var(target_var, delta, min_value=min_value)
        try:
            step_var.set(0)
        except Exception:
            pass
