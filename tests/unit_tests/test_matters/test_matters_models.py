def test_conveyance_matter_model_string_representation(conveyance_matter):
    assert (
        str(conveyance_matter)
        == "Deeds Transfer between Jane Doe and First Capital Bank"
    )


def test_bank_model_string_representation(bank):
    assert str(bank) == "First Capital Bank"
