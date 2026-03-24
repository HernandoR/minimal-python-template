# Phase 2: Dijkstra Next-Step Solver

## Objective

Given a maze and a current position `(x,y)`, return the next action that moves toward goal `(N-1,N-1)` on a shortest path.

## API Draft

```python
def next_step_by_dijkstra(
    grid: list[list[int]],
    pos: tuple[int, int],
    tie_break: tuple[int, ...] = (3, 1, 2, 0),
) -> tuple[int, tuple[int, int]] | None:
    ...
```

Notes:

- Default `tie_break=(3,1,2,0)` means Right > Down > Left > Up
- Return `None` if no path from `pos` to goal

## Preconditions

- `grid` must be square and use 0/1 encoding
- `pos` must be in bounds and on a free cell
- Goal must be free

## Algorithm Steps

1. If `pos == goal`, define policy behavior:

- Option A: return `None`
- Option B: return a special action code
  (Choose one and keep consistent in training data builder)

2. Run Dijkstra from `pos`:

- Node: cell `(x,y)`
- Edge weight: 1 for each valid move

3. Build shortest-path predecessor map.

4. Extract candidate first actions from `pos` that can lead to shortest distance.

5. Apply tie-break priority to select deterministic action.

6. Return `(action_id, next_pos)`.

## Why Dijkstra Here

- Uniform cost means BFS is enough, but Dijkstra keeps the interface extensible if weighted cells are added later.

## Unit Tests

- Simple open grid returns expected action
- Multi-shortest-path case follows tie-break
- Blocked position returns `None`
- `pos == goal` follows the chosen contract
- Invalid input raises clear errors

## Complexity

- O(V log V + E log V), here V ~ N^2 and E ~ 4N^2
