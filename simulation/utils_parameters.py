__all__ = [
    'compute_r_parameter',
    'compute_a_parameter',
    'compute_r0_parameter',
    'compute_q_parameter'
]


def compute_r_parameter(ago_susceptible: int, current_susceptible: int, current_infected: int) -> float:
    """
    Function for compute infection ratio parameter based od SIR model.

    Parameters
    ----------
    ago_susceptible: int, required
        Amount of susceptible people one interval before current iteration.
    current_susceptible: int, required
        Amount of susceptible people in current interval.
    current_infected: int, required
        Amount of infected people in current interval.

    Returns
    -------
    Returns value of infection ratio.

    Example
    -------
    >>> compute_r_parameter(10, 9, 1)
    """

    d_susceptible = current_susceptible - ago_susceptible

    return -d_susceptible * (1 / (current_susceptible * current_infected))


def compute_a_parameter(ago_removed: int, current_removed: int, current_infected: int) -> float:
    """
    Function for compute recover rate value based od SIR model.

    Parameters
    ----------
    ago_removed: int, required
        Amount of recovered and dead people one interval before current iteration.
    current_removed: int, required
        Amount of recovered and dead people in current interval.
    current_infected: int, required
        Amount of infected people in current interval.

    Returns
    -------
    Returns value of recover rate parameter.

    Example
    -------
    >>> compute_a_parameter(0, 2, 10)
    """

    d_removed = current_removed - ago_removed

    return d_removed * (1 / (current_removed * current_infected))


def compute_r0_parameter(r_parameter: float, a_parameter: float, start_susceptible_amount: int) -> float:
    return r_parameter * start_susceptible_amount / a_parameter


def compute_q_parameter(r_parameter: float, a_parameter: float) -> float:
    return r_parameter / a_parameter
