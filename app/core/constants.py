# CharityProject
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

# Donation
ERROR_DONATION_SUM_LESS_ZERO = 'Сумма пожертвования должна быть больше 0.'

# Общие поля
APP_NAME = 'Кошачий благотворительный фонд'
APP_DESCRIPTION = 'Сервис для поддержки котиков!'
APP_VERSION = '0.1.0'
FIELD_NAME = 'name'
FIELD_DESCRIPTION = 'description'
FIELD_FULL_AMOUNT = 'full_amount'
FIELD_INVESTED_AMOUNT = 'invested_amount'
FIELD_CREATE_DATE = 'create_date'
FIELD_CLOSE_DATE = 'close_date'
FIELD_FULLY_INVESTED = 'fully_invested'
FIELD_ID = 'id'
FIELD_USER_ID = 'user_id'
FIELD_COMMENT = 'comment'

# Списки разрешённых/запрещённых полей
FORBIDDEN_FIELDS = {
    FIELD_INVESTED_AMOUNT,
    FIELD_CREATE_DATE,
    FIELD_CLOSE_DATE,
    FIELD_FULLY_INVESTED,
    FIELD_ID
}
ALLOWED_FIELDS = {FIELD_NAME, FIELD_DESCRIPTION, FIELD_FULL_AMOUNT}