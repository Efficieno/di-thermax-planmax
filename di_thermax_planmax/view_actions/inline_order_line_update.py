from sqlalchemy import Integer, Select, bindparam, String, Date
from efficieno.components.actions_object import Action, Parameter

from di_thermax_planmax.erd.ont.oe_order_lines_all import OeOrderLinesAll
from di_thermax_planmax.erd.apps.org_organization_definitions import OrgOrganizationDefinitions


class InlineOrderLineUpdate(Action):
    __action_name__ = "Inline Order Line Update"
    __action_description__ = "Inline Order Line Update"

    request_date = Parameter(display_name="Request Date", param_type=None, data_type=Date, editable=True, show_on_form=True, values=None)

    shipping_method_code = Parameter(display_name="Shipping Method",
                                        param_type=None,
                                        data_type=String,
                                        editable=True,
                                        show_on_form=True,
                                        values=None)

    ship_from_org_id = Parameter(display_name="Organization ID",
                                  param_type=None,
                                  data_type=String,
                                  editable=True,
                                  show_on_form=True,
                                  values=Select(OrgOrganizationDefinitions.organization_id.label("value"), OrgOrganizationDefinitions.organization_code.label("label")))

    ordered_quantity = Parameter(display_name="Ordered Quantity",
                            param_type=None,
                            data_type=Integer,
                            editable=True,
                            show_on_form=True,
                            values=None
                            )

    @classmethod
    def execute_action(cls):
        print("Executing Action ")
        print(f"request_date          old - {cls.request_date.old_value}        new - {cls.request_date.new_value}")
        print(f"shipping_method_code          old - {cls.shipping_method_code.old_value}        new - {cls.shipping_method_code.new_value}")
        print(f"ship_from_org_id   old - {cls.ship_from_org_id.old_value} new - {cls.ship_from_org_id.new_value}")
        print(f"ordered_quantity         old - {cls.ordered_quantity.old_value}       new - {cls.ordered_quantity.new_value}")
        print("Completed Execution")
        return {}
