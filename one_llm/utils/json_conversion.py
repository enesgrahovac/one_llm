def _convert_to_serializable(obj):
    """
    Convert custom objects to a JSON serializable format.
    """
    if isinstance(obj, dict):
        return {k: _convert_to_serializable(v) for k, v in obj.items()}
    elif isinstance(obj, list):
        return [_convert_to_serializable(i) for i in obj]
    elif hasattr(obj, '__dict__'):
        return {k: _convert_to_serializable(v) for k, v in obj.__dict__.items()}
    else:
        return obj