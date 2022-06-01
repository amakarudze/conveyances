import json

from dataclasses import dataclass
from datetime import datetime
from typing import Dict, Iterable, List, Text


transfer = [
    "acknowledge_instructions",
    "rates_application",
    "transfer_document_signed",
    "statement_issued",
    "statement_paid",
    "cgt_documents_submitted",
    "interviews_conducted",
    "cgt_assessment_collected",
    "assessment_paid",
    "rates_certificate_collected",
    "documents_lodged",
    "documents_queried",
    "documents_registered",
    "owner_collected_deed",
]

mortgage_bond = [
    "acknowledge_instructions",
    "statement_issued",
    "power_of_attorney_signed",
    "statement_paid",
    "documents_lodged",
    "documents_queried",
    "documents_registered",
    "documents_delivered_to_bank",
]

mortgage_bond_other_lawyers = [
    "acknowledge_instructions",
    "power_of_attorney_signed",
    "transfer_document_signed",
    "statement_issued",
    "statement_paid",
    "cgt_documents_submitted",
    "interviews_conducted",
    "cgt_assessment_collected",
    "assessment_paid",
    "cgt_collected",
    "rates_certificate_collected",
    "documents_lodged",
    "documents_queried",
    "documents_registered",
    "documents_delivered_to_bank",
]

lost_deed_application = [
    "acknowledge_instructions",
    "statement_issued",
    "statement_paid",
    "adverts_sent_out",
    "adverts_published",
    "affidavit_signed",
    "documents_lodged",
    "documents_queried",
    "documents_registered",
    "owner_collected_deed",
]
mortgage_bond_cancellation = [
    "acknowledge_instructions",
    "statement_issued",
    "statement_paid",
    "consent_available" "documents_lodged",
    "documents_queried",
    "documents_registered",
    "documents_delivered_to_bank",
    "owner_collected_deed",
    "documents_co_lodged",
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


@dataclass
class Stage:
    comment: Text = None
    date_updated: datetime = None
    user: Text = None
    done: bool = None

    def default(self):
        pass


@dataclass
class Matter:
    name: Text
    stages: Dict


def create_conveyance_object(name: str, stages: List) -> Iterable[Matter]:
    matter_stages = {}
    for stage in stages:
        matter_stages[stage] = vars(Stage())
    convenyance_matter = Matter(name, matter_stages)
    return convenyance_matter
