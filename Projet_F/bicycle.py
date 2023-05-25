class Bicycle:
    bicycle_count = 0

    def __init__(self, brand, model, year, color, num_vignette_critair):
        self.brand = brand
        self.model = model
        self.year = year
        self.color = color
        self.num_vignette_critair = num_vignette_critair
        Bicycle.bicycle_count += 1

    def get_brand(self):
        return self.brand

    def get_model(self):
        return self.model

    def get_year(self):
        return self.year

    def get_color(self):
        return self.color

    def get_num_vignette_critair(self):
        return self.num_vignette_critair
