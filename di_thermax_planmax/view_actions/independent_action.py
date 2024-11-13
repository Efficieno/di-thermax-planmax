from sqlalchemy import Integer, Select, bindparam, String
from efficieno.components.actions_object import Action, Parameter

from di_thermax_planmax.erd.apps.org_organization_definitions import OrgOrganizationDefinitions
from di_thermax_planmax.erd.inv.mtl_system_items_b import MtlSystemItemsB


class IndependentAction(Action):
    __action_name__ = "Independent Action"
    __action_description__ = "Independent Action Details"

    parameter1 = Parameter(display_name="Parameter 1", param_type=None, data_type=Integer, editable=False, show_on_form=True, values=None)

    parameter2 = Parameter(display_name="Parameter 2", param_type=None, data_type=Integer, editable=True, show_on_form=True, values=[{"label": "One",
                                                                                                                                      "value": 1},
                                                                                                                                     {"label": "Two",
                                                                                                                                      "value": 2},
                                                                                                                                     {"label": "Four",
                                                                                                                                      "value": 4}])

    organization_code = Parameter(display_name="Organization Code",
                                  param_type=None,
                                  data_type=String,
                                  editable=True,
                                  show_on_form=True,
                                  values=Select(OrgOrganizationDefinitions.organization_id.label("value"), OrgOrganizationDefinitions.organization_code.label("label")))

    item_number = Parameter(display_name="Item Number",
                            param_type=None,
                            data_type=String,
                            editable=True,
                            show_on_form=True,
                            values=Select(MtlSystemItemsB.segment1.label("label"), MtlSystemItemsB.segment1.label("value")).filter(MtlSystemItemsB.organization_id == bindparam("organization_code"))
                            )

    @classmethod
    def execute_action(cls):
        print("Executing Action ")
        print(f"parameter1          old - {cls.parameter1.old_value}        new - {cls.parameter1.new_value}")
        print(f"parameter2          old - {cls.parameter2.old_value}        new - {cls.parameter2.new_value}")
        print(f"organization_code   old - {cls.organization_code.old_value} new - {cls.organization_code.new_value}")
        print(f"item_number         old - {cls.item_number.old_value}       new - {cls.item_number.new_value}")
        print("Completed Execution")
        return {}
