from pydantic import BaseModel, ValidationError, Field, model_validator
from enum import Enum
from datetime import datetime
from typing import Optional


class ContactType(Enum):
    RADIO = "RADIO"
    VISUAL = "VISUAL"
    PHYSICAL = "PHYSICAL"
    TELEPATHIC = "TELEPATHIC"


class AlienContact(BaseModel):
    contact_id: str = Field(
        min_length=5, max_length=15, description="id of contact")
    timestamp: datetime
    location: str = Field(min_length=3, max_length=100)
    contact_type: ContactType
    signal_strength: float = Field(ge=0.0, le=10.0)
    duration_minutes: int = Field(ge=1, le=1440)
    witness_count: int = Field(ge=1, le=100)
    message_received: Optional[str] = Field(max_length=500)
    is_verified: bool = False

    @model_validator(mode='after')
    def validator(self) -> "AlienContact":
        if self.contact_id[0] != "A" or self.contact_id[1] != "C":
            raise ValueError("Contact ID must start with 'AC'")
        if (self.contact_type == ContactType.PHYSICAL and
                self.is_verified is False):
            raise ValueError("Physical Contact reports must be verified")
        if (self.contact_type == ContactType.TELEPATHIC and
                self.witness_count < 3):
            raise ValueError(
                "Telepathic contact requires at least 3 witnesses")
        if self.signal_strength > 7 and self.message_received is None:
            raise ValueError(
                "Strong signals (> 7.0) should include received messages"
            )
        return self


def main() -> None:
    try:
        alien_1 = AlienContact(
            contact_id="AC_2024",
            timestamp=datetime.now(),
            location="Nevada",
            contact_type=ContactType.VISUAL,
            signal_strength=8.5,
            duration_minutes=45,
            witness_count=6,
            message_received="Greeting from Zeta Reticuli"
            )
        print("=======================")
        print("Valid contact report:")
        print(f"ID: {alien_1.contact_id}")
        print(f"Type: {alien_1.contact_type.value}")
        print(f"Location: {alien_1.location}")
        print(f"Signal: {alien_1.signal_strength}/10")
        print(f"Duration: {alien_1.duration_minutes}")
        print(f"Witnesses: {alien_1.witness_count}")
        print(f"Message: '{alien_1.message_received}'")
        print()
        print("=======================")
        print("Expected validation error:")
        alien_2 = AlienContact(
            contact_id="AC_2024",
            timestamp=datetime.now(),
            location="Nevada",
            contact_type=ContactType.VISUAL,
            signal_strength=8.5,
            duration_minutes=45,
            witness_count=1,
            message_received=None
        )
        print(alien_2.contact_id)
    except ValidationError as e:
        error = e.errors()[0]['msg']
        print(error)
    except Exception as e:
        print(e)


if __name__ == "__main__":
    main()
