from dataclasses import dataclass
from typing import Dict, Iterable, List, Text


transfer = [
    "Acknowledge Instructions",
    "Rates Application",
    "Transfer Document Signed",
    "Statement Issued",
    "Statement Paid",
    "CGT Documents Submitted",
    "Interviews Conducted",
    "CGT Assessment Collected",
    "Assessment Paid",
    "Rates Certificate Collected",
    "Documents Lodged",
    "Documents Queried",
    "Documents Registered",
    "Owner Collected Deed",
]

mortgage_bond = [
    "Acknowledge Instructions",
    "Statement Issued",
    "Power of Attorney Signed",
    "Statement Paid",
    "Documents Lodged",
    "Documents Queried",
    "Documents Registered",
    "Documents Delivered to Bank",
]

mortgage_bond_other_lawyers = [
    "Acknowledge Instructions",
    "Power of Attorney Signed",
    "Transfer Document Signed",
    "Statement Issued",
    "Statement Paid",
    "CGT Documents Submitted",
    "Interviews Conducted",
    "CGT Assessment Collected",
    "Assessment Paid",
    "CGT Collected",
    "Rates Certificate Collected",
    "Documents Lodged",
    "Documents Queried",
    "Documents Registered",
    "Documents Delivered to Bank",
]

lost_deed_application = [
    "Acknowledge Instructions",
    "Statement Issued",
    "Statement Paid",
    "Adverts Sent Out",
    "Adverts Published",
    "Affidavit Signed",
    "Documents Lodged",
    "Documents Queried",
    "Documents Registered",
    "Owner Collected Deed",
]
mortgage_bond_cancellation = [
    "Acknowledge Instructions",
    "Statement Issued",
    "Statement Paid",
    "Consent Aailable",
    "Documents Lodged",
    "Documents Queried",
    "Documents Registered",
    "Documents Delivered to Bank",
    "Owner Collected Deed",
    "Documents Co-lodged",
]

matters = {
    "transfer": {"name": "Transfer", "stages": transfer},
    "mortgage_bond": {"name": "Mortgage Bond", "stages": mortgage_bond},
    "mortgage_bond_other_lawyers": {
        "name": "Mortgage Bond with Other Lawyers Transfering",
        "stages": mortgage_bond_other_lawyers,
    },
    "lost_deed_application": {
        "name": "Lost Deed Application",
        "stages": lost_deed_application,
    },
    " mortgage_bond_cancellation": {
        "name": "Mortgage Bond Cancellation",
        "stages": mortgage_bond_cancellation,
    },
}


class Stage:
    def __init__(self, step, stage):
        self.stage = stage
        self.step = step
        self.comment: Text = None
        self.done: bool = False


@dataclass
class BaseMatter:
    name: Text
    stages: List


def create_conveyance_object(name: str, stages: List) -> Iterable[BaseMatter]:
    matter_stages = []
    for i, stage in enumerate(stages):
        matter_stages.append(vars(Stage(i + 1, stage)))

    convenyance_matter = BaseMatter(name, matter_stages)
    return convenyance_matter
