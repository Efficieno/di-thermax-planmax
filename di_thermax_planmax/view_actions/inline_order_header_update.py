from sqlalchemy import Integer, Select, bindparam, String, Date
from efficieno.components.actions_object import Action, Parameter

from di_thermax_planmax.erd.ont.oe_order_headers_all import OeOrderHeadersAll
from di_thermax_planmax.erd.apps.org_organization_definitions import OrgOrganizationDefinitions


class InlineOrderHeaderUpdate(Action):
    __action_name__ = "Inline Order Header Update"
    __action_description__ = "Inline Order Header Update"

    # ordered_date = Parameter(display_name="Ordered Date", param_type=None, data_type=Date, editable=True, show_on_form=True, values=None)

    transactional_curr_code = Parameter(display_name="Currency Code",
                                        param_type=None,
                                        data_type=String,
                                        editable=True,
                                        show_on_form=True,
                                        values=[{"label": "One",
                                                  "value": 1},
                                                 {"label": "Two",
                                                  "value": 2},
                                                 {"label": "Four",
                                                  "value": 4}])

    org_id = Parameter(display_name="Organization ID",
                                  param_type=None,
                                  data_type=String,
                                  editable=True,
                                  show_on_form=True,
                                  values=Select(OrgOrganizationDefinitions.organization_id.label("value"), OrgOrganizationDefinitions.organization_code.label("label")))

    cust_po_number = Parameter(display_name="Customer PO Number",
                            param_type=None,
                            data_type=String,
                            editable=True,
                            show_on_form=True,
                            values=None
                            )

    @classmethod
    def execute_action(cls):
        print("Executing Action ")
        # print(f"ordered_date          old - {cls.ordered_date.old_value}        new - {cls.ordered_date.new_value}")
        print(f"transactional_curr_code          old - {cls.transactional_curr_code.old_value}        new - {cls.transactional_curr_code.new_value}")
        print(f"org_id   old - {cls.org_id.old_value} new - {cls.org_id.new_value}")
        print(f"cust_po_number         old - {cls.cust_po_number.old_value}       new - {cls.cust_po_number.new_value}")
        print("Completed Execution")
        return {}
