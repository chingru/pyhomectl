from .. import BaseDriver, FeatureNotAvailableError

class TVDriver(BaseDriver):
        '''
        Base class for TVs.
        '''
        def power(on=True):
                raise FeatureNotAvailableError('power')

        def mute(on=True):
                raise FeatureNotAvailableError('mute')
