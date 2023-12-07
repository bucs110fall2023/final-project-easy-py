import json

class SaveProg:

    def __init__(self, save= None):
        """
        Accepts the save file name as a property
        args: self, save
        return: None
        """
        self.save = save

    def save_update(self):
        """
        Updates the save data based on the player's progress
        args: self
        return: None
        """
        with open(r"../final-project-easy-py/assets/save_data.json", "r") as save_read:    
            save_data = json.load(save_read)
        with open(r"../final-project-easy-py/assets/save_data.json", "w") as save_add:
            print(save_read)
            save_data[self.save]["Progress"] += 1
            json.dump(save_data, save_add, indent=4)

    def save_reset(self):
        """
        Resets the players save data to default
        args: self
        return: None
        """
        with open(r"../final-project-easy-py/assets/static_save_data.txt", "r") as static_save_read:
            default = static_save_read.read()
        with open(r"../final-project-easy-py/assets/save_data.json", "w") as save_reset:
            save_reset.write(default)
