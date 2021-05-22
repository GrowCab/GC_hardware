class ChamberSchedule:
    def __init__(self, chamber_schedule):
        self.chamber_schedule = chamber_schedule

    def  expected_measures(self):
        return self.chamber_schedule.get("expected_measure", [])

    def hardware_labels(self):
        ems = self.expected_measures()
        labels = map(lambda em: em['unit']['hardware_label'], ems) 
        return list(set(labels))

    def expected_measures_for(self, unit="temperature"):
        ems = self.expected_measures()
        ems = filter(lambda em: em['unit']['hardware_label'] == unit, ems)

        return list(ems)

    def expected_measure_for(self, hour=0, minute=0,  unit="temperature"):
        ems = self.expected_measures_for(unit=unit)
        for em in ems: 
            if (em['end_hour'], em['end_minute']) > (hour, minute): 
                return em
        return em