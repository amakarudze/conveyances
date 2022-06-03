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
def sample_matter(db, transfer_object, user):
    return Matter.objects.create(
        name="Transfer",
        stages=transfer_object.stages,
        created_by=user
    )


@pytest.fixture
def sample_matter2(db, mortgage_bond_object, user):
    return Matter.objects.create(
        name="Mortgage Bond",
        stages=mortgage_bond_object.stages,
        created_by=user
    )


@pytest.fixture
def sample_matter3(db, mortgage_bond_other_lawyers_object, user2):
    return Matter.objects.create(
        name="Mortgage Bond Other Lawyers Transferring",
        stages = mortgage_bond_other_lawyers_object.stages,
        created_by=user2
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
def basic_conveyance_matter(db, bank, user):
    matter = ConveyanceMatter.objects.create(
        title="Deeds Transfer between Jane Doe and First Capital Bank",
        created_by=user,
        bank=bank,
    )
    return matter


@pytest.fixture
def conveyance_matters(
    db, bank, user2, sample_matter2, sample_matter3
):
    matter = ConveyanceMatter.objects.create(
        title="Mortgage Bond and Mortgage Bond Other Lawyers between John Doe and First Capital Bank",
        created_by=user2,
        bank=bank
    )
    matter.matters.add(sample_matter2.id)
    matter.matters.add(sample_matter3.id)
    return matter


@pytest.fixture
def matter(db, user, mortgage_bond_object):
    return Matter.objects.create(
        created_by=user,
        name=mortgage_bond_object.name,
        stages=mortgage_bond_object.stages
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
    return {
        'name': 'CBZ'
    }


@pytest.fixture
def edit_bank(bank):
    return {
        'id': bank.id,
        'name': 'First Capital Bank Zimbabwe'
    }


@pytest.fixture
def conveyance_matter_payload(bank):
    return {
        "title": "Deeds Transfer between Jane Doe and First Capital Bank",
        "bank": bank.id,
    }


@pytest.fixture
def conveyance_matter_one_matter_payload(bank, sample_matter):
    return {
        "title": "Nortgage Bond between Jane Doe and First Capital Bank",
        "bank": bank.id,
        "matters": [sample_matter.id]
    }


@pytest.fixture
def conveyance_two_matters_payload(bank2, sample_matter2, sample_matter3):
    return {
        "title": "Deeds Transfer between Jane Doe and Stanbic Bank",
        "bank": bank2.id,
        "matters": [sample_matter2.id, sample_matter3.id]
    }


@pytest.fixture
def edit_conveyance_matter_payload(bank, sample_matter):
    return {
        "matters": [sample_matter.id]
    }
