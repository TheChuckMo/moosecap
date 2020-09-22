from marshmallow import Schema, fields


class OrganizationSchema(Schema):
    bat = fields.String(required=True)
    name = fields.String(required=True)
    display = fields.String()
    note = fields.String()
    work_unit_name = fields.String(required=True, default='hour')
    work_unit_per_week = fields.Int(required=True, default=40)
    work_unit_admin_ratio = fields.Decimal(required=True, default=0.20)
    teams = fields.List(fields.Nested(lambda: TeamSchema(only='bat')))
    extra = fields.Mapping()


class TeamSchema(Schema):
    bat = fields.String(required=True)
    name = fields.String(required=True)
    organization = fields.Nested(OrganizationSchema(only='bat'))
    display = fields.String()


class PersonSchema(Schema):
    bat = fields.String(required=True)
    name = fields.String(required=True)
    display = fields.String()
    email = fields.Email()
    manage = fields.Nested(TeamSchema(only='bat'))
    team = fields.Nested(TeamSchema(only='bat'))
    work_unit_ratio = fields.Int(default=1)
    note = fields.String()
    extra = fields.Mapping()
    technology_skills = fields.List(fields.Nested(lambda: Technology_SkillSchema))


class Technology_SkillSchema(Schema):
    bat = fields.String(required=True)
    name = fields.String(required=True)
    display = fields.String()

