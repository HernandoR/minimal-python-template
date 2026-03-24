from __future__ import annotations

from collections import deque
import random
from typing import Optional

Grid = list[list[int]]


def in_bounds(x: int, y: int, n: int) -> bool:
    """Check whether a cell is inside an n x n grid."""
    return 0 <= x < n and 0 <= y < n


def neighbors4(x: int, y: int, n: int) -> list[tuple[int, int]]:
    """Return in-bounds 4-direction neighbors in fixed order: up/down/left/right."""
    candidates = ((x - 1, y), (x + 1, y), (x, y - 1), (x, y + 1))
    return [(nx, ny) for nx, ny in candidates if in_bounds(nx, ny, n)]


def is_reachable_start_to_goal(grid: Grid) -> bool:
    """Return True if there is a path from (0,0) to (n-1,n-1)."""
    n = len(grid)
    if n == 0 or any(len(row) != n for row in grid):
        return False

    if grid[0][0] != 0 or grid[n - 1][n - 1] != 0:
        return False

    queue: deque[tuple[int, int]] = deque([(0, 0)])
    visited = {(0, 0)}

    while queue:
        x, y = queue.popleft()
        if (x, y) == (n - 1, n - 1):
            return True

        for nx, ny in neighbors4(x, y, n):
            if (nx, ny) not in visited and grid[nx][ny] == 0:
                visited.add((nx, ny))
                queue.append((nx, ny))

    return False


def generate_maze(
    n: int,
    wall_prob: float = 0.25,
    seed: Optional[int] = None,
    max_retry: int = 200,
) -> Grid:
    """Generate a random solvable maze from top-left to bottom-right."""
    if n < 2:
        raise ValueError("n must be >= 2")
    if not (0.0 <= wall_prob < 1.0):
        raise ValueError("wall_prob must satisfy 0 <= wall_prob < 1")
    if max_retry < 1:
        raise ValueError("max_retry must be >= 1")

    rng = random.Random(seed)

    for _ in range(max_retry):
        grid: Grid = [
            [1 if rng.random() < wall_prob else 0 for _ in range(n)] for _ in range(n)
        ]

        # Always keep start and goal open.
        grid[0][0] = 0
        grid[n - 1][n - 1] = 0

        if is_reachable_start_to_goal(grid):
            return grid

    raise ValueError(
        "Failed to generate a solvable maze within max_retry attempts. "
        "Try lowering wall_prob or increasing max_retry."
    )
