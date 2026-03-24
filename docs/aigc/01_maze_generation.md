# Phase 1: Maze Generation Module

## Objective

Generate random but solvable mazes:

- Start: (0,0)
- Goal: (N-1,N-1)
- Must have at least one valid path from start to goal

## API Draft

```python
def generate_maze(
    n: int,
    wall_prob: float = 0.25,
    seed: int | None = None,
    max_retry: int = 200,
) -> list[list[int]]:
    ...
```

## Implementation Steps

1. Validate inputs:

- `n >= 2`
- `0 <= wall_prob < 1`
- `max_retry >= 1`

2. For each retry:

- Use RNG with `seed`
- Sample each cell as wall with probability `wall_prob`
- Force `grid[0][0] = 0` and `grid[n-1][n-1] = 0`
- Check reachability from start to goal with BFS/DFS
- If reachable, return grid

3. If all retries fail:

- Raise `ValueError` with clear message

## Helper Functions

- `in_bounds(x, y, n) -> bool`
- `neighbors4(x, y, n) -> list[tuple[int, int]]`
- `is_reachable_start_to_goal(grid) -> bool`

## Edge Cases

- `n = 2`
- Very high `wall_prob` causing frequent retries
- Same seed should produce deterministic behavior

## Unit Tests

- Shape is [N, N]
- Cell values only in {0,1}
- Start and goal are free
- `is_reachable_start_to_goal(grid)` is True
- Different seeds generate different mazes (statistical check)
- Invalid args raise `ValueError`

## Complexity

- Generation: O(max_retry \* N^2)
- Reachability check per retry: O(N^2)
