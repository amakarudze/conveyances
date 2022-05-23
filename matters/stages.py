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
    "transfer": transfer,
    "mortgage_bond": mortgage_bond,
    "mortgage_bond_other_lawyers": mortgage_bond_other_lawyers,
    "lost_deed_application": lost_deed_application,
    "mortgage_bond_cancellation": mortgage_bond_cancellation,
}


@dataclass
class Stage:
    comment: Text = None
    date_updated: datetime = None
    user: Text = None
    done: bool = None


class Matter:
    def __init__(self, **kwargs):
        pass


def create_conveyance_object(code: str, stages: List, Stage: Dict) -> Iterable[Matter]:
    matter_stages = {}
    for stage in stages:
        matter_stages[stage] = Stage()
    convenyance_matter = Matter(code, matter_stages)
    return convenyance_matter
