# Phase 4: Customizable Training Loop

## Objective

Train a policy model with pluggable architecture.

## Baseline Model (MLP)

Input features:

- Flattened maze: `N*N`
- Position encoding: `x`, `y` (or normalized x/N, y/N)

Total input dim = `N*N + 2`
Output dim = 4 action logits

## Model Contract

```python
class PolicyModel(nn.Module):
    def forward(self, maze_tensor, pos_tensor):
        """Return logits with shape [B, 4]."""
```

## Train Loop Steps

1. Build DataLoader for train/val.
2. Instantiate model (default MLP, support custom model factory).
3. Loss: `CrossEntropyLoss`.
4. Optimizer: `Adam`.
5. Epoch loop:

- forward
- loss backward
- optimizer step
- log train loss/acc
- run val evaluation

6. Save best checkpoint by val accuracy.

## API Draft

```python
def train_policy(
    train_ds,
    val_ds,
    model_factory=None,
    epochs: int = 20,
    batch_size: int = 64,
    lr: float = 1e-3,
    seed: int = 42,
    device: str = "cpu",
):
    ...
```

## Script Entry

Create script:

- `scripts/train_policy.py`
- Parse args: `--n --num-mazes --epochs --batch-size --lr --seed --device`
- Print final metrics and checkpoint path

## Smoke Validation Target

- 1-2 epochs on small data should run without errors
- Accuracy should beat random baseline (random = 25%) on easy config

## Optional Extensions

- Weighted CE loss for class imbalance
- Early stopping
- Learning rate scheduler
