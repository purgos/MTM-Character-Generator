import tkinter as tk
from tkinter import ttk, messagebox, filedialog
import json
import os
from reportlab.lib import colors
from reportlab.lib.pagesizes import letter
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, Table, TableStyle, PageBreak
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.lib.units import inch
from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import letter

class CharacterSheetGUI:
    def __init__(self, root):
        self.root = root
        self.root.title("MTM Character Sheet")
        self.root.geometry("1200x800")
        
        # Initialize character data
        self.character_data = {
            'name': '',
            'playerName': '',
            'rank': 1,
            'rankPoints': 0,
            'race': '',
            'type': 'non-specialized',
            'aspects': {
                'melee': 'd4',
                'ranged': 'd4',
                'rogue': 'd4',
                'magic': 'd4'
            },
            'aspectIncreases': {
                'allowed': 0,  # Number of increases allowed at current even level
                'used': 0,    # Number of increases used at current even level
                'history': {}  # Track increases by level
            },
            'combatStats': {
                'hp': 0,
                'maxHp': 0,
                'initiative': 0,
                'speed': 0,
                'heroPoints': 0
            },
            'spells': {},
            'profession': '',
            'specialAbilities': {
                'rank1': '',
                'rank4': '',
                'rank8': ''
            },
            'magicalItems': [],
            'inventory': {
                'stored': [],
                'magic': [],
                'stored_magic': [],
                'elsewhere': []
            },
            'money': 0,
            'magicDust': 0,
            'gearDieSlots': {
                'd4': 2,  # Start with 1 free d4 slot + 1 d4 slot
                'd6': 1,  # Start with 1 d6 slot
                'd8': 1,  # Start with 1 d8 slot
                'd10': 1,  # Start with 1 d10 slot
                'd12': 1  # Start with 1 d12 slot
            },
            'gearDieEntries': {die: [] for die in ['d4', 'd6', 'd8', 'd10', 'd12']}
        }

        # Initialize aspect variables dictionary
        self.aspect_vars = {}
        self.choices_locked = False
        self.modifier_vars = {}

        # Create main notebook (tabs)
        self.notebook = ttk.Notebook(root)
        self.notebook.pack(expand=True, fill='both')

        # Create tabs
        self.basic_info_tab = ttk.Frame(self.notebook)
        self.aspects_tab = ttk.Frame(self.notebook)
        self.abilities_tab = ttk.Frame(self.notebook)
        self.gear_die_tab = ttk.Frame(self.notebook)
        self.inventory_tab = ttk.Frame(self.notebook)

        self.notebook.add(self.basic_info_tab, text='Basic Info')
        self.notebook.add(self.aspects_tab, text='Aspects')
        self.notebook.add(self.abilities_tab, text='Abilities')
        self.notebook.add(self.gear_die_tab, text='Gear Die')
        self.notebook.add(self.inventory_tab, text='Inventory')

        # Initialize gear die variables
        self.gear_die_slots = {
            'd4': tk.StringVar(value='2'),  # Start with 1 free d4 slot + 1 d4 slot
            'd6': tk.StringVar(value='1'),  # Start with 1 d6 slot
            'd8': tk.StringVar(value='1'),  # Start with 1 d8 slot
            'd10': tk.StringVar(value='1'),  # Start with 1 d10 slot
            'd12': tk.StringVar(value='1')  # Start with 1 d12 slot
        }
        self.gear_die_entries = {}  # Will store text entries for each slot

        # Create menu bar
        self.create_menu_bar()
        
        # Initialize tabs
        self.create_basic_info_tab()
        self.create_aspects_tab()
        self.create_abilities_tab()
        self.create_gear_die_tab()
        self.create_inventory_tab()

        # Calculate initial max HP
        self.calculate_max_hp()

    def create_menu_bar(self):
        menubar = tk.Menu(self.root)
        self.root.config(menu=menubar)

        file_menu = tk.Menu(menubar, tearoff=0)
        menubar.add_cascade(label="File", menu=file_menu)
        file_menu.add_command(label="Save", command=self.save_character)
        file_menu.add_command(label="Load", command=self.load_character)
        file_menu.add_separator()
        file_menu.add_command(label="Print", command=self.print_character)
        file_menu.add_separator()
        file_menu.add_command(label="Reset", command=self.reset_character)

    def create_basic_info_tab(self):
        # Main container frame
        main_frame = ttk.Frame(self.basic_info_tab)
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

        # Profession Selection
        ttk.Label(frame, text="Profession:").grid(row=3, column=0, padx=5, pady=2)
        self.profession_entry = ttk.Entry(frame)
        self.profession_entry.grid(row=3, column=1, padx=5, pady=2)

        # Rank and Rank Points
        rank_frame = ttk.Frame(frame)
        rank_frame.grid(row=4, column=0, columnspan=2, padx=5, pady=2, sticky='w')
        
        ttk.Label(rank_frame, text="Rank:").pack(side='left', padx=5)
        self.rank_var = tk.StringVar(value="1")
        self.rank_label = ttk.Label(rank_frame, textvariable=self.rank_var)
        self.rank_label.pack(side='left', padx=5)
        
        ttk.Label(rank_frame, text="Current Points:").pack(side='left', padx=5)
        self.current_points_var = tk.StringVar(value="0")
        self.current_points_label = ttk.Label(rank_frame, textvariable=self.current_points_var)
        self.current_points_label.pack(side='left', padx=5)
        
        # Add points frame
        add_points_frame = ttk.Frame(rank_frame)
        add_points_frame.pack(side='left', padx=5)
        
        ttk.Label(add_points_frame, text="Add Points:").pack(side='left', padx=5)
        self.add_points_var = tk.StringVar(value="0")
        self.add_points_entry = ttk.Entry(add_points_frame, textvariable=self.add_points_var, width=5)
        self.add_points_entry.pack(side='left', padx=5)
        
        add_button = ttk.Button(add_points_frame, text="Add", command=self.add_rank_points)
        add_button.pack(side='left', padx=5)
        
        # Add trace to monitor total rank points changes
        self.total_rank_points_var = tk.StringVar(value="0")
        self.total_rank_points_var.trace_add('write', self.update_rank)

        # Magic Items Frame
        magic_items_frame = ttk.LabelFrame(frame, text="Magic Items")
        magic_items_frame.grid(row=5, column=0, columnspan=2, padx=5, pady=5, sticky='ew')
        
        # Create 7 magic item entries
        self.magic_item_entries = []
        for i in range(7):
            ttk.Label(magic_items_frame, text=f"Magic Item {i+1}:").grid(row=i, column=0, padx=5, pady=2)
            entry = ttk.Entry(magic_items_frame, width=60)  # Increased width from default to 60
            entry.grid(row=i, column=1, padx=5, pady=2, sticky='ew')
            self.magic_item_entries.append(entry)

        # Combat Stats Frame
        combat_frame = ttk.LabelFrame(frame, text="Combat Statistics")
        combat_frame.grid(row=6, column=0, columnspan=2, padx=5, pady=5, sticky='ew')

        # HP
        ttk.Label(combat_frame, text="Current HP:").grid(row=0, column=0, padx=5, pady=2)
        self.hp_entry = ttk.Entry(combat_frame)
        self.hp_entry.grid(row=0, column=1, padx=5, pady=2)

        ttk.Label(combat_frame, text="/").grid(row=0, column=2, padx=5, pady=2)
        ttk.Label(combat_frame, text="Max HP:").grid(row=0, column=3, padx=5, pady=2)
        self.max_hp_entry = ttk.Entry(combat_frame)
        self.max_hp_entry.grid(row=0, column=4, padx=5, pady=2)

        # Initiative
        ttk.Label(combat_frame, text="Initiative:").grid(row=1, column=0, padx=5, pady=2)
        self.initiative_entry = ttk.Entry(combat_frame)
        self.initiative_entry.grid(row=1, column=1, padx=5, pady=2)

        # Hero Points
        ttk.Label(combat_frame, text="Hero Points:").grid(row=2, column=0, padx=5, pady=2)
        self.hero_points_entry = ttk.Entry(combat_frame)
        self.hero_points_entry.grid(row=2, column=1, padx=5, pady=2)

        # Resources
        resources_frame = ttk.LabelFrame(frame, text="Resources")
        resources_frame.grid(row=7, column=0, columnspan=2, padx=5, pady=5, sticky='ew')

        ttk.Label(resources_frame, text="Money:").grid(row=0, column=0, padx=5, pady=2)
        self.money_entry = ttk.Entry(resources_frame)
        self.money_entry.grid(row=0, column=1, padx=5, pady=2)

        ttk.Label(resources_frame, text="Magic Dust:").grid(row=1, column=0, padx=5, pady=2)
        self.magic_dust_entry = ttk.Entry(resources_frame)
        self.magic_dust_entry.grid(row=1, column=1, padx=5, pady=2)

        # Right side frame for dice roller
        right_frame = ttk.Frame(main_frame)
        right_frame.pack(side='right', fill='both', padx=5, pady=5)

        # Dice Roller Frame
        dice_frame = ttk.LabelFrame(right_frame, text="Dice Roller")
        dice_frame.pack(fill='both', expand=True, padx=5, pady=5)

        # Result display
        self.dice_result_var = tk.StringVar(value="Roll some dice!")
        result_label = ttk.Label(dice_frame, textvariable=self.dice_result_var, 
                               font=('Arial', 12), wraplength=200)
        result_label.pack(padx=5, pady=5)

        # Dice buttons frame
        dice_buttons_frame = ttk.Frame(dice_frame)
        dice_buttons_frame.pack(fill='x', padx=5, pady=5)

        # Common dice buttons
        common_dice = ['d4', 'd6', 'd8', 'd10', 'd12', 'd20', 'd100']
        for i, die in enumerate(common_dice):
            btn = ttk.Button(dice_buttons_frame, text=die, 
                           command=lambda d=die: self.roll_dice(d))
            btn.grid(row=i//4, column=i%4, padx=2, pady=2, sticky='ew')

        # Custom roll frame
        custom_frame = ttk.Frame(dice_frame)
        custom_frame.pack(fill='x', padx=5, pady=5)

        ttk.Label(custom_frame, text="Custom:").pack(side='left', padx=5)
        self.custom_dice_var = tk.StringVar(value="1d6")
        custom_entry = ttk.Entry(custom_frame, textvariable=self.custom_dice_var, width=10)
        custom_entry.pack(side='left', padx=5)
        custom_btn = ttk.Button(custom_frame, text="Roll", 
                              command=lambda: self.roll_custom_dice(self.custom_dice_var.get()))
        custom_btn.pack(side='left', padx=5)

        # Aspect modifiers frame
        modifiers_frame = ttk.Frame(dice_frame)
        modifiers_frame.pack(fill='x', padx=5, pady=5)

        # Create checkboxes for each aspect
        self.aspect_check_vars = {}
        for aspect in ['melee', 'ranged', 'rogue', 'magic']:
            check_frame = ttk.Frame(modifiers_frame)
            check_frame.pack(side='left', padx=5)
            
            self.aspect_check_vars[aspect] = tk.BooleanVar(value=False)
            check = ttk.Checkbutton(check_frame, text=aspect.capitalize(), 
                                  variable=self.aspect_check_vars[aspect])
            check.pack(side='left')

        # Roll History Frame
        history_frame = ttk.LabelFrame(dice_frame, text="Roll History")
        history_frame.pack(fill='both', expand=True, padx=5, pady=5)

        # Create a scrollbar for the history listbox
        scrollbar = ttk.Scrollbar(history_frame)
        scrollbar.pack(side='right', fill='y')

        # Create the history listbox
        self.roll_history_listbox = tk.Listbox(history_frame, yscrollcommand=scrollbar.set)
        self.roll_history_listbox.pack(fill='both', expand=True, padx=5, pady=5)
        scrollbar.config(command=self.roll_history_listbox.yview)

        # Clear history button
        clear_history_btn = ttk.Button(history_frame, text="Clear History", 
                                     command=self.clear_roll_history)
        clear_history_btn.pack(padx=5, pady=5)

        # Initialize roll history
        self.roll_history = []

    def create_aspects_tab(self):
        # Aspects Frame
        frame = ttk.LabelFrame(self.aspects_tab, text="Character Aspects")
        frame.pack(fill='both', expand=True, padx=5, pady=5)

        # Create a frame for instructions
        instructions_frame = ttk.Frame(frame)
        instructions_frame.pack(fill='x', padx=5, pady=5)
        ttk.Label(instructions_frame, 
                 text="Select one aspect for each die type (d6, d8, d10, d12).\nOnce selected, other aspects will be locked to prevent duplicates.\nUse + and - buttons to increase/decrease die values.\nModifiers: d4=-1, d6=0, d8=+1, d10=+2, d12=+3",
                 wraplength=400).pack()

        # Add lock button frame
        lock_frame = ttk.Frame(frame)
        lock_frame.pack(fill='x', padx=5, pady=5)
        self.lock_button = ttk.Button(lock_frame, text="Lock Choices", command=self.lock_aspect_choices)
        self.lock_button.pack(side='right', padx=5)
        self.choices_locked = False

        aspects = ['melee', 'ranged', 'rogue', 'magic']
        dice_values = ['d4', 'd6', 'd8', 'd10', 'd12']  # Removed * option
        
        # Dictionary to track which die values are already selected
        self.selected_dice = {die: None for die in dice_values if die != 'd4'}
        
        # Create aspect frames
        for i, aspect in enumerate(aspects):
            aspect_frame = ttk.Frame(frame)
            aspect_frame.pack(fill='x', padx=5, pady=2)
            
            ttk.Label(aspect_frame, text=aspect.capitalize() + ":", width=10).pack(side='left', padx=5)
            
            self.aspect_vars[aspect] = tk.StringVar(value='d4')
            aspect_combo = ttk.Combobox(aspect_frame, textvariable=self.aspect_vars[aspect], state='readonly')
            aspect_combo['values'] = dice_values
            aspect_combo.pack(side='left', padx=5)
            
            # Add modifier label
            self.modifier_vars[aspect] = tk.StringVar(value="-1")
            modifier_label = ttk.Label(aspect_frame, textvariable=self.modifier_vars[aspect], width=4)
            modifier_label.pack(side='left', padx=5)
            
            # Add increase/decrease buttons
            decrease_button = ttk.Button(aspect_frame, text="-", width=2,
                                       command=lambda a=aspect: self.adjust_die_value(a, -1))
            decrease_button.pack(side='left', padx=5)
            
            increase_button = ttk.Button(aspect_frame, text="+", width=2,
                                       command=lambda a=aspect: self.adjust_die_value(a, 1))
            increase_button.pack(side='left', padx=5)
            
            # Add trace to monitor changes
            self.aspect_vars[aspect].trace_add('write', lambda *args, a=aspect: self.on_aspect_change(a))
            
            # Store the combobox and buttons for later reference
            setattr(self, f'{aspect}_combo', aspect_combo)
            setattr(self, f'{aspect}_decrease_button', decrease_button)
            setattr(self, f'{aspect}_increase_button', increase_button)

    def create_gear_die_tab(self):
        """Create the gear die tab with text boxes for each spell slot"""
        # Clear existing content
        for widget in self.gear_die_tab.winfo_children():
            widget.destroy()
            
        # Main frame
        frame = ttk.LabelFrame(self.gear_die_tab, text="Gear Die Slots")
        frame.pack(fill='both', expand=True, padx=5, pady=5)

        # Instructions
        instructions = ttk.Label(frame, 
                               text="You start with 1 free d4 slot, 1 d4 slot, 1 d6 slot, 1 d8 slot, 1 d10 slot, and 1 d12 slot.\n"
                                    "At rank 3: Gain 2 additional d4 slots\n"
                                    "At rank 5: Gain 2 additional d6 slots\n"
                                    "At rank 7: Gain 2 additional d8 slots\n"
                                    "At rank 9: Gain 2 additional d10 slots\n"
                                    "At rank 11: Gain 2 additional d12 slots",
                               wraplength=400)
        instructions.pack(padx=5, pady=5)

        # Create a frame for each die type
        for die in ['d4', 'd6', 'd8', 'd10', 'd12']:
            die_frame = ttk.Frame(frame)
            die_frame.pack(fill='x', padx=5, pady=2)

            # Die type label
            ttk.Label(die_frame, text=f"{die} Slots:").pack(pady=2)

            # Create text entries for each slot
            slots_frame = ttk.Frame(die_frame)
            slots_frame.pack(fill='x', padx=5)
            
            # Clear existing entries
            if die in self.gear_die_entries:
                for entry in self.gear_die_entries[die]:
                    entry.destroy()
            self.gear_die_entries[die] = []
            
            # Create initial entries based on available slots
            for i in range(int(self.gear_die_slots[die].get())):
                entry_frame = ttk.Frame(slots_frame)
                entry_frame.pack(fill='x', pady=2)
                entry = ttk.Entry(entry_frame, width=30)
                entry.pack(side='left', padx=2, fill='x', expand=True)
                self.gear_die_entries[die].append(entry)
                # Initialize the entry in character data
                if 'gearDieEntries' not in self.character_data:
                    self.character_data['gearDieEntries'] = {die: [] for die in ['d4', 'd6', 'd8', 'd10', 'd12']}
                if i >= len(self.character_data['gearDieEntries'][die]):
                    self.character_data['gearDieEntries'][die].append('')
                else:
                    entry.insert(0, self.character_data['gearDieEntries'][die][i])

    def calculate_max_hp(self):
        """Calculate max HP based on race and rank"""
        race = self.character_data['race']
        rank = self.character_data['rank']
        
        if race in ['Half-Dragon', 'Human']:
            max_hp = 18 + (7 * (rank - 1))
        elif race in ['Elf', 'Half Elf', 'Galdur', 'Gnome', 'Halfling']:
            max_hp = 15 + (5 * (rank - 1))
        elif race in ['Dwarf', 'Minotaur']:
            max_hp = 20 + (8 * (rank - 1))
        elif race == 'Half Giant':
            max_hp = 25 + (10 * (rank - 1))
        else:
            max_hp = 0  # Default case if no race selected
        
        # Update max HP in character data and GUI
        self.character_data['combatStats']['maxHp'] = max_hp
        self.max_hp_entry.delete(0, tk.END)
        self.max_hp_entry.insert(0, str(max_hp))

    def update_rank(self, *args):
        """Update rank and current points based on total rank points"""
        try:
            total_points = int(self.total_rank_points_var.get())
            # Calculate rank based on points (1 rank per 25 points, max rank 12)
            new_rank = min(12, 1 + (total_points // 25))
            self.rank_var.set(str(new_rank))
            
            # Calculate current points (remainder after dividing by 25)
            current_points = total_points % 25
            self.current_points_var.set(str(current_points))
            
            # Update character data
            self.character_data['rank'] = new_rank
            self.character_data['rankPoints'] = total_points
            
            # Calculate max HP
            self.calculate_max_hp()
            
            # Update gear die slots based on current rank
            # Reset all slots to base values first
            base_slots = {
                'd4': 2,  # Start with 1 free d4 slot + 1 d4 slot
                'd6': 1,  # Start with 1 d6 slot
                'd8': 1,  # Start with 1 d8 slot
                'd10': 1,  # Start with 1 d10 slot
                'd12': 1  # Start with 1 d12 slot
            }
            
            # Apply rank-based increases
            if new_rank >= 3:  # Gain 2d4 slots
                base_slots['d4'] += 2
            if new_rank >= 5:  # Gain 2d6 slots
                base_slots['d6'] += 2
            if new_rank >= 7:  # Gain 2d8 slots
                base_slots['d8'] += 2
            if new_rank >= 9:  # Gain 2d10 slots
                base_slots['d10'] += 2
            if new_rank >= 11:  # Gain 2d12 slots
                base_slots['d12'] += 2
                
            # Update both the GUI variables and character data
            for die, slots in base_slots.items():
                self.gear_die_slots[die].set(str(slots))
                self.character_data['gearDieSlots'][die] = slots
            
            # Update aspect increases based on level/2 rounded down
            self.character_data['aspectIncreases']['allowed'] = new_rank // 2
            
            # Initialize history for new even levels
            if new_rank % 2 == 0 and new_rank > 1:
                if new_rank not in self.character_data['aspectIncreases']['history']:
                    self.character_data['aspectIncreases']['history'][new_rank] = 0
            
            # Recreate the gear die tab to show new slots
            self.create_gear_die_tab()
            
            # Update ability visibility
            self.update_ability_visibility()
        except ValueError:
            # Handle invalid input (non-numeric)
            pass

    def create_inventory_tab(self):
        # Inventory Frame
        frame = ttk.LabelFrame(self.inventory_tab, text="Inventory")
        frame.pack(fill='both', expand=True, padx=5, pady=5)

        # Create notebook for different inventory sections
        inventory_notebook = ttk.Notebook(frame)
        inventory_notebook.pack(fill='both', expand=True, padx=5, pady=5)

        # Stored Equipment
        stored_frame = ttk.Frame(inventory_notebook)
        inventory_notebook.add(stored_frame, text="Stored Equipment")
        
        # Add item frame for stored equipment
        stored_add_frame = ttk.Frame(stored_frame)
        stored_add_frame.pack(fill='x', padx=5, pady=5)
        
        ttk.Label(stored_add_frame, text="Add Item:").pack(side='left', padx=5)
        self.stored_item_var = tk.StringVar()
        stored_entry = ttk.Entry(stored_add_frame, textvariable=self.stored_item_var)
        stored_entry.pack(side='left', padx=5, expand=True, fill='x')
        
        ttk.Label(stored_add_frame, text="Quantity:").pack(side='left', padx=5)
        self.stored_quantity_var = tk.StringVar(value="1")
        stored_quantity = ttk.Entry(stored_add_frame, textvariable=self.stored_quantity_var, width=5)
        stored_quantity.pack(side='left', padx=5)
        
        stored_add_button = ttk.Button(stored_add_frame, text="Add", 
                                     command=lambda: self.add_inventory_item('stored'))
        stored_add_button.pack(side='left', padx=5)
        
        # Listbox for stored items
        self.stored_listbox = tk.Listbox(stored_frame)
        self.stored_listbox.pack(fill='both', expand=True, padx=5, pady=5)
        
        # Controls frame for stored items
        stored_controls = ttk.Frame(stored_frame)
        stored_controls.pack(fill='x', padx=5, pady=5)
        
        stored_remove_button = ttk.Button(stored_controls, text="Remove Selected",
                                        command=lambda: self.remove_inventory_item('stored'))
        stored_remove_button.pack(side='left', padx=5)
        
        stored_decrease_button = ttk.Button(stored_controls, text="Decrease Quantity",
                                          command=lambda: self.adjust_quantity('stored', -1))
        stored_decrease_button.pack(side='left', padx=5)
        
        stored_increase_button = ttk.Button(stored_controls, text="Increase Quantity",
                                          command=lambda: self.adjust_quantity('stored', 1))
        stored_increase_button.pack(side='left', padx=5)

        # Magic Bag
        magic_frame = ttk.Frame(inventory_notebook)
        inventory_notebook.add(magic_frame, text="Magic Bag")
        
        # Add item frame for magic bag
        magic_add_frame = ttk.Frame(magic_frame)
        magic_add_frame.pack(fill='x', padx=5, pady=5)
        
        ttk.Label(magic_add_frame, text="Add Item:").pack(side='left', padx=5)
        self.magic_item_var = tk.StringVar()
        magic_entry = ttk.Entry(magic_add_frame, textvariable=self.magic_item_var)
        magic_entry.pack(side='left', padx=5, expand=True, fill='x')
        
        ttk.Label(magic_add_frame, text="Quantity:").pack(side='left', padx=5)
        self.magic_quantity_var = tk.StringVar(value="1")
        magic_quantity = ttk.Entry(magic_add_frame, textvariable=self.magic_quantity_var, width=5)
        magic_quantity.pack(side='left', padx=5)
        
        magic_add_button = ttk.Button(magic_add_frame, text="Add",
                                    command=lambda: self.add_inventory_item('magic'))
        magic_add_button.pack(side='left', padx=5)
        
        # Listbox for magic items
        self.magic_listbox = tk.Listbox(magic_frame)
        self.magic_listbox.pack(fill='both', expand=True, padx=5, pady=5)
        
        # Controls frame for magic items
        magic_controls = ttk.Frame(magic_frame)
        magic_controls.pack(fill='x', padx=5, pady=5)
        
        magic_remove_button = ttk.Button(magic_controls, text="Remove Selected",
                                       command=lambda: self.remove_inventory_item('magic'))
        magic_remove_button.pack(side='left', padx=5)
        
        magic_decrease_button = ttk.Button(magic_controls, text="Decrease Quantity",
                                         command=lambda: self.adjust_quantity('magic', -1))
        magic_decrease_button.pack(side='left', padx=5)
        
        magic_increase_button = ttk.Button(magic_controls, text="Increase Quantity",
                                         command=lambda: self.adjust_quantity('magic', 1))
        magic_increase_button.pack(side='left', padx=5)

        # Stored Magic Items
        stored_magic_frame = ttk.Frame(inventory_notebook)
        inventory_notebook.add(stored_magic_frame, text="Stored Magic Items")
        
        # Add item frame for stored magic items
        stored_magic_add_frame = ttk.Frame(stored_magic_frame)
        stored_magic_add_frame.pack(fill='x', padx=5, pady=5)
        
        ttk.Label(stored_magic_add_frame, text="Add Item:").pack(side='left', padx=5)
        self.stored_magic_item_var = tk.StringVar()
        stored_magic_entry = ttk.Entry(stored_magic_add_frame, textvariable=self.stored_magic_item_var)
        stored_magic_entry.pack(side='left', padx=5, expand=True, fill='x')
        
        ttk.Label(stored_magic_add_frame, text="Quantity:").pack(side='left', padx=5)
        self.stored_magic_quantity_var = tk.StringVar(value="1")
        stored_magic_quantity = ttk.Entry(stored_magic_add_frame, textvariable=self.stored_magic_quantity_var, width=5)
        stored_magic_quantity.pack(side='left', padx=5)
        
        stored_magic_add_button = ttk.Button(stored_magic_add_frame, text="Add",
                                           command=lambda: self.add_inventory_item('stored_magic'))
        stored_magic_add_button.pack(side='left', padx=5)
        
        # Listbox for stored magic items
        self.stored_magic_listbox = tk.Listbox(stored_magic_frame)
        self.stored_magic_listbox.pack(fill='both', expand=True, padx=5, pady=5)
        
        # Controls frame for stored magic items
        stored_magic_controls = ttk.Frame(stored_magic_frame)
        stored_magic_controls.pack(fill='x', padx=5, pady=5)
        
        stored_magic_remove_button = ttk.Button(stored_magic_controls, text="Remove Selected",
                                              command=lambda: self.remove_inventory_item('stored_magic'))
        stored_magic_remove_button.pack(side='left', padx=5)
        
        stored_magic_decrease_button = ttk.Button(stored_magic_controls, text="Decrease Quantity",
                                                command=lambda: self.adjust_quantity('stored_magic', -1))
        stored_magic_decrease_button.pack(side='left', padx=5)
        
        stored_magic_increase_button = ttk.Button(stored_magic_controls, text="Increase Quantity",
                                                command=lambda: self.adjust_quantity('stored_magic', 1))
        stored_magic_increase_button.pack(side='left', padx=5)

        # Elsewhere
        elsewhere_frame = ttk.Frame(inventory_notebook)
        inventory_notebook.add(elsewhere_frame, text="Elsewhere")
        
        # Add item frame for elsewhere
        elsewhere_add_frame = ttk.Frame(elsewhere_frame)
        elsewhere_add_frame.pack(fill='x', padx=5, pady=5)
        
        ttk.Label(elsewhere_add_frame, text="Add Item:").pack(side='left', padx=5)
        self.elsewhere_item_var = tk.StringVar()
        elsewhere_entry = ttk.Entry(elsewhere_add_frame, textvariable=self.elsewhere_item_var)
        elsewhere_entry.pack(side='left', padx=5, expand=True, fill='x')
        
        ttk.Label(elsewhere_add_frame, text="Quantity:").pack(side='left', padx=5)
        self.elsewhere_quantity_var = tk.StringVar(value="1")
        elsewhere_quantity = ttk.Entry(elsewhere_add_frame, textvariable=self.elsewhere_quantity_var, width=5)
        elsewhere_quantity.pack(side='left', padx=5)
        
        ttk.Label(elsewhere_add_frame, text="Location:").pack(side='left', padx=5)
        self.elsewhere_location_var = tk.StringVar()
        elsewhere_location = ttk.Entry(elsewhere_add_frame, textvariable=self.elsewhere_location_var)
        elsewhere_location.pack(side='left', padx=5, expand=True, fill='x')
        
        elsewhere_add_button = ttk.Button(elsewhere_add_frame, text="Add",
                                        command=lambda: self.add_inventory_item('elsewhere'))
        elsewhere_add_button.pack(side='left', padx=5)
        
        # Listbox for elsewhere items
        self.elsewhere_listbox = tk.Listbox(elsewhere_frame)
        self.elsewhere_listbox.pack(fill='both', expand=True, padx=5, pady=5)
        
        # Controls frame for elsewhere items
        elsewhere_controls = ttk.Frame(elsewhere_frame)
        elsewhere_controls.pack(fill='x', padx=5, pady=5)
        
        elsewhere_remove_button = ttk.Button(elsewhere_controls, text="Remove Selected",
                                           command=lambda: self.remove_inventory_item('elsewhere'))
        elsewhere_remove_button.pack(side='left', padx=5)
        
        elsewhere_decrease_button = ttk.Button(elsewhere_controls, text="Decrease Quantity",
                                             command=lambda: self.adjust_quantity('elsewhere', -1))
        elsewhere_decrease_button.pack(side='left', padx=5)
        
        elsewhere_increase_button = ttk.Button(elsewhere_controls, text="Increase Quantity",
                                             command=lambda: self.adjust_quantity('elsewhere', 1))
        elsewhere_increase_button.pack(side='left', padx=5)
        
        # Add button to edit location
        elsewhere_edit_location_button = ttk.Button(elsewhere_controls, text="Edit Location",
                                                  command=self.edit_elsewhere_location)
        elsewhere_edit_location_button.pack(side='left', padx=5)

    def add_inventory_item(self, category):
        """Add an item to the specified inventory category"""
        item_var = getattr(self, f'{category}_item_var')
        quantity_var = getattr(self, f'{category}_quantity_var')
        listbox = getattr(self, f'{category}_listbox')
        
        item = item_var.get().strip()
        try:
            quantity = int(quantity_var.get())
            if quantity < 1:
                raise ValueError
        except ValueError:
            messagebox.showwarning("Invalid Quantity", "Please enter a valid positive number for quantity.")
            return
            
        if item:
            # Check if item already exists
            for i in range(listbox.size()):
                existing_item = listbox.get(i)
                if existing_item.startswith(f"{item} ("):
                    # Update quantity of existing item
                    current_quantity = int(existing_item.split('(')[1].split(')')[0])
                    new_quantity = current_quantity + quantity
                    listbox.delete(i)
                    listbox.insert(i, f"{item} ({new_quantity})")
                    # Update character data
                    for inv_item in self.character_data['inventory'][category]:
                        if inv_item['name'] == item:
                            inv_item['quantity'] = new_quantity
                            break
                    item_var.set('')
                    quantity_var.set('1')
                    return
            
            # Add new item
            if category == 'elsewhere':
                location = self.elsewhere_location_var.get().strip()
                display_text = f"{item} ({quantity}) - {location}"
                self.character_data['inventory'][category].append({
                    'name': item,
                    'quantity': quantity,
                    'location': location
                })
            else:
                display_text = f"{item} ({quantity})"
                self.character_data['inventory'][category].append({
                    'name': item,
                    'quantity': quantity
                })
            
            listbox.insert(tk.END, display_text)
            item_var.set('')
            quantity_var.set('1')
            if category == 'elsewhere':
                self.elsewhere_location_var.set('')

    def edit_elsewhere_location(self):
        """Edit the location of the selected elsewhere item"""
        selection = self.elsewhere_listbox.curselection()
        if not selection:
            messagebox.showwarning("No Selection", "Please select an item to edit its location.")
            return
            
        index = selection[0]
        item_text = self.elsewhere_listbox.get(index)
        item_name = item_text.split('(')[0].strip()
        
        # Find the item in character data
        for item in self.character_data['inventory']['elsewhere']:
            if item['name'] == item_name:
                # Create a dialog to edit the location
                dialog = tk.Toplevel(self.root)
                dialog.title("Edit Location")
                dialog.geometry("300x100")
                
                ttk.Label(dialog, text="New Location:").pack(padx=5, pady=5)
                location_var = tk.StringVar(value=item.get('location', ''))
                location_entry = ttk.Entry(dialog, textvariable=location_var)
                location_entry.pack(padx=5, pady=5)
                
                def save_location():
                    new_location = location_var.get().strip()
                    item['location'] = new_location
                    # Update the listbox display
                    quantity = item['quantity']
                    self.elsewhere_listbox.delete(index)
                    self.elsewhere_listbox.insert(index, f"{item_name} ({quantity}) - {new_location}")
                    dialog.destroy()
                
                ttk.Button(dialog, text="Save", command=save_location).pack(padx=5, pady=5)
                break

    def remove_inventory_item(self, category):
        """Remove the selected item from the specified inventory category"""
        listbox = getattr(self, f'{category}_listbox')
        selection = listbox.curselection()
        
        if selection:
            index = selection[0]
            item_text = listbox.get(index)
            item_name = item_text.split('(')[0].strip()
            listbox.delete(index)
            # Remove from character data
            self.character_data['inventory'][category] = [
                item for item in self.character_data['inventory'][category]
                if item['name'] != item_name
            ]

    def adjust_quantity(self, category, change):
        """Adjust the quantity of the selected item"""
        listbox = getattr(self, f'{category}_listbox')
        selection = listbox.curselection()
        
        if selection:
            index = selection[0]
            item_text = listbox.get(index)
            item_name = item_text.split('(')[0].strip()
            current_quantity = int(item_text.split('(')[1].split(')')[0])
            new_quantity = current_quantity + change
            
            if new_quantity < 1:
                messagebox.showwarning("Invalid Quantity", "Quantity cannot be less than 1.")
                return
                
            # Update listbox
            listbox.delete(index)
            listbox.insert(index, f"{item_name} ({new_quantity})")
            
            # Update character data
            for item in self.character_data['inventory'][category]:
                if item['name'] == item_name:
                    item['quantity'] = new_quantity
                    break

    def create_abilities_tab(self):
        # Abilities Frame
        frame = ttk.LabelFrame(self.abilities_tab, text="Special Abilities")
        frame.pack(fill='both', expand=True, padx=5, pady=5)

        # Dragon's Breath Ability (only for Half-Dragon)
        self.dragons_breath_frame = ttk.Frame(frame)
        ttk.Label(self.dragons_breath_frame, text="Dragon's Breath:").pack(side='left', padx=5)
        
        # Create a frame for the fixed text
        dragons_breath_text_frame = ttk.Frame(self.dragons_breath_frame)
        dragons_breath_text_frame.pack(side='left', padx=5, fill='x', expand=True)
        
        # Calculate range and damage based on rank
        current_rank = self.character_data['rank']
        range_value = 10 + (5 * (current_rank - 1))
        
        # Calculate damage based on rank
        if current_rank >= 11:
            damage = "1d12+1d4"
        elif current_rank >= 9:
            damage = "1d12"
        elif current_rank >= 7:
            damage = "1d10"
        elif current_rank >= 5:
            damage = "1d8"
        elif current_rank >= 3:
            damage = "1d6"
        else:
            damage = "1d4"
            
        # Calculate uses per encounter based on rank
        uses = 1
        if current_rank >= 11:
            uses = 4
        elif current_rank >= 9:
            uses = 3
        elif current_rank >= 5:
            uses = 2
        
        # Add the fixed text with dynamic range and damage
        ttk.Label(dragons_breath_text_frame, text=f"Range: 10x{range_value} feet\nDamage: {damage} fire damage\nUses per Encounter: {uses}").pack(anchor='w')

        # Rank 1 Ability
        self.rank1_frame = ttk.Frame(frame)
        ttk.Label(self.rank1_frame, text="Rank 1 Ability:").pack(side='left', padx=5)
        self.ability_1_text = tk.Text(self.rank1_frame, height=5, width=50)
        self.ability_1_text.pack(side='left', padx=5, fill='x', expand=True)

        # Rank 4 Ability
        self.rank4_frame = ttk.Frame(frame)
        ttk.Label(self.rank4_frame, text="Rank 4 Ability:").pack(side='left', padx=5)
        self.ability_4_text = tk.Text(self.rank4_frame, height=5, width=50)
        self.ability_4_text.pack(side='left', padx=5, fill='x', expand=True)

        # Rank 8 Ability
        self.rank8_frame = ttk.Frame(frame)
        ttk.Label(self.rank8_frame, text="Rank 8 Ability:").pack(side='left', padx=5)
        self.ability_8_text = tk.Text(self.rank8_frame, height=5, width=50)
        self.ability_8_text.pack(side='left', padx=5, fill='x', expand=True)

        # Update visibility based on current rank and race
        self.update_ability_visibility()

    def update_ability_visibility(self):
        """Update visibility of ability text boxes based on current rank and race"""
        current_rank = self.character_data['rank']
        current_race = self.character_data['race']
        
        # Show/hide Dragon's Breath ability
        if current_race == 'Half-Dragon':
            self.dragons_breath_frame.pack(fill='x', padx=5, pady=2, before=self.rank1_frame)
            # Update range and damage values
            range_value = 10 + (5 * (current_rank - 1))
            
            # Calculate damage based on rank
            if current_rank >= 11:
                damage = "1d12+1d4"
            elif current_rank >= 9:
                damage = "1d12"
            elif current_rank >= 7:
                damage = "1d10"
            elif current_rank >= 5:
                damage = "1d8"
            elif current_rank >= 3:
                damage = "1d6"
            else:
                damage = "1d4"
                
            # Calculate uses per encounter based on rank
            uses = 1
            if current_rank >= 11:
                uses = 4
            elif current_rank >= 9:
                uses = 3
            elif current_rank >= 5:
                uses = 2
                
            for widget in self.dragons_breath_frame.winfo_children():
                if isinstance(widget, ttk.Frame):
                    for label in widget.winfo_children():
                        if isinstance(label, ttk.Label):
                            label.config(text=f"Range: 10x{range_value} feet\nDamage: {damage} fire damage\nUses per Encounter: {uses}")
        else:
            self.dragons_breath_frame.pack_forget()
            
        # Show/hide Rank 1 ability
        if current_rank >= 1:
            self.rank1_frame.pack(fill='x', padx=5, pady=2)
        else:
            self.rank1_frame.pack_forget()
            
        # Show/hide Rank 4 ability
        if current_rank >= 4:
            self.rank4_frame.pack(fill='x', padx=5, pady=2)
        else:
            self.rank4_frame.pack_forget()
            
        # Show/hide Rank 8 ability
        if current_rank >= 8:
            self.rank8_frame.pack(fill='x', padx=5, pady=2)
        else:
            self.rank8_frame.pack_forget()

    def save_character(self):
        file_path = filedialog.asksaveasfilename(
            defaultextension=".json",
            filetypes=[("JSON files", "*.json"), ("All files", "*.*")]
        )
        if file_path:
            try:
                # Update all character data before saving
                self.character_data['name'] = self.name_entry.get()
                self.character_data['playerName'] = self.player_name_entry.get()
                self.character_data['race'] = self.race_var.get()
                self.character_data['profession'] = self.profession_entry.get()
                self.character_data['rank'] = int(self.rank_var.get())
                self.character_data['rankPoints'] = int(self.total_rank_points_var.get())
                
                # Update magic items
                self.character_data['magicalItems'] = [entry.get() for entry in self.magic_item_entries]
                
                # Update aspects
                for aspect in ['melee', 'ranged', 'rogue', 'magic']:
                    self.character_data['aspects'][aspect] = self.aspect_vars[aspect].get()
                
                # Update combat stats
                self.character_data['combatStats']['hp'] = int(self.hp_entry.get())
                self.character_data['combatStats']['initiative'] = int(self.initiative_entry.get())
                self.character_data['combatStats']['heroPoints'] = int(self.hero_points_entry.get())
                
                # Update special abilities
                self.character_data['specialAbilities']['rank1'] = self.ability_1_text.get(1.0, tk.END).strip()
                self.character_data['specialAbilities']['rank4'] = self.ability_4_text.get(1.0, tk.END).strip()
                self.character_data['specialAbilities']['rank8'] = self.ability_8_text.get(1.0, tk.END).strip()
                
                # Update gear die slots and entries
                self.character_data['gearDieSlots'] = {die: int(self.gear_die_slots[die].get()) for die in ['d4', 'd6', 'd8', 'd10', 'd12']}
                self.character_data['gearDieEntries'] = {die: [entry.get() for entry in self.gear_die_entries[die]] for die in ['d4', 'd6', 'd8', 'd10', 'd12']}
                
                # Update resources
                self.character_data['money'] = int(self.money_entry.get())
                self.character_data['magicDust'] = int(self.magic_dust_entry.get())
                
                # Save the updated character data
                with open(file_path, 'w') as f:
                    json.dump(self.character_data, f, indent=4)
                messagebox.showinfo("Success", "Character saved successfully!")
            except Exception as e:
                messagebox.showerror("Error", f"Failed to save character: {str(e)}")

    def load_character(self):
        file_path = filedialog.askopenfilename(
            filetypes=[("JSON files", "*.json"), ("All files", "*.*")]
        )
        if file_path:
            try:
                with open(file_path, 'r') as f:
                    self.character_data = json.load(f)
                self.update_gui_from_data()
                messagebox.showinfo("Success", "Character loaded successfully!")
            except Exception as e:
                messagebox.showerror("Error", f"Failed to load character: {str(e)}")

    def reset_character(self):
        if messagebox.askyesno("Reset Character", "Are you sure you want to reset the character sheet?"):
            self.character_data = {
                'name': '',
                'playerName': '',
                'rank': 1,
                'rankPoints': 0,
                'race': '',
                'type': 'non-specialized',
                'aspects': {
                    'melee': 'd4',
                    'ranged': 'd4',
                    'rogue': 'd4',
                    'magic': 'd4'
                },
                'aspectIncreases': {
                    'allowed': 0,  # Number of increases allowed at current even level
                    'used': 0,    # Number of increases used at current even level
                    'history': {}  # Track increases by level
                },
                'combatStats': {
                    'hp': 0,
                    'maxHp': 0,
                    'initiative': 0,
                    'speed': 0,
                    'heroPoints': 0
                },
                'spells': {},
                'profession': '',
                'specialAbilities': {
                    'rank1': '',
                    'rank4': '',
                    'rank8': ''
                },
                'magicalItems': [],
                'inventory': {
                    'stored': [],
                    'magic': [],
                    'stored_magic': [],
                    'elsewhere': []
                },
                'money': 0,
                'magicDust': 0,
                'gearDieSlots': {
                    'd4': 2,  # Start with 1 free d4 slot + 1 d4 slot
                    'd6': 1,  # Start with 1 d6 slot
                    'd8': 1,  # Start with 1 d8 slot
                    'd10': 1,  # Start with 1 d10 slot
                    'd12': 1  # Start with 1 d12 slot
                },
                'gearDieEntries': {die: [] for die in ['d4', 'd6', 'd8', 'd10', 'd12']}
            }
            self.update_gui_from_data()
            
            # Reset gear die variables
            self.gear_die_slots = {
                'd4': tk.StringVar(value='2'),  # Start with 1 free d4 slot + 1 d4 slot
                'd6': tk.StringVar(value='1'),  # Start with 1 d6 slot
                'd8': tk.StringVar(value='1'),  # Start with 1 d8 slot
                'd10': tk.StringVar(value='1'),  # Start with 1 d10 slot
                'd12': tk.StringVar(value='1')  # Start with 1 d12 slot
            }
            self.gear_die_entries = {}  # Will store text entries for each slot
            
            # Recreate the gear die tab
            self.create_gear_die_tab()
            
            # Reset aspect choices
            self.choices_locked = False
            self.lock_button.config(state='normal')
            
            # Reset selected dice tracking
            self.selected_dice = {die: None for die in ['d6', 'd8', 'd10', 'd12']}
            
            # Reset aspect comboboxes
            for aspect in ['melee', 'ranged', 'rogue', 'magic']:
                combo = getattr(self, f'{aspect}_combo')
                combo.config(state='readonly')
                self.aspect_vars[aspect].set('d4')
                combo['values'] = ['d4', 'd6', 'd8', 'd10', 'd12']

    def print_character(self):
        """Print the character sheet to PDF with content split across multiple pages"""
        try:
            # Get save location from user
            file_path = filedialog.asksaveasfilename(
                defaultextension=".pdf",
                filetypes=[("PDF files", "*.pdf"), ("All files", "*.*")]
            )
            if not file_path:
                return

            # Create PDF document
            doc = SimpleDocTemplate(file_path, pagesize=letter)
            styles = getSampleStyleSheet()
            story = []

            # Custom style for section headers
            section_style = ParagraphStyle(
                'Section',
                parent=styles['Heading1'],
                fontSize=10,
                spaceAfter=6
            )

            # Custom style for normal text
            normal_style = ParagraphStyle(
                'Normal',
                parent=styles['Normal'],
                fontSize=8,
                spaceAfter=4
            )

            # Character Sheet Page (Basic Info, Combat Stats, Aspects)
            story.append(Paragraph(f"Character Sheet: {self.character_data['name']}", styles['Title']))
            story.append(Spacer(1, 6))

            # Basic Information
            story.append(Paragraph("Basic Information", section_style))
            basic_info = [
                ["Character Name:", self.character_data['name']],
                ["Player Name:", self.character_data['playerName']],
                ["Race:", self.character_data['race']],
                ["Profession:", self.character_data['profession']],
                ["Rank:", str(self.character_data['rank'])],
                ["Rank Points:", str(self.character_data['rankPoints'])]
            ]
            basic_table = Table(basic_info, colWidths=[1.5*inch, 2*inch])
            basic_table.setStyle(TableStyle([
                ('ALIGN', (0, 0), (-1, -1), 'LEFT'),
                ('FONTNAME', (0, 0), (-1, -1), 'Helvetica-Bold'),
                ('FONTSIZE', (0, 0), (-1, -1), 8),
                ('BOTTOMPADDING', (0, 0), (-1, -1), 4),
            ]))
            story.append(basic_table)
            story.append(Spacer(1, 6))

            # Combat Stats
            story.append(Paragraph("Combat Statistics", section_style))
            combat_info = [
                ["HP:", f"{self.character_data['combatStats']['hp']}/{self.character_data['combatStats']['maxHp']}"],
                ["Initiative:", str(self.character_data['combatStats']['initiative'])],
                ["Hero Points:", str(self.character_data['combatStats']['heroPoints'])]
            ]
            combat_table = Table(combat_info, colWidths=[1.5*inch, 2*inch])
            combat_table.setStyle(TableStyle([
                ('ALIGN', (0, 0), (-1, -1), 'LEFT'),
                ('FONTNAME', (0, 0), (-1, -1), 'Helvetica-Bold'),
                ('FONTSIZE', (0, 0), (-1, -1), 8),
                ('BOTTOMPADDING', (0, 0), (-1, -1), 4),
            ]))
            story.append(combat_table)
            story.append(Spacer(1, 6))

            # Aspects
            story.append(Paragraph("Aspects", section_style))
            aspects_info = []
            for aspect, value in self.character_data['aspects'].items():
                modifier = self.get_die_modifier(value)
                aspects_info.append([f"{aspect.capitalize()}:", f"{value} ({modifier:+d})"])
            aspects_table = Table(aspects_info, colWidths=[1.5*inch, 2*inch])
            aspects_table.setStyle(TableStyle([
                ('ALIGN', (0, 0), (-1, -1), 'LEFT'),
                ('FONTNAME', (0, 0), (-1, -1), 'Helvetica-Bold'),
                ('FONTSIZE', (0, 0), (-1, -1), 8),
                ('BOTTOMPADDING', (0, 0), (-1, -1), 4),
            ]))
            story.append(aspects_table)
            story.append(PageBreak())

            # Special Abilities Page
            story.append(Paragraph("Special Abilities", section_style))
            if self.character_data['race'] == 'Half-Dragon':
                current_rank = self.character_data['rank']
                range_value = 10 + (5 * (current_rank - 1))
                
                # Calculate damage based on rank
                if current_rank >= 11:
                    damage = "1d12+1d4"
                elif current_rank >= 9:
                    damage = "1d12"
                elif current_rank >= 7:
                    damage = "1d10"
                elif current_rank >= 5:
                    damage = "1d8"
                elif current_rank >= 3:
                    damage = "1d6"
                else:
                    damage = "1d4"
                    
                # Calculate uses per encounter based on rank
                uses = 1
                if current_rank >= 11:
                    uses = 4
                elif current_rank >= 9:
                    uses = 3
                elif current_rank >= 5:
                    uses = 2
                    
                story.append(Paragraph("Dragon's Breath:", styles['Heading2']))
                story.append(Paragraph(f"Range: 10x{range_value} feet", normal_style))
                story.append(Paragraph(f"Damage: {damage} fire damage", normal_style))
                story.append(Paragraph(f"Uses per Encounter: {uses}", normal_style))
                story.append(Spacer(1, 6))
            
            if self.character_data['rank'] >= 1:
                story.append(Paragraph("Rank 1 Ability:", styles['Heading2']))
                story.append(Paragraph(self.character_data['specialAbilities']['rank1'], normal_style))
                story.append(Spacer(1, 6))
            if self.character_data['rank'] >= 4:
                story.append(Paragraph("Rank 4 Ability:", styles['Heading2']))
                story.append(Paragraph(self.character_data['specialAbilities']['rank4'], normal_style))
                story.append(Spacer(1, 6))
            if self.character_data['rank'] >= 8:
                story.append(Paragraph("Rank 8 Ability:", styles['Heading2']))
                story.append(Paragraph(self.character_data['specialAbilities']['rank8'], normal_style))
                story.append(Spacer(1, 6))
            story.append(PageBreak())

            # Gear Die Page
            story.append(Paragraph("Gear Die", section_style))
            gear_info = []
            for die in ['d4', 'd6', 'd8', 'd10', 'd12']:
                slots = self.character_data['gearDieSlots'][die]
                gear_info.append([f"{die} Slots ({slots}):", ""])
                for entry in self.character_data['gearDieEntries'][die]:
                    if entry:
                        gear_info.append(["", f"• {entry}"])
            gear_table = Table(gear_info, colWidths=[2*inch, 3*inch])
            gear_table.setStyle(TableStyle([
                ('ALIGN', (0, 0), (-1, -1), 'LEFT'),
                ('FONTNAME', (0, 0), (-1, -1), 'Helvetica-Bold'),
                ('FONTSIZE', (0, 0), (-1, -1), 10),
                ('BOTTOMPADDING', (0, 0), (-1, -1), 6),
            ]))
            story.append(gear_table)
            story.append(PageBreak())

            # Inventory and Resources Page
            story.append(Paragraph("Inventory", section_style))
            
            # Stored Equipment
            story.append(Paragraph("Stored Equipment:", styles['Heading2']))
            for item in self.character_data['inventory']['stored']:
                story.append(Paragraph(f"• {item['name']} ({item['quantity']})", normal_style))
            story.append(Spacer(1, 6))
            
            # Magic Bag
            story.append(Paragraph("Magic Bag:", styles['Heading2']))
            for item in self.character_data['inventory']['magic']:
                story.append(Paragraph(f"• {item['name']} ({item['quantity']})", normal_style))
            story.append(Spacer(1, 6))
            
            # Stored Magic Items
            story.append(Paragraph("Stored Magic Items:", styles['Heading2']))
            for item in self.character_data['inventory']['stored_magic']:
                story.append(Paragraph(f"• {item['name']} ({item['quantity']})", normal_style))
            story.append(Spacer(1, 6))
            
            # Elsewhere
            story.append(Paragraph("Elsewhere:", styles['Heading2']))
            for item in self.character_data['inventory']['elsewhere']:
                location = item.get('location', '')
                story.append(Paragraph(f"• {item['name']} ({item['quantity']}) - {location}", normal_style))
            story.append(Spacer(1, 6))

            # Resources
            story.append(Paragraph("Resources:", styles['Heading2']))
            resources_info = [
                ["Money:", str(self.character_data['money'])],
                ["Magic Dust:", str(self.character_data['magicDust'])]
            ]
            resources_table = Table(resources_info, colWidths=[2*inch, 3*inch])
            resources_table.setStyle(TableStyle([
                ('ALIGN', (0, 0), (-1, -1), 'LEFT'),
                ('FONTNAME', (0, 0), (-1, -1), 'Helvetica-Bold'),
                ('FONTSIZE', (0, 0), (-1, -1), 10),
                ('BOTTOMPADDING', (0, 0), (-1, -1), 6),
            ]))
            story.append(resources_table)

            # Build the PDF
            doc.build(story, onFirstPage=self.add_page_number, onLaterPages=self.add_page_number)
            messagebox.showinfo("Success", "Character sheet saved as PDF successfully!")
            
        except Exception as e:
            messagebox.showerror("Error", f"Failed to create PDF: {str(e)}")

    def add_page_number(self, canvas, doc):
        """Add page numbers to the PDF"""
        page_num = canvas.getPageNumber()
        text = f"Page {page_num}"
        canvas.saveState()
        canvas.setFont('Helvetica', 9)
        canvas.drawRightString(doc.pagesize[0] - 50, 50, text)
        canvas.restoreState()

    def update_gui_from_data(self):
        # Update all GUI elements with character data
        self.name_entry.delete(0, tk.END)
        self.name_entry.insert(0, self.character_data['name'])

        self.player_name_entry.delete(0, tk.END)
        self.player_name_entry.insert(0, self.character_data['playerName'])

        self.race_var.set(self.character_data['race'])
        self.profession_entry.delete(0, tk.END)
        self.profession_entry.insert(0, self.character_data['profession'])
        self.rank_var.set(str(self.character_data['rank']))
        self.current_points_var.set(str(self.character_data['rankPoints'] % 25))

        # Update magic items
        for i, entry in enumerate(self.magic_item_entries):
            entry.delete(0, tk.END)
            if i < len(self.character_data['magicalItems']):
                entry.insert(0, self.character_data['magicalItems'][i])

        # Update aspect values and lock choices
        self.choices_locked = True  # Lock choices by default when loading
        self.lock_button.config(state='disabled')  # Disable the lock button
        
        for aspect in ['melee', 'ranged', 'rogue', 'magic']:
            self.aspect_vars[aspect].set(self.character_data['aspects'][aspect])
            combo = getattr(self, f'{aspect}_combo')
            combo.config(state='disabled')  # Disable the combobox
            
            # Update selected dice tracking
            die_value = self.character_data['aspects'][aspect]
            if die_value in self.selected_dice:
                self.selected_dice[die_value] = aspect
            
            # Update the modifier display
            self.update_modifier_display(aspect)

        # Update aspect increases tracking
        current_rank = self.character_data['rank']
        if current_rank % 2 == 0 and current_rank > 1:
            if current_rank not in self.character_data['aspectIncreases']['history']:
                self.character_data['aspectIncreases']['history'][current_rank] = 0
            self.character_data['aspectIncreases']['used'] = self.character_data['aspectIncreases']['history'][current_rank]

        self.hp_entry.delete(0, tk.END)
        self.hp_entry.insert(0, str(self.character_data['combatStats']['hp']))

        # Calculate and update max HP
        self.calculate_max_hp()

        self.initiative_entry.delete(0, tk.END)
        self.initiative_entry.insert(0, str(self.character_data['combatStats']['initiative']))

        self.hero_points_entry.delete(0, tk.END)
        self.hero_points_entry.insert(0, str(self.character_data['combatStats']['heroPoints']))

        # Update money and magic dust
        self.money_entry.delete(0, tk.END)
        self.money_entry.insert(0, str(self.character_data['money']))
        
        self.magic_dust_entry.delete(0, tk.END)
        self.magic_dust_entry.insert(0, str(self.character_data['magicDust']))

        self.ability_1_text.delete(1.0, tk.END)
        self.ability_1_text.insert(1.0, self.character_data['specialAbilities']['rank1'])

        self.ability_4_text.delete(1.0, tk.END)
        self.ability_4_text.insert(1.0, self.character_data['specialAbilities']['rank4'])

        self.ability_8_text.delete(1.0, tk.END)
        self.ability_8_text.insert(1.0, self.character_data['specialAbilities']['rank8'])

        # Update inventory lists
        self.stored_listbox.delete(0, tk.END)
        for item in self.character_data['inventory']['stored']:
            self.stored_listbox.insert(tk.END, f"{item['name']} ({item['quantity']})")

        self.magic_listbox.delete(0, tk.END)
        for item in self.character_data['inventory']['magic']:
            self.magic_listbox.insert(tk.END, f"{item['name']} ({item['quantity']})")

        self.stored_magic_listbox.delete(0, tk.END)
        for item in self.character_data['inventory']['stored_magic']:
            self.stored_magic_listbox.insert(tk.END, f"{item['name']} ({item['quantity']})")

        self.elsewhere_listbox.delete(0, tk.END)
        for item in self.character_data['inventory']['elsewhere']:
            location = item.get('location', '')
            self.elsewhere_listbox.insert(tk.END, f"{item['name']} ({item['quantity']}) - {location}")

        # Update gear die slots and entries
        if 'gearDieSlots' in self.character_data:
            # Update gear die slot variables
            for die in ['d4', 'd6', 'd8', 'd10', 'd12']:
                current_slots = self.character_data['gearDieSlots'].get(die, 0)
                self.gear_die_slots[die].set(str(current_slots))
            
            # Recreate the gear die tab to show all slots
            self.create_gear_die_tab()
            
            # Update gear die entries with saved data
            if 'gearDieEntries' in self.character_data:
                for die in ['d4', 'd6', 'd8', 'd10', 'd12']:
                    for i, entry in enumerate(self.gear_die_entries[die]):
                        if i < len(self.character_data['gearDieEntries'][die]):
                            entry.delete(0, tk.END)
                            entry.insert(0, self.character_data['gearDieEntries'][die][i])

        # Update ability visibility
        self.update_ability_visibility()

    def add_rank_points(self):
        """Add points to total rank points"""
        try:
            points_to_add = int(self.add_points_var.get())
            if points_to_add < 0:
                messagebox.showwarning("Invalid Input", "Cannot add negative points.")
                return
                
            current_total = int(self.total_rank_points_var.get())
            new_total = current_total + points_to_add
            self.total_rank_points_var.set(str(new_total))
            self.add_points_var.set("0")  # Reset the add points entry
        except ValueError:
            messagebox.showwarning("Invalid Input", "Please enter a valid number of points.")

    def lock_aspect_choices(self):
        """Lock the current aspect choices and disable further changes"""
        # Check if all aspects have been assigned
        if any(self.selected_dice[die] is None for die in ['d6', 'd8', 'd10', 'd12']):
            messagebox.showwarning("Incomplete Selection", 
                                "Please assign all die types (d6, d8, d10, d12) before locking choices.")
            return
        
        # Lock choices
        self.choices_locked = True
        self.lock_button.config(state='disabled')  # Disable the button after locking
        for aspect in ['melee', 'ranged', 'rogue', 'magic']:
            combo = getattr(self, f'{aspect}_combo')
            combo.config(state='disabled')

    def get_die_modifier(self, die_type):
        """Get the modifier for a given die type"""
        modifiers = {
            'd4': -1,
            'd6': 0,
            'd8': 1,
            'd10': 2,
            'd12': 3
        }
        return modifiers.get(die_type, 0)

    def update_modifier_display(self, aspect):
        """Update the modifier display for an aspect"""
        die_type = self.aspect_vars[aspect].get()
        modifier = self.get_die_modifier(die_type)
        modifier_text = f"{modifier:+d}"  # Format with + or - sign
        self.modifier_vars[aspect].set(modifier_text)

    def on_aspect_change(self, aspect):
        """Handle changes to aspect die selections"""
        if self.choices_locked:
            return
            
        new_value = self.aspect_vars[aspect].get()
        
        # Handle hidden state
        if new_value == '*':
            self.choices_locked = True
            return
        
        # Check if this die value is already selected by another aspect
        if new_value in self.selected_dice and self.selected_dice[new_value] is not None:
            # Revert the change
            self.aspect_vars[aspect].set('d4')
            messagebox.showwarning("Invalid Selection", 
                                 f"The {new_value} die is already assigned to {self.selected_dice[new_value].capitalize()}.")
            return
        
        # Update the selected dice tracking
        for die, selected_aspect in self.selected_dice.items():
            if selected_aspect == aspect:
                self.selected_dice[die] = None
        if new_value in self.selected_dice:
            self.selected_dice[new_value] = aspect
        
        # Update the modifier display
        self.update_modifier_display(aspect)
        
        # Update available options for all aspects
        self.update_aspect_options()

    def update_aspect_options(self):
        """Update available options for each aspect based on current selections"""
        if self.choices_locked:
            return
            
        for aspect in ['melee', 'ranged', 'rogue', 'magic']:
            combo = getattr(self, f'{aspect}_combo')
            current_value = self.aspect_vars[aspect].get()
            
            # Skip if aspect is hidden
            if current_value == '*':
                continue
            
            # If this aspect has a value, keep it
            if current_value:
                continue
            
            # Update available options
            available_values = ['d4', '*']  # Always include d4 and hidden option
            for die in ['d6', 'd8', 'd10', 'd12']:
                if self.selected_dice[die] is None:
                    available_values.append(die)
            
            combo['values'] = available_values

    def toggle_hidden(self, aspect):
        """Toggle the hidden state of an aspect"""
        self.aspect_hidden[aspect] = not self.aspect_hidden[aspect]
        button = getattr(self, f'{aspect}_hidden_button')
        
        if self.aspect_hidden[aspect]:
            button.config(style='Hidden.TButton')
            # Store the current value before hiding
            self.character_data['aspects'][f'{aspect}_hidden'] = self.aspect_vars[aspect].get()
            self.aspect_vars[aspect].set('*')
        else:
            button.config(style='TButton')
            # Restore the previous value
            if f'{aspect}_hidden' in self.character_data['aspects']:
                self.aspect_vars[aspect].set(self.character_data['aspects'][f'{aspect}_hidden'])
            else:
                self.aspect_vars[aspect].set('d4')

    def on_race_change(self):
        """Handle race changes"""
        race = self.race_var.get()
        self.character_data['race'] = race
        # Recalculate max HP when race changes
        self.calculate_max_hp()
        # Update ability visibility when race changes
        self.update_ability_visibility()

    def roll_dice(self, die_type):
        """Roll a single die of the specified type"""
        import random
        try:
            sides = int(die_type[1:])  # Extract number from 'dX'
            result = random.randint(1, sides)
            
            # Calculate total modifiers from checked aspects
            total_modifier = 0
            checked_aspects = []
            for aspect in ['melee', 'ranged', 'rogue', 'magic']:
                if self.aspect_check_vars[aspect].get():
                    die_type = self.aspect_vars[aspect].get()
                    modifier = self.get_die_modifier(die_type)
                    total_modifier += modifier
                    checked_aspects.append(f"{aspect.capitalize()}({modifier:+d})")
            
            # Add rank to modifier
            rank = self.character_data['rank']
            total_modifier += rank
            
            # Calculate final result
            final_result = result + total_modifier
            
            # Format the result text
            result_text = f"{die_type}: {result}"
            if total_modifier != 0:
                result_text += f" + {total_modifier} (Rank:{rank}"
                if checked_aspects:
                    result_text += f", {' '.join(checked_aspects)}"
                result_text += f") = {final_result}"
            
            self.dice_result_var.set(result_text)
            self.add_to_roll_history(result_text)
        except:
            self.dice_result_var.set("Invalid die type!")

    def roll_custom_dice(self, dice_string):
        """Roll custom dice based on input string (e.g., '2d6+3')"""
        import random
        try:
            # Parse the dice string
            parts = dice_string.split('+')
            dice_part = parts[0]
            base_modifier = int(parts[1]) if len(parts) > 1 else 0
            
            # Parse number of dice and sides
            num_dice, sides = map(int, dice_part.split('d'))
            
            # Roll the dice
            results = [random.randint(1, sides) for _ in range(num_dice)]
            total = sum(results) + base_modifier
            
            # Calculate total modifiers from checked aspects
            total_modifier = 0
            checked_aspects = []
            for aspect in ['melee', 'ranged', 'rogue', 'magic']:
                if self.aspect_check_vars[aspect].get():
                    die_type = self.aspect_vars[aspect].get()
                    modifier = self.get_die_modifier(die_type)
                    total_modifier += modifier
                    checked_aspects.append(f"{aspect.capitalize()}({modifier:+d})")
            
            # Add rank to modifier
            rank = self.character_data['rank']
            total_modifier += rank
            
            # Calculate final result
            final_result = total + total_modifier
            
            # Format the result
            if num_dice == 1:
                result_text = f"{dice_string}: {total}"
            else:
                result_text = f"{dice_string}: {results} = {total}"
                if base_modifier != 0:
                    result_text += f" + {base_modifier}"
            
            if total_modifier != 0:
                result_text += f" + {total_modifier} (Rank:{rank}"
                if checked_aspects:
                    result_text += f", {' '.join(checked_aspects)}"
                result_text += f") = {final_result}"
            
            self.dice_result_var.set(result_text)
            self.add_to_roll_history(result_text)
        except:
            self.dice_result_var.set("Invalid dice format! Use format like '2d6+3'")

    def add_to_roll_history(self, result_text):
        """Add a roll result to the history"""
        # Add to the beginning of the list (most recent first)
        self.roll_history.insert(0, result_text)
        # Keep only the last 20 rolls
        if len(self.roll_history) > 20:
            self.roll_history.pop()
        # Update the listbox
        self.roll_history_listbox.delete(0, tk.END)
        for roll in self.roll_history:
            self.roll_history_listbox.insert(tk.END, roll)

    def clear_roll_history(self):
        """Clear the roll history"""
        self.roll_history = []
        self.roll_history_listbox.delete(0, tk.END)

    def adjust_die_value(self, aspect, change):
        """Adjust the die value of an aspect"""
        current_value = self.aspect_vars[aspect].get()
        if current_value == '*':
            return
            
        # Convert current value to number
        current_num = int(current_value[1:])
        
        # Prevent increasing beyond d12
        if change > 0 and current_num == 12:
            messagebox.showwarning("Maximum Value Reached", "Cannot increase aspect beyond d12.")
            return
            
        # Calculate new value
        new_num = current_num + (2 * change)  # Change by 2 to go d4->d6->d8->d10->d12
        new_num = max(4, min(12, new_num))  # Clamp between d4 and d12
            
        new_value = f'd{new_num}'
        
        # Check if trying to increase
        if change > 0:
            # Check if increases are available
            if self.character_data['aspectIncreases']['used'] >= self.character_data['aspectIncreases']['allowed']:
                messagebox.showwarning("No Increases Available", 
                                     f"You have used all {self.character_data['aspectIncreases']['allowed']} increases allowed.")
                return
        
        # Only check for duplicate die values if choices are not locked
        if not self.choices_locked:
            if new_value in self.selected_dice and self.selected_dice[new_value] is not None:
                messagebox.showwarning("Invalid Selection", 
                                     f"The {new_value} die is already assigned to {self.selected_dice[new_value].capitalize()}.")
                return
            
        # Update the value
        self.aspect_vars[aspect].set(new_value)
        
        # Update the modifier display
        self.update_modifier_display(aspect)
        
        # Update tracking
        for die, selected_aspect in self.selected_dice.items():
            if selected_aspect == aspect:
                self.selected_dice[die] = None
        if new_value in self.selected_dice:
            self.selected_dice[new_value] = aspect
            
        # Update aspect increases tracking
        if change > 0:
            self.character_data['aspectIncreases']['used'] += 1
            self.character_data['aspectIncreases']['history'][self.character_data['rank']] = self.character_data['aspectIncreases']['used']
            
        # Update available options
        self.update_aspect_options()

def main():
    root = tk.Tk()
    app = CharacterSheetGUI(root)
    root.mainloop()

if __name__ == "__main__":
    main() 