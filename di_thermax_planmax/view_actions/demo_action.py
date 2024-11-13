from sqlalchemy import Integer, Select, bindparam
from efficieno.components.actions_object import Action, Parameter

from di_thermax_planmax.erd.apps.org_organization_definitions import OrgOrganizationDefinitions
from di_thermax_planmax.erd.inv.mtl_system_items_b import MtlSystemItemsB


class DemoAction(Action):
    __action_name__ = "Update Details"
    __action_description__ = "Update action details"

    field1 = Parameter(param_type=None, data_type=Integer, editable=False, show_on_form=True, values=None)

    field2 = Parameter(param_type=None, data_type=Integer, editable=True, show_on_form=True, values=[{"label": "One",
                                                                                                      "value": 1},
                                                                                                     {"label": "Two",
                                                                                                      "value": 2},
                                                                                                     {"label": "Four",
                                                                                                      "value": 4}])

    field3 = Parameter(
        param_type=None,
        data_type=Integer,
        editable=True,
        show_on_form=True,
        values=Select(MtlSystemItemsB.segment1.label("label"), MtlSystemItemsB.segment1.label("value")).filter(MtlSystemItemsB.organization_id == bindparam("field2")),
    )

    field4 = Parameter(
        param_type=None,
        data_type=Integer,
        editable=True,
        show_on_form=True,
        values=Select(OrgOrganizationDefinitions.organization_id.label("value"), OrgOrganizationDefinitions.organization_code.label("label")).filter(OrgOrganizationDefinitions.organization_id > 1),
    )

    @classmethod
    def execute_action(cls):
        print("Executing Action ")
        print(f"Field1          old - {cls.field1.old_value} new - {cls.field1.new_value}")
        print(f"Field2          old - {cls.field2.old_value} new - {cls.field2.new_value}")
        print(f"Field3          old - {cls.field3.old_value} new - {cls.field3.new_value}")
        print(f"Field4          old - {cls.field4.old_value} new - {cls.field4.new_value}")
        print("Completed Execution")
        return {}
