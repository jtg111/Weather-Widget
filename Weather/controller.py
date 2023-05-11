import requests
from PyQt5.QtWidgets import *
from weather import *


class Controller(QMainWindow, Ui_Weather):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.setupUi(self)

        # Hiding elements
        hidden = [self.weather_des, self.temp_numC, self.temp_numF, self.farenhei_label,
                  self.celsius_label, self.error_thing]

        for i in hidden:
            i.setVisible(False)

        # When "go button" is clicked
        self.enter_button.clicked.connect(lambda: self.get_weather())

    def get_weather(self):
        # Grab city name and set api key
        api_key = "325be6584c255d1c6e7e67c8bfda6899"
        city = self.city_entry.text()

        response = requests.get(f"http://api.weatherstack.com/current?access_key={api_key}&query={city}")
        try:
            # https://weatherstack.com/quickstart and https://weatherstack.com/documentation
            if response.status_code == 200:
                # Changing hidden elements to received values
                weather_data = response.json()["current"]
                self.temp_numC.setText(str(weather_data["temperature"]))
                self.temp_numF.setText(str(((int(weather_data["temperature"]))*9//5)+32))
                self.weather_des.setText(str(weather_data["weather_descriptions"]))

                # Making sure error message is not visible
                self.error_thing.setVisible(False)

                # Unhiding hidden elements
                hidden = [self.weather_des, self.temp_numC, self.temp_numF, self.farenhei_label,
                          self.celsius_label]

                for i in hidden:
                    i.setVisible(True)

            else:
                # If city is misspelled or is not in database
                hidden = [self.weather_des, self.w_graphic, self.temp_numC, self.temp_numF, self.farenhei_label,
                          self.celsius_label]
                for i in hidden:
                    i.setVisible(False)
                raise KeyError
        except KeyError:
            # Re-hiding everything and displaying error message
            hidden = [self.weather_des, self.temp_numC, self.temp_numF, self.farenhei_label,
                      self.celsius_label, self.error_thing]

            for i in hidden:
                i.setVisible(False)

            self.error_thing.setVisible(True)

