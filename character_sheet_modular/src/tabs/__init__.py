# MTM Character Sheet Tabs Package
# This package contains all the individual tab modules for the character sheet application

from .basic_info_tab import BasicInfoTab
from .aspects_tab import AspectsTab
from .gear_die_tab import GearDieTab
from .inventory_tab import InventoryTab
from .abilities_tab import AbilitiesTab

__all__ = [
    'BasicInfoTab',
    'AspectsTab', 
    'GearDieTab',
    'InventoryTab',
    'AbilitiesTab'
] 