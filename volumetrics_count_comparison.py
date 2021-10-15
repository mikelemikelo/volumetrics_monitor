import modelop.monitors.volumetrics as volumetrics
import modelop.utils as utils

logger = utils.configure_logger()


# modelop.metrics
def metrics(df_1, df_2):
    # Initialize Volumetric monitor with 1st input DataFrame
    volumetric_monitor = volumetrics.VolumetricMonitor(df_1)

    count_comparison = volumetric_monitor.count_comparison(df_2)

    result = {
        # Boolean top-level metric
        "record_count_difference": count_comparison["values"][
            "record_count_difference"
        ],
        # Complete test results
        "volumetrics": [count_comparison],
    }
    yield result
