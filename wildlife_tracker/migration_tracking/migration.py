from typing import Optional, Any
from wildlife_tracker.migration_tracking.migration_path import MigrationPath


class Migration:
    def __init__(
        self,
        migration_id: int,
        migration_path: MigrationPath,
        start_date: str,
        status: str = "Scheduled",
        current_location: Optional[str] = None,
        current_date: Optional[str] = None,
    ) -> None:
        self.migration_id = migration_id
        self.migration_path = migration_path
        self.start_date = start_date
        self.status = status
        self.current_location = current_location
        self.current_date = current_date

    def update_migration_details(self, **kwargs: Any) -> None:
        for key, value in kwargs.items():
            if hasattr(self, key):
                setattr(self, key, value)

    def get_migration_details(self) -> dict[str, Any]:
        return {
            "migration_id": self.migration_id,
            "migration_path_id": self.migration_path.path_id,
            "start_date": self.start_date,
            "status": self.status,
            "current_location": self.current_location,
            "current_date": self.current_date,
        }
