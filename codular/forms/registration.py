import colander
import deform

from .csrf import CSRFSchema

username_regex = '^[a-z0-9\-]+$'

class Registration(CSRFSchema):
    username = colander.SchemaNode(colander.String(),
                                   validator=colander.Regex(username_regex,
                                       'Your username can only contain '\
                                      +'lowercase alphanumerical characters or dashes'))
    name = colander.SchemaNode(colander.String())
    # TODO: write an anti-duplicates validator
    email = colander.SchemaNode(colander.String(),
                                validator=colander.Email())
    password = colander.SchemaNode(colander.String(),
                                   validator=colander.Length(min=8),
                                   widget=deform.widget.CheckedPasswordWidget(size='20'),
                                   description='Enter a password')

