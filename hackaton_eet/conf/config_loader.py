import importlib


def init_cls_from_settings(settings_dict):
    res = {}
    for name, settings in settings_dict.items():
        try:
            driver = settings['driver']
            mod, _, classname = driver.rpartition('.')
            module = importlib.import_module(mod)
            res[name] = (settings, getattr(module, classname))
        except:
            pass
    return res
