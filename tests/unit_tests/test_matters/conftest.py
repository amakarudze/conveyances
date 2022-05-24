import pytest

from matters.models import Bank, ConveyanceMatter
from matters.stages import create_conveyance_object


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
def conveyance_matter(db, transfer_object, bank, user):
    return ConveyanceMatter.objects.create(
        title="Deeds Transfer between Jane Doe and First Capital Bank",
        matters=[transfer_object],
        created_by=user,
        bank=bank,
    )


@pytest.fixture
def conveyance_matters(
    db, mortgage_bond_object, mortgage_bond_other_lawyers_object, bank, user
):
    return ConveyanceMatter.objects.create(
        title="Mortgage Bond and Mortgage Bond Other Lawyers between John Doe and First Capital Bank",
        matters=[mortgage_bond_object, mortgage_bond_other_lawyers_object],
        created_by=user,
        bank=bank,
    )
