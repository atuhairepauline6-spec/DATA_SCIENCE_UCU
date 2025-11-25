class ENGINE:
    """
    Represents an engine with basic properties and functionality.
    """

    def __init__(self, displacement_liters, cylinders, fuel_type="Gasoline"):
        """
        Initializes the ENGINE object.

        Args:
            displacement_liters (float): The engine's displacement in liters.
            cylinders (int): The number of cylinders the engine has.
            fuel_type (str, optional): The type of fuel the engine uses.
                                       Defaults to "Gasoline".
        """
        if displacement_liters <= 0:
            raise ValueError("Displacement must be positive.")
        if cylinders <= 0 or not isinstance(cylinders, int):
            raise ValueError("Cylinders must be a positive integer.")

        self.displacement = displacement_liters
        self.num_cylinders = cylinders
        self.fuel_type = fuel_type
        self.is_running = False

    def start(self):
        """
        Simulates starting the engine.
        """
        if not self.is_running:
            print(f"Starting the {self.fuel_type} engine ({self.displacement}L, {self.num_cylinders} cyl)... Vroom!")
            self.is_running = True
        else:
            print("The engine is already running.")

    def stop(self):
        """
        Simulates stopping the engine.
        """
        if self.is_running:
            print("Stopping the engine... Clunk.")
            self.is_running = False
        else:
            print("The engine is already stopped.")

    def get_specs(self):
        """
        Returns a dictionary containing the engine's specifications.
        """
        return {
            "Displacement (L)": self.displacement,
            "Cylinders": self.num_cylinders,
            "Fuel Type": self.fuel_type,
            "Status": "Running" if self.is_running else "Stopped"
        }

# --- Example Usage ---
if __name__ == "__main__":
    # 1. Create an instance of the ENGINE class
    my_engine = ENGINE(displacement_liters=2.0, cylinders=4)
    big_engine = ENGINE(displacement_liters=6.2, cylinders=8, fuel_type="Diesel")

    # 2. Print initial specs
    print("--- My Engine Specs ---")
    print(my_engine.get_specs())
    print("-" * 25)

    # 3. Start the engine
    my_engine.start()
    print("-" * 25)

    # 4. Try to start it again
    my_engine.start()
    print("-" * 25)

    # 5. Check the status after starting
    print("--- My Engine Updated Specs ---")
    print(my_engine.get_specs())
    print("-" * 25)

    # 6. Use the big engine
    print("--- Big Engine Actions ---")
    print(f"Big Engine Fuel: {big_engine.fuel_type}")
    big_engine.start()
    big_engine.stop()
    print("-" * 25)

    # 7. Stop the engine
    my_engine.stop()
    print("-" * 25)

    # 8. Try to stop it again
    my_engine.stop()
