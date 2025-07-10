from app.schemas import CharityProjectUpdate
from fastapi import HTTPException, status


def validate_charity_project_name(name: str):
    if not (1 <= len(name) <= 100):
        raise HTTPException(
            status_code=status.HTTP_422_UNPROCESSABLE_ENTITY,
            detail='Название проекта должно быть от 1 до 100 символов.'
        )


def validate_charity_project_description(description: str):
    if len(description.strip()) < 1:
        raise HTTPException(
            status_code=status.HTTP_422_UNPROCESSABLE_ENTITY,
            detail='Описание проекта не может быть пустым.'
        )


def validate_charity_project_full_amount(full_amount: int):
    if full_amount <= 0:
        raise HTTPException(
            status_code=status.HTTP_422_UNPROCESSABLE_ENTITY,
            detail='Требуемая сумма должна быть больше 0.'
        )


def validate_update_full_amount(new_full_amount: int, invested_amount: int):
    if new_full_amount < invested_amount:
        raise HTTPException(
            status_code=status.HTTP_422_UNPROCESSABLE_ENTITY,
            detail='Новая сумма проекта не может быть меньше уже внесённой суммы.'
        )


def validate_donation_full_amount(full_amount: int):
    if full_amount <= 0:
        raise HTTPException(
            status_code=status.HTTP_422_UNPROCESSABLE_ENTITY,
            detail='Сумма пожертвования должна быть больше 0.'
        )
