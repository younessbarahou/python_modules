from pydantic import BaseModel, Field, model_validator, ValidationError
from enum import Enum
from datetime import datetime


class Rank(Enum):
    CADET = 'cadet'
    OFFICER = 'officer'
    LIEUTENANT = 'lieutenant'
    CAPTAIN = 'captain'
    COMMANDER = 'commander'


class CrewMember(BaseModel):
    member_id: str = Field(min_length=3, max_length=10)
    name: str = Field(min_length=2, max_length=50)
    rank: Rank
    age: int = Field(ge=18, le=80)
    specialization: str = Field(min_length=3, max_length=30)
    years_experience: int = Field(ge=0, le=50)
    is_active: bool = True


class SpaceMission(BaseModel):
    mission_id: str = Field(
        min_length=5, max_length=15, description="id of a mission")
    mission_name: str = Field(min_length=3, max_length=100)
    destination: str = Field(min_length=3, max_length=50)
    launch_date: datetime
    duration_days: int = Field(ge=1, le=3650)
    crew: list[CrewMember] = Field(min_length=1, max_length=12)
    mission_status: str = "planned"
    budget_millions: float = Field(ge=1.0, le=10000.0)

    @model_validator(mode='after')
    def validate(self) -> "SpaceMission":
        if self.mission_id[0] != "M":
            raise ValueError("Mission ID must start with 'M'")
        commander_captain = 0
        for member in self.crew:
            if member.rank == Rank.CAPTAIN or member.rank == Rank.COMMANDER:
                commander_captain += 1
        if commander_captain == 0:
            raise ValueError("Must have at least one Commander or Captain")
        if self.duration_days > 365:
            cte = 0
            for member in self.crew:
                if member.years_experience >= 5:
                    cte += 1
            if len(self.crew) / 2 > cte:
                raise ValueError(
                    "missions (> 365 days) need 50% (crew 5+ years exp)"
                )
        for member in self.crew:
            if member.is_active is False:
                raise ValueError("All crew members must be active")
        return self


def main() -> None:
    try:
        commander_1 = CrewMember(
            member_id="W001",
            name="Max",
            rank=Rank.CAPTAIN,
            age=28,
            specialization="Mission Command",
            years_experience=2,
            is_active=True
        )
        officer_1 = CrewMember(
            member_id="W002",
            name="Stevan",
            rank=Rank.OFFICER,
            age=38,
            specialization="Navigation",
            years_experience=12,
            is_active=True
        )
        mission_1 = SpaceMission(
            mission_id="M2024",
            mission_name="EAGLE",
            destination="MARS",
            crew=[commander_1, officer_1],
            launch_date=datetime.now(),
            duration_days=20,
            budget_millions=100
        )
        print("=========================================")
        print("Valid mission created:")
        print(f"Mission: {mission_1.mission_name}")
        print(f"ID: {mission_1.mission_id}")
        print(f"Destination: {mission_1.destination}")
        print(f"Duration: {mission_1.duration_days} Days")
        print(f"Budget: ${mission_1.budget_millions}M")
        print(f"Crew size: {len(mission_1.crew)}")
        print("Crew members: ")
        for member in mission_1.crew:
            print(
                f"-{member.name}({member.rank.value})-{member.specialization}")
        print("\n=========================================")
        print("Expected validation error:")
        cadet_1 = CrewMember(
            member_id="C-01",
            name="Max",
            rank=Rank.CADET,
            age=28,
            specialization="Doctor",
            years_experience=2,
            is_active=True
        )
        mission_2 = SpaceMission(
            mission_id="M2024",
            mission_name="EAGLE",
            destination="MARS",
            crew=[cadet_1],
            launch_date=datetime.now(),
            duration_days=20,
            budget_millions=100
        )
        print(f"Mission: {mission_2.mission_name}")
        print(f"ID: {mission_2.mission_id}")
        print(f"Destination: {mission_2.destination}")
        print(f"Duration: {mission_2.duration_days} Days")
        print(f"Budget: ${mission_2.budget_millions}M")
        print(f"Crew size: {len(mission_2.crew)}")
        print("Crew members: ")
        for member in mission_2.crew:
            print(
                f"-{member.name}({member.rank.value})-{member.specialization}")
    except ValidationError as e:
        print(e.errors()[0]['msg'])
    except Exception as e:
        print(e)


if __name__ == "__main__":
    main()
