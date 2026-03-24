# Phase 5: Validation and Runbook

## Quality Gates

Run in this order:

1. `uv sync`
2. `just lint`
3. `just format`
4. `just type-check`
5. `just test`

## End-to-End Checklist

- Maze generation returns solvable grids
- Dijkstra solver returns deterministic next step
- Dataset labels are consistent with solver
- Training script finishes and saves checkpoint
- Metrics/logs are produced

## Minimal Execution Example

```bash
uv run python scripts/train_policy.py \
  --n 8 \
  --num-mazes 200 \
  --epochs 2 \
  --batch-size 64 \
  --lr 1e-3 \
  --seed 42
```

## Debug Playbook

1. If dataset is empty:

- decrease `wall_prob`
- increase `max_retry`
- verify reachability checker

2. If labels look wrong:

- validate tie-break priority order
- check action-id mapping consistency everywhere

3. If training does not learn:

- verify feature construction (`maze + pos`)
- inspect class imbalance and loss setup
- reduce task difficulty (smaller N, lower wall density)

## Definition of Done

- All tests pass
- Quality gates pass
- End-to-end run completes
- docs/aigc content is aligned with implementation
