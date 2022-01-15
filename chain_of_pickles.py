class Pickle:

    def __init__(self, *seeds, callback=None, err_callback=None):
        self._seeds = seeds
        self._callback = callback
        self._err_callback = err_callback

    def __call__(self, data):
        _data = data
        for seed in self._seeds:
            try:
                _data = seed(_data)
            except Exception as e:
                (self._err_callback or (lambda e: None))(e)
                raise e

        (self._callback or (lambda: None))()
        return _data


def action_1(data):
    data['action_1'] = True
    return data


def action_2(data):
    data['action_2'] = True
    return data


class CallableAction:
    def __call__(self, data):
        data['callable_action_class'] = True
        return data


class MethodAction:
    def run(self, data):
        data['method_action_class'] = True
        return data


lambda_action = lambda data: (data.update({'lambda': True}), data)[1]


pic1 = Pickle(action_1, callback=lambda: print('ACTION 1 OKAY'))
pic2 = Pickle(action_2)
pic3 = Pickle(pic2, pic1)
pic4 = Pickle(CallableAction())
pic5 = Pickle(MethodAction().run)

data = {'run': True}
pickle_jar = Pickle(
    pic3,
    pic4,
    pic5,
    lambda_action,
    callback=lambda: print('Pickledone!')
)
pickle_jar(data, )

assert (
    data == 
    {
        'run': True, 
        'action_2': True, 
        'action_1': True, 
        'callable_action_class': True, 
        'method_action_class': True,
        'lambda': True
    }
)
