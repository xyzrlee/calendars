import enum


@enum.unique
class STATUS(enum.Enum):
    CONFIRMED = "CONFIRMED"
    TENTATIVE = "TENTATIVE"
    CANCELLED = "CANCELLED"


@enum.unique
class TRANSP(enum.Enum):
    OPAQUE = "OPAQUE"
    TRANSPARENT = "TRANSPARENT"
