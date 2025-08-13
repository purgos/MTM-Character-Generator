import tkinter as tk
from tkinter import ttk

class InventoryMaterials:
    """Materials tab: choose a spell with material components and add components with quantity and cost.

    Cost mapping by prerequisite:
      - D6 -> 1 gold per component
      - D8 -> 10 gold per component
      - D10 -> 20 gold per component
      - D12 -> N/A (not purchasable)
    """

    COST_BY_PREREQ = {
        'D6': 1,
        'D8': 10,
        'D10': 20,
        'D12': None,  # N/A
    }

    def __init__(self, parent, spell_var, component_var, quantity_var, add_callback, listbox):
        self.frame = ttk.Frame(parent)

        # Bindings from parent
        self.spell_var = spell_var
        self.component_var = component_var
        self.quantity_var = quantity_var
        self.listbox = listbox
        self.add_callback = add_callback

        # Try to import SPELLS from spells.py
        try:
            from src.spells import SPELLS
        except ImportError:
            try:
                from spells import SPELLS
            except Exception:
                SPELLS = {}
        self.SPELLS = SPELLS

        # Build list of spells requiring material components
        self.material_spells = self._collect_material_spells()
        # Also build a unique list of components -> representative die (max die across spells)
        # and a mapping of component -> spells that use it
        self.components_list, self.component_to_die, self.component_to_spells = self._build_component_index()

        # UI state vars
        self.cost_each_var = tk.StringVar(value='-')
        self.total_cost_var = tk.StringVar(value='-')
        self.prereq_var = tk.StringVar(value='')

        # Row 0: Mode selection (by Spell or by Component)
        self.mode_var = tk.StringVar(value='spell')
        ttk.Label(self.frame, text="Add by:").grid(row=0, column=0, padx=5, pady=5, sticky='w')
        mode_frame = ttk.Frame(self.frame)
        mode_frame.grid(row=0, column=1, columnspan=3, padx=5, pady=5, sticky='w')
        ttk.Radiobutton(mode_frame, text='Spell', variable=self.mode_var, value='spell', command=self.update_mode_ui).pack(side='left', padx=(0, 10))
        ttk.Radiobutton(mode_frame, text='Component', variable=self.mode_var, value='component', command=self.update_mode_ui).pack(side='left')

        # Row 1: Spell selector (shown in Spell mode)
        self.spell_label = ttk.Label(self.frame, text="Spell:")
        self.spell_label.grid(row=1, column=0, padx=5, pady=5, sticky='w')
        self.spell_combo = ttk.Combobox(self.frame, textvariable=self.spell_var, state='readonly', width=40)
        self.spell_combo['values'] = [name for name, _ in self.material_spells]
        self.spell_combo.grid(row=1, column=1, columnspan=3, padx=5, pady=5, sticky='ew')
        self.spell_combo.bind('<<ComboboxSelected>>', self.on_spell_selected)

        # Row 1 (alt): Component selector (shown in Component mode)
        self.component_list_label = ttk.Label(self.frame, text="Component (from list):")
        self.component_combo = ttk.Combobox(self.frame, state='readonly', width=40)
        self.component_combo['values'] = self.components_list
        self.component_combo.bind('<<ComboboxSelected>>', self.on_component_selected)

        # Row 2: Prerequisite display only (component chosen via dropdowns)
        ttk.Label(self.frame, text="Prereq:").grid(row=2, column=0, padx=5, pady=5, sticky='e')
        ttk.Label(self.frame, textvariable=self.prereq_var).grid(row=2, column=1, columnspan=3, padx=5, pady=5, sticky='w')

        # Row 3: Quantity + costs
        ttk.Label(self.frame, text="Quantity:").grid(row=3, column=0, padx=5, pady=5, sticky='w')
        self.qty_combo = ttk.Combobox(self.frame, textvariable=self.quantity_var, state='readonly', width=8)
        self.qty_combo['values'] = [str(i) for i in range(1, 21)]
        self.qty_combo.grid(row=3, column=1, padx=5, pady=5, sticky='w')
        self.qty_combo.current(0)
        self.qty_combo.bind('<<ComboboxSelected>>', self.update_total_cost)

        ttk.Label(self.frame, text="Gold each:").grid(row=3, column=2, padx=5, pady=5, sticky='e')
        ttk.Label(self.frame, textvariable=self.cost_each_var).grid(row=3, column=3, padx=5, pady=5, sticky='w')

        ttk.Label(self.frame, text="Total Gold:").grid(row=4, column=2, padx=5, pady=5, sticky='e')
        ttk.Label(self.frame, textvariable=self.total_cost_var).grid(row=4, column=3, padx=5, pady=5, sticky='w')

        # Row 5: Free checkbox + Add/Update button
        self.free_var = tk.BooleanVar(value=False)
        btns = ttk.Frame(self.frame)
        btns.grid(row=5, column=0, columnspan=4, sticky='w', padx=5, pady=(0, 8))
        ttk.Checkbutton(btns, text='Free', variable=self.free_var).pack(side='left', padx=(0, 10))
        handler = self.add_callback if self.add_callback else self.add_or_update
        ttk.Button(btns, text='Add/Update', command=handler).pack(side='left')

        # Grid weights
        for c in (0, 1, 2, 3):
            self.frame.grid_columnconfigure(c, weight=1 if c in (1,) else 0)

        # Initialize mode-dependent UI
        self.update_mode_ui()

        # Initialize defaults for combos to ensure component/prereq/cost are populated
        try:
            if self.material_spells:
                self.spell_combo.current(0)
                self.on_spell_selected()
            if self.components_list:
                self.component_combo.current(0)
                # Do not override spell choice unless in component mode; handled when toggled
        except Exception:
            pass

    def _collect_material_spells(self):
        items = []
        for name, data in (self.SPELLS or {}).items():
            comps = data.get('spell_components', [])
            if 'MC' in comps:
                prereq = data.get('prerequisite', '')
                # Extract Dx from strings like 'Magic Aspect D8'
                die = None
                if isinstance(prereq, str):
                    prereq_upper = prereq.upper()
                    if 'D12' in prereq_upper:
                        die = 'D12'
                    elif 'D10' in prereq_upper:
                        die = 'D10'
                    elif 'D8' in prereq_upper:
                        die = 'D8'
                    elif 'D6' in prereq_upper:
                        die = 'D6'
                items.append((name, {
                    'component': data.get('material_component', '').strip() or 'Material Component',
                    'prereq_die': die or '',
                }))
        # Sort by name for UX
        items.sort(key=lambda t: t[0])
        return items

    def _build_component_index(self):
        # Aggregate dies per component and track which spells use each component
        comp_dies = {}
        comp_spells = {}
        for name, meta in self.material_spells:
            comp = meta.get('component', '').strip()
            die = meta.get('prereq_die') or ''
            if not comp:
                continue
            comp_dies.setdefault(comp, set())
            if die:
                comp_dies[comp].add(die)
            comp_spells.setdefault(comp, set()).add(name)
        # Choose the highest die per component to be conservative on cost
        order = {'D6': 1, 'D8': 2, 'D10': 3, 'D12': 4}
        comp_to_die = {}
        for comp, dies in comp_dies.items():
            if not dies:
                comp_to_die[comp] = ''
            else:
                comp_to_die[comp] = max(dies, key=lambda d: order.get(d, 0))
        components = sorted(comp_to_die.keys())
        comp_to_spells = {comp: sorted(list(spells)) for comp, spells in comp_spells.items()}
        return components, comp_to_die, comp_to_spells

    def on_spell_selected(self, event=None):
        name = self.spell_var.get()
        comp = next((meta['component'] for n, meta in self.material_spells if n == name), '')
        die = next((meta['prereq_die'] for n, meta in self.material_spells if n == name), '')
        self.component_var.set(comp)
        self.prereq_var.set(die)
        cost_each = self.COST_BY_PREREQ.get(die or '', None)
        self.cost_each_var.set('N/A' if cost_each is None else str(cost_each))
        self.update_total_cost()

    def on_component_selected(self, event=None):
        comp = self.component_combo.get()
        self.component_var.set(comp)
        die = self.component_to_die.get(comp, '')
        self.prereq_var.set(die)
        cost_each = self.COST_BY_PREREQ.get(die or '', None)
        self.cost_each_var.set('N/A' if cost_each is None else str(cost_each))
        self.update_total_cost()

    def update_total_cost(self, event=None):
        die = self.prereq_var.get().strip()
        cost_each = self.COST_BY_PREREQ.get(die, None)
        try:
            qty = int(self.quantity_var.get())
        except Exception:
            qty = 1
        if cost_each is None:
            self.total_cost_var.set('N/A')
        else:
            self.total_cost_var.set(str(cost_each * qty))

    def add_or_update(self):
        comp = self.component_var.get().strip() or 'Material Component'
        die = self.prereq_var.get().strip()
        try:
            qty = int(self.quantity_var.get())
        except Exception:
            qty = 1
        cost_each = self.COST_BY_PREREQ.get(die, None)
        cost_str = 'N/A' if cost_each is None else f"{cost_each}"
        # Determine associated spell name(s) to show beside the component
        spell_names = []
        try:
            mode = self.mode_var.get()
        except Exception:
            mode = 'spell'
        if mode == 'spell':
            selected_spell = (self.spell_var.get() or '').strip()
            if selected_spell:
                spell_names = [selected_spell]
        if not spell_names:
            spell_names = self.component_to_spells.get(comp, [])
        spell_suffix = f" [{', '.join(spell_names)}]" if spell_names else ''

        entry = f"{comp}{spell_suffix} (x{qty}) - {cost_str}g each"

        # If the component already exists in the list, update its quantity line; naive match by component name prefix
        lb = self.listbox
        found_idx = None
        for i in range(lb.size()):
            text = lb.get(i)
            # Compare by base component name (strip any spell suffix or quantity)
            base = text.split(' [', 1)[0]
            base = base.split(' (x', 1)[0]
            if base == comp:
                found_idx = i
                break
        if found_idx is not None:
            lb.delete(found_idx)
            lb.insert(found_idx, entry)
            lb.select_set(found_idx)
        else:
            lb.insert(tk.END, entry)

    def update_mode_ui(self):
        mode = self.mode_var.get()
        if mode == 'spell':
            # Show spell controls
            self.spell_label.grid()
            self.spell_combo.grid()
            # Hide component list controls
            self.component_list_label.grid_remove()
            self.component_combo.grid_remove()
        else:
            # Hide spell controls
            self.spell_label.grid_remove()
            self.spell_combo.grid_remove()
            # Show component list controls
            self.component_list_label.grid(row=1, column=0, padx=5, pady=5, sticky='w')
            self.component_combo.grid(row=1, column=1, columnspan=3, padx=5, pady=5, sticky='ew')
