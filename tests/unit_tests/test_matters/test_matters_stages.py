def test_transfer_matter_object(transfer_object):
    assert len(transfer_object.stages) == 14
    assert transfer_object.name == "Transfer"


def test_mortgage_bond_object(mortgage_bond_object):
    assert len(mortgage_bond_object.stages) == 8
    assert mortgage_bond_object.name == "Mortgage Bond"


def test_mortgage_bond_other_lawyers_object(mortgage_bond_other_lawyers_object):
    assert len(mortgage_bond_other_lawyers_object.stages) == 15
    assert mortgage_bond_other_lawyers_object.name == "Mortgage Bond Other Lawyers"


def test_lost_deed_application_object(lost_deed_application_object):
    assert len(lost_deed_application_object.stages) == 10
    assert lost_deed_application_object.name == "Lost Deed Application"


def test_mortgage_bond_cancellation_object(mortgage_bond_cancellation_object):
    assert len(mortgage_bond_cancellation_object.stages) == 9
    assert mortgage_bond_cancellation_object.name == "Mortgage Bond Cancellation"
