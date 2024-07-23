def task_validate(task):
    errors = {}
    if not task.description:
        errors["description"] = "Название обязательное поле"
    elif len(task.description) > 3:
        errors["description"] = "Длина поля не может быть больше чем 50"

    if not task.status:
        errors["status"] = "Контент обязательное поле"

    if not task.date:
        errors["date"] = "Автор обязательное поле"

    return errors