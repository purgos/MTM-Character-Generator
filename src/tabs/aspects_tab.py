import tkinter as tk
from tkinter import ttk

class AspectsTab:
    def __init__(self, parent, character_data, on_data_change, get_rank_callback):
        self.parent = parent
        self.character_data = character_data
        self.tab = ttk.Frame(parent)
        
        # Initialize aspect variables dictionary
        self.aspect_vars = {}
        self.modifier_vars = {}
        self.choices_locked = False
        
        # Dictionary to track which die values are already selected
        self.selected_dice = {}
        
        # Gear die increase tracking
        self.aspect_die_increases = 0  # Single variable for available increases
        self.locked_aspects = {}  # Store the aspect values when choices are locked
        
        self.on_data_change = on_data_change
        self.get_rank = get_rank_callback
        self.rank_last_checked = self.get_rank()
        self.locked = False
        self.abilities_callback = None
        
        self.create_tab()
        self.create_widgets()
        self.update_lock_state()  # Initial lock state
    
    def set_abilities_callback(self, callback):
        """Set callback to update abilities dropdown when D12 aspect changes"""
        self.abilities_callback = callback
        
    def create_tab(self):
        """Create the aspects tab"""
        # Aspects Frame
        frame = ttk.LabelFrame(self.tab, text="Character Aspects")
        frame.pack(fill='both', expand=True, padx=5, pady=5)

        # Create a frame for instructions
        instructions_frame = ttk.Frame(frame)
        instructions_frame.pack(fill='x', padx=5, pady=5)
        ttk.Label(instructions_frame, 
                 text="Select one aspect for each die type (d6, d8, d10, d12).\nNULL means no die value assigned.\nIf options are locked to NULL, select from the highest available dice.\nOnce finished lock choices.\nUse + and - buttons to increase/decrease die values.\nModifiers: NULL=--, d4=-1, d6=0, d8=+1, d10=+2, d12=+3",
                 wraplength=400).pack()

        # Add aspect die increases display
        increases_frame = ttk.Frame(frame)
        increases_frame.pack(fill='x', padx=5, pady=5)
        
        self.aspect_die_increases_label = ttk.Label(increases_frame, text="Aspect Die Increases: 0 Available")
        self.aspect_die_increases_label.pack(side='left', padx=5)
        
        # Add lock button frame
        lock_frame = ttk.Frame(frame)
        lock_frame.pack(fill='x', padx=5, pady=5)
        # self.lock_button = ttk.Button(lock_frame, text="Lock Choices", command=self.lock_aspect_choices)
        # self.lock_button.pack(side='right', padx=5)

        aspects = ['melee', 'ranged', 'rogue', 'magic']
        dice_values = ['d6', 'd8', 'd10', 'd12']
        
        # Dictionary to track which die values are already selected
        self.selected_dice = {die: None for die in dice_values}
        
        # Create aspect frames
        for i, aspect in enumerate(aspects):
            aspect_frame = ttk.Frame(frame)
            aspect_frame.pack(fill='x', padx=5, pady=2)
            
            ttk.Label(aspect_frame, text=aspect.capitalize() + ":", width=10).pack(side='left', padx=5)
            
            self.aspect_vars[aspect] = tk.StringVar(value='d6')
            aspect_combo = ttk.Combobox(aspect_frame, textvariable=self.aspect_vars[aspect], state='readonly')
            aspect_combo['values'] = dice_values
            aspect_combo.pack(side='left', padx=5)
            setattr(self, f'{aspect}_combo', aspect_combo)
            
            # Add Disabled label (hidden by default)
            disabled_label = ttk.Label(aspect_frame, text="Disabled", foreground='red')
            disabled_label.pack(side='left', padx=2)
            disabled_label.pack_forget()
            setattr(self, f'{aspect}_disabled_label', disabled_label)
            
            # Add modifier label
            self.modifier_vars[aspect] = tk.StringVar(value="--")
            modifier_label = ttk.Label(aspect_frame, textvariable=self.modifier_vars[aspect], width=4)
            modifier_label.pack(side='left', padx=5)
            
            # Add increase/decrease buttons
            decrease_button = ttk.Button(aspect_frame, text="-", width=2,
                                       command=lambda a=aspect: self.adjust_die_value(a, -1))
            decrease_button.pack(side='left', padx=5)
            
            increase_button = ttk.Button(aspect_frame, text="+", width=2,
                                       command=lambda a=aspect: self.adjust_die_value(a, 1))
            increase_button.pack(side='left', padx=5)
            
            print(f"Created buttons for {aspect}: - and +")

            # Add trace to monitor changes
            self.aspect_vars[aspect].trace_add('write', lambda *args, a=aspect: self.on_aspect_change(a))
            
            # Store the combobox and buttons for later reference
            setattr(self, f'{aspect}_decrease_button', decrease_button)
            setattr(self, f'{aspect}_increase_button', increase_button)

        # Test button functionality
        self.test_button_functionality()
        
        # Initialize aspect values from character data
        self.initialize_from_character_data()

    def create_widgets(self):
        """Create widgets for the aspects tab."""
        # This method is called from __init__ to set up the widgets.
        # The lock button creation is removed as per the edit hint.
        pass # No specific widgets to create here, as the tab is a frame.

    def initialize_from_character_data(self):
        """Initialize aspect values from character data"""
        print("[DEBUG] Initializing aspects from character data...")
        for aspect in ['melee', 'ranged', 'rogue', 'magic']:
            if aspect in self.character_data['aspects']:
                value = self.character_data['aspects'][aspect]
                print(f"[DEBUG] Setting {aspect} to {value}")
                if value != 'NULL':
                    self.aspect_vars[aspect].set(value)
                    self.update_modifier_display(aspect)
                else:
                    # Handle NULL values by showing disabled state
                    self.set_aspect_value(aspect, 'NULL')

    def on_rank_change(self):
        """Called when rank changes. Lock fields if rank > 1."""
        current_rank = self.get_rank()
        print(f"[DEBUG] on_rank_change called: current_rank={current_rank}, self.locked={self.locked}")
        if current_rank > 1 and not self.locked:
            print(f"[DEBUG] Setting locked=True and choices_locked=True")
            self.locked = True
            self.choices_locked = True  # Set choices locked when fields are locked
            
            # Store the current aspect values as the baseline for locked aspects
            self.locked_aspects = {aspect: self.aspect_vars[aspect].get() for aspect in self.aspect_vars}
            print(f"[DEBUG] Locked aspects: {self.locked_aspects}")
            
            self.update_lock_state()
        else:
            print(f"[DEBUG] Not setting locked (current_rank={current_rank}, already_locked={self.locked})")
        self.rank_last_checked = current_rank

    def update_lock_state(self):
        """Enable or disable editing of fields based on lock state."""
        lock = self.locked
        try:
            for aspect in ['melee', 'ranged', 'rogue', 'magic']:
                decrease_button = getattr(self, f'{aspect}_decrease_button')
                increase_button = getattr(self, f'{aspect}_increase_button')
                combo = getattr(self, f'{aspect}_combo')
                disabled_label = getattr(self, f'{aspect}_disabled_label')
                current_die = self.aspect_vars[aspect].get()
                
                # Always disable comboboxes when locked
                combo.config(state='disabled' if lock else 'readonly')
                
                # Always hide disabled label when locked
                disabled_label.pack_forget()
                
                # Allow increase buttons if aspect die increases are available
                if lock and self.aspect_die_increases > 0:
                    increase_button.config(state='normal')
                    print(f"[DEBUG] {aspect} increase button enabled (locked, increases available)")
                else:
                    increase_button.config(state='disabled' if lock else 'normal')
                    print(f"[DEBUG] {aspect} increase button {'disabled' if lock else 'enabled'}")
                
                # Disable decrease button if at d4, otherwise enable based on lock state
                if current_die == 'd4':
                    decrease_button.config(state='disabled')
                    print(f"[DEBUG] {aspect} decrease button disabled (at d4)")
                elif lock:
                    decrease_button.config(state='normal')
                    print(f"[DEBUG] {aspect} decrease button enabled (locked, not at d4)")
                else:
                    decrease_button.config(state='normal')
                    print(f"[DEBUG] {aspect} decrease button enabled (unlocked)")
        except Exception as e:
            print(f"Error updating lock state: {e}")

    def periodic_check(self):
        """Periodically check for rank changes and update lock state."""
        # Check for rank change
        if self.get_rank() != self.rank_last_checked:
            self.on_rank_change()

    def lock_aspect_choices(self):
        """Lock the aspect choices to prevent further changes"""
        self.choices_locked = True
        # self.lock_button.config(text="Choices Locked", state='disabled') # This line is removed
        
        # Store the current aspect values as the baseline
        self.locked_aspects = {aspect: self.aspect_vars[aspect].get() for aspect in self.aspect_vars}
        
        # Update selected dice tracking for locked state
        self.update_selected_dice_for_locked_state()
        
        # Disable all comboboxes
        for aspect in ['melee', 'ranged', 'rogue', 'magic']:
            combo = getattr(self, f'{aspect}_combo')
            combo.config(state='disabled')

    def update_selected_dice_for_locked_state(self):
        """Update selected dice tracking when choices are locked"""
        # Clear current tracking
        for die in self.selected_dice:
            self.selected_dice[die] = None
        
        # Set tracking based on current locked values
        for aspect, die_value in self.aspect_vars.items():
            if die_value.get() in self.selected_dice:
                self.selected_dice[die_value.get()] = aspect

    def get_die_modifier(self, die_type):
        """Get the modifier for a die type"""
        modifiers = {'NULL': None, 'd4': -1, 'd6': 0, 'd8': 1, 'd10': 2, 'd12': 3}
        return modifiers.get(die_type, 0)

    def update_modifier_display(self, aspect):
        """Update the modifier display for an aspect"""
        current_die = self.aspect_vars[aspect].get()
        modifier = self.get_die_modifier(current_die)
        if modifier is None:
            self.modifier_vars[aspect].set("--")
        else:
            self.modifier_vars[aspect].set(f"{modifier:+d}")

    def on_aspect_change(self, aspect):
        """Handle aspect change"""
        current_die = self.aspect_vars[aspect].get()
        
        # Update modifier display
        self.update_modifier_display(aspect)
        
        # Update character data
        self.character_data['aspects'][aspect] = current_die
        
        # Track D12 at level 1
        current_rank = self.get_rank()
        if current_rank == 1 and current_die == 'd12':
            # Only set this if it hasn't been set yet, or replace if not locked
            if (self.character_data.get('levelOneD12Aspect') is None or 
                not self.choices_locked):
                self.character_data['levelOneD12Aspect'] = aspect
                print(f"[DEBUG] Level 1 D12 aspect set to: {aspect}")
                
                # Update abilities dropdown via callback
                if self.abilities_callback:
                    self.abilities_callback()
                    print(f"[DEBUG] Updated abilities dropdown for aspect: {aspect}")
        # Note: We no longer clear the D12 aspect when it loses D12 status
        # It will only be replaced if a different aspect reaches D12 before locking
        
        # Update selected dice tracking
        if not self.choices_locked:
            # Check if this die is already selected by another aspect
            conflicting_aspect = None
            for asp, die_value in self.aspect_vars.items():
                if asp != aspect and die_value.get() == current_die:
                    conflicting_aspect = asp
                    break
            
            # If there's a conflict, swap the dice
            if conflicting_aspect:
                # Get the die that was previously selected by the current aspect
                # We need to track what the current aspect had before this change
                # For now, let's use a simple approach - find an available die for the conflicting aspect
                available_dice = ['d6', 'd8', 'd10', 'd12']
                used_dice = set()
                for asp, die_value in self.aspect_vars.items():
                    if asp != conflicting_aspect and asp != aspect:
                        used_dice.add(die_value.get())
                
                # Find an available die for the conflicting aspect
                for die in available_dice:
                    if die not in used_dice:
                        self.aspect_vars[conflicting_aspect].set(die)
                        self.character_data['aspects'][conflicting_aspect] = die
                        self.update_modifier_display(conflicting_aspect)
                        break
            
            # Update selected dice tracking
            self.selected_dice = {die: None for die in ['d6', 'd8', 'd10', 'd12']}
            
            # Rebuild tracking based on current values
            for asp, die_value in self.aspect_vars.items():
                current_val = die_value.get()
                if (self.character_data['aspects'].get(asp) != 'NULL' and 
                    current_val in self.selected_dice):
                    self.selected_dice[current_val] = asp
            
            # Update available options for other aspects
            self.update_aspect_options()
            
            # If this is initial selection and a die was selected, remove it from other aspects' options
            if current_die in ['d6', 'd8', 'd10', 'd12']:
                # Count aspects with selected dice to see if this is still initial selection
                selected_aspects = 0
                for a in ['melee', 'ranged', 'rogue', 'magic']:
                    if self.aspect_vars[a].get() in ['d6', 'd8', 'd10', 'd12']:
                        selected_aspects += 1
                
                # If this is initial selection, remove the selected die from other aspects
                if selected_aspects <= 1:
                    for a in ['melee', 'ranged', 'rogue', 'magic']:
                        if a != aspect and not (a == 'ranged' and self.character_data.get('unarmedCombat', False)):
                            combo = getattr(self, f'{a}_combo')
                            current_values = list(combo['values'])
                            if current_die in current_values:
                                current_values.remove(current_die)
                                combo['values'] = current_values
        
        # Update aspect die increases display
        self.update_aspect_die_increases_display()
        
        # Update lock state to enable/disable buttons based on new die value
        if self.locked:
            self.update_lock_state()

    def update_aspect_die_increases_display(self):
        """Update the display of aspect die increases"""
        self.aspect_die_increases_label.config(text=f"Aspect Die Increases: {self.aspect_die_increases} Available")

    def is_higher_die(self, die1, die2):
        """Check if die1 is higher than die2"""
        die_order = ['NULL', 'd4', 'd6', 'd8', 'd10', 'd12']
        try:
            index1 = die_order.index(die1)
            index2 = die_order.index(die2)
            return index1 > index2
        except ValueError:
            return False

    def update_aspect_die_increases(self, increases):
        """Update the number of aspect die increases available"""
        self.aspect_die_increases = increases
        self.update_aspect_die_increases_display()
        
        # Update lock state to enable/disable increase buttons based on available increases
        if self.locked:
            self.update_lock_state()

    def use_aspect_die_increase(self):
        """Use one aspect die increase"""
        if self.aspect_die_increases > 0:
            self.aspect_die_increases -= 1
            self.update_aspect_die_increases_display()
            
            # Update lock state to disable increase buttons if no increases remain
            if self.locked:
                self.update_lock_state()
                
            return True
        return False

    def update_unarmed_combat_effects(self, unarmed_combat):
        """Update aspects based on unarmed combat status"""
        if unarmed_combat:
            # Set ranged aspect to NULL and lock it
            self.set_aspect_value('ranged', 'NULL')
            
            # Disable ranged aspect controls
            ranged_decrease = getattr(self, 'ranged_decrease_button')
            ranged_increase = getattr(self, 'ranged_increase_button')
            
            ranged_decrease.config(state='disabled')
            ranged_increase.config(state='disabled')
        else:
            # Re-enable ranged aspect controls
            ranged_combo = getattr(self, 'ranged_combo')
            ranged_decrease = getattr(self, 'ranged_decrease_button')
            ranged_increase = getattr(self, 'ranged_increase_button')
            
            ranged_combo.config(state='readonly')
            ranged_decrease.config(state='normal')
            ranged_increase.config(state='normal')
            
            # Update aspect options to reflect current state
            self.update_aspect_options()

    def update_aspect_options(self):
        """Update available options for aspects based on current selections"""
        if self.choices_locked:
            return
            
        aspects = ['melee', 'ranged', 'rogue', 'magic']
        dice_values = ['d6', 'd8', 'd10', 'd12']
        
        # Count how many aspects are NULL
        null_count = 0
        for aspect in aspects:
            if self.character_data['aspects'].get(aspect) == 'NULL':
                null_count += 1
        
        # Determine available dice based on NULL count
        if null_count == 0:
            # No aspects are NULL - show all dice
            available_dice = ['d6', 'd8', 'd10', 'd12']
        elif null_count == 1:
            # One aspect is NULL - show d8, d10, d12
            available_dice = ['d8', 'd10', 'd12']
        else:
            # Multiple aspects are NULL - show d10, d12
            available_dice = ['d10', 'd12']
        
        # Update selected dice tracking first
        self.update_selected_dice_for_current_state()
        
        # Update dropdown options for each aspect
        for aspect in aspects:
            combo = getattr(self, f'{aspect}_combo')
            current_value = self.aspect_vars[aspect].get()
            
            # Skip ranged aspect if it's locked due to unarmed combat
            if aspect == 'ranged' and self.character_data.get('unarmedCombat', False):
                continue
            
            # Skip aspects that are NULL (they show "Disabled" instead)
            if self.character_data['aspects'].get(aspect) == 'NULL':
                continue
            
            # Before locking, allow all available dice for reassignment
            # This allows swapping dice between aspects
            available_values = available_dice.copy()
            
            # Update combobox values
            combo['values'] = available_values
            
            # Only reset if current value is not in available values
            if current_value not in available_values and available_values:
                self.aspect_vars[aspect].set(available_values[0])

    def toggle_hidden(self, aspect):
        """Toggle visibility of aspect controls"""
        combo = getattr(self, f'{aspect}_combo')
        decrease_btn = getattr(self, f'{aspect}_decrease_button')
        increase_btn = getattr(self, f'{aspect}_increase_button')
        
        current_state = combo.cget('state')
        new_state = 'disabled' if current_state == 'readonly' else 'readonly'
        
        combo.config(state=new_state)
        decrease_btn.config(state=new_state)
        increase_btn.config(state=new_state)

    def adjust_die_value(self, aspect, change):
        """Adjust die value for an aspect"""
        print(f"[DEBUG] adjust_die_value called: aspect={aspect}, change={change}, choices_locked={self.choices_locked}, aspect_die_increases={self.aspect_die_increases}")
        print(f"[DEBUG] selected_dice: {self.selected_dice}")
        
        # Full dice order including NULL and d4 for internal use
        dice_values = ['NULL', 'd4', 'd6', 'd8', 'd10', 'd12']
        current_die = self.aspect_vars[aspect].get()
        
        if self.choices_locked:
            locked_value = self.locked_aspects.get(aspect, 'NULL')
            print(f"[DEBUG] Locked: current_die={current_die}, locked_value={locked_value}, available_increases={self.aspect_die_increases}")
            try:
                current_index = dice_values.index(current_die)
                new_index = max(0, min(len(dice_values) - 1, current_index + change))
                new_die = dice_values[new_index]
                print(f"[DEBUG] Would change from {current_die} to {new_die}")

                # Prevent decreasing to NULL after locking
                if change < 0 and new_die == 'NULL':
                    print(f"[DEBUG] Cannot decrease {aspect} to NULL after locking")
                    return

                # Only check for aspect die increase if the new value would be higher than the locked value
                # AND the current value is not already higher than the locked value
                if change > 0 and (self.is_higher_die(new_die, locked_value) and not self.is_higher_die(current_die, locked_value)):
                    print("[DEBUG] This would be a new increase beyond locked value")
                    if not self.use_aspect_die_increase():
                        print("[DEBUG] No increases available, returning")
                        return  # No increases available
                    print("[DEBUG] Used aspect die increase")

                # Update selected dice tracking to reflect current state for availability check
                self.update_selected_dice_for_current_state()

                # After locking, allow any increase or decrease (except to NULL)
                print(f"[DEBUG] Setting {aspect} to {new_die} (using aspect die increase/decrease, uniqueness not enforced)")
                self.aspect_vars[aspect].set(new_die)
                print(f"[DEBUG] {aspect} die value is now {self.aspect_vars[aspect].get()}")
                
                # Update modifier display
                self.update_modifier_display(aspect)
                
                # Update character data
                self.character_data['aspects'][aspect] = new_die
                
                # Track D12 at level 1 (even in locked state)
                current_rank = self.get_rank()
                if current_rank == 1 and new_die == 'd12':
                    # Only set this if it hasn't been set yet
                    if self.character_data.get('levelOneD12Aspect') is None:
                        self.character_data['levelOneD12Aspect'] = aspect
                        print(f"[DEBUG] Level 1 D12 aspect set to: {aspect} (locked state)")
                        
                        # Update abilities dropdown via callback
                        if self.abilities_callback:
                            self.abilities_callback()
                            print(f"[DEBUG] Updated abilities dropdown for aspect: {aspect} (locked state)")
                # Note: We no longer clear the D12 aspect when it loses D12 status in locked state
                # The original D12 aspect at level 1 is preserved
                
                # Update lock state
                self.update_lock_state()
                
            except ValueError:
                print(f"[DEBUG] Current die value '{current_die}' not found in dice_values")
        else:
            # Unlocked state - only allow selection from dropdown values
            dropdown_values = ['d6', 'd8', 'd10', 'd12']
            try:
                current_index = dropdown_values.index(current_die)
                new_index = max(0, min(len(dropdown_values) - 1, current_index + change))
                new_die = dropdown_values[new_index]
                
                # Check if the new die is available
                if new_die in ['NULL', 'd4'] or self.selected_dice[new_die] is None or self.selected_dice[new_die] == aspect:
                    self.aspect_vars[aspect].set(new_die)
                    self.update_modifier_display(aspect)
                    self.on_aspect_change(aspect)
                else:
                    print(f"[DEBUG] Die {new_die} is already selected by {self.selected_dice[new_die]}")
                    
            except ValueError:
                print(f"[DEBUG] Current die value '{current_die}' not found in dropdown_values")

    def update_selected_dice_for_current_state(self):
        """Update selected dice tracking to reflect current aspect values"""
        # Clear current tracking
        for die in self.selected_dice:
            self.selected_dice[die] = None
        
        # Set tracking based on current values
        for aspect, die_value in self.aspect_vars.items():
            current_value = die_value.get()
            if current_value in self.selected_dice:
                self.selected_dice[current_value] = aspect

    def get_data(self):
        """Get aspect data"""
        return {
            'aspects': self.character_data['aspects'],
            'choices_locked': self.choices_locked,
            'lockedAspects': self.locked_aspects,
            'aspectDieIncreases': self.aspect_die_increases,
            'levelOneD12Aspect': self.character_data.get('levelOneD12Aspect')
        }

    def set_data(self, data):
        """Set aspect data"""
        aspects_data = data.get('aspects', {})
        for aspect, die_value in aspects_data.items():
            if aspect in self.aspect_vars:
                self.set_aspect_value(aspect, die_value)
        
        self.choices_locked = data.get('choices_locked', False)
        if self.choices_locked:
            # self.lock_button.config(text="Choices Locked", state='disabled') # This line is removed
            for aspect in ['melee', 'ranged', 'rogue', 'magic']:
                combo = getattr(self, f'{aspect}_combo')
                combo.config(state='disabled')
        
        # Handle unarmed combat state
        unarmed_combat = data.get('unarmedCombat', False)
        if unarmed_combat:
            self.update_unarmed_combat_effects(True)
        
        # Handle aspect die increases
        self.aspect_die_increases = data.get('aspectDieIncreases', 0)
        
        # Handle locked aspects
        self.locked_aspects = data.get('lockedAspects', {})
        
        # Handle level 1 D12 aspect tracking
        level_one_d12_aspect = data.get('levelOneD12Aspect')
        if level_one_d12_aspect is not None:
            self.character_data['levelOneD12Aspect'] = level_one_d12_aspect
            print(f"[DEBUG] Loaded level 1 D12 aspect: {level_one_d12_aspect}")
        
        self.update_aspect_die_increases_display()
        
    def test_button_functionality(self):
        """Test that buttons are working correctly"""
        print("Testing button functionality...")
        print(f"Current aspect values: {self.aspect_vars}")
        print(f"Choices locked: {self.choices_locked}")
        print(f"Aspect die increases: {self.aspect_die_increases}")
        print(f"Selected dice: {self.selected_dice}")
        print(f"Locked aspects: {self.locked_aspects}")

    def set_aspect_value(self, aspect, value):
        """Set the value of a specific aspect"""
        print(f"[DEBUG] set_aspect_value called: aspect={aspect}, value={value}")
        if aspect in self.aspect_vars:
            # Update character data first
            self.character_data['aspects'][aspect] = value
            print(f"[DEBUG] Character data {aspect} set to: {self.character_data['aspects'][aspect]}")
            combo = getattr(self, f'{aspect}_combo')
            disabled_label = getattr(self, f'{aspect}_disabled_label')
            
            if value == 'NULL':
                combo.pack_forget()
                disabled_label.pack(side='left', padx=5)
                self.modifier_vars[aspect].set("--")
            else:
                disabled_label.pack_forget()
                combo.pack(side='left', padx=5)
                self.aspect_vars[aspect].set(value)
                self.update_modifier_display(aspect)
                print(f"[DEBUG] {aspect} StringVar set to: {value}")
        else:
            print(f"[DEBUG] Aspect {aspect} not found in aspect_vars")

    def lock_aspect(self, aspect):
        """Lock a specific aspect (disable its combobox and buttons)"""
        if aspect in self.aspect_vars:
            combo = getattr(self, f'{aspect}_combo')
            combo.config(state='disabled')
            
            # Disable increase and decrease buttons for this aspect
            increase_button = getattr(self, f'{aspect}_increase_button')
            decrease_button = getattr(self, f'{aspect}_decrease_button')
            increase_button.config(state='disabled')
            decrease_button.config(state='disabled')

    def unlock_aspect(self, aspect):
        """Unlock a specific aspect (enable its combobox and buttons)"""
        if aspect in self.aspect_vars:
            combo = getattr(self, f'{aspect}_combo')
            combo.config(state='readonly')
            
            # Re-enable increase and decrease buttons for this aspect
            increase_button = getattr(self, f'{aspect}_increase_button')
            decrease_button = getattr(self, f'{aspect}_decrease_button')
            
            # Re-enable buttons based on current lock state and aspect die increases
            if self.locked and self.aspect_die_increases > 0:
                increase_button.config(state='normal')
            elif not self.locked:
                increase_button.config(state='normal')
            else:
                increase_button.config(state='disabled')
            
            # Re-enable decrease button unless at d4
            current_die = self.aspect_vars[aspect].get()
            if current_die == 'd4':
                decrease_button.config(state='disabled')
            else:
                decrease_button.config(state='normal')
        
 