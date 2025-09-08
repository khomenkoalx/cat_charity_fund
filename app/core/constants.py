ERROR_PROJECT_EXISTS = 'Проект с таким именем уже существует!'
ERROR_PROJECT_NOT_FOUND = 'Проект не найден'
ERROR_PROJECT_CLOSED_EDIT = 'Закрытый проект нельзя редактировать!'
ERROR_PROJECT_SUM_LESS_INVESTED = (
    'Нельзя установить требуемую сумму меньше уже вложенной!'
)

ERROR_PROJECT_DELETE_FORBIDDEN = (
    'Нельзя удалять закрытый проект или проект, '
    'в который уже были инвестированы средства.'
)
ERROR_PROJECT_PATCH_FORBIDDEN_FIELDS = 'Запрещено изменять эти поля: '

ERROR_DONATION_SUM_LESS_ZERO = 'Сумма пожертвования должна быть больше 0.'

APP_NAME = 'Кошачий благотворительный фонд'
APP_DESCRIPTION = 'Сервис для поддержки котиков!'
APP_VERSION = '0.1.0'

FORBIDDEN_FIELDS = {
    'invested_amount',
    'create_date',
    'close_date',
    'fully_invested',
    'id',
}
ALLOWED_FIELDS = {'name', 'description', 'full_amount'}

JWT_LIFETIME_VALUE = 3600
MIN_PASSWORD_LENGTH = 3
