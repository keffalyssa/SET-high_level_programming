# Almost a Circle - Python OOP Project

This project implements object-oriented programming concepts in Python through the creation of geometric classes (`Base`, `Rectangle`, and `Square`) with serialization and file I/O capabilities.

## Learning Objectives

- Understand class attributes and instance attributes
- Implement private attributes with getters and setters
- Use static methods and class methods
- Work with JSON serialization and deserialization
- Perform file I/O operations with JSON
- Develop comprehensive unit tests for Python code

## Classes

### Base
The base class that manages an `id` attribute.
- Auto-generates unique IDs
- Provides JSON serialization methods
- Handles file persistence

### Rectangle
Inherits from `Base`. Represents a rectangle with width and height.
- Validates positive integer dimensions
- Calculates area
- Displays rectangle in terminal
- Outputs rectangle to CSV format

### Square
Inherits from `Rectangle`. Represents a square (width == height).
- Simplified interface for square-specific operations
- Updates size for both width and height simultaneously

## Testing

Run the test suite with:

```bash
python3 -m unittest discover tests
```

All classes and methods are fully unit tested.
