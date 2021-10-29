
from flaskblog.users import forms


def test_registration_form(client):
    """
    Tests whether the Registration for allows only valid data
    :param client:
    :return:
    """

    # POSITIVE TEST
    form = forms.RegistrationForm(meta={'csrf': False})
    form.username.data = "test"
    form.email.data = "test@email.com"
    form.password.data = "test"
    form.confirm_password.data = "test"
    assert form.validate()

    # NEGATIVE TEST
    form = forms.RegistrationForm(meta={'csrf': False})
    form.username.data = "test"
    form.email.data = "faraz@flaskbloger.com"
    form.password.data = "test"
    form.confirm_password.data = "test"
    assert form.validate() is False
