# Target Mean Encoding Function
def target_mean_encoding(data, col, target):
    """
    Encodes a categorical column using target mean encoding.
    """
    mean_encoded = data.groupby(col)[target].mean()
    return data[col].map(mean_encoded)
