def transform(legacy_data):
    transformed_storage = {}
    for key, value in legacy_data.items():
        for v in value:
            transformed_storage[v.lower()] = key

    transformed_storage = dict(sorted(transformed_storage.items()))
    return transformed_storage