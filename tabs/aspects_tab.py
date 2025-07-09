import tkinter as tk
from tkinter import ttk

class AspectsTab:
    def __init__(self, parent, character_data):
        self.parent = parent
        self.character_data = character_data
        self.tab = ttk.Frame(parent)
        
        # Initialize aspect variables dictionary
        self.aspect_vars = {}
        self.modifier_vars = {}
        self.choices_locked = False
        
        # Dictionary to track which die values are already selected
        self.selected_dice = {}
        
        self.create_tab()
        
    def create_tab(self):
        """Create the aspects tab"""
        # Aspects Frame
        frame = ttk.LabelFrame(self.tab, text="Character Aspects")
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

    def lock_aspect_choices(self):
        """Lock the aspect choices to prevent further changes"""
        self.choices_locked = True
        self.lock_button.config(text="Choices Locked", state='disabled')
        
        # Disable all comboboxes
        for aspect in ['melee', 'ranged', 'rogue', 'magic']:
            combo = getattr(self, f'{aspect}_combo')
            combo.config(state='disabled')

    def get_die_modifier(self, die_type):
        """Get the modifier for a die type"""
        modifiers = {'d4': -1, 'd6': 0, 'd8': 1, 'd10': 2, 'd12': 3}
        return modifiers.get(die_type, 0)

    def update_modifier_display(self, aspect):
        """Update the modifier display for an aspect"""
        current_die = self.aspect_vars[aspect].get()
        modifier = self.get_die_modifier(current_die)
        self.modifier_vars[aspect].set(f"{modifier:+d}")

    def on_aspect_change(self, aspect):
        """Handle aspect change"""
        if self.choices_locked:
            return
            
        current_die = self.aspect_vars[aspect].get()
        
        # Update modifier display
        self.update_modifier_display(aspect)
        
        # Update selected dice tracking
        for die in self.selected_dice:
            if self.selected_dice[die] == aspect:
                self.selected_dice[die] = None
        
        if current_die in self.selected_dice:
            self.selected_dice[current_die] = aspect
        
        # Update available options for other aspects
        self.update_aspect_options()

    def update_aspect_options(self):
        """Update available options for aspects based on current selections"""
        if self.choices_locked:
            return
            
        aspects = ['melee', 'ranged', 'rogue', 'magic']
        dice_values = ['d4', 'd6', 'd8', 'd10', 'd12']
        
        for aspect in aspects:
            combo = getattr(self, f'{aspect}_combo')
            current_value = self.aspect_vars[aspect].get()
            
            # Always allow d4
            available_values = ['d4']
            
            # Add other dice only if not selected by another aspect
            for die in dice_values[1:]:  # Skip d4
                if self.selected_dice[die] is None or self.selected_dice[die] == aspect:
                    available_values.append(die)
            
            # Update combobox values
            combo['values'] = available_values
            
            # If current value is no longer available, reset to d4
            if current_value not in available_values:
                self.aspect_vars[aspect].set('d4')

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
        if self.choices_locked:
            return
            
        current_die = self.aspect_vars[aspect].get()
        dice_values = ['d4', 'd6', 'd8', 'd10', 'd12']
        
        try:
            current_index = dice_values.index(current_die)
            new_index = max(0, min(len(dice_values) - 1, current_index + change))
            new_die = dice_values[new_index]
            
            # Check if the new die is available
            if new_die == 'd4' or self.selected_dice[new_die] is None or self.selected_dice[new_die] == aspect:
                self.aspect_vars[aspect].set(new_die)
        except ValueError:
            pass

    def get_data(self):
        """Get aspect data"""
        return {
            'aspects': {aspect: self.aspect_vars[aspect].get() for aspect in self.aspect_vars},
            'choices_locked': self.choices_locked
        }

    def set_data(self, data):
        """Set aspect data"""
        aspects_data = data.get('aspects', {})
        for aspect, die_value in aspects_data.items():
            if aspect in self.aspect_vars:
                self.aspect_vars[aspect].set(die_value)
        
        self.choices_locked = data.get('choices_locked', False)
        if self.choices_locked:
            self.lock_button.config(text="Choices Locked", state='disabled')
            for aspect in ['melee', 'ranged', 'rogue', 'magic']:
                combo = getattr(self, f'{aspect}_combo')
                combo.config(state='disabled') 