def get_temp (tabcsv, hour):
    for entry in tabcsv:
        if entry.get("time")[-5:-2] == hour[-5:-2]:
            return float(entry.get("temperature"))
    return None

class FilterModule(object):
    def filters(self):
        return {
                "get_temp":get_temp
                }
        
