def task_validate(task):
    errors = {}
    if not task.description:
        errors["description"] = "Описание обязательное поле"
    elif len(task.description) > 50:
        errors["description"] = "Длина поля не может быть больше чем 50"

    if not task.status:
        errors['status'] = "Статус обязатльное поле"
    elif len(task.status) > 50:
        errors["description"] = "Длина поля не может быть больше чем 50"

    if not task.date:
        errors['date'] = 'Дата обязательное поле'

    return errors