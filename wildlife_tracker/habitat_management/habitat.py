from typing import List, Optional, Any
from wildlife_tracker.animal_management.animal import Animal


class Habitat:
    def __init__(
        self,
        habitat_id: int,
        geographic_area: str,
        size: int,
        environment_type: str,
        animals: Optional[List[int]] = None,
    ) -> None:
        self.habitat_id = habitat_id
        self.geographic_area = geographic_area
        self.size = size
        self.environment_type = environment_type
        self.animals = animals or []

    def assign_animals_to_habitat(self, animals: List[Animal]) -> None:
        self.animals.extend([animal.animal_id for animal in animals])

    def remove_animals_from_habitat(self, animal_ids: List[int]) -> None:
        self.animals = [aid for aid in self.animals if aid not in animal_ids]

    def get_animals_in_habitat(self) -> List[int]:
        return self.animals

    def update_habitat_details(self, **kwargs: Any) -> None:
        for key, value in kwargs.items():
            if hasattr(self, key):
                setattr(self, key, value)

    def get_habitat_details(self) -> dict[str, Any]:
        return {
            "habitat_id": self.habitat_id,
            "geographic_area": self.geographic_area,
            "size": self.size,
            "environment_type": self.environment_type,
            "animals": self.animals,
        }
