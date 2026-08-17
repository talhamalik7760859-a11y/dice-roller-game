# dice-roller-game
A Python-based dice roller game that simulates rolling dice with random outcomes--built as a beginner-friendly command-line project.
# Complete Dice Roller Simulator

A comprehensive dice rolling application with statistics tracking, game modes, and a user-friendly interface. Available in Python.

# Features

 **Core Features:**
- Roll two dice (1-6 each)
- Display results with visual formatting
- Ask user if they want to roll again
- Clear, maintainable code structure

 **Advanced Features:**
- Complete roll history tracking
- Statistical analysis (average, highest, lowest, most common rolls)
- Count of sevens and doubles
- Craps game mode
- Statistics reset functionality
- Beautiful formatted output with emojis


  Quick Start
 Python Version
Requirements:Python 3.6+

```bash
# Run the program
python dice_roller_complete.py
```

Features:
- Object-oriented design with DiceRoller class
- Type hints for better code clarity
- Comprehensive documentation
- Statistics calculation methods

### JavaScript Version

**Requirements:** Node.js 12+

```bash
# Run the program
node dice_roller_complete.js
```

**Features:**
- Class-based implementation
- Async/await for user input handling
- Promise-based interaction
- Clean readline interface

### Java Version

**Requirements:** Java 8+

```bash
# Compile the program
javac DiceRoller.java

# Run the program
java DiceRoller
```

**Features:**
- Object-oriented with methods
- HashMap for statistics
- Scanner for user input
- Stream API for data processing

---

##  Menu Options

```
DICE ROLLER MENU
==================================================
  1. Roll the Dice          - Roll two dice once
  2. View Statistics        - See detailed statistics
  3. View Roll History      - See all previous rolls
  4. Play Craps Game        - Play a game of Craps
  5. Reset Statistics       - Clear all roll history
  6. Exit                   - Close the program
==================================================
```

---

##  Statistics Provided

After rolling, you can view:

| Statistic | Description |
|-----------|-------------|
| **Total Rolls** | Number of dice rolls performed |
| **Highest Roll** | Maximum sum from any roll |
| **Lowest Roll** | Minimum sum from any roll |
| **Average Roll** | Mean value of all rolls |
| **Most Common Roll** | Most frequently rolled sum |
| **Number of Sevens** | Count of rolls that sum to 7 |
| **Number of Doubles** | Count of rolls where both dice match |

---

##  Craps Game Mode

A simplified Craps game implementation:

**Rules:**
- First Roll:
  - **7 or 11** → WIN immediately
  - **2, 3, or 12** → LOSE immediately
  - **Any other number** → Establish that number as the "point"

- Point Roll:
  - **Roll your point number** → WIN
  - **Roll a 7** → LOSE (seven out)
  - **Any other number** → Keep rolling

---

##  Code Structure

### Python Version

```python
class DiceRoller:
    - __init__()              # Initialize
    - roll_dice()             # Roll two dice
    - display_results()       # Show results
    - get_statistics()        # Calculate stats
    - display_statistics()    # Show stats
    - display_roll_history()  # Show all rolls
    - play_game_mode()        # Play Craps
    - reset_statistics()      # Clear data
    - display_menu()          # Show menu
    - run()                   # Main loop
```

### JavaScript Version

```javascript
class DiceRoller:
  - constructor()             // Initialize
  - rollDice()               // Roll two dice
  - displayResults()         // Show results
  - getStatistics()          // Calculate stats
  - displayStatistics()      // Show stats
  - displayRollHistory()     // Show all rolls
  - playGameMode()           // Play Craps (async)
  - resetStatistics()        // Clear data (async)
  - promptUser()             // Get input (async)
  - displayMenu()            // Show menu (async)
  - run()                    // Main loop (async)
```

### Java Version

```java
public class DiceRoller:
  - DiceRoller()              // Constructor
  - rollDice()                // Roll two dice
  - displayResults()          // Show results
  - getStatistics()           // Calculate stats
  - displayStatistics()       // Show stats
  - displayRollHistory()      // Show all rolls
  - playGameMode()            // Play Craps
  - resetStatistics()         // Clear data
  - promptUser()              // Get input
  - displayMenu()             // Show menu
  - run()                     // Main loop
  - main()                    // Entry point
```

---

##  Example Workflow

```
1. Start the program
2. Choose "1. Roll the Dice"
3. Press Enter to roll
4. See results (Die 1, Die 2, Total)
5. Choose "2. View Statistics" to see current stats
6. Choose "3. View Roll History" to see all rolls
7. Choose "4. Play Craps Game" for a game
8. Choose "5. Reset Statistics" to clear data
9. Choose "6. Exit" to quit
```

---

##  Installation & Setup

### Python
```bash
# No external dependencies required
# Just make sure Python 3.6+ is installed
python dice_roller_complete.py
```

### JavaScript
```bash
# Make sure Node.js is installed
# No npm packages required
node dice_roller_complete.js
```

### Java
```bash
# Make sure Java 8+ is installed
javac DiceRoller.java
java DiceRoller
```

---

##  Code Quality Features
**Best Practices:**
- Object-oriented design
- Single responsibility principle
- Clear method documentation
- Type hints/annotations
- Error handling
- Input validation
- Modular structure
- DRY (Don't Repeat Yourself)

 **Professional Standards:**
- Meaningful variable names
- Proper code formatting
- Comprehensive comments
- Consistent naming conventions
- Proper encapsulation
- Separated concerns

---

##  User Interface

The program features:

-  **Clear Menus** - Easy navigation
-  **Formatted Output** - Visual separators and emojis
-  **Input Validation** - Handles invalid entries gracefully
-   **Visual Feedback** - Emoji indicators for results
-  **Organized Display** - Well-structured information

---

##  Error Handling

The program handles:
- Invalid menu selections
- Empty roll history queries
- Invalid Craps game responses
- Reset confirmation prompts
- Graceful exit handling

---

##  Statistics Calculation

### Algorithm for Most Common Roll
1. Count frequency of each roll sum (2-12)
2. Find the sum with highest frequency
3. Return that value

### Algorithm for Average
1. Sum all roll totals
2. Divide by number of rolls
3. Round to 2 decimal places

---

##  Learning Outcomes

By studying this code, you'll learn:

1. **Object-Oriented Programming**
   - Class design
   - Method organization
   - Encapsulation

2. **Data Structures**
   - Lists/Arrays
   - Hash Maps/Dictionaries

3. **Control Flow**
   - While loops
   - Switch statements
   - Conditional logic

4. **User Interaction**
   - Input validation
   - Output formatting
   - Menu systems

5. **Statistics**
   - Calculating averages
   - Finding max/min
   - Frequency counting

---

##  Comparing Implementations

| Feature | Python | JavaScript | Java |
|---------|--------|-----------|------|
| **Syntax** | Simple, Pythonic | ES6+ Modern | Verbose, Type-safe |
| **Learning Curve** | Easiest | Medium | Steeper |
| **Performance** | Good | Fast | Very Fast |
| **Best For** | Learning, Quick Scripts | Web, Node.js | Large Applications |
| **Type Safety** | Dynamic | Dynamic | Static |
| **Async Support** | Limited | Full (async/await) | Multithreading |

---

##  Files Included

1. **dice_roller_complete.py** - Complete Python implementation
2. **dice_roller_complete.js** - Complete JavaScript implementation
3. **DiceRoller.java** - Complete Java implementation
4. **README.md** - This documentation file
5. **dice_roller.py** - Simple Python version (basic)
6. **dice_roller.js** - Simple JavaScript version (basic)

---

##  Running the Simple Versions

If you want the basic dice roller without advanced features:

```bash
# Python
python dice_roller.py

# JavaScript
node dice_roller.js
```

---

##  Tips & Tricks

1. **Quick Exit:** Press Ctrl+C to force quit
2. **View History:** Choose option 3 to see all rolls
3. **Game Strategy:** In Craps, establishing a point can be strategic
4. **Statistics:** Review stats periodically to see patterns
5. **Reset Wisely:** Make sure you want to clear data before resetting

---

##  Contributing

Feel free to enhance this project:
- Add more game modes (Yahtzee, High/Low betting)
- Implement save/load functionality
- Add GUI version
- Support for more dice
- Leaderboard system
- Probability analysis

---

##  License

This project is free to use and modify for educational purposes.

---

##  Version History

**v1.0** - Initial Release
- Core dice rolling functionality
- Statistics tracking
- Craps game mode
- Multi-language support
- Complete documentation

---

##  Next Steps

1. Choose your preferred language (Python, JavaScript, or Java)
2. Run the program
3. Try all menu options
4. Play the Craps game
5. Review the statistics
6. Study the code structure

---

##  Support

If you encounter any issues:
1. Check that the correct version of your language is installed
2. Verify file is in the correct directory
3. Make sure you have execution permissions
4. Review the code comments for usage details

---

**Happy Rolling! **
