import sys
from pathlib import Path

LESSON_DIR = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(LESSON_DIR))
sys.modules.pop("workbench", None)

from workbench import (
    LinearModel,
    gradient_step,
    inference_trace,
    mean_squared_error,
    predict,
    recommend_adaptation,
    train_one_epoch,
)


def test_predict_uses_weight_and_bias():
    assert predict(LinearModel(2.0, 1.0), 3.0) == 7.0


def test_mean_squared_error_averages_squared_differences():
    assert mean_squared_error([2.0, 4.0], [1.0, 6.0]) == 2.5


def test_gradient_step_returns_new_model_that_reduces_simple_error():
    model = LinearModel(0.0, 0.0)
    updated = gradient_step(model, x=1.0, target=2.0, learning_rate=0.1)

    assert updated != model
    assert predict(updated, 1.0) > predict(model, 1.0)


def test_train_one_epoch_updates_parameters_in_order():
    trained = train_one_epoch(LinearModel(0.0, 0.0), [(1.0, 2.0), (2.0, 4.0)], 0.1)

    assert trained.weight > 0
    assert trained.bias > 0


def test_inference_trace_does_not_mutate_model():
    model = LinearModel(1.5, 0.5)
    trace = inference_trace(model, 2.0)

    assert trace["prediction"] == 3.5
    assert model == LinearModel(1.5, 0.5)


def test_recommend_adaptation_avoids_fine_tuning_as_first_fix():
    decision = recommend_adaptation("bad math", has_examples=False, failure_mode="calculation")

    assert decision["first_choice"] == "tool"
    assert "reason" in decision
