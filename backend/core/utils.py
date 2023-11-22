def calculate_merit_order(load, fuels, powerplants):
    ret = []
    generated_p = 0
    # First, we get the real cost of a MWh per powerplant
    for powerplant in powerplants:
        fuel_cost = {
            'windturbine': 0,
            'gasfired': fuels['gas(euro/MWh)'],
            'turbojet': fuels['kerosine(euro/MWh)']
        }.get(powerplant['type'])
        efficiency = powerplant['efficiency']
        
        powerplant['mwh_cost'] = fuel_cost / efficiency

    # Order by mwh_cost
    powerplants = sorted(powerplants, key=lambda x: x['mwh_cost'])

    # Iterate over plants to get how much p generates every of them
    for plant in powerplants:
        p_needed = load - generated_p
        if p_needed <= 0:
            ret.append({
                'name': plant['name'],
                'p': 0
            })
        else:
            p_from_plant = (
                plant['pmax']
                if plant['type'] != 'windturbine'
                else round(plant['pmax'] * (fuels['wind(%)'] / 100), 1)
            )
            p = min(p_from_plant, p_needed)
            p_min = plant['pmin']
            if p_min > p:
                p = p_min

            ret.append({
                'name': plant['name'],
                'p': p
            })
            generated_p += p

    return ret
