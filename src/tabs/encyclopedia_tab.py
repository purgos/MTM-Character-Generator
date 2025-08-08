import tkinter as tk
from tkinter import ttk
import re

# Robust import for MAGIC_ITEMS, SPELLS, and ASPECT_ABILITIES
try:
    from magic_items import MAGIC_ITEMS
except ModuleNotFoundError:
    try:
        from ..magic_items import MAGIC_ITEMS
    except Exception:
        import os, sys as _sys
        _base_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
        if _base_dir not in _sys.path:
            _sys.path.insert(0, _base_dir)
        from magic_items import MAGIC_ITEMS

try:
    from spells import SPELLS
except ModuleNotFoundError:
    try:
        from ..spells import SPELLS
    except Exception:
        import os, sys as _sys
        _base_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
        if _base_dir not in _sys.path:
            _sys.path.insert(0, _base_dir)
        from spells import SPELLS

try:
    from aspect_abilities import ASPECT_ABILITIES
except ModuleNotFoundError:
    try:
        from ..aspect_abilities import ASPECT_ABILITIES
    except Exception:
        import os, sys as _sys
        _base_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
        if _base_dir not in _sys.path:
            _sys.path.insert(0, _base_dir)
        from aspect_abilities import ASPECT_ABILITIES

class EncyclopediaTab:
    """A read-only encyclopedia to browse and search magic items, spells, and abilities."""
    def __init__(self, parent, character_data=None):
        self.parent = parent
        self.character_data = character_data or {}
        self.tab = ttk.Frame(parent)
        self.MAGIC_ITEMS = MAGIC_ITEMS
        self.SPELLS = SPELLS
        self.ASPECT_ABILITIES = ASPECT_ABILITIES
        # Build indices
        self._build_item_index()
        self._build_spells_index()
        self._build_abilities_index()
        self.create_tab()

    # --- Helpers ---
    def sanitize_item_name(self, name: str) -> str:
        if not name:
            return name
        name = re.sub(r"[\u2018\u2019\u02BC\u2032`']", "", name)
        name = re.sub(r"\s+", " ", name).strip()
        return name

    def sanitize_text(self, text: str) -> str:
        if not text:
            return text
        text = re.sub(r"[\u2018\u2019\u02BC\u2032`']", "", text)
        text = re.sub(r"\s+", " ", text)
        return text.strip()

    def _titlecase_with_exceptions(self, s: str) -> str:
        """Title-case a string but keep small words lowercase unless first. Also lowercases 'your'."""
        if not s:
            return s
        small_words = {
            'a', 'an', 'and', 'as', 'at', 'but', 'by', 'for', 'in', 'nor', 'of', 'on', 'or',
            'per', 'the', 'to', 'up', 'via', 'with', 'from', 'into', 'over', 'under', 'off', 'out',
            'vs', 'v', 'your'
        }
        parts = self.sanitize_item_name(s).lower().split()
        if not parts:
            return ''
        titled = [parts[0].capitalize()]
        for w in parts[1:]:
            if w in small_words:
                titled.append(w)
            else:
                titled.append(w[:1].upper() + w[1:])
        return ' '.join(titled)

    def _build_item_index(self):
        """Flatten MAGIC_ITEMS into a searchable list."""
        self.item_index = []
        self.item_groups = []
        for group, group_dict in self.MAGIC_ITEMS.items():
            self.item_groups.append(group)
            for key, item_data in group_dict.items():
                name = self.sanitize_item_name(item_data.get('name', key))
                entry = {
                    'name': name,
                    'group': group,
                    'description': self.sanitize_text(item_data.get('description', '')),
                    'variants': list(item_data.get('variants', [])) if isinstance(item_data.get('variants'), (list, tuple)) else [],
                    'charges': item_data.get('charges', None)
                }
                # Avoid duplicate names by keeping first appearance
                if not any(e['name'] == name and e['group'] == group for e in self.item_index):
                    self.item_index.append(entry)
        self.item_groups = sorted(set(self.item_groups))

    def _build_spells_index(self):
        """Flatten SPELLS into a searchable list."""
        self.spell_index = []
        # Group for spells: use first letter for quick filtering or single 'All Spells'
        self.spell_groups = set()
        for name, data in self.SPELLS.items():
            clean_name = self._titlecase_with_exceptions(name)
            group = clean_name[0] if clean_name else 'Other'
            self.spell_groups.add(group)
            entry = {
                'name': clean_name,
                'group': group,
                'data': data
            }
            self.spell_index.append(entry)
        self.spell_groups = sorted(self.spell_groups)

    def _build_abilities_index(self):
        """Flatten ASPECT_ABILITIES into a searchable list."""
        self.ability_index = []
        self.ability_groups = []
        for aspect, abilities in self.ASPECT_ABILITIES.items():
            self.ability_groups.append(aspect)
            for ability_name, description in abilities.items():
                entry = {
                    'name': self.sanitize_item_name(ability_name),
                    'group': aspect,
                    'description': self.sanitize_text(description)
                }
                self.ability_index.append(entry)
        self.ability_groups = sorted(set(self.ability_groups))

    def create_tab(self):
        # Layout: top = source + filters; left = list, right = description
        container = ttk.Frame(self.tab)
        container.pack(fill='both', expand=True, padx=5, pady=5)

        top = ttk.Frame(container)
        top.pack(side='top', fill='x', padx=5, pady=5)

        ttk.Label(top, text='Source:').pack(side='left', padx=(0,5))
        self.mode_var = tk.StringVar(value='Magic Items')
        self.mode_combo = ttk.Combobox(top, textvariable=self.mode_var,
                                       values=['Magic Items', 'Spells', 'Abilities'], state='readonly', width=16)
        self.mode_combo.pack(side='left', padx=(0,10))
        self.mode_combo.bind('<<ComboboxSelected>>', self._on_mode_changed)

        ttk.Label(top, text='Query:').pack(side='left', padx=5)
        self.search_var = tk.StringVar()
        search_entry = ttk.Entry(top, textvariable=self.search_var, width=28)
        search_entry.pack(side='left', padx=5)
        search_entry.bind('<KeyRelease>', self._on_filter_changed)

        ttk.Label(top, text='Group:').pack(side='left', padx=5)
        self.group_var = tk.StringVar(value='All')
        self.group_combo = ttk.Combobox(top, textvariable=self.group_var, values=['All'], state='readonly', width=14)
        self.group_combo.pack(side='left', padx=5)
        self.group_combo.bind('<<ComboboxSelected>>', self._on_filter_changed)

        clear_btn = ttk.Button(top, text='Clear', command=self._clear_search)
        clear_btn.pack(side='left', padx=5)

        body = ttk.Frame(container)
        body.pack(side='top', fill='both', expand=True)

        left = ttk.LabelFrame(body, text='Items')
        left.pack(side='left', fill='both', expand=False, padx=5, pady=5)
        right = ttk.LabelFrame(body, text='Description')
        right.pack(side='right', fill='both', expand=True, padx=5, pady=5)

        self.items_listbox = tk.Listbox(left, height=24, width=45)
        self.items_listbox.pack(fill='both', expand=True, padx=5, pady=5)
        self.items_listbox.bind('<<ListboxSelect>>', self._on_select_item)

        self.desc_text = tk.Text(right, wrap='word', height=25, state='disabled')
        self.desc_text.pack(fill='both', expand=True, padx=5, pady=5)

        # Initialize group filter and list for default mode
        self._refresh_groups()
        self._refresh_list()

    # --- UI actions ---
    def _on_mode_changed(self, event=None):
        self._refresh_groups()
        self._refresh_list()

    def _clear_search(self):
        self.search_var.set('')
        self.group_var.set('All')
        self._refresh_list()

    def _on_filter_changed(self, event=None):
        self._refresh_list()

    def _refresh_groups(self):
        mode = self.mode_var.get()
        if mode == 'Magic Items':
            groups = ['All'] + self.item_groups
        elif mode == 'Spells':
            groups = ['All'] + self.spell_groups
        else:  # Abilities
            groups = ['All'] + self.ability_groups
        self.group_combo['values'] = groups
        if self.group_var.get() not in groups:
            self.group_var.set('All')

    def _refresh_list(self):
        mode = self.mode_var.get()
        query = self.search_var.get().strip().lower()
        group = self.group_var.get()
        self.items_listbox.delete(0, tk.END)
        self.filtered_items = []
        if mode == 'Magic Items':
            data = sorted(self.item_index, key=lambda e: (e['group'], e['name']))
            for entry in data:
                if group != 'All' and entry['group'] != group:
                    continue
                if query and query not in entry['name'].lower():
                    continue
                self.filtered_items.append(('item', entry))
                display = f"{entry['name']}  [{entry['group']}]"
                self.items_listbox.insert(tk.END, display)
        elif mode == 'Spells':
            data = sorted(self.spell_index, key=lambda e: (e['group'], e['name']))
            for entry in data:
                if group != 'All' and entry['group'] != group:
                    continue
                if query and query not in entry['name'].lower():
                    continue
                self.filtered_items.append(('spell', entry))
                display = f"{entry['name']}  [Spells {entry['group']}]"
                self.items_listbox.insert(tk.END, display)
        else:  # Abilities
            data = sorted(self.ability_index, key=lambda e: (e['group'], e['name']))
            for entry in data:
                if group != 'All' and entry['group'] != group:
                    continue
                if query and query not in entry['name'].lower():
                    continue
                self.filtered_items.append(('ability', entry))
                display = f"{entry['name']}  [Ability {entry['group']}]"
                self.items_listbox.insert(tk.END, display)
        # Auto-select first and update description
        if not self.filtered_items:
            self._set_description_text("No entries match your search.")
        else:
            self.items_listbox.select_clear(0, tk.END)
            self.items_listbox.select_set(0)
            self.items_listbox.event_generate('<<ListboxSelect>>')

    def _on_select_item(self, event=None):
        sel = self.items_listbox.curselection()
        if not sel:
            self._set_description_text("Select an entry to view details.")
            return
        idx = sel[0]
        if idx >= len(self.filtered_items):
            return
        kind, entry = self.filtered_items[idx]
        if kind == 'item':
            parts = [self.sanitize_text(entry.get('description', '(No description available)'))]
            if entry.get('variants'):
                parts.append("\nVariants: " + ', '.join(entry['variants']))
            if entry.get('charges') is not None:
                parts.append(f"\nDefault Charges: {entry['charges']}")
            self._set_description_text('\n'.join(parts))
        elif kind == 'spell':
            s = entry['data']
            lines = []
            lines.append(self.sanitize_text(s.get('description', '(No description)')))
            if s.get('area_of_effect'):
                lines.append(f"\nArea of Effect: {s['area_of_effect']}")
            if s.get('duration'):
                lines.append(f"\nDuration: {s['duration']}")
            if s.get('frequency'):
                lines.append(f"\nFrequency: {s['frequency']}")
            if s.get('prerequisite'):
                lines.append(f"\nPrerequisite: {s['prerequisite']}")
            if s.get('material_component'):
                lines.append(f"\nMaterial Component: {s['material_component']}")
            if s.get('spell_components'):
                try:
                    comps = ', '.join(s['spell_components'])
                except Exception:
                    comps = str(s['spell_components'])
                lines.append(f"\nSpell Components: {comps}")
            self._set_description_text('\n'.join(lines))
        else:  # ability
            text = self.sanitize_text(entry.get('description', '(No description)'))
            self._set_description_text(text)

    def _set_description_text(self, text: str):
        self.desc_text.config(state='normal')
        self.desc_text.delete('1.0', tk.END)
        self.desc_text.insert('1.0', text)
        self.desc_text.config(state='disabled')
