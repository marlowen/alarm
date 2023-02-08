from datetime import datetime


def dia(D, L, M, Mi, J, V, S):
    hoy = datetime.today().strftime("%A")
    Sunday = D
    Monday = L
    Tuesday = M
    Wendsday = Mi
    Thursday = J
    Friday = V
    Saturday = S
    if Sunday == 1:
        if hoy == "Sunday":
            return True
        else:
            return False
    elif Monday == 1:
        if hoy == "Monday":
            return True
        else:
            return False
    elif Tuesday == 1:
        if hoy == "Tuesday":
            return True
        else:
            return False
    elif Wendsday == 1:
        if hoy == "Wednesday":
            return True
        else:
            return False
    elif Thursday == 1:
        if hoy == "Thursday":
            return True
        else:
            return False
    elif Friday == 1:
        if hoy == "Friday":
            return True
        else:
            return False
    elif Saturday == 1:
        if hoy == "Saturday":
            return True
        else:
            return False