MIN_DRIVING_AGE = 18


def allowed_driving(name, age):
    """Print '{name} is allowed to drive' or '{name} is not allowed to drive'
       checking the passed in age against the MIN_DRIVING_AGE constant"""
    status = ""
    if age >= 18:
        status = name + " is allowed to drive"
    else:
        status = name + " is not allowed to drive"
    return(print(status))
