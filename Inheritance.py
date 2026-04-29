# Base Class
class MobilePhone:
    def __init__(self, screen_type, network_type, dual_sim, front_camera, rear_camera, ram, storage):
        self.screen_type = screen_type
        self.network_type = network_type
        self.dual_sim = dual_sim
        self.front_camera = front_camera
        self.rear_camera = rear_camera
        self.ram = ram
        self.storage = storage

    # Basic functionalities
    def make_call(self):
        print("Calling...")

    def receive_call(self):
        print("Receiving call...")

    def take_picture(self):
        print("Picture taken!")

    def show_specs(self):
        print("\nSpecifications:")
        print("Screen:", self.screen_type)
        print("Network:", self.network_type)
        print("Dual SIM:", self.dual_sim)
        print("Front Camera:", self.front_camera)
        print("Rear Camera:", self.rear_camera)
        print("RAM:", self.ram)
        print("Storage:", self.storage)


# Child Class - Apple
class Apple(MobilePhone):
    def __init__(self, front_camera, rear_camera, ram, storage):
        super().__init__(
            screen_type="Touch Screen",
            network_type="5G",
            dual_sim=False,
            front_camera=front_camera,
            rear_camera=rear_camera,
            ram=ram,
            storage=storage
        )

    def brand(self):
        print("Brand: Apple")


# Child Class - Samsung
class Samsung(MobilePhone):
    def __init__(self, dual_sim, front_camera, rear_camera, ram, storage):
        super().__init__(
            screen_type="Touch Screen",
            network_type="5G",
            dual_sim=dual_sim,
            front_camera=front_camera,
            rear_camera=rear_camera,
            ram=ram,
            storage=storage
        )

    def brand(self):
        print("Brand: Samsung")


# -----------------------------
# Creating Objects
# -----------------------------

# Apple objects
iphone1 = Apple("12MP", "48MP", "4GB", "64GB")
iphone2 = Apple("16MP", "32MP", "3GB", "32GB")

# Samsung objects
samsung1 = Samsung(True, "16MP", "48MP", "4GB", "64GB")
samsung2 = Samsung(True, "8MP", "32MP", "3GB", "32GB")


# -----------------------------
# Testing
# -----------------------------

print("Apple Phone 1:")
iphone1.brand()
iphone1.show_specs()
iphone1.make_call()

print("\nSamsung Phone 1:")
samsung1.brand()
samsung1.show_specs()
samsung1.take_picture()