# Phase 3: Dataset and Labeling Spec

## Objective

Build supervised samples using the maze generator + Dijkstra policy.

## Sample Schema

```text
maze: [N, N] int (0 free / 1 wall)
pos: [2] int (x, y)
label: int (0..3)
meta:
  seed: int
  maze_id: int
  step_idx: int
  dist_to_goal: int
```

## Data Building Strategy

1. Generate solvable maze.
2. Pick valid source positions:

- Option A: all free cells that can reach goal
- Option B: only cells on one sampled shortest path

3. For each position, call `next_step_by_dijkstra` to get label.
4. Skip positions where solver returns `None`.
5. Append sample to dataset.

## Splitting

- Train/Val/Test = 80/10/10 (or 70/15/15)
- Split by `maze_id` to avoid leakage

## Class Distribution

- Track action counts for 4 classes
- Report imbalance ratio
- Optional: compute class weights for loss

## API Draft

```python
def build_dataset(
    num_mazes: int,
    n: int,
    wall_prob: float,
    seed: int | None = None,
) -> list[dict]:
    ...
```

## Validation Checks

- Every sample has valid shape/types
- `label` is within [0..3]
- `pos` is free in corresponding maze
- Reproducible when seed is fixed

## Tests

- Non-empty dataset for normal configs
- Stable sample count for fixed seed/config
- No invalid labels
- No leakage across splits (maze_id disjoint)
