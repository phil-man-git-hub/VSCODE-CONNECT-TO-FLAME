import fu_bootstrap

class FuMenuRegistry:
    """
    Singleton registry for Flame contextual menu actions.
    Stores actions registered via decorators and formats them for Flame hooks.
    """
    _instance = None

    def __new__(cls):
        if not cls._instance:
            cls._instance = object.__new__(cls)
            cls._instance._registry = {}
        return cls._instance

    def register(self, menu_context, action_def):
        """
        Register an action definition for a specific menu context.
        
        Args:
            menu_context (str): The hook context (e.g., 'media_panel', 'batch').
            action_def (dict): The action definition containing keys like:
                               'name', 'execute', 'path', 'isVisible', etc.
        """
        if menu_context not in self._registry:
            self._registry[menu_context] = []
        
        self._registry[menu_context].append(action_def)

    def get_actions_for_hook(self, menu_context):
        """
        Returns the list of action groups formatted for a Flame hook.
        
        This implementation groups actions by their 'group_name' (derived from path).
        """
        if menu_context not in self._registry:
            return []

        raw_actions = self._registry[menu_context]
        
        # Organize by top-level group to avoid creating 100 separate groups
        # We assume the 'path' starts with the Group Name.
        # e.g. path="Flame Utilities / Export" -> Group="Flame Utilities", Hierarchy=["Export"]
        
        grouped_actions = {}

        for action in raw_actions:
            path_parts = [p.strip() for p in action.get('path', 'Flame Utilities').split('/')]
            
            group_name = path_parts[0]
            hierarchy = path_parts[1:]
            
            # Construct the Flame action dictionary
            flame_action = {
                "name": action['name'],
                "execute": action['execute']
            }
            
            if 'isVisible' in action:
                flame_action['isVisible'] = action['isVisible']
            if 'isEnabled' in action:
                flame_action['isEnabled'] = action['isEnabled']
            if 'minimumVersion' in action:
                flame_action['minimumVersion'] = action['minimumVersion']
            if 'maximumVersion' in action:
                flame_action['maximumVersion'] = action['maximumVersion']
            if 'waitCursor' in action:
                flame_action['waitCursor'] = action['waitCursor']

            # Retrieve or create the group definition
            if group_name not in grouped_actions:
                grouped_actions[group_name] = []

            # Determine structure based on hierarchy
            # If there is hierarchy, we need a way to represent it.
            # Flame's 2023.2+ 'hierarchy' key is on the group definition, not the action.
            # However, hooks return a list of groups.
            # If we have mixed hierarchies in the same group, it gets complex.
            # For simplicity in V1: We will create a separate "Flame Group" 
            # for every unique path to ensure hierarchy is correct, 
            # OR we rely on Flame's flat menu capability if hierarchy is empty.
            
            # Strategy: One dictionary per action wrapper to support full hierarchy per item
            # This is verbose but safe.
            
            group_def = {
                "name": group_name,
                "actions": [flame_action]
            }
            
            if hierarchy:
                # If there is a sub-path (e.g. "Utils / Export")
                # Flame expects 'hierarchy': ['Utils', 'Export']
                # But wait, 'hierarchy' defines where the GROUP is placed.
                # So if group_name is "Flame Utilities", and hierarchy is ["My Tools"]
                # The menu is Main > Flame Utilities > My Tools > Action.
                # This works if we treat the first part of path as the custom menu name.
                
                # To support complex nesting, we just pass the hierarchy
                group_def["hierarchy"] = hierarchy

            grouped_actions.setdefault(group_name + str(hierarchy), []).append(group_def)

        # Flatten the values
        final_list = []
        for key in grouped_actions:
            # grouped_actions[key] is a list of group_defs (one per action basically)
            # We can try to merge them if they share exact name and hierarchy
            # But for now, returning the list is safe.
             final_list.extend(grouped_actions[key])
             
        return final_list
