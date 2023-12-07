import json

class SaveProg:

    def __init__(self, save):
        self.save = save

    def save_update(self):
        with open(r"../assets/save_data.json", "r") as save_read:    
            save_data = json.load(save_read)
        with open(r"../assets/save_data.json", "w") as save_add:
            print(save_read)
            save_data[self.save]["Progress"] += 1
            json.dump(save_data, save_add, indent=4)