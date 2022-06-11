import json
import pytest

from matters.models import Bank, ConveyanceMatter, Matter
from matters.serializers import BaseMatterSerializer
from matters.stages import create_conveyance_object, matters


@pytest.fixture
def transfer():
    return [
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


@pytest.fixture
def mortgage_bond():
    return [
        "acknowledge_instructions",
        "statement_issued",
        "power_of_attorney_signed",
        "statement_paid",
        "documents_lodged",
        "documents_queried",
        "documents_registered",
        "documents_delivered_to_bank",
    ]


@pytest.fixture
def mortgage_bond_other_lawyers():
    return [
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


@pytest.fixture
def mortgage_bond_cancellation():
    return [
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


@pytest.fixture
def lost_deed_application():
    return [
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


@pytest.fixture
def transfer_object(transfer):
    transfer_object = create_conveyance_object("Transfer", transfer)
    return transfer_object


@pytest.fixture
def mortgage_bond_object(mortgage_bond):
    mortgage_bond_object = create_conveyance_object("Mortgage Bond", mortgage_bond)
    return mortgage_bond_object


@pytest.fixture
def mortgage_bond_other_lawyers_object(mortgage_bond_other_lawyers):
    mortgage_bond_object = create_conveyance_object(
        "Mortgage Bond Other Lawyers", mortgage_bond_other_lawyers
    )
    return mortgage_bond_object


@pytest.fixture
def lost_deed_application_object(lost_deed_application):
    lost_deed_object = create_conveyance_object(
        "Lost Deed Application", lost_deed_application
    )
    return lost_deed_object


@pytest.fixture
def mortgage_bond_cancellation_object(mortgage_bond_cancellation):
    mortgage_bond_object = create_conveyance_object(
        "Mortgage Bond Cancellation", mortgage_bond_cancellation
    )
    return mortgage_bond_object


@pytest.fixture
def bank(db):
    return Bank.objects.create(name="First Capital Bank")


@pytest.fixture
def bank2(db):
    return Bank.objects.create(name="Stanbic Bank")


@pytest.fixture
def sample_matter(db, transfer_object):
    return Matter.objects.create(name="Transfer", stages=transfer_object.stages)


@pytest.fixture
def sample_matter2(db, mortgage_bond_object):
    return Matter.objects.create(
        name="Mortgage Bond", stages=mortgage_bond_object.stages
    )


@pytest.fixture
def sample_matter3(db, mortgage_bond_other_lawyers_object):
    return Matter.objects.create(
        name="Mortgage Bond Other Lawyers Transferring",
        stages=mortgage_bond_other_lawyers_object.stages,
    )


@pytest.fixture
def conveyance_matter(db, bank, user, sample_matter):
    matter = ConveyanceMatter.objects.create(
        title="Deeds Transfer between Jane Doe and First Capital Bank",
        created_by=user,
        bank=bank,
    )
    matter.matters.add(sample_matter.id)
    return matter


@pytest.fixture
def basic_conveyance_matter(db, bank2, user):
    matter = ConveyanceMatter.objects.create(
        title="Deeds Transfer between Jane Doe and First Capital Bank",
        created_by=user,
        bank=bank2,
    )
    return matter


@pytest.fixture
def conveyance_matters(db, bank, user2, sample_matter2, sample_matter3):
    matter = ConveyanceMatter.objects.create(
        title="Mortgage Bond and Mortgage Bond Other Lawyers between John Doe and First Capital Bank",
        created_by=user2,
        bank=bank,
    )
    matter.matters.add(sample_matter2.id)
    matter.matters.add(sample_matter3.id)
    return matter


@pytest.fixture
def matter(db, mortgage_bond_object):
    return Matter.objects.create(
        name=mortgage_bond_object.name,
        stages=mortgage_bond_object.stages,
    )


@pytest.fixture
def conveyances():
    conveyance_matters = []
    for key in matters.keys():
        conveyance_matter = create_conveyance_object(
            matters[key]["name"], matters[key]["stages"]
        )
        conveyance_matters.append(conveyance_matter)
    results = BaseMatterSerializer(conveyance_matters, many=True).data
    return results


@pytest.fixture
def bank_payload():
    return {"name": "CBZ"}


@pytest.fixture
def edit_bank(bank):
    return {"id": bank.id, "name": "First Capital Bank Zimbabwe"}


@pytest.fixture
def conveyance_matter_payload(bank):
    return {
        "title": "Deeds Transfer between Jane Doe and First Capital Bank",
        "matters": [],
        "bank": bank.name,
        "complete": False,
        "comment": None,
    }


@pytest.fixture
def conveyance_matter_one_matter_payload(bank):
    return {
        "title": "Rose and CBZ Mortgage Bond Cancellation",
        "matters": [
            {
                "name": "Rose - Mortgage Bond Cancellation",
                "stages": [
                    {
                        "stage": "Acknowledge Instructions",
                        "step": 1,
                        "comment": None,
                        "done": False,
                    },
                    {
                        "stage": "Statement Issued",
                        "step": 2,
                        "comment": None,
                        "done": False,
                    },
                    {
                        "stage": "Statement Paid",
                        "step": 3,
                        "comment": None,
                        "done": False,
                    },
                    {
                        "stage": "Consent Aailable",
                        "step": 4,
                        "comment": None,
                        "done": False,
                    },
                    {
                        "stage": "Documents Lodged",
                        "step": 5,
                        "comment": None,
                        "done": False,
                    },
                    {
                        "stage": "Documents Queried",
                        "step": 6,
                        "comment": None,
                        "done": False,
                    },
                    {
                        "stage": "Documents Registered",
                        "step": 7,
                        "comment": None,
                        "done": False,
                    },
                    {
                        "stage": "Documents Delivered to Bank",
                        "step": 8,
                        "comment": None,
                        "done": False,
                    },
                    {
                        "stage": "Owner Collected Deed",
                        "step": 9,
                        "comment": None,
                        "done": False,
                    },
                    {
                        "stage": "Documents Co-lodged",
                        "step": 10,
                        "comment": None,
                        "done": False,
                    },
                ],
            }
        ],
        "bank": bank.name,
        "complete": False,
        "comment": "",
    }


@pytest.fixture
def conveyance_two_matters_payload(bank2):
    return {
        "title": "Deeds Transfer between Jane Doe and Stanbic Bank",
        "bank": bank2.name,
        "matters": [
            {
                "name": "Elizabeth & Ermet - Mortgage Bond with Other Lawyers Transfering",
                "stages": [
                    {
                        "stage": "Acknowledge Instructions",
                        "step": 1,
                        "comment": None,
                        "done": False,
                    },
                    {
                        "stage": "Power of Attorney Signed",
                        "step": 2,
                        "comment": None,
                        "done": False,
                    },
                    {
                        "stage": "Transfer Document Signed",
                        "step": 3,
                        "comment": None,
                        "done": False,
                    },
                    {
                        "stage": "Statement Issued",
                        "step": 4,
                        "comment": None,
                        "done": False,
                    },
                    {
                        "stage": "Statement Paid",
                        "step": 5,
                        "comment": None,
                        "done": False,
                    },
                    {
                        "stage": "CGT Documents Submitted",
                        "step": 6,
                        "comment": None,
                        "done": False,
                    },
                    {
                        "stage": "Interviews Conducted",
                        "step": 7,
                        "comment": None,
                        "done": False,
                    },
                    {
                        "stage": "CGT Assessment Collected",
                        "step": 8,
                        "comment": None,
                        "done": False,
                    },
                    {
                        "stage": "Assessment Paid",
                        "step": 9,
                        "comment": None,
                        "done": False,
                    },
                    {
                        "stage": "CGT Collected",
                        "step": 10,
                        "comment": None,
                        "done": False,
                    },
                    {
                        "stage": "Rates Certificate Collected",
                        "step": 11,
                        "comment": None,
                        "done": False,
                    },
                    {
                        "stage": "Documents Lodged",
                        "step": 12,
                        "comment": None,
                        "done": False,
                    },
                    {
                        "stage": "Documents Queried",
                        "step": 13,
                        "comment": None,
                        "done": False,
                    },
                    {
                        "stage": "Documents Registered",
                        "step": 14,
                        "comment": None,
                        "done": False,
                    },
                    {
                        "stage": "Documents Delivered to Bank",
                        "step": 15,
                        "comment": None,
                        "done": False,
                    },
                ],
            },
            {
                "name": "Elizabeth & Ermet - Lost Deed Application",
                "stages": [
                    {
                        "stage": "Acknowledge Instructions",
                        "step": 1,
                        "comment": None,
                        "done": False,
                    },
                    {
                        "stage": "Statement Issued",
                        "step": 2,
                        "comment": None,
                        "done": False,
                    },
                    {
                        "stage": "Statement Paid",
                        "step": 3,
                        "comment": None,
                        "done": False,
                    },
                    {
                        "stage": "Adverts Sent Out",
                        "step": 4,
                        "comment": None,
                        "done": False,
                    },
                    {
                        "stage": "Adverts Published",
                        "step": 5,
                        "comment": None,
                        "done": False,
                    },
                    {
                        "stage": "Affidavit Signed",
                        "step": 6,
                        "comment": None,
                        "done": False,
                    },
                    {
                        "stage": "Documents Lodged",
                        "step": 7,
                        "comment": None,
                        "done": False,
                    },
                    {
                        "stage": "Documents Queried",
                        "step": 8,
                        "comment": None,
                        "done": False,
                    },
                    {
                        "stage": "Documents Registered",
                        "step": 9,
                        "comment": None,
                        "done": False,
                    },
                    {
                        "stage": "Owner Collected Deed",
                        "step": 10,
                        "comment": None,
                        "done": False,
                    },
                ],
            },
        ],
        "complete": False,
        "comment": "",
    }


@pytest.fixture
def edit_conveyance_matter_payload(bank, sample_matter):
    return {
        "title": "Deeds Transfer between Jane Doe and First Capital Bank",
        "matters": [
            {
                "name": "Jane Doe - Transfer",
                "stages": [
                    {
                        "stage": "Acknowledge Instructions",
                        "step": 1,
                        "comment": None,
                        "done": False,
                    },
                    {
                        "stage": "Rates Application",
                        "step": 2,
                        "comment": None,
                        "done": False,
                    },
                    {
                        "stage": "Transfer Document Signed",
                        "step": 3,
                        "comment": None,
                        "done": False,
                    },
                    {
                        "stage": "Statement Issued",
                        "step": 4,
                        "comment": None,
                        "done": False,
                    },
                    {
                        "stage": "Statement Paid",
                        "step": 5,
                        "comment": None,
                        "done": False,
                    },
                    {
                        "stage": "CGT Documents Submitted",
                        "step": 6,
                        "comment": None,
                        "done": False,
                    },
                    {
                        "stage": "Interviews Conducted",
                        "step": 7,
                        "comment": None,
                        "done": False,
                    },
                    {
                        "stage": "CGT Assessment Collected",
                        "step": 8,
                        "comment": None,
                        "done": False,
                    },
                    {
                        "stage": "Assessment Paid",
                        "step": 9,
                        "comment": None,
                        "done": False,
                    },
                    {
                        "stage": "Rates Certificate Collected",
                        "step": 10,
                        "comment": None,
                        "done": False,
                    },
                    {
                        "stage": "Documents Lodged",
                        "step": 11,
                        "comment": None,
                        "done": False,
                    },
                    {
                        "stage": "Documents Queried",
                        "step": 12,
                        "comment": None,
                        "done": False,
                    },
                    {
                        "stage": "Documents Registered",
                        "step": 13,
                        "comment": None,
                        "done": False,
                    },
                    {
                        "stage": "Owner Collected Deed",
                        "step": 14,
                        "comment": None,
                        "done": False,
                    },
                ],
            }
        ],
        "bank": bank.name,
        "complete": False,
        "comment": "",
    }


@pytest.fixture
def create_matter():
    return {
        "name": "Richard Bucket - Transfer",
        "stages": [
            {
                "stage": "Acknowledge Instructions",
                "step": 1,
                "comment": "Received and signed.",
                "done": True,
            },
            {
                "stage": "Rates Application",
                "step": 2,
                "comment": "Application submitted",
                "done": False,
            },
            {
                "stage": "Transfer Document Signed",
                "step": 3,
                "comment": None,
                "done": False,
            },
            {"stage": "Statement Issued", "step": 4, "comment": None, "done": False},
            {"stage": "Statement Paid", "step": 5, "comment": None, "done": False},
            {
                "stage": "CGT Documents Submitted",
                "step": 6,
                "comment": None,
                "done": False,
            },
            {
                "stage": "Interviews Conducted",
                "step": 7,
                "comment": None,
                "done": False,
            },
            {
                "stage": "CGT Assessment Collected",
                "step": 8,
                "comment": None,
                "done": False,
            },
            {"stage": "Assessment Paid", "step": 9, "comment": None, "done": False},
            {
                "stage": "Rates Certificate Collected",
                "step": 10,
                "comment": None,
                "done": False,
            },
            {"stage": "Documents Lodged", "step": 11, "comment": None, "done": False},
            {"stage": "Documents Queried", "step": 12, "comment": None, "done": False},
            {
                "stage": "Documents Registered",
                "step": 13,
                "comment": None,
                "done": False,
            },
            {
                "stage": "Owner Collected Deed",
                "step": 14,
                "comment": None,
                "done": False,
            },
        ],
    }


@pytest.fixture
def edit_matter():
    return {
        "name": "Mortgage Bond",
        "stages": [
            {
                "stage": "Acknowledge Instructions",
                "step": 1,
                "comment": "Received and filed.",
                "done": True,
            },
            {
                "stage": "Statement Issued",
                "step": 2,
                "comment": "Statement issued to client.",
                "done": True,
            },
            {
                "stage": "Power of Attorney Signed",
                "step": 3,
                "comment": None,
                "done": False,
            },
            {"stage": "Statement Paid", "step": 4, "comment": None, "done": False},
            {"stage": "Documents Lodged", "step": 5, "comment": None, "done": False},
            {"stage": "Documents Queried", "step": 6, "comment": None, "done": False},
            {
                "stage": "Documents Registered",
                "step": 7,
                "comment": None,
                "done": False,
            },
            {
                "stage": "Documents Delivered to Bank",
                "step": 8,
                "comment": None,
                "done": False,
            },
        ],
    }
