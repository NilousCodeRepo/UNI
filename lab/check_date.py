def check_date(d: int, m:int, y:int ) -> bool:
    if d in range(1,31):
        return True
    if m in range(1,12):
        return True
    else:
        return False


day = input("inserire giorno: ")
month = input("inserire mese: ")
year = input("inserire anno: ")

check_date(day, month, year)
