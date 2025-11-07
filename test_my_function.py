import numpy as np
from signals import (
    generate_sine_wave,
    generate_sawtooth_wave,
    time_shift,
    time_scale,
    signal_addition,
    signal_multiplication
)


def test_generate_sine_wave():
    t, y = generate_sine_wave(1, 2, 0, 1, 100)
    assert len(t) == 100
    assert len(y) == 100
    assert np.isclose(max(y), 2, atol=0.1)  # amplitude check


def test_generate_sawtooth_wave():
    t, y = generate_sawtooth_wave(1, 1, 0, 1, 100)
    assert len(t) == 100
    assert len(y) == 100
    assert np.all(np.abs(y) <= 1.1)  # values should stay roughly within amplitude range


def test_time_shift():
    t = np.linspace(0, 1, 5)
    y = np.ones_like(t)
    t_shifted, y_shifted = time_shift(t, y, 0.5)
    assert np.allclose(t_shifted, t + 0.5)
    assert np.allclose(y_shifted, y)


def test_time_scale():
    t = np.linspace(0, 1, 5)
    y = np.ones_like(t)
    t_scaled, y_scaled = time_scale(t, y, 2)
    assert np.allclose(t_scaled, t * 2)
    assert np.allclose(y_scaled, y)


def test_signal_addition():
    y1 = np.array([1, 2, 3])
    y2 = np.array([4, 5, 6])
    y_sum = signal_addition(y1, y2)
    assert np.array_equal(y_sum, np.array([5, 7, 9]))


def test_signal_multiplication():
    y1 = np.array([1, 2, 3])
    y2 = np.array([4, 5, 6])
    y_product = signal_multiplication(y1, y2)
    assert np.array_equal(y_product, np.array([4, 10, 18]))