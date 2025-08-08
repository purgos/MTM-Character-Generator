import tkinter as tk
from tkinter import ttk
import random
import datetime as _dt

class DiceRollerTab:
    def __init__(self, parent, character_data=None):
        self.parent = parent
        self.character_data = character_data or {}
        self.tab = ttk.Frame(parent)
        self._build_ui()
        # Keep in-memory list of history entries (newest first)
        self.history = []
        # Prefix label for context (e.g., aspect name)
        self._roll_prefix = None

    def _build_ui(self):
        container = ttk.Frame(self.tab)
        container.pack(fill='both', expand=True, padx=8, pady=8)

        # Use a PanedWindow to split Roll controls (left) and History (right)
        paned = ttk.Panedwindow(container, orient='horizontal')
        paned.pack(fill='both', expand=True)

        # Left: Roll controls
        left = ttk.Frame(paned)
        paned.add(left, weight=2)

        # Global roll options at the top (apply to all rolls)
        options_frame = ttk.LabelFrame(left, text='Roll Options')
        options_frame.pack(fill='x', padx=8, pady=(8, 6))
        self.adv_var = tk.BooleanVar(value=False)
        self.disadv_var = tk.BooleanVar(value=False)
        self.adv_check = ttk.Checkbutton(options_frame, text='Advantage', variable=self.adv_var, command=self._on_adv_changed)
        self.adv_check.grid(row=0, column=0, sticky='w', padx=(8,6), pady=4)
        self.disadv_check = ttk.Checkbutton(options_frame, text='Disadvantage', variable=self.disadv_var, command=self._on_disadv_changed)
        self.disadv_check.grid(row=0, column=1, sticky='w', padx=(4,8), pady=4)

        # Quick Dice row(s)
        roll_frame = ttk.LabelFrame(left, text='Roll Dice')
        roll_frame.pack(fill='x', padx=8, pady=(0,6))

        # Internal variables (kept for compatibility with roll()/aspect rolls)
        self.die_var = tk.StringVar(value='d20')
        self.count_var = tk.IntVar(value=1)
        self.mod_var = tk.IntVar(value=0)

        # Two-row quick buttons: d4 d6 d8 d10 / d12 d20 d100
        btn_specs_row1 = [("d4", 4), ("d6", 6), ("d8", 8), ("d10", 10)]
        btn_specs_row2 = [("d12", 12), ("d20", 20), ("d100", 100)]
        for col, (label, sides) in enumerate(btn_specs_row1):
            ttk.Button(roll_frame, text=label, width=6, command=lambda s=sides: self.quick_roll(s)).grid(
                row=0, column=col, padx=4, pady=6, sticky='w'
            )
        for col, (label, sides) in enumerate(btn_specs_row2):
            ttk.Button(roll_frame, text=label, width=6, command=lambda s=sides: self.quick_roll(s)).grid(
                row=1, column=col, padx=4, pady=2, sticky='w'
            )

        # Aspect quick-rolls
        aspect_frame = ttk.LabelFrame(left, text='Aspect Rolls')
        aspect_frame.pack(fill='x', padx=8, pady=(0,8))
        ttk.Label(aspect_frame, text='Quick:').grid(row=0, column=0, sticky='w', padx=(8,4), pady=6)
        self.aspect_melee_btn = ttk.Button(aspect_frame, text='Melee', command=lambda: self.roll_aspect('melee'))
        self.aspect_melee_btn.grid(row=0, column=1, sticky='w', padx=2, pady=6)
        self.aspect_ranged_btn = ttk.Button(aspect_frame, text='Ranged', command=lambda: self.roll_aspect('ranged'))
        self.aspect_ranged_btn.grid(row=0, column=2, sticky='w', padx=2, pady=6)
        self.aspect_rogue_btn = ttk.Button(aspect_frame, text='Rogue', command=lambda: self.roll_aspect('rogue'))
        self.aspect_rogue_btn.grid(row=0, column=3, sticky='w', padx=2, pady=6)
        self.aspect_magic_btn = ttk.Button(aspect_frame, text='Magic', command=lambda: self.roll_aspect('magic'))
        self.aspect_magic_btn.grid(row=0, column=4, sticky='w', padx=2, pady=6)

        # Damage: two rows of gear dice (d4 d6 d8 / d10 d12)
        damage_frame = ttk.LabelFrame(left, text='Damage')
        damage_frame.pack(fill='x', padx=8, pady=(0,8))
        self.crit_var = tk.BooleanVar(value=False)
        ttk.Label(damage_frame, text='Critical:').grid(row=0, column=0, sticky='w', padx=(8,4), pady=6)
        self.crit_check = ttk.Checkbutton(damage_frame, text='', variable=self.crit_var)
        self.crit_check.grid(row=0, column=1, sticky='w', padx=(0,12), pady=6)
        ttk.Label(damage_frame, text='Roll:').grid(row=0, column=2, sticky='w', padx=(8,4), pady=6)
        ttk.Button(damage_frame, text='d4', command=lambda: self.roll_damage(4)).grid(row=0, column=3, padx=2, pady=6)
        ttk.Button(damage_frame, text='d6', command=lambda: self.roll_damage(6)).grid(row=0, column=4, padx=2, pady=6)
        ttk.Button(damage_frame, text='d8', command=lambda: self.roll_damage(8)).grid(row=0, column=5, padx=2, pady=6)
        ttk.Button(damage_frame, text='d10', command=lambda: self.roll_damage(10)).grid(row=1, column=3, padx=2, pady=(0,6))
        ttk.Button(damage_frame, text='d12', command=lambda: self.roll_damage(12)).grid(row=1, column=4, padx=2, pady=(0,6))

        # Skill Check: two rows of aspect buttons
        skill_frame = ttk.LabelFrame(left, text='Skill Check')
        skill_frame.pack(fill='x', padx=8, pady=(0,8))
        self.prof_bonus_var = tk.BooleanVar(value=False)
        self.prof_check = ttk.Checkbutton(skill_frame, text='Profession', variable=self.prof_bonus_var)
        self.prof_check.grid(row=0, column=0, columnspan=2, sticky='w', padx=(8,8), pady=6)
        ttk.Label(skill_frame, text='Aspect:').grid(row=0, column=2, rowspan=2, sticky='w', padx=(8,4), pady=6)
        ttk.Button(skill_frame, text='Melee', command=lambda: self.skill_check('melee')).grid(row=0, column=3, padx=2, pady=6)
        ttk.Button(skill_frame, text='Ranged', command=lambda: self.skill_check('ranged')).grid(row=0, column=4, padx=2, pady=6)
        ttk.Button(skill_frame, text='Rogue', command=lambda: self.skill_check('rogue')).grid(row=1, column=3, padx=2, pady=(0,6))
        ttk.Button(skill_frame, text='Magic', command=lambda: self.skill_check('magic')).grid(row=1, column=4, padx=2, pady=(0,6))

        # Armor / Dodge / Parry
        saves_frame = ttk.LabelFrame(left, text='Armor / Dodge / Parry')
        saves_frame.pack(fill='x', padx=8, pady=(0,8))
        ttk.Button(saves_frame, text='Armor Save', command=self.armor_save).grid(row=0, column=0, padx=8, pady=6, sticky='w')
        ttk.Button(saves_frame, text='Dodge Save', command=self.dodge_save).grid(row=0, column=1, padx=8, pady=6, sticky='w')
        ttk.Button(saves_frame, text='Parry Info', command=self.parry_info).grid(row=0, column=2, padx=8, pady=6, sticky='w')

        # Magic Save
        magic_frame = ttk.LabelFrame(left, text='Magic Save')
        magic_frame.pack(fill='x', padx=8, pady=(0,8))
        ttk.Button(magic_frame, text='Roll Magic Save', command=self.magic_save).grid(row=0, column=0, padx=8, pady=6, sticky='w')

        # Result area
        result_frame = ttk.LabelFrame(left, text='Result')
        result_frame.pack(fill='both', expand=True, padx=8, pady=(0,8))

        self.result_label = ttk.Label(result_frame, text='—', anchor='w', wraplength=600, justify='left')
        self.result_label.pack(fill='x', padx=8, pady=8)

        # Right: History
        right = ttk.Frame(paned)
        paned.add(right, weight=1)

        history_frame = ttk.LabelFrame(right, text='History')
        history_frame.pack(fill='both', expand=True, padx=8, pady=8)

        # Replace Listbox with Text for word-wrapped, indented history
        self.history_text = tk.Text(history_frame, height=20, wrap='word', state='disabled')
        self.history_text.pack(side='left', fill='both', expand=True, padx=(8,0), pady=8)

        scrollbar = ttk.Scrollbar(history_frame, orient='vertical', command=self.history_text.yview)
        scrollbar.pack(side='right', fill='y', padx=(0,8), pady=8)
        self.history_text.config(yscrollcommand=scrollbar.set)
        # Indent wrapped lines for readability
        self.history_text.tag_configure('entry', lmargin1=0, lmargin2=24)

        # History controls
        controls = ttk.Frame(right)
        controls.pack(fill='x', padx=8, pady=(0,8))

        ttk.Button(controls, text='Clear History', command=self.clear_history).pack(side='right')

    def _parse_die(self, die: str) -> int:
        try:
            return int(die.lower().lstrip('d'))
        except Exception:
            return 20

    def _aspect_die(self, aspect: str) -> str:
        """Return die string for aspect. Treat 'NULL' as 'd4'."""
        aspects = (self.character_data or {}).get('aspects', {})
        val = aspects.get(aspect, 'd4') or 'd4'
        return 'd4' if str(val).upper() == 'NULL' else str(val)

    def _aspect_modifier(self, aspect: str) -> int:
        """Map aspect die to its modifier: d4:-1, d6:0, d8:+1, d10:+2, d12:+3. NULL counts as d4."""
        die = self._aspect_die(aspect).lower()
        mapping = {'d4': -1, 'd6': 0, 'd8': 1, 'd10': 2, 'd12': 3}
        return mapping.get(die, 0)

    def _on_adv_changed(self):
        # If advantage is turned on, ensure disadvantage is off
        if self.adv_var.get():
            self.disadv_var.set(False)

    def _on_disadv_changed(self):
        # If disadvantage is turned on, ensure advantage is off
        if self.disadv_var.get():
            self.adv_var.set(False)

    def _roll_d20_adv_dis(self):
        """Roll a d20 applying advantage/disadvantage settings."""
        use_adv = bool(self.adv_var.get())
        use_disadv = bool(self.disadv_var.get())
        if use_adv and use_disadv:
            use_adv = use_disadv = False
        if use_adv:
            a = random.randint(1, 20)
            b = random.randint(1, 20)
            return max(a, b), [a, b], ['adv']
        if use_disadv:
            a = random.randint(1, 20)
            b = random.randint(1, 20)
            return min(a, b), [a, b], ['dis']
        r = random.randint(1, 20)
        return r, [r], []

    def _uc_specialist_bonus(self) -> int:
        """Unarmed Combat Specialist bonus to armor-like checks: +1 at rank 2, +1 every two ranks to max +5."""
        if not (self.character_data or {}).get('unarmedCombat', False):
            return 0
        try:
            rank = int((self.character_data or {}).get('rank', 1) or 1)
        except Exception:
            rank = 1
        return min(5, rank // 2)

    def _find_allocation(self, alloc_type: str):
        """Return (present: bool, die: str|None) for a given gear allocation type."""
        allocations = (self.character_data or {}).get('gearDieAllocations', {})
        for key, data in allocations.items():
            if data.get('type') == alloc_type:
                return True, data.get('die')
        return False, None

    def _armor_gear_bonus(self):
        """Return roll bonus and table shift from equipped armor."""
        has_armor, die = self._find_allocation('armor')
        if not has_armor:
            return 0, 0, None
        die = (die or 'd4').lower()
        roll_bonus = 0
        if die in ('d8', 'd10'):
            roll_bonus = 1
        elif die == 'd12':
            roll_bonus = 2
        else:  # d4 or d6
            roll_bonus = 0
        table_shift = 1  # Additional +1 when comparing to the table
        return roll_bonus, table_shift, die

    def roll_aspect(self, aspect: str):
        """Quick-roll for an aspect using its current die."""
        die = self._aspect_die(aspect)
        # Set the UI die to reflect what's being rolled (so user sees it)
        self.die_var.set(die)
        # Prefix result/history with aspect name
        self._roll_prefix = aspect.capitalize()
        # Execute roll with current count/modifier/advantage settings
        self.roll()

    def quick_roll(self, sides: int):
        """Quick roll: set die, count=1, modifier=0, then delegate to roll() with global Adv/Dis."""
        try:
            int(sides)
        except Exception:
            return
        self.die_var.set(f'd{int(sides)}')
        self.count_var.set(1)
        self.mod_var.set(0)
        # Ensure no stale aspect prefix
        self._roll_prefix = None
        self.roll()

    def _reset_roll_toggles(self):
        """Reset Advantage, Disadvantage, Critical, and Profession checkboxes."""
        try:
            self.adv_var.set(False)
            self.disadv_var.set(False)
        except Exception:
            pass
        try:
            self.crit_var.set(False)
        except Exception:
            pass
        try:
            self.prof_bonus_var.set(False)
        except Exception:
            pass

    def roll(self):
        sides = self._parse_die(self.die_var.get())
        count = max(1, int(self.count_var.get() or 1))
        modifier = int(self.mod_var.get() or 0)
        use_adv = bool(self.adv_var.get())
        use_disadv = bool(self.disadv_var.get())

        # Safety: if both are somehow True, treat as normal
        if use_adv and use_disadv:
            use_adv = use_disadv = False

        rolls = []
        if use_adv:
            for _ in range(count):
                a = random.randint(1, sides)
                b = random.randint(1, sides)
                rolls.append(max(a, b))
        elif use_disadv:
            for _ in range(count):
                a = random.randint(1, sides)
                b = random.randint(1, sides)
                rolls.append(min(a, b))
        else:
            rolls = [random.randint(1, sides) for _ in range(count)]

        total = sum(rolls) + modifier

        # Build display strings
        die_notation = f"{count}{self.die_var.get()}"
        mod_str = f"{modifier:+d}" if modifier else ""
        flags = []
        if use_adv:
            flags.append('adv')
        if use_disadv:
            flags.append('dis')
        flags_str = f" ({', '.join(flags)})" if flags else ""
        detail = f"({', '.join(map(str, rolls))}{(' ' + mod_str) if mod_str else ''})"
        result_text = f"{die_notation}{mod_str} = {total}{flags_str}  {detail}"

        # Optional context prefix (e.g., Aspect name)
        prefix = f"{self._roll_prefix}: " if self._roll_prefix else ""
        final_text = f"{prefix}{result_text}"

        # Update result label
        self.result_label.config(text=final_text)

        # Append to history
        self._add_history_entry(final_text)

        # Clear prefix after use
        self._roll_prefix = None
        # Reset toggles after a roll
        self._reset_roll_toggles()

    def roll_damage(self, sides: int):
        """Roll damage: normal = roll + rank; critical = max + roll + rank.
        Advantage/Disadvantage applies to the damage die as well.
        """
        try:
            rank = int((self.character_data or {}).get('rank', 1) or 1)
        except Exception:
            rank = 1

        # Apply advantage/disadvantage to the damage die
        use_adv = bool(self.adv_var.get())
        use_disadv = bool(self.disadv_var.get())
        if use_adv and use_disadv:
            use_adv = use_disadv = False

        if use_adv:
            a = random.randint(1, sides)
            b = random.randint(1, sides)
            r = max(a, b)
            rolls_detail = [a, b]
            flag_list = ['adv']
        elif use_disadv:
            a = random.randint(1, sides)
            b = random.randint(1, sides)
            r = min(a, b)
            rolls_detail = [a, b]
            flag_list = ['dis']
        else:
            r = random.randint(1, sides)
            rolls_detail = [r]
            flag_list = []

        is_crit = bool(self.crit_var.get())
        has_improved_crit = 'Improved Critical' in ((self.character_data or {}).get('selectedAbilities', []) or [])
        die_notation = f"d{sides}"

        if is_crit:
            if has_improved_crit:
                total = (2 * sides) + r + rank
                flags = ['crit', 'Improved Critical'] + flag_list
                breakdown = f"({sides} + {sides} + {r} + {rank})"
            else:
                total = sides + r + rank
                flags = ['crit'] + flag_list
                breakdown = f"({sides} + {r} + {rank})"
        else:
            total = r + rank
            flags = flag_list
            breakdown = f"({r} + {rank})"

        flags_str = f" ({', '.join(flags)})" if flags else ""
        final_text = f"Damage {die_notation} = {total}{flags_str}  {breakdown}"
        
        # Update result label
        self.result_label.config(text=final_text)
        # Append to history
        self._add_history_entry(final_text)
        # Reset toggles after a roll
        self._reset_roll_toggles()

    def _melee_table_outcome(self, value: int) -> str:
        """Return outcome string per Melee table for a clamped 1..20 value."""
        if value <= 1:
            return 'Critical Failure — Lingering Damage*'
        if 2 <= value <= 9:
            return 'Failure — Full Damage'
        if 10 <= value <= 18:
            return 'Partial Save — Damage dealt minus armor'
        if value == 19:
            return 'Moderate Save — Minimum Damage'
        return 'Full Save — No Damage'

    def _spell_table_outcome(self, value: int) -> str:
        """Return outcome string per Spells table for a clamped 1..20 value."""
        if value <= 1:
            return 'Critical Failure — Lingering Damage/Shaken*'
        if 2 <= value <= 9:
            return 'Failure — Full Damage/Full Effect'
        if 10 <= value <= 18:
            return 'Partial Save — 1/2 Damage/Half Effect'
        if value == 19:
            return 'Moderate Save — Minimum Damage/Effect'
        return 'Full Save — No Damage/Effect'

    def armor_save(self):
        """Armor save: d20 + armor gear bonus + UC bonus. Apply +1 table shift when wearing armor."""
        roll, rolls_detail, flags = self._roll_d20_adv_dis()
        uc_bonus = self._uc_specialist_bonus()
        armor_roll_bonus, table_shift, armor_die = self._armor_gear_bonus()
        total_roll = roll + uc_bonus + armor_roll_bonus
        # For table comparison, apply shift if wearing armor
        table_value = min(20, max(1, total_roll + table_shift))
        outcome = self._melee_table_outcome(table_value)

        # Build text
        mods = []
        if uc_bonus:
            mods.append(f"UC+{uc_bonus}")
        if armor_roll_bonus:
            mods.append(f"Armor+{armor_roll_bonus}")
        mod_sum = uc_bonus + armor_roll_bonus
        mod_str = f"{mod_sum:+d}" if mod_sum else ""
        flags_str = f" ({', '.join(flags)})" if flags else ""
        detail_mods = []
        if mods:
            detail_mods.append('+'.join(mods))
        if table_shift:
            detail_mods.append('table+1')
        detail_tail = (" " + ", ".join(detail_mods)) if detail_mods else ""
        final_text = f"Armor Save: d20{mod_str} = {total_roll}{flags_str}  ({', '.join(map(str, rolls_detail))}{detail_tail})\n→ {outcome}"

        self.result_label.config(text=final_text)
        self._add_history_entry(final_text)
        # Reset toggles after a roll
        self._reset_roll_toggles()

    def dodge_save(self):
        """Dodge save: same table as armor. Apply UC bonus only."""
        roll, rolls_detail, flags = self._roll_d20_adv_dis()
        uc_bonus = self._uc_specialist_bonus()
        total_roll = roll + uc_bonus
        table_value = min(20, max(1, total_roll))
        outcome = self._melee_table_outcome(table_value)

        mod_str = f"{uc_bonus:+d}" if uc_bonus else ""
        flags_str = f" ({', '.join(flags)})" if flags else ""
        detail_tail = (" UC+%d" % uc_bonus) if uc_bonus else ""
        final_text = f"Dodge Save: d20{mod_str} = {total_roll}{flags_str}  ({', '.join(map(str, rolls_detail))}{detail_tail})\n→ {outcome}"

        self.result_label.config(text=final_text)
        self._add_history_entry(final_text)
        # Reset toggles after a roll
        self._reset_roll_toggles()

    def parry_info(self):
        """Show parry effect based on UC rank; also show if Parry is allocated."""
        has_parry, die = self._find_allocation('parry')
        try:
            rank = int((self.character_data or {}).get('rank', 1) or 1)
        except Exception:
            rank = 1
        rolls_required = 3 if rank >= 6 else 2
        status = 'Yes' if has_parry else 'No'
        extra = f" (slot {die})" if has_parry and die else ""
        text = (
            f"Parry Defense: Attacker rolls {rolls_required} damage rolls and takes the lowest.\n"
            f"Parry Equipped: {status}{extra}"
        )
        self.result_label.config(text=text)
        self._add_history_entry(text)

    def magic_save(self):
        """Magic save: d20, apply Spells table outcome (no gear bonuses)."""
        roll, rolls_detail, flags = self._roll_d20_adv_dis()
        table_value = min(20, max(1, roll))
        outcome = self._spell_table_outcome(table_value)
        flags_str = f" ({', '.join(flags)})" if flags else ""
        final_text = f"Magic Save: d20 = {roll}{flags_str}  ({', '.join(map(str, rolls_detail))})\n→ {outcome}"
        self.result_label.config(text=final_text)
        self._add_history_entry(final_text)
        # Reset toggles after a roll
        self._reset_roll_toggles()

    def skill_check(self, aspect: str):
        """Roll d20 and add aspect-based modifier and optional profession bonus."""
        # Determine d20 with advantage/disadvantage
        use_adv = bool(self.adv_var.get())
        use_disadv = bool(self.disadv_var.get())
        if use_adv and use_disadv:
            use_adv = use_disadv = False
        if use_adv:
            a = random.randint(1, 20)
            b = random.randint(1, 20)
            roll_used = max(a, b)
            rolls_detail = [a, b]
        elif use_disadv:
            a = random.randint(1, 20)
            b = random.randint(1, 20)
            roll_used = min(a, b)
            rolls_detail = [a, b]
        else:
            roll_used = random.randint(1, 20)
            rolls_detail = [roll_used]

        # Modifiers
        aspect_mod = self._aspect_modifier(aspect)
        prof_bonus = 2 if self.prof_bonus_var.get() else 0
        modifier_total = aspect_mod + prof_bonus

        total = roll_used + modifier_total

        # Build strings
        mod_str = f"{modifier_total:+d}" if modifier_total else ""
        flags = []
        if use_adv:
            flags.append('adv')
        if use_disadv:
            flags.append('dis')
        if prof_bonus:
            flags.append('prof +2')
        flags_str = f" ({', '.join(flags)})" if flags else ""
        detail = f"({', '.join(map(str, rolls_detail))}{(' ' + mod_str) if mod_str else ''})"
        prefix = f"Skill {aspect.capitalize()}: "
        result_text = f"d20{mod_str} = {total}{flags_str}  {detail}"
        final_text = f"{prefix}{result_text}"

        # Update result label and history
        self.result_label.config(text=final_text)
        self._add_history_entry(final_text)
        # Reset toggles after a roll
        self._reset_roll_toggles()

    def _add_history_entry(self, text: str):
        """Add a new entry to the history (newest first) with wrapping and indentation."""
        timestamp = _dt.datetime.now().strftime('%H:%M:%S')
        entry = f"[{timestamp}] {text}\n"
        # Insert at beginning and cap to 200 entries
        self.history.insert(0, entry)
        if len(self.history) > 200:
            self.history = self.history[:200]
        # Re-render the Text widget
        self.history_text.config(state='normal')
        self.history_text.delete('1.0', 'end')
        for e in self.history:
            self.history_text.insert('end', e, ('entry',))
        self.history_text.config(state='disabled')

    def clear_history(self):
        self.history.clear()
        if hasattr(self, 'history_text'):
            self.history_text.config(state='normal')
            self.history_text.delete('1.0', 'end')
            self.history_text.config(state='disabled')

    def set_data(self, data: dict):
        """Update character data reference used for aspect quick-rolls."""
        self.character_data = data or {}
