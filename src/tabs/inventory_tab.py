import tkinter as tk
from tkinter import ttk, messagebox

from .inventory_magic_bag import InventoryMagicBag
from .inventory_stored_magic import InventoryStoredMagic
from .inventory_materials import InventoryMaterials
from .inventory_elsewhere import InventoryElsewhere

class InventoryTab:
    def __init__(self, parent, character_data, update_gold_callback=None):
        self.parent = parent
        self.character_data = character_data
        # Callback to update visible Gold in Basic Info tab
        self.update_gold_callback = update_gold_callback
        self.tab = ttk.Frame(parent)

        inventory_notebook = ttk.Notebook(self.tab)
        inventory_notebook.pack(fill='both', expand=True, padx=5, pady=5)

        self.magic_item_var = tk.StringVar()
        self.magic_quantity_var = tk.StringVar(value="1")
        self.magic_listbox = tk.Listbox()  # placeholder; replaced with visible widget below
        self.magic_bag_tab = InventoryMagicBag(
            inventory_notebook,
            self.magic_item_var,
            self.magic_quantity_var,
            self.add_magic_bag_item,
            self.magic_listbox
        )
        inventory_notebook.add(self.magic_bag_tab.frame, text="Magic Bag")

        # Make Magic Bag listbox visible inside its tab
        try:
            for c in range(4):
                self.magic_bag_tab.frame.grid_columnconfigure(c, weight=1 if c in (1, 3) else 0)
            ttk.Label(self.magic_bag_tab.frame, text="Items:").grid(row=4, column=0, columnspan=4, sticky='w', padx=5)
            magic_list_frame = ttk.Frame(self.magic_bag_tab.frame)
            magic_list_frame.grid(row=5, column=0, columnspan=4, sticky='nsew', padx=5, pady=(0, 5))
            self.magic_bag_tab.frame.grid_rowconfigure(5, weight=1)
            self.magic_listbox = tk.Listbox(magic_list_frame, height=8)
            magic_scroll = ttk.Scrollbar(magic_list_frame, orient='vertical', command=self.magic_listbox.yview)
            self.magic_listbox.configure(yscrollcommand=magic_scroll.set)
            self.magic_listbox.pack(side='left', fill='both', expand=True)
            magic_scroll.pack(side='right', fill='y')
            # ensure the tab instance uses the visible listbox
            self.magic_bag_tab.listbox = self.magic_listbox

            # Buttons row for Magic Bag: Decrement only
            magic_btns = ttk.Frame(self.magic_bag_tab.frame)
            magic_btns.grid(row=6, column=0, columnspan=4, sticky='w', padx=5, pady=(0, 8))
            ttk.Button(magic_btns, text="Decrement", command=self.decrement_magic_item).pack(side='left')
        except Exception:
            pass

        self.sm_item_var = tk.StringVar()
        self.sm_variant_var = tk.StringVar()
        self.sm_charges_var = tk.StringVar(value="")
        self.stored_magic_listbox = tk.Listbox()
        self.stored_magic_tab = InventoryStoredMagic(
            inventory_notebook,
            self.sm_item_var,
            self.sm_variant_var,
            self.sm_charges_var,
            self.add_stored_magic_item,
            self.stored_magic_listbox
        )
        inventory_notebook.add(self.stored_magic_tab.frame, text="Stored Magic Items")

        # Make Stored Magic a two-column layout: left list, right details
        try:
            self.stored_magic_tab.frame.grid_columnconfigure(0, weight=1)
            self.stored_magic_tab.frame.grid_columnconfigure(1, weight=2)
            self.stored_magic_tab.frame.grid_rowconfigure(1, weight=1)

            # Left side: list and remove button
            left = ttk.Frame(self.stored_magic_tab.frame)
            left.grid(row=0, column=0, rowspan=3, sticky='nsew', padx=(5, 2), pady=5)
            left.grid_columnconfigure(0, weight=1)
            ttk.Label(left, text="Items:").grid(row=0, column=0, sticky='w')
            sm_list_frame = ttk.Frame(left)
            sm_list_frame.grid(row=1, column=0, sticky='nsew', pady=(0, 5))
            left.grid_rowconfigure(1, weight=1)
            self.stored_magic_listbox = tk.Listbox(sm_list_frame, height=12)
            sm_scroll = ttk.Scrollbar(sm_list_frame, orient='vertical', command=self.stored_magic_listbox.yview)
            self.stored_magic_listbox.configure(yscrollcommand=sm_scroll.set)
            self.stored_magic_listbox.pack(side='left', fill='both', expand=True)
            sm_scroll.pack(side='right', fill='y')
            ttk.Button(left, text="Remove", command=self.remove_stored_magic_item).grid(row=2, column=0, sticky='w')
            # Bind selection change to update right panel
            self.stored_magic_listbox.bind('<<ListboxSelect>>', self.on_stored_magic_select)

            # Right side: details panel from sub-tab
            right = self.stored_magic_tab.right_frame
            right.grid(row=0, column=1, rowspan=3, sticky='nsew', padx=(2, 5), pady=5)
        except Exception:
            pass

        self.mc_spell_var = tk.StringVar()
        self.mc_component_var = tk.StringVar()
        self.mc_quantity_var = tk.StringVar(value="1")
        self.materials_listbox = tk.Listbox()  # placeholder; replaced with visible widget below
        self.materials_tab = InventoryMaterials(
            inventory_notebook,
            self.mc_spell_var,
            self.mc_component_var,
            self.mc_quantity_var,
            self.add_or_update_material,
            self.materials_listbox
        )
        inventory_notebook.add(self.materials_tab.frame, text="Material Components")

        # Make Materials listbox visible inside its tab (place below the controls)
        try:
            for c in range(4):
                self.materials_tab.frame.grid_columnconfigure(c, weight=1 if c in (1, 3) else 0)
            # Controls in InventoryMaterials occupy rows 0-5, so start list at row 6
            ttk.Label(self.materials_tab.frame, text="Items:").grid(row=6, column=0, columnspan=4, sticky='w', padx=5)
            mat_list_frame = ttk.Frame(self.materials_tab.frame)
            mat_list_frame.grid(row=7, column=0, columnspan=4, sticky='nsew', padx=5, pady=(0, 5))
            self.materials_tab.frame.grid_rowconfigure(7, weight=1)
            self.materials_listbox = tk.Listbox(mat_list_frame, height=8)
            mat_scroll = ttk.Scrollbar(mat_list_frame, orient='vertical', command=self.materials_listbox.yview)
            self.materials_listbox.configure(yscrollcommand=mat_scroll.set)
            self.materials_listbox.pack(side='left', fill='both', expand=True)
            mat_scroll.pack(side='right', fill='y')
            # ensure the tab instance uses the visible listbox
            self.materials_tab.listbox = self.materials_listbox

            # Buttons row for Materials: Decrement only
            mat_btns = ttk.Frame(self.materials_tab.frame)
            mat_btns.grid(row=8, column=0, columnspan=4, sticky='w', padx=5, pady=(0, 8))
            ttk.Button(mat_btns, text="Decrement", command=self.decrement_material_item).pack(side='left')
        except Exception:
            pass

        self.elsewhere_item_var = tk.StringVar()
        self.elsewhere_quantity_var = tk.StringVar(value="1")
        self.elsewhere_location_var = tk.StringVar()
        self.elsewhere_listbox = tk.Listbox()  # placeholder; replaced with visible widget below
        self.elsewhere_tab = InventoryElsewhere(
            inventory_notebook,
            self.elsewhere_item_var,
            self.elsewhere_quantity_var,
            self.elsewhere_location_var,
            self.add_elsewhere_item,
            self.elsewhere_listbox
        )
        inventory_notebook.add(self.elsewhere_tab.frame, text="Elsewhere")

        # Make Elsewhere listbox visible inside its tab
        try:
            for c in range(4):
                self.elsewhere_tab.frame.grid_columnconfigure(c, weight=1 if c in (1, 3) else 0)
            ttk.Label(self.elsewhere_tab.frame, text="Items:").grid(row=5, column=0, columnspan=4, sticky='w', padx=5)
            elsewhere_list_frame = ttk.Frame(self.elsewhere_tab.frame)
            elsewhere_list_frame.grid(row=6, column=0, columnspan=4, sticky='nsew', padx=5, pady=(0, 5))
            self.elsewhere_tab.frame.grid_rowconfigure(6, weight=1)
            self.elsewhere_listbox = tk.Listbox(elsewhere_list_frame, height=8)
            elsewhere_scroll = ttk.Scrollbar(elsewhere_list_frame, orient='vertical', command=self.elsewhere_listbox.yview)
            self.elsewhere_listbox.configure(yscrollcommand=elsewhere_scroll.set)
            self.elsewhere_listbox.pack(side='left', fill='both', expand=True)
            elsewhere_scroll.pack(side='right', fill='y')
            self.elsewhere_tab.listbox = self.elsewhere_listbox

            # Buttons row for Elsewhere: Decrement only
            elsewhere_btns = ttk.Frame(self.elsewhere_tab.frame)
            elsewhere_btns.grid(row=7, column=0, columnspan=4, sticky='w', padx=5, pady=(0, 8))
            ttk.Button(elsewhere_btns, text="Decrement", command=self.decrement_elsewhere_item).pack(side='left')
        except Exception:
            pass

    # Map categories to their listboxes for load/save helpers
        self.listboxes = {
            'magic': self.magic_listbox,
            'stored_magic': self.stored_magic_listbox,
            'elsewhere': self.elsewhere_listbox,
        }

        # Load any pre-existing inventory data into the visible listboxes
        try:
            self.load_inventory_data()
        except Exception:
            pass

    def on_stored_magic_select(self, event=None):
        """When a stored magic entry is selected, mirror it to the right panel controls."""
        try:
            lb = self.stored_magic_listbox
            sel = lb.curselection()
            if not sel:
                return
            idx = sel[0]
            items = self.character_data['inventory'].get('stored_magic', [])
            if idx >= len(items):
                return
            entry = items[idx]
            # Ask the sub-tab to sync its controls
            if hasattr(self.stored_magic_tab, 'set_selection_from_entry'):
                self.stored_magic_tab.set_selection_from_entry(entry)
        except Exception:
            pass

    def add_magic_bag_item(self):
        item = self.magic_item_var.get()
        if item == "Custom...":
            item = self.magic_bag_tab.custom_item_entry.get().strip() or "Custom Item"
            gold = "-"
        else:
            gold = self.magic_bag_tab.gold_var.get()
        # store quantity as int in data
        try:
            qty_int = int(self.magic_quantity_var.get())
        except Exception:
            qty_int = 1
        # Deduct gold if not free and gold is numeric (guard against spending past 0)
        try:
            if getattr(self.magic_bag_tab, 'free_var', None) and not self.magic_bag_tab.free_var.get():
                cost_each = int(gold) if str(gold).isdigit() else None
                if cost_each is not None:
                    total_cost = cost_each * qty_int
                    if not self._ensure_funds_and_spend(total_cost):
                        return
        except Exception:
            pass
        items = self.character_data['inventory']['magic']
        # Find existing by name
        existing_idx = next((i for i, d in enumerate(items) if d.get('name') == item), None)
        if existing_idx is not None:
            items[existing_idx]['quantity'] = int(items[existing_idx].get('quantity', 1)) + qty_int
            # Keep existing gold value
            ex = items[existing_idx]
            try:
                desc = (self.magic_bag_tab.equipment_index.get(ex.get('name','')) or {}).get('description', '') or ''
            except Exception:
                desc = ''
            prefix = f"{ex.get('name','')} - {desc}" if desc else ex.get('name','')
            display = f"{prefix} (x{ex.get('quantity',1)}) - {ex.get('gold','-')}g each"
            # Update listbox at same index
            if existing_idx < self.magic_listbox.size():
                self.magic_listbox.delete(existing_idx)
                self.magic_listbox.insert(existing_idx, display)
                self.magic_listbox.select_set(existing_idx)
            else:
                self.magic_listbox.insert(tk.END, display)
        else:
            items.append({'name': item, 'quantity': qty_int, 'gold': gold})
            try:
                desc = (self.magic_bag_tab.equipment_index.get(item) or {}).get('description', '') or ''
            except Exception:
                desc = ''
            prefix = f"{item} - {desc}" if desc else item
            entry = f"{prefix} (x{qty_int}) - {gold}g each"
            self.magic_listbox.insert(tk.END, entry)

    def add_elsewhere_item(self):
        item = self.elsewhere_item_var.get()
        if item == "Custom...":
            item = self.elsewhere_tab.custom_item_entry.get().strip() or "Custom Item"
            gold = "-"
        else:
            gold = self.elsewhere_tab.gold_var.get()
        try:
            qty_int = int(self.elsewhere_quantity_var.get())
        except Exception:
            qty_int = 1
        location = self.elsewhere_location_var.get().strip() or "(No location)"
        # Deduct gold if not free and gold is numeric (guard against spending past 0)
        try:
            if getattr(self.elsewhere_tab, 'free_var', None) and not self.elsewhere_tab.free_var.get():
                cost_each = int(gold) if str(gold).isdigit() else None
                if cost_each is not None:
                    total_cost = cost_each * qty_int
                    if not self._ensure_funds_and_spend(total_cost):
                        return
        except Exception:
            pass
        items = self.character_data['inventory']['elsewhere']
        # Combine by name and location
        existing_idx = next((i for i, d in enumerate(items)
                             if d.get('name') == item and (d.get('location','') == location)), None)
        if existing_idx is not None:
            items[existing_idx]['quantity'] = int(items[existing_idx].get('quantity', 1)) + qty_int
            ex = items[existing_idx]
            try:
                desc = (self.elsewhere_tab.equipment_index.get(ex.get('name','')) or {}).get('description', '') or ''
            except Exception:
                desc = ''
            prefix = f"{ex.get('name','')} - {desc}" if desc else ex.get('name','')
            display = f"{prefix} (x{ex.get('quantity',1)}) - {ex.get('gold','-')}g each @ {ex.get('location','')}"
            if existing_idx < self.elsewhere_listbox.size():
                self.elsewhere_listbox.delete(existing_idx)
                self.elsewhere_listbox.insert(existing_idx, display)
                self.elsewhere_listbox.select_set(existing_idx)
            else:
                self.elsewhere_listbox.insert(tk.END, display)
        else:
            items.append({'name': item, 'quantity': qty_int, 'gold': gold, 'location': location})
            try:
                desc = (self.elsewhere_tab.equipment_index.get(item) or {}).get('description', '') or ''
            except Exception:
                desc = ''
            prefix = f"{item} - {desc}" if desc else item
            entry = f"{prefix} (x{qty_int}) - {gold}g each @ {location}"
            self.elsewhere_listbox.insert(tk.END, entry)

    def decrement_magic_item(self):
        lb = self.magic_listbox
        sel = lb.curselection()
        if not sel:
            messagebox.showwarning("Warning", "Select an item to decrement.")
            return
        idx = sel[0]
        items = self.character_data['inventory']['magic']
        if idx >= len(items):
            return
        item = items[idx]
        qty = item.get('quantity', 1)
        try:
            qty_int = int(qty)
        except Exception:
            qty_int = 1
        qty_int -= 1
        if qty_int <= 0:
            # remove item
            items.pop(idx)
            lb.delete(idx)
        else:
            item['quantity'] = qty_int
            try:
                desc = (self.magic_bag_tab.equipment_index.get(item.get('name','')) or {}).get('description', '') or ''
            except Exception:
                desc = ''
            prefix = f"{item.get('name','')} - {desc}" if desc else item.get('name','')
            display = f"{prefix} (x{qty_int}) - {item.get('gold','-')}g each"
            lb.delete(idx)
            lb.insert(idx, display)
            lb.select_set(idx)

    def decrement_elsewhere_item(self):
        lb = self.elsewhere_listbox
        sel = lb.curselection()
        if not sel:
            messagebox.showwarning("Warning", "Select an item to decrement.")
            return
        idx = sel[0]
        items = self.character_data['inventory']['elsewhere']
        if idx >= len(items):
            return
        item = items[idx]
        qty = item.get('quantity', 1)
        try:
            qty_int = int(qty)
        except Exception:
            qty_int = 1
        qty_int -= 1
        if qty_int <= 0:
            items.pop(idx)
            lb.delete(idx)
        else:
            item['quantity'] = qty_int
            try:
                desc = (self.elsewhere_tab.equipment_index.get(item.get('name','')) or {}).get('description', '') or ''
            except Exception:
                desc = ''
            prefix = f"{item.get('name','')} - {desc}" if desc else item.get('name','')
            display = f"{prefix} (x{qty_int}) - {item.get('gold','-')}g each @ {item.get('location','')}"
            lb.delete(idx)
            lb.insert(idx, display)
            lb.select_set(idx)

    def remove_stored_magic_item(self):
        lb = self.stored_magic_listbox
        sel = lb.curselection()
        if not sel:
            messagebox.showwarning("Warning", "Select a stored magic item to remove.")
            return
        idx = sel[0]
        items = self.character_data['inventory']['stored_magic']
        if idx >= len(items):
            return
        items.pop(idx)
        lb.delete(idx)

    def add_stored_magic_item(self):
        name = self.sm_item_var.get().strip()
        variant = self.sm_variant_var.get().strip()
        charges_text = self.sm_charges_var.get().strip()
        current = None
        maxc = None
        if charges_text:
            try:
                current = int(charges_text)
                maxc = current
            except Exception:
                current = None
                maxc = None
        # Persist
        entry = {'name': name}
        if variant:
            entry['variant'] = variant
        if current is not None and maxc is not None:
            entry['current_charges'] = str(current)
            entry['max_charges'] = str(maxc)
        self.character_data['inventory']['stored_magic'].append(entry)
        # Display in listbox
        parts = [name]
        if variant:
            parts.append(f"({variant})")
        if current is not None and maxc is not None:
            parts.append(f"Charges {current}/{maxc}")
        display = ' - '.join([p for p in parts if p])
        self.stored_magic_listbox.insert(tk.END, display)

    def normalize_stored_magic(self):
        """Normalize legacy stored_magic entries with quantities into individual items."""
        items = self.character_data['inventory'].get('stored_magic', [])
        normalized = []
        for item in items:
            if isinstance(item, dict) and 'quantity' in item and isinstance(item.get('quantity'), int):
                count = max(1, item.get('quantity', 1))
                for _ in range(count):
                    normalized.append({'name': item.get('name', '')})
            else:
                normalized.append(item)
        self.character_data['inventory']['stored_magic'] = normalized

    def load_inventory_data(self):
        """Load existing inventory data into the GUI"""
        # Normalize legacy stored_magic first
        self.normalize_stored_magic()
        for category in ['magic', 'stored_magic', 'elsewhere']:
            listbox = self.listboxes[category]
            # Clear any existing items first to avoid duplicates on reload
            listbox.delete(0, tk.END)
            for item_data in self.character_data['inventory'][category]:
                if category == 'elsewhere':
                    # Include description where available
                    try:
                        desc = (self.elsewhere_tab.equipment_index.get(item_data.get('name','')) or {}).get('description', '') or ''
                    except Exception:
                        desc = ''
                    prefix = f"{item_data.get('name','')} - {desc}" if desc else item_data.get('name','')
                    entry = f"{prefix} (x{item_data.get('quantity',1)}) - {item_data.get('gold','-')}g each @ {item_data.get('location','')}"
                elif category == 'stored_magic':
                    # Use rich display like in BasicInfoTab
                    if 'quantity' in item_data and isinstance(item_data.get('quantity'), int):
                        entry = f"{item_data.get('name','')} (x{item_data.get('quantity',1)})"
                    else:
                        parts = [item_data.get('name','')]
                        if item_data.get('variant'):
                            parts.append(f"({item_data['variant']})")
                        if 'current_charges' in item_data and 'max_charges' in item_data:
                            parts.append(f"Charges {item_data['current_charges']}/{item_data['max_charges']}")
                        entry = ' - '.join([p for p in parts if p])
                else:
                    # magic bag
                    try:
                        desc = (self.magic_bag_tab.equipment_index.get(item_data.get('name','')) or {}).get('description', '') or ''
                    except Exception:
                        desc = ''
                    prefix = f"{item_data.get('name','')} - {desc}" if desc else item_data.get('name','')
                    entry = f"{prefix} (x{item_data.get('quantity',1)}) - {item_data.get('gold','-')}g each"
                listbox.insert(tk.END, entry)

        # Optional: if materials are stored in character_data, display them in the Materials listbox
        try:
            materials = self.character_data['inventory'].get('materials', [])
            self.materials_listbox.delete(0, tk.END)
            comp_to_spells = getattr(self.materials_tab, 'component_to_spells', {}) or {}
            for m in materials:
                comp_name = m.get('name', '')
                spell_list = comp_to_spells.get(comp_name, [])
                spell_suffix = f" [{', '.join(spell_list)}]" if spell_list else ''
                cost_each = m.get('gold', '-')
                cost_str = 'N/A' if cost_each in (None, 'N/A') else f"{cost_each}"
                self.materials_listbox.insert(tk.END, f"{comp_name}{spell_suffix} (x{m.get('quantity',1)}) - {cost_str}g each")
        except Exception:
            pass

    def add_or_update_material(self):
        comp = self.mc_component_var.get().strip() or 'Material Component'
        try:
            qty_int = int(self.mc_quantity_var.get())
        except Exception:
            qty_int = 1
        die = getattr(self.materials_tab, 'prereq_var', tk.StringVar(value='')).get().strip()
        cost_each = getattr(self.materials_tab, 'COST_BY_PREREQ', {}).get(die, None)
        cost_str = 'N/A' if cost_each is None else f"{cost_each}"
        # Determine spell suffix to display
        try:
            mode = getattr(self.materials_tab, 'mode_var').get()
        except Exception:
            mode = 'spell'
        spell_names = []
        if mode == 'spell':
            selected_spell = (self.mc_spell_var.get() or '').strip()
            if selected_spell:
                spell_names = [selected_spell]
        if not spell_names:
            comp_to_spells = getattr(self.materials_tab, 'component_to_spells', {}) or {}
            spell_names = comp_to_spells.get(comp, [])
        spell_suffix = f" [{', '.join(spell_names)}]" if spell_names else ''
        # Deduct gold if not free and cost_each is numeric (guard against spending past 0)
        try:
            if getattr(self.materials_tab, 'free_var', None) and not self.materials_tab.free_var.get():
                if isinstance(cost_each, int):
                    total_cost = cost_each * qty_int
                    if not self._ensure_funds_and_spend(total_cost):
                        return
        except Exception:
            pass

        # Persist to character_data with quantity combining
        materials = self.character_data['inventory'].setdefault('materials', [])
        existing_idx = next((i for i, m in enumerate(materials) if m.get('name') == comp), None)
        if existing_idx is not None:
            materials[existing_idx]['quantity'] = int(materials[existing_idx].get('quantity', 1)) + qty_int
            # Keep existing gold
            ex = materials[existing_idx]
            disp_cost = 'N/A' if ex.get('gold') in (None, 'N/A') else f"{ex.get('gold')}"
            # Build display with spell suffix (use mapping for existing comp)
            comp_name = ex.get('name', '')
            if not spell_names:
                comp_to_spells = getattr(self.materials_tab, 'component_to_spells', {}) or {}
                spell_list = comp_to_spells.get(comp_name, [])
                spell_suffix = f" [{', '.join(spell_list)}]" if spell_list else ''
            display = f"{comp_name}{spell_suffix} (x{ex.get('quantity',1)}) - {disp_cost}g each"
            # Update listbox at same index
            if existing_idx < self.materials_listbox.size():
                self.materials_listbox.delete(existing_idx)
                self.materials_listbox.insert(existing_idx, display)
                self.materials_listbox.select_set(existing_idx)
            else:
                self.materials_listbox.insert(tk.END, display)
        else:
            new_gold = cost_each if cost_each is not None else 'N/A'
            materials.append({'name': comp, 'quantity': qty_int, 'gold': new_gold})
            entry = f"{comp}{spell_suffix} (x{qty_int}) - {('N/A' if new_gold == 'N/A' else str(new_gold))}g each"
            self.materials_listbox.insert(tk.END, entry)

    def decrement_material_item(self):
        lb = self.materials_listbox
        sel = lb.curselection()
        if not sel:
            messagebox.showwarning("Warning", "Select a material to decrement.")
            return
        idx = sel[0]
        materials = self.character_data['inventory'].setdefault('materials', [])
        if idx >= len(materials):
            return
        item = materials[idx]
        qty = item.get('quantity', 1)
        try:
            qty_int = int(qty)
        except Exception:
            qty_int = 1
        qty_int -= 1
        if qty_int <= 0:
            materials.pop(idx)
            lb.delete(idx)
        else:
            item['quantity'] = qty_int
            cost_each = item.get('gold', '-')
            cost_str = 'N/A' if cost_each in (None, 'N/A') else f"{cost_each}"
            comp_name = item.get('name', '')
            comp_to_spells = getattr(self.materials_tab, 'component_to_spells', {}) or {}
            spell_list = comp_to_spells.get(comp_name, [])
            spell_suffix = f" [{', '.join(spell_list)}]" if spell_list else ''
            display = f"{comp_name}{spell_suffix} (x{qty_int}) - {cost_str}g each"
            lb.delete(idx)
            lb.insert(idx, display)
            lb.select_set(idx)

    def get_data(self):
        """Get inventory data"""
        return {
            'inventory': self.character_data['inventory']
        }

    def _adjust_gold(self, delta: int):
        try:
            current = int(self.character_data.get('resources', {}).get('gold', 0))
            new_val = current + int(delta)
            if 'resources' not in self.character_data:
                self.character_data['resources'] = {}
            self.character_data['resources']['gold'] = new_val
            # Update Basic Info tab via callback if provided
            if callable(self.update_gold_callback):
                self.update_gold_callback(new_val)
        except Exception:
            pass

    def _ensure_funds_and_spend(self, total_cost: int) -> bool:
        """Return True if funds are sufficient and spend applied, else warn and return False."""
        try:
            if total_cost is None or total_cost <= 0:
                return True
            current = int(self.character_data.get('resources', {}).get('gold', 0))
            if total_cost > current:
                messagebox.showwarning("Insufficient Gold", f"You don't have enough gold for this purchase.\nRequired: {total_cost}g, Available: {current}g")
                return False
            self._adjust_gold(-total_cost)
            return True
        except Exception:
            # If anything unexpected happens, do not spend
            messagebox.showwarning("Insufficient Gold", "Unable to process purchase due to an unexpected error.")
            return False

    def set_data(self, data):
        """Set inventory data"""
        self.character_data['inventory'] = data.get('inventory', {
            'magic': [],
            'stored_magic': [],
            'elsewhere': [],
            'materials': []
        })
        
        # Clear all listboxes
        for listbox in self.listboxes.values():
            listbox.delete(0, tk.END)
        
        # Load the new data
        self.load_inventory_data()