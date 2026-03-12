from typing import List, Tuple, Optional

class Position:
    """Simple placeholder for a grid coordinate."""
    x: int
    y: int

    def __init__(self, x: int, y: int) -> None:
        self.x = x
        self.y = y


class GameController:
    def initializeGame(self) -> None:
        """Create initial game objects (no implementation)."""
        pass

    def spawnSnake(self) -> None:
        """Create the Snake object (no implementation)."""
        pass

    def spawnFood(self) -> None:
        """Create the Food object (no implementation)."""
        pass

    def startLoop(self) -> None:
        """Begin the game loop (no implementation)."""
        pass


class Snake:
    headPosition: Position
    direction: Tuple[int, int]

    def __init__(self) -> None:
        """Initialize Snake fields (no implementation)."""
        pass

    def move(self) -> None:
        """Advance the snake (no implementation)."""
        pass

    def grow(self) -> None:
        """Increase the snake size (no implementation)."""
        pass


class Tail:
    segments: List[Position]

    def __init__(self) -> None:
        """Initialize Tail fields (no implementation)."""
        pass

    def length(self) -> int:
        """Return the number of tail segments (no implementation)."""
        pass

    def append(self, segment: Position) -> None:
        """Append a segment (no implementation)."""
        pass

    def popLast(self) -> Optional[Position]:
        """Remove and return last segment (no implementation)."""
        pass


class Food:
    position: Position

    def __init__(self) -> None:
        """Initialize Food fields (no implementation)."""
        pass

    def respawn(self) -> None:
        """Reposition food (no implementation)."""
        pass


class Board:
    width: int
    height: int

    def __init__(self) -> None:
        """Initialize Board fields (no implementation)."""
        pass

    def isInsideBounds(self) -> bool:
        """Check if a position is inside the board (no implementation)."""
        pass

    def randomEmptyCell(self) -> Position:
        """Return a random empty cell (no implementation)."""
        pass


# demo_verify_instantiation_and_calls.py
# Assumes your class stubs are defined above or imported.

def main():
    # Instantiate objects (proves objects can be created)
    game = GameController()
    snake = Snake()
    tail = Tail()
    food = Food()
    board = Board()
    pos = Position(3, 4)

    # Method calls (proves methods execute)
    game.initializeGame()
    game.spawnSnake()
    game.spawnFood()
    game.startLoop()

    snake.move()
    snake.grow()

    # Tail method calls
    _ = tail.length()
    tail.append(pos)
    _ = tail.popLast()

    # Food + Board method calls
    food.respawn()
    _ = board.isInsideBounds()
    _ = board.randomEmptyCell()

    print("✅ Classes exist, objects can be instantiated, and methods execute (no game logic).")

if __name__ == "__main__":
    main()