from .ddc import DDC

import helpers


def get_clustering_module(cfg, input_size):
    return helpers.dict_selector({
        "DDC": DDC,
    }, "clustering module")(cfg.class_name)(cfg, input_size)
