import requests as r
import webbrowser

def loc_tower():
    URL = 'https://opencellid.org/ajax/searchCell.php'
    print('='*100)
    mcc = str(input("Enter MCC : "))
    mnc = str(input("Enter MNC : "))
    lac = str(input("Enter LAC : "))
    cid = str(input("Cell ID   : "))
    print('='*100)
    PARAMS = {'mcc':mcc, 'mnc':mnc, 'lac':lac, 'cell_id':cid}
    req = r.get(url=URL, params=PARAMS)
    res = req.json()
    if res==False:
        print("Couldn't find the tower")
    else:
        print(f"Longitude :\t{res['lon']}\nLatitude :\t{res['lat']}\nRange  :\t{res['range']} m")
        mapUrl = f"https://www.google.com/maps/place/{res['lat']}+{res['lon']}/@{res['lat']},{res['lon']},19z"
        print(mapUrl)
        webbrowser.open_new_tab(mapUrl)


if __name__ == '__main__' :
    loc_tower()
