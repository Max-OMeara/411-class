from typing import Optional, Any


class Animal:
    def __init__(
        self,
        animal_id: int,
        species: str,
        age: Optional[int] = None,
        health_status: Optional[str] = None,
    ) -> None:
        self.animal_id = animal_id
        self.species = species
        self.age = age
        self.health_status = health_status

    def get_animal_details(self) -> dict[str, Any]:
        return {
            "animal_id": self.animal_id,
            "species": self.species,
            "age": self.age,
            "health_status": self.health_status,
        }
