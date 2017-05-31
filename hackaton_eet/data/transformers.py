def align_data(feature_data, target_data):
    min_length = min(feature_data.shape[1], target_data.shape[1])
    return (
        feature_data[:, -min_length:],
        target_data[:, -min_length:]
    )
