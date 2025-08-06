import tkinter as tk
from tkinter import ttk
import random

class BasicInfoTab:
    def __init__(self, parent, character_data, type_callback=None, gear_die_tab=None):
        self.parent = parent
        self.character_data = character_data
        self.type_callback = type_callback
        self.gear_die_tab = gear_die_tab
        self.tab = ttk.Frame(parent)
        self.create_tab()
        
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

        # Profession Selection
        ttk.Label(frame, text="Profession:").grid(row=3, column=0, padx=5, pady=2)
        self.profession_entry = ttk.Entry(frame)
        self.profession_entry.grid(row=3, column=1, padx=5, pady=2)

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

        # Magic Items Frame
        magic_items_frame = ttk.LabelFrame(frame, text="Magic Items")
        magic_items_frame.grid(row=6, column=0, columnspan=2, padx=5, pady=5, sticky='ew')
        
        # Create 7 magic item entries
        self.magic_item_entries = []
        for i in range(7):
            ttk.Label(magic_items_frame, text=f"Magic Item {i+1}:").grid(row=i, column=0, padx=5, pady=2)
            entry = ttk.Entry(magic_items_frame, width=60)  # Increased width from default to 60
            entry.grid(row=i, column=1, padx=5, pady=2, sticky='ew')
            self.magic_item_entries.append(entry)

        # Combat Stats Frame
        combat_frame = ttk.LabelFrame(frame, text="Combat Statistics")
        combat_frame.grid(row=7, column=0, columnspan=2, padx=5, pady=5, sticky='ew')

        # HP
        ttk.Label(combat_frame, text="Current HP:").grid(row=0, column=0, padx=5, pady=2)
        self.hp_entry = ttk.Entry(combat_frame)
        self.hp_entry.grid(row=0, column=1, padx=5, pady=2)

        ttk.Label(combat_frame, text="/").grid(row=0, column=2, padx=5, pady=2)
        ttk.Label(combat_frame, text="Max HP:").grid(row=0, column=3, padx=5, pady=2)
        self.max_hp_entry = ttk.Entry(combat_frame)
        self.max_hp_entry.grid(row=0, column=4, padx=5, pady=2)

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

        # Hero Points
        ttk.Label(combat_frame, text="Hero Points:").grid(row=3, column=0, padx=5, pady=2)
        self.hero_points_entry = ttk.Entry(combat_frame)
        self.hero_points_entry.grid(row=3, column=1, padx=5, pady=2)

        # Resources
        resources_frame = ttk.LabelFrame(frame, text="Resources")
        resources_frame.grid(row=8, column=0, columnspan=2, padx=5, pady=5, sticky='ew')

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
        
        # Initialize initiative display
        self.update_initiative_display()

    def calculate_max_hp(self):
        """Calculate max HP based on race, rank, and gear die allocations"""
        base_hp = 20
        rank = int(self.rank_var.get())
        
        # Race HP modifiers
        race_hp_modifiers = {
            'Half-Dragon': 10,
            'Human': 0,
            'Elf': -5,
            'Half Elf': -2,
            'Galdur': 5,
            'Gnome': -10,
            'Halfling': -10,
            'Dwarf': 5,
            'Minotaur': 15,
            'Half Giant': 20
        }
        
        race_modifier = race_hp_modifiers.get(self.race_var.get(), 0)
        rank_hp = rank * 5
        
        # Calculate base max HP
        max_hp = base_hp + race_modifier + rank_hp
        
        # Add gear die hitpoints if gear die tab is available
        if self.gear_die_tab:
            gear_die_hp = self.gear_die_tab.calculate_gear_die_hitpoints()
            max_hp += gear_die_hp
        
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
        """Update the max HP display with current calculation"""
        max_hp = self.calculate_max_hp()
        self.max_hp_entry.delete(0, tk.END)
        self.max_hp_entry.insert(0, str(max_hp))

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

    def roll_dice(self, die_type):
        """Roll a specific die type"""
        die_map = {'d4': 4, 'd6': 6, 'd8': 8, 'd10': 10, 'd12': 12, 'd20': 20, 'd100': 100}
        
        if die_type in die_map:
            result = random.randint(1, die_map[die_type])
            self.dice_result_var.set(f"Rolled {die_type}: {result}")
            self.add_to_roll_history(f"{die_type}: {result}")
        else:
            self.dice_result_var.set("Invalid die type")

    def roll_custom_dice(self, dice_string):
        """Roll custom dice (e.g., '2d6+3')"""
        try:
            # Parse dice string like "2d6+3" or "1d20"
            parts = dice_string.lower().replace(' ', '').split('d')
            if len(parts) != 2:
                raise ValueError("Invalid dice format")
            
            num_dice = int(parts[0]) if parts[0] else 1
            die_part = parts[1]
            
            # Check for modifiers
            if '+' in die_part:
                die_size, modifier = die_part.split('+')
                modifier = int(modifier)
            elif '-' in die_part:
                die_size, modifier = die_part.split('-')
                modifier = -int(modifier)
            else:
                die_size = die_part
                modifier = 0
            
            die_size = int(die_size)
            
            # Roll the dice
            total = sum(random.randint(1, die_size) for _ in range(num_dice)) + modifier
            
            result_text = f"{dice_string}: {total}"
            if modifier != 0:
                result_text += f" (dice: {total - modifier}, modifier: {modifier:+d})"
            
            self.dice_result_var.set(result_text)
            self.add_to_roll_history(result_text)
            
        except (ValueError, IndexError):
            self.dice_result_var.set("Invalid dice format. Use format like '2d6+3'")

    def add_to_roll_history(self, result_text):
        """Add roll result to history"""
        self.roll_history.append(result_text)
        self.roll_history_listbox.insert(0, result_text)
        
        # Keep only last 50 entries
        if len(self.roll_history) > 50:
            self.roll_history.pop(0)
            self.roll_history_listbox.delete(tk.END)

    def clear_roll_history(self):
        """Clear the roll history"""
        self.roll_history.clear()
        self.roll_history_listbox.delete(0, tk.END)

    def get_data(self):
        """Get all data from the tab"""
        # Calculate indoor speed dynamically
        rank = int(self.rank_var.get())
        unarmed_combat = self.unarmed_combat_var.get()
        
        if unarmed_combat:
            indoor_speed = 35 + (5 * rank)
        else:
            indoor_speed = 30
        
        return {
            'name': self.name_entry.get(),
            'playerName': self.player_name_entry.get(),
            'race': self.race_var.get(),
            'profession': self.profession_entry.get(),
            'type': self.type_var.get(),
            'unarmedCombat': self.unarmed_combat_var.get(),
            'rank': int(self.rank_var.get()),
            'rankPoints': int(self.total_rank_points_var.get()),
            'magicItems': [entry.get() for entry in self.magic_item_entries],
            'combatStats': {
                'hp': int(self.hp_entry.get() or 0),
                'maxHp': int(self.max_hp_entry.get() or 0),
                'indoorSpeed': indoor_speed,
                'initiative': self.calculate_initiative(),
                'heroPoints': int(self.hero_points_entry.get() or 0)
            },
            'resources': {
                'money': int(self.money_entry.get() or 0),
                'magicDust': int(self.magic_dust_entry.get() or 0)
            }
        }

    def set_data(self, data):
        """Set data in the tab"""
        self.name_entry.delete(0, tk.END)
        self.name_entry.insert(0, data.get('name', ''))
        
        self.player_name_entry.delete(0, tk.END)
        self.player_name_entry.insert(0, data.get('playerName', ''))
        
        self.race_var.set(data.get('race', ''))
        
        self.profession_entry.delete(0, tk.END)
        self.profession_entry.insert(0, data.get('profession', ''))
        
        self.type_var.set(data.get('type', 'Non-Specialized'))
        
        self.unarmed_combat_var.set(data.get('unarmedCombat', False))
        
        self.total_rank_points_var.set(str(data.get('rankPoints', 0)))
        
        # Calculate and display indoor speed based on loaded data
        self.calculate_indoor_speed()
        
        # Set magic items
        magic_items = data.get('magicItems', [])
        for i, entry in enumerate(self.magic_item_entries):
            entry.delete(0, tk.END)
            if i < len(magic_items):
                entry.insert(0, magic_items[i])
        
        # Set combat stats
        combat_stats = data.get('combatStats', {})
        self.hp_entry.delete(0, tk.END)
        self.hp_entry.insert(0, str(combat_stats.get('hp', 0)))
        
        self.max_hp_entry.delete(0, tk.END)
        self.max_hp_entry.insert(0, str(combat_stats.get('maxHp', 0)))
        
        # Initiative is calculated automatically, so we just update the display
        self.update_initiative_display()
        
        self.hero_points_entry.delete(0, tk.END)
        self.hero_points_entry.insert(0, str(combat_stats.get('heroPoints', 0)))
        
        # Set resources
        resources = data.get('resources', {})
        self.money_entry.delete(0, tk.END)
        self.money_entry.insert(0, str(resources.get('money', 0)))
        
        self.magic_dust_entry.delete(0, tk.END)
        self.magic_dust_entry.insert(0, str(resources.get('magicDust', 0))) 

    def lock_fields(self):
        """Disable editing of key character info fields."""
        try:
            self.name_entry.config(state='disabled')
            self.player_name_entry.config(state='disabled')
            self.race_combo.config(state='disabled')
            self.profession_entry.config(state='disabled')
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
            self.profession_entry.config(state='normal')
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

 