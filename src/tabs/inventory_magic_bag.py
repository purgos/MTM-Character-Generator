import tkinter as tk
from tkinter import ttk

class InventoryMagicBag:
    def __init__(self, parent, item_var, quantity_var, add_callback, listbox):
        self.frame = ttk.Frame(parent)

        # Data bindings
        self.item_var = item_var
        self.quantity_var = quantity_var
        self.listbox = listbox

        # Import equipment list from equipment_list.py
        try:
            from src.equipment_list import equipment as equipment_data
        except ImportError:
            from equipment_list import equipment as equipment_data
        self.equipment_list = [(item['name'], item.get('price')) for item in equipment_data]
        self.equipment_list.append(("Custom...", None))

        # UI state vars
        self.gold_var = tk.StringVar(value="-")
        self.total_gold_var = tk.StringVar(value="-")

        # Row 0: Item + price
        ttk.Label(self.frame, text="Select Item:").grid(row=0, column=0, padx=5, pady=5, sticky="w")
        self.item_combo = ttk.Combobox(self.frame, textvariable=self.item_var, state="readonly")
        self.item_combo['values'] = [name for name, _ in self.equipment_list]
        self.item_combo.grid(row=0, column=1, padx=5, pady=5, sticky="ew")
        self.item_combo.bind('<<ComboboxSelected>>', self.on_item_selected)

        ttk.Label(self.frame, text="Gold per Item:").grid(row=0, column=2, padx=5, pady=5, sticky="w")
        ttk.Label(self.frame, textvariable=self.gold_var).grid(row=0, column=3, padx=5, pady=5, sticky="w")

        # Row 1: Custom item name (hidden by default)
        self.custom_item_entry = ttk.Entry(self.frame)
        self.custom_item_entry.grid(row=1, column=1, padx=5, pady=5, sticky="ew")
        self.custom_item_entry.grid_remove()

        # Row 2: Quantity + total gold
        ttk.Label(self.frame, text="Quantity:").grid(row=2, column=0, padx=5, pady=5, sticky="w")
        self.quantity_combo = ttk.Combobox(self.frame, textvariable=self.quantity_var, state="readonly")
        self.quantity_combo['values'] = [str(i) for i in range(1, 11)]
        self.quantity_combo.grid(row=2, column=1, padx=5, pady=5, sticky="ew")
        self.quantity_combo.current(0)
        self.quantity_combo.bind('<<ComboboxSelected>>', self.update_total_gold)

        ttk.Label(self.frame, text="Total Gold:").grid(row=2, column=2, padx=5, pady=5, sticky="w")
        ttk.Label(self.frame, textvariable=self.total_gold_var).grid(row=2, column=3, padx=5, pady=5, sticky="w")

        # Row 3: Add button (use provided callback if any)
        handler = add_callback if add_callback else self.add_item
        ttk.Button(self.frame, text="Add", command=handler).grid(row=3, column=0, columnspan=4, pady=10)

    def on_item_selected(self, event=None):
        item = self.item_var.get()
        if item == "Custom...":
            self.custom_item_entry.grid()
            self.gold_var.set("-")
        else:
            self.custom_item_entry.grid_remove()
            gold = next((g for i, g in self.equipment_list if i == item), None)
            self.gold_var.set(str(gold) if gold is not None else "-")
        self.update_total_gold()

    def update_total_gold(self, event=None):
        try:
            qty = int(self.quantity_var.get())
        except Exception:
            qty = 1
        item = self.item_var.get()
        if item == "Custom...":
            self.total_gold_var.set("-")
            return
        gold = next((g for i, g in self.equipment_list if i == item), None)
        if gold is not None:
            self.total_gold_var.set(str(gold * qty))
        else:
            self.total_gold_var.set("-")

    def add_item(self):
        item = self.item_var.get()
        if item == "Custom...":
            item = self.custom_item_entry.get().strip() or "Custom Item"
            gold = "-"
        else:
            gold = self.gold_var.get()
        qty = self.quantity_var.get()
        entry = f"{item} (x{qty}) - {gold}g each"
        self.listbox.insert(tk.END, entry)
