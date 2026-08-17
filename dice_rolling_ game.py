import random
from typing import Tuple, List, Dict
from datetime import datetime


class DiceRoller:
    """A complete dice roller simulator with statistics tracking."""

    def __init__(self):
        """Initialize the dice roller with default values."""
        self.roll_history: List[Tuple[int, int]] = []
        self.total_rolls: int = 0
        self.start_time: datetime = datetime.now()

    def roll_dice(self) -> Tuple[int, int]:
        """
        Simulate rolling two dice.
        
        Returns:
            Tuple[int, int]: Two random integers between 1 and 6
        """
        die1 = random.randint(1, 6)
        die2 = random.randint(1, 6)
        self.roll_history.append((die1, die2))
        self.total_rolls += 1
        return die1, die2

    def display_results(self, die1: int, die2: int) -> None:
        """
        Display the dice roll results in a formatted way.
        
        Args:
            die1 (int): Result of the first die
            die2 (int): Result of the second die
        """
        total = die1 + die2
        print("\n" + "=" * 50)
        print(f"   Die 1: {die1}  |  Die 2: {die2}")
        print(f"  Total: {total}")
        print("=" * 50)

    def get_statistics(self) -> Dict[str, any]:
        """
        Calculate statistics from roll history.
        
        Returns:
            Dict: Dictionary containing various statistics
        """
        if not self.roll_history:
            return {}

        all_rolls = [die1 + die2 for die1, die2 in self.roll_history]
        
        stats = {
            'total_rolls': self.total_rolls,
            'highest_roll': max(all_rolls),
            'lowest_roll': min(all_rolls),
            'average_roll': round(sum(all_rolls) / len(all_rolls), 2),
            'most_common': max(set(all_rolls), key=all_rolls.count),
            'sevens': sum(1 for roll in all_rolls if roll == 7),
            'doubles': sum(1 for d1, d2 in self.roll_history if d1 == d2),
        }
        return stats

    def display_statistics(self) -> None:
        """Display the roll statistics."""
        if self.total_rolls == 0:
            print("\n No rolls yet! Play some rolls first.\n")
            return

        stats = self.get_statistics()
        
        print("\n" + "=" * 50)
        print("               STATISTICS")
        print("=" * 50)
        print(f"  Total Rolls:       {stats['total_rolls']}")
        print(f"  Highest Roll:      {stats['highest_roll']}")
        print(f"  Lowest Roll:       {stats['lowest_roll']}")
        print(f"  Average Roll:      {stats['average_roll']}")
        print(f"  Most Common Roll:  {stats['most_common']}")
        print(f"  Number of Sevens:  {stats['sevens']}")
        print(f"  Number of Doubles: {stats['doubles']}")
        print("=" * 50 + "\n")

    def display_roll_history(self) -> None:
        """Display the complete roll history."""
        if not self.roll_history:
            print("\n No rolls yet!\n")
            return

        print("\n" + "=" * 50)
        print("              📋 ROLL HISTORY")
        print("=" * 50)
        
        for idx, (die1, die2) in enumerate(self.roll_history, 1):
            total = die1 + die2
            doubles = "✓ DOUBLES" if die1 == die2 else ""
            print(f"  Roll {idx:3d}: {die1} + {die2} = {total}  {doubles}")
            
            # Show 10 rolls per screen
            if idx % 10 == 0 and idx < len(self.roll_history):
                input("  Press Enter to see more rolls...")
        
        print("=" * 50 + "\n")

    def play_game_mode(self) -> None:
        """Play the Craps game mode (simple version)."""
        print("\n" + "=" * 50)
        print("               CRAPS GAME MODE")
        print("=" * 50)
        print("  Roll the dice!")
        print("  - First roll: 7 or 11 = WIN, 2, 3, or 12 = LOSE")
        print("  - Other numbers = establish point")
        print("=" * 50 + "\n")

        input("Press Enter to roll the dice...")
        die1, die2 = self.roll_dice()
        self.display_results(die1, die2)
        total = die1 + die2

        if total in (7, 11):
            print("   NATURAL! YOU WIN!\n")
        elif total in (2, 3, 12):
            print("   CRAPS! YOU LOSE!\n")
        else:
            print(f"  Point established: {total}")
            point = total

            while True:
                input("\nPress Enter to roll again...")
                die1, die2 = self.roll_dice()
                self.display_results(die1, die2)
                total = die1 + die2

                if total == point:
                    print("    MADE THE POINT! YOU WIN!\n")
                    break
                elif total == 7:
                    print("   SEVEN OUT! YOU LOSE!\n")
                    break
                else:
                    print(f"  Rolling again... (Point: {point})\n")

    def display_menu(self) -> str:
        """
        Display the main menu and get user choice.
        
        Returns:
            str: User's menu choice
        """
        print("\n" + "=" * 50)
        print("               DICE ROLLER MENU")
        print("=" * 50)
        print("  1. Roll the Dice")
        print("  2. View Statistics")
        print("  3. View Roll History")
        print("  4. Play Craps Game")
        print("  5. Reset Statistics")
        print("  6. Exit")
        print("=" * 50)
        
        while True:
            choice = input("\nSelect an option (1-6): ").strip()
            if choice in ('1', '2', '3', '4', '5', '6'):
                return choice
            print(" Invalid choice. Please enter 1-6.")

    def reset_statistics(self) -> None:
        """Reset all statistics."""
        confirm = input("\n  Are you sure? This will clear all roll history. (yes/no): ").strip().lower()
        if confirm in ('yes', 'y'):
            self.roll_history.clear()
            self.total_rolls = 0
            print(" Statistics cleared!\n")
        else:
            print(" Reset cancelled.\n")

    def run(self) -> None:
        """Run the main dice roller program."""
        print("\n" + "=" * 50)
        print("    WELCOME TO THE COMPLETE DICE ROLLER! ")
        print("=" * 50)
        print("  Roll dice, track statistics, and play games!")
        print("=" * 50)

        while True:
            choice = self.display_menu()

            if choice == '1':
                input("\nPress Enter to roll the dice...")
                die1, die2 = self.roll_dice()
                self.display_results(die1, die2)

            elif choice == '2':
                self.display_statistics()

            elif choice == '3':
                self.display_roll_history()

            elif choice == '4':
                self.play_game_mode()

            elif choice == '5':
                self.reset_statistics()

            elif choice == '6':
                print("\n" + "=" * 50)
                print("  Thanks for using Dice Roller! Goodbye! ")
                print("=" * 50 + "\n")
                break


def main():
    """Main entry point of the program."""
    roller = DiceRoller()
    roller.run()


if __name__ == "__main__":
    main() 