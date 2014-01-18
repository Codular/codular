import colander
import deform

from .csrf import CSRFSchema

username_regex = '^[a-z0-9\-]+$'

class RegistrationLoginPart(colander.Schema):
    username = colander.SchemaNode(colander.String(),
                                   validator=colander.Regex(username_regex,
                                       'Your username can only contain '\
                                      +'lowercase alphanumerical characters or dashes'))
    # TODO: write an anti-duplicates validator
    password = colander.SchemaNode(colander.String(),
                                   validator=colander.Length(min=8),
                                   widget=deform.widget.CheckedPasswordWidget(size='20'),
                                   description='Enter a password')

class Registration(CSRFSchema):
    name = colander.SchemaNode(colander.String())
    email = colander.SchemaNode(colander.String(),
                                validator=colander.Email())
    login_infos = RegistrationLoginPart()
