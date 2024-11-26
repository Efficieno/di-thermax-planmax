from sqlalchemy import Integer, Select, bindparam, String, Date
from efficieno.components.actions_object import Action, Parameter

from di_thermax_planmax.erd.apps.org_organization_definitions import OrgOrganizationDefinitions
from di_thermax_planmax.erd.inv.mtl_system_items_b import MtlSystemItemsB
from di_thermax_planmax.erd.xxtmx_planmax.xxplanmax_header_dtls import XxplanmaxHeaderDtls


class UpdateOrderIntake(Action):
    __action_name__ = "Update Order Intake Fields"
    __action_description__ = "Update Order Intake Fields"

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

        if cls.std_nstd.current_value == 'STD':
            v_ocl_required = 'N'
        else:
            v_ocl_required = 'Y'
        
        subQuery = Select(OrgOrganizationDefinitions.organization_id).filter(OrgOrganizationDefinitions.organization_code == cls.mfg_organization_code.current_value).scalar_subquery()
        update_sql = (Update(XxplanmaxHeaderDtls)
                      .where(and_(XxplanmaxHeaderDtls.sales_order_header_id == cls.sales_order_header_id.current_value, XxplanmaxHeaderDtls.model_line_id == cls.model_line_id.current_value))
                      .values(mfg_organization_code = cls.mfg_organization_code.current_value, 
                      std_nstd=cls.std_nstd.current_value, 
                      sos_item=cls.sos_item.current_value, 
                      oc_no=cls.oc_number.current_value,
                      mfg_organization_id = subQuery,
                      oc_required=v_ocl_required,
                      curr_cust_required_date=cls.curr_cust_required_date.current_value,
                      curr_thx_commitment_date=cls.curr_thx_commitment_date.current_value,
                      remarks=cls.remarks.current_value))

        print(f"Executing Statement {update_sql}")
        print("Completed Execution")
        return {}
