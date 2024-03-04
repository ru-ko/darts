"""
Difference Scorer
-----------------

This scorer simply computes the elementwise difference
between two series. If the two series are multivariate, it
returns a multivariate series.
"""

from darts.ad.scorers.scorers import AnomalyScorer
from darts.timeseries import TimeSeries


class DifferenceScorer(AnomalyScorer):
    def __init__(self) -> None:
        super().__init__(
            univariate_scorer=False,
            window=1,
            fittable=False,
            single_series_support=False,
            probabilistic_support=False,
            window_agg=False,
        )

    def __str__(self):
        return "Difference"

    def _score_core_from_prediction(
        self,
        actual_series: TimeSeries,
        pred_series: TimeSeries,
    ) -> TimeSeries:
        return actual_series - pred_series
