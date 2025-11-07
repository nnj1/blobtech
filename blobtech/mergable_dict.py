from numbers import Number
from typing import Dict, Any

class MergeableDict:
    """
    A dictionary wrapper that overloads the + operator.
    When merging, if two keys have numerical values, it adds them.
    Otherwise, the value from the right-hand dictionary is used (overwrite).
    """
    def __init__(self, initial_data: Dict[Any, Any] = None):
        # The internal dictionary stores the data
        self.data: Dict[Any, Any] = dict(initial_data) if initial_data else {}

    # Define the special method for the '+' operator
    def __add__(self, other: 'MergeableDict') -> 'MergeableDict':
        if not isinstance(other, MergeableDict):
            raise TypeError("Can only add MergeableDict objects")
        
        # Start with a copy of the current dictionary's data
        new_data = self.data.copy()

        # Iterate through the items of the 'other' dictionary
        for key, value in other.data.items():
            
            if key in new_data:
                existing_value = new_data[key]
                
                # Check if both values (existing and incoming) are numbers
                if isinstance(existing_value, Number) and isinstance(value, Number):
                    # If they are numbers, add the values together
                    new_data[key] = existing_value + value
                else:
                    # If they are non-numeric (e.g., strings, lists, or mixed types),
                    # use the value from the right-hand dictionary (standard overwrite)
                    new_data[key] = value
            else:
                # Key does not exist in the base dictionary, so just add it
                new_data[key] = value
        
        # Return a new MergeableDict instance with the combined data
        return MergeableDict(new_data)

    def __repr__(self) -> str:
        return_str = f"MergeableDict("
        """Ensures clean printing of the object."""
        if 'poison' in self.data:
            return_str += '🤢 ' + str(self.data.get('poison')) + ', '
        if 'burn' in self.data:
            return_str += '🔥 ' + str(self.data.get('burn')) + ', '
        if 'sleep' in self.data:
            return_str += '💤 ' + str(self.data.get('sleep')) + ', '
        if 'silence' in self.data:
            return_str += '🤫 ' + str(self.data.get('silence')) + ', '
        if 'blind' in self.data:
            return_str += '👓 ' + str(self.data.get('blind')) + ', '
        if 'petrify' in self.data:
            return_str += '🪦 ' + str(self.data.get('petrify')) + ')'
        else:
            return_str = f"MergeableDict({self.data})"
        return return_str