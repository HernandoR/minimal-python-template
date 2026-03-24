# Maze Policy Learning Plan (Overview)

## Goal

Train a simple neural network policy:

- Input: maze grid (N x N) + current position (x, y)
- Output: next move direction (4-way)

Confirmed specs:

- Search algorithm: Dijkstra
- Grid encoding: 0 = free, 1 = wall
- Moves: Up, Down, Left, Right
- Tie-break for multiple shortest paths: Right > Down > Left > Up
- Baseline model: MLP

## Deliverables

1. Maze generation module (always solvable from (0,0) to (N-1,N-1))
2. Dijkstra next-step solver from any valid position
3. Dataset/label builder from solver
4. Customizable training loop (default MLP)
5. Tests + quality checks

## Suggested Package Layout

- src/ml_maze/maze_generator.py
- src/ml_maze/solver_dijkstra.py
- src/ml_maze/dataset_builder.py
- src/ml_maze/models/mlp_policy.py
- src/ml_maze/train_loop.py
- scripts/train_policy.py
- tests/test_maze_generator.py
- tests/test_solver_dijkstra.py
- tests/test_dataset_builder.py
- tests/test_train_loop_smoke.py

## Action Encoding

- 0: UP (-1, 0)
- 1: DOWN ( 1, 0)
- 2: LEFT ( 0,-1)
- 3: RIGHT ( 0, 1)

## Data Contract

Single sample fields:

- maze: int array, shape [N, N], values in {0,1}
- pos: int array, shape [2], value [x, y]
- label: int in [0..3]
- meta (optional): seed, episode_id, step_idx, dist_to_goal

## Execution Order

1. Implement generator + tests
2. Implement Dijkstra next-step + tests
3. Implement dataset builder + tests
4. Implement model + train loop + smoke test
5. Run check and test gates

## Commands

- Install: `uv sync`
- Lint: `just lint`
- Format check: `just format`
- Type check: `just type-check`
- Test: `just test`
