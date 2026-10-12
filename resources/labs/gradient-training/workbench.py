"""Training versus inference workbench for Module 2 Phase 6."""

from __future__ import annotations

from dataclasses import dataclass


@dataclass(frozen=True)
class LinearModel:
    weight: float
    bias: float


def predict(model: LinearModel, x: float) -> float:
    """Return a linear prediction."""
    # TODO: Return weight * x + bias.
    return 0.0


def mean_squared_error(predictions: list[float], targets: list[float]) -> float:
    """Return mean squared error."""
    # TODO: Validate aligned non-empty lists and average squared differences.
    return 0.0


def gradient_step(model: LinearModel, x: float, target: float, learning_rate: float) -> LinearModel:
    """Return updated parameters for one training example."""
    # TODO: Compute gradients for squared error and return a new model.
    return model


def train_one_epoch(
    model: LinearModel, examples: list[tuple[float, float]], learning_rate: float
) -> LinearModel:
    """Run one deterministic epoch over examples."""
    # TODO: Apply gradient_step in order.
    return model


def inference_trace(model: LinearModel, x: float) -> dict[str, float]:
    """Return prediction details without changing model parameters."""
    # TODO: Include input, weight, bias, and prediction.
    return {}


def recommend_adaptation(problem: str, has_examples: bool, failure_mode: str) -> dict[str, str]:
    """Recommend prompt, RAG, tool, or fine-tuning as a first adaptation."""
    # TODO: Prefer tools for calculation, RAG for missing knowledge,
    # prompt/schema for formatting, and fine-tuning only with examples.
    return {}
