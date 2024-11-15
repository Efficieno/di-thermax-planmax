from sqlalchemy import Integer, Select, bindparam, String, Date
from efficieno.components.actions_object import Action, Parameter

from di_thermax_planmax.erd.apps.org_organization_definitions import OrgOrganizationDefinitions
from di_thermax_planmax.erd.inv.mtl_system_items_b import MtlSystemItemsB


class UpdateOrderIntake(Action):
    __action_name__ = "Update Order Intake Fields"
    __action_description__ = "Update Order Intake Fields"

            curr_cust_required_date: dict = None,
            curr_thx_commitment_date: dict = None,

    sales_order_header_id = Parameter(display_name="sales_order_header_id", param_type=None, data_type=Integer, editable=False, show_on_form=True, values=None)

    model_line_id = Parameter(display_name="model_line_id", param_type=None, data_type=Integer, editable=False, show_on_form=True, values=None)


    std_nstd = Parameter(display_name="Standard / Non Standard", param_type=None, data_type=String, editable=True, show_on_form=True, values=[{"label": "Standard",
                                                                                                                                                "value": "STD"},
                                                                                                                                              {"label": "Non Standard",
                                                                                                                                               "value": "NSTD"}])

    mfg_organization_code = Parameter(display_name="MFG Organization Code",
                                  param_type=None,
                                  data_type=String,
                                  editable=True,
                                  show_on_form=True,
                                  values=Select(OrgOrganizationDefinitions.organization_id.label("value"), OrgOrganizationDefinitions.organization_code.label("label")))

    sos_item = Parameter(display_name="SOS Item Number",
                            param_type=None,
                            data_type=String,
                            editable=True,
                            show_on_form=True,
                            values=Select(MtlSystemItemsB.segment1.label("label"), MtlSystemItemsB.segment1.label("value")).filter(MtlSystemItemsB.organization_id == bindparam("mfg_organization_code"))
                            )
    oc_number = Parameter(display_name="OC Number", param_type=None, data_type=Integer, editable=True, show_on_form=True, values=None)

    remarks = Parameter(display_name="Remarks", param_type=None, data_type=String, editable=True, show_on_form=True, values=None)

    curr_cust_required_date = Parameter(display_name="Curr Cust Required Date", param_type=None, data_type=Date, editable=True, show_on_form=True, values=None)

    curr_thx_commitment_date = Parameter(display_name="Curr Thx Commitment Date", param_type=None, data_type=Date, editable=True, show_on_form=True, values=None)


    @classmethod
    def execute_action(cls):
        print("Executing Action ")
        print(f"sales_order_header_id          old - {cls.sales_order_header_id.old_value}        new - {cls.sales_order_header_id.new_value}")
        print(f"model_line_id          old - {cls.model_line_id.old_value}        new - {cls.model_line_id.new_value}")
        print(f"std_nstd   old - {cls.std_nstd.old_value} new - {cls.std_nstd.new_value}")
        print(f"mfg_organization_code         old - {cls.mfg_organization_code.old_value}       new - {cls.mfg_organization_code.new_value}")
        print("Completed Execution")
        return {}
