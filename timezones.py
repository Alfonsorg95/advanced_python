from datetime import datetime
import pytz

def run():
    caracas_timezone = pytz.timezone("America/Caracas")
    caracas_date = datetime.now(caracas_timezone)
    print("Caracas: ", caracas_date.strftime("%d/%m/%y, %H:%M"))


if __name__=='__main__':
    run()