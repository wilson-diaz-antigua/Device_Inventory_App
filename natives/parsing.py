from datetime import date 
def Data(output):
    deviceInfo = []

    for name, info in output['Output'].items():
        if name != 'Errors':
            device = {
                'Hospital': '',
                'Device': '',
                'SN': info['serialNumber'],
                'MAC': info['wifiAddress'],
                'DateAdded': date.today()
            }
    # if theres a delimeter split name and assign to its corresponding key else assign the devic key to none
            if ' ' in info['name']:
                device['Hospital'], device['Device'] = info['name'].split(
                    " ", 1)
            else:
                device['Hospital'] = info['name']
                device['Device'] = None
            deviceInfo.append(device)
    return deviceInfo
