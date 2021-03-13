import abc


class ErrorValidator(metaclass=abc.ABCMeta):

    @abc.abstractmethod
    def validate(self, ae, cm, ae_df, cm_df):
        raise NotImplementedError
