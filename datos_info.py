from datetime import datetime
class datos_info:
    def __init__(self, report_name:str, report_date: float=0) -> None:
        self.num_jugadores = 0
        self.report_name = report_name
        self.report_date = datetime.fromtimestamp(report_date)
        self.total_power =0
        self.average_power = 0
        self.total_kp = 0
        self.average_kp=0 
        self.total_t4kills = 0
        self.average_t4kills = 0
        self.total_t5kills = 0
        self.average_t5kills = 0


    def add_data(self, raw_data:datos_reporte)->None:
        self.num_jugadores +=1
        self.total_power += raw_data.power
        self.total_kp += raw_data.kp
        self.total_t4kills += raw_data.t4kills
        self.total_t5kills += raw_data.t5kills

        if (self.num_jugadores ==1): self.report_date = datetime.fromtimestamp(raw_data.timestamp)

    def get_data(self)->list:
        
        self.average_kp = round (self.total_kp / self.num_jugadores,2)
        self.average_power = round (self.total_power / self.num_jugadores,2)
        self.average_t4kills = round (self.total_t4kills / self.num_jugadores,2)
        self.average_t5kills = round (self.total_t5kills / self.num_jugadores,2)
        
        datos = list ([
            self.report_name,
            self.report_date,
            self.num_jugadores,
            self.total_power,
            self.average_power,
            self.total_kp,
            self.average_kp,
            self.total_t4kills,
            self.average_t4kills,
            self.total_t5kills,
            self.average_t5kills
        ])
        return datos

    def get_header(self) ->list:
        info_header = list([
            'REPORT NAME',
            'REPORT DATE',
            'PLAYERS',
            'TOP300 TOTAL POWER',
            'TOP300 AVERAGE POWER',
            'TOP300 TOTAL KP',
            'TOP300 AVERAGE KP',
            'TOP300 TOTAL T4KILLS',
            'TOP300 AVERAGE T4KILLS',
            'TOP300 TOTAL T5KILLS',
            'TOP300 AVERAGE T5KILLS'
        ])

        return info_header

