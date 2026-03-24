from __future__ import annotations

import pytest

from ml_maze.maze_generator import generate_maze, is_reachable_start_to_goal


def test_generate_maze_basic_properties() -> None:
    n = 10
    grid = generate_maze(n=n, wall_prob=0.30, seed=42)

    assert len(grid) == n
    assert all(len(row) == n for row in grid)
    assert all(cell in {0, 1} for row in grid for cell in row)


def test_start_and_goal_are_free_and_reachable() -> None:
    n = 12
    grid = generate_maze(n=n, wall_prob=0.35, seed=7)

    assert grid[0][0] == 0
    assert grid[n - 1][n - 1] == 0
    assert is_reachable_start_to_goal(grid) is True


def test_same_seed_is_deterministic() -> None:
    grid_a = generate_maze(n=10, wall_prob=0.30, seed=123)
    grid_b = generate_maze(n=10, wall_prob=0.30, seed=123)

    assert grid_a == grid_b


def test_different_seeds_usually_generate_different_mazes() -> None:
    grid_a = generate_maze(n=12, wall_prob=0.35, seed=1)
    grid_b = generate_maze(n=12, wall_prob=0.35, seed=2)

    assert grid_a != grid_b


@pytest.mark.parametrize(
    ("n", "wall_prob", "max_retry"),
    [
        (1, 0.25, 50),
        (8, -0.1, 50),
        (8, 1.0, 50),
        (8, 0.25, 0),
    ],
)
def test_generate_maze_invalid_args(n: int, wall_prob: float, max_retry: int) -> None:
    with pytest.raises(ValueError):
        generate_maze(n=n, wall_prob=wall_prob, max_retry=max_retry)
