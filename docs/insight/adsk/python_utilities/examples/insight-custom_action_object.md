# Insight: Using Callable Objects for Custom Actions

This document explains the `custom_action_object.py` example script. It shows an advanced but very efficient way to create many similar menu items without writing a separate function for each one.

**Target Audience:** Novice Python programmers learning about Classes and "Callables."

---

## 1. The Problem: Repeating Yourself

Imagine you want 4 menu items: "Action 1", "Action 2", "Action 3", and "Action 4". All of them should do basically the same thing, but they need to know *which* button was clicked.

The "old" way would be to write 4 separate functions. That's a lot of copying and pasting!

## 2. The Solution: The "Callable" Object

In Python, you can create a **Class** that acts like a function. This is called making an object "callable."

### How it works:
Look at the `Action` class inside the script:

```python
class Action(object):
    def __init__(self, action_id):
        self._action_id = action_id # Remember which ID I am

    def __call__(self, selection):
        # This makes the object act like a function!
        return action_on_selection(self._action_id, selection)
```

1.  **`__init__`**: When we create `Action("Action1")`, it saves "Action1" inside itself.
2.  **`__call__`**: This is a special Python magic method. It tells Python: "If someone tries to run this object like a function (using parentheses), run this code."

## 3. Why is this powerful?

Look at how the menu is built in the loop:

```python
action_ids = ["Action1", "Action2", "Action3", "Action4"]
for action_id in action_ids:
    # We create a NEW object for each ID
    actions["actions"].append({
        "name": action_id, 
        "execute": Action(action_id) # Pass the object as the command
    })
```

By using this trick, you can generate hundreds of menu items dynamically (for example, one for every preset file in a folder) while only writing the logic **once**.

---

## 4. Key Takeaway for Beginners

If you find yourself writing `function1()`, `function2()`, `function3()` that all look identical, consider using a **Callable Class**. It keeps your code clean, short, and much easier to fix if you need to change the logic later!
