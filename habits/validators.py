from rest_framework.serializers import ValidationError


class DurationValidator:

    def __init__(self, field):
        self.field = field

    def __call__(self, value):
        duration = dict(value).get(self.field)
        duration = int(duration)
        if duration > 120:
            raise ValidationError(f'Продолжительность задачи не может быть больше 120 минут! {value}')


class AwardValidator:

    def __init__(self, is_pleasant, award, link_pleasant):
        self.award = award
        self.is_pleasant = is_pleasant
        self.link_pleasant = link_pleasant

    def __call__(self, value):
        award = dict(value).get(self.award)
        is_pleasant = dict(value).get(self.is_pleasant)
        link_pleasant = dict(value).get(self.link_pleasant)

        if not is_pleasant:
            if not award:
                if not link_pleasant:
                    raise ValidationError('По завершении задачи обязательно должно быть вознаграждение либо приятная '
                                          'привычка!')
            else:
                if link_pleasant:
                    raise ValidationError('Выберите либо вознаграждение, либо приятную привычку.')
        else:
            if award or link_pleasant:
                raise ValidationError('У приятной привычки не может быть вознаграждения.')
