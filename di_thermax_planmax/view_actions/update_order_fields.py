from sqlalchemy import Integer, Select, bindparam, String, Date
from efficieno.components.actions_object import Action, Parameter

from di_thermax_planmax.erd.apps.org_organization_definitions import OrgOrganizationDefinitions
from di_thermax_planmax.erd.inv.mtl_system_items_b import MtlSystemItemsB
from di_thermax_planmax.erd.xxtmx_planmax.xxplanmax_model_xref import XxplanmaxModelXref


class UpdateOrderFields(Action):
    __action_name__ = "Update Order Fields"
    __action_description__ = "Update Order Fields"

    # sales_order_header_id: int,
    # model_line_id: str,
    # order_status: str,
    # project_segment1: str,
    # order_intake_status: str,
    # bom_common_status: str,
    # prn_creation_status: str,
    # curr_cust_required_date: dict = None,
    # curr_thx_commitment_date: dict = None,
    # mfg_organization_code: str = None,
    # std_nstd: str = None,
    # sos_item: str = None,
    # product_model: str = None,
    # ld_applicable: str = None,
    # # manual_order_status: str = None,
    # wip_folder_release_date: dict = None,
    # remarks: str = None,
    # product_category: str = None,
    # rated_standard_man_hrs: str = None, 
    # reason_for_otp: str = None, 
    # prn_applicable: str = None,
    # oc_status: str = None,
    # oc_closure_date: dict = None,
    # plan_eol_mech_date: dict = None,
    # plan_eol_ei_date: dict = None,
    # mfg_commitment_date: dict = None,

    # Non Editable fields 
    sales_order_header_id = Parameter(display_name="sales_order_header_id", param_type=None, data_type=Integer, editable=False, show_on_form=True, values=None)

    model_line_id = Parameter(display_name="model_line_id", param_type=None, data_type=Integer, editable=False, show_on_form=True, values=None)

    order_intake_status = Parameter(display_name="order_intake_status", param_type=None, data_type=String, editable=False, show_on_form=True, values=None)

    bom_common_status = Parameter(display_name="bom_common_status", param_type=None, data_type=String, editable=False, show_on_form=True, values=None)

    prn_creation_status = Parameter(display_name="prn_creation_status", param_type=None, data_type=String, editable=False, show_on_form=True, values=None)
  
    # Editable fields 
    order_status = Parameter(display_name="Order Status", param_type=None, data_type=String, editable=True, show_on_form=True, values=[{"label": "Open",
                                                                                                                                        "value": "OPEN"},
                                                                                                                                       {"label": "Closed",
                                                                                                                                        "value": "CLOSED"},
                                                                                                                                       {"label": "Cancelled",
                                                                                                                                        "value": "CANCELLED"}])
    
    project_segment1 = Parameter(display_name="Project Number",
                                  param_type=None,
                                  data_type=String,
                                  editable=True,
                                  show_on_form=True,
                                  values=Select(OrgOrganizationDefinitions.organization_id.label("value"), OrgOrganizationDefinitions.organization_code.label("label")))

    curr_cust_required_date = Parameter(display_name="Curr Cust Required Date", param_type=None, data_type=Date, editable=True, show_on_form=True, values=None)

    curr_thx_commitment_date = Parameter(display_name="Curr Thx Commitment Date", param_type=None, data_type=Date, editable=True, show_on_form=True, values=None)

    mfg_organization_code = Parameter(display_name="MFG Organization Code",
                                  param_type=None,
                                  data_type=String,
                                  editable=True,
                                  show_on_form=True,
                                  values=Select(OrgOrganizationDefinitions.organization_id.label("value"), OrgOrganizationDefinitions.organization_code.label("label")))


    std_nstd = Parameter(display_name="Standard / Non Standard", param_type=None, data_type=String, editable=True, show_on_form=True, values=[{"label": "Standard",
                                                                                                                                                "value": "STD"},
                                                                                                                                              {"label": "Non Standard",
                                                                                                                                               "value": "NSTD"}])


    sos_item = Parameter(display_name="SOS Item Number",
                            param_type=None,
                            data_type=String,
                            editable=True,
                            show_on_form=True,
                            values=None
                            # values=Select(MtlSystemItemsB.segment1.label("label"), MtlSystemItemsB.segment1.label("value")).filter(MtlSystemItemsB.organization_id == bindparam("mfg_organization_code"))
                            )

  
    # product_model = Parameter(display_name="Product Model", param_type=None, data_type=String, editable=True, show_on_form=True, values=None)
    product_model = Parameter(display_name="Product Model", 
                              param_type=None, 
                              data_type=String, 
                              editable=True, 
                              show_on_form=True, 
                              values=Select(XxplanmaxModelXref.model_number.label('label'), XxplanmaxModelXref.model_number.label('value')))
    
    ld_applicable = Parameter(display_name="LD Applicable", param_type=None, data_type=String, editable=True, show_on_form=True, values=[{"label": "Yes", "value": "Y"},
                                                                                                                                         {"label": "No", "value": "N"}])
    
    wip_folder_release_date = Parameter(display_name="WIP Folder Release Date", param_type=None, data_type=Date, editable=True, show_on_form=True, values=None)
    remarks = Parameter(display_name="Remarks", param_type=None, data_type=String, editable=True, show_on_form=True, values=None)

    product_category = Parameter(display_name="Product Category", param_type=None, data_type=String, editable=True, show_on_form=True, values=None)
    
    rated_standard_man_hrs = Parameter(display_name="RSMH", param_type=None, data_type=String, editable=True, show_on_form=True, values=None)
    reason_for_otp = Parameter(display_name="Reason for OTP", param_type=None, data_type=String, editable=True, show_on_form=True, values=[{"label": "Delay due to Materials", "value": "Delay due to Materials"},
                                                                                                                                            {"label": "Delay due to Engineering", "value": "Delay due to Engineering"},
                                                                                                                                            {"label": "Delay due to Manufacturing", "value": "Delay due to Manufacturing"},
                                                                                                                                            {"label": "Delay due to Stores", "value": "Delay due to Stores"},
                                                                                                                                            {"label": "Change in specs by Customer", "value": "Change in specs by Customer"},
                                                                                                                                            {"label": "Planning input Delay", "value": "Planning input Delay"},
                                                                                                                                            {"label": "QC related Delay", "value": "QC related Delay"},
                                                                                                                                            {"label": "Wrong commitment", "value": "Wrong commitment"},
                                                                                                                                            {"label": "Delay due to technical unclarity", "value": "Delay due to technical unclarity"},
                                                                                                                                            {"label": "IBR related delay", "value": "IBR related delay"},
                                                                                                                                            {"label": "Vendor and Engineering related rework", "value": "Vendor and Engineering related rework"}])
    prn_applicable = Parameter(display_name="PRN Applicable", param_type=None, data_type=String, editable=True, show_on_form=True, values=None)
    oc_status = Parameter(display_name="OC Status", param_type=None, data_type=String, editable=True, show_on_form=True, values=[{"label": "Partial", "value": "P"},
                                                                                                                                {"label": "Open", "value": "O"},
                                                                                                                                {"label": "Closed", "value": "C"}])
    
    oc_closure_date = Parameter(display_name="OC Closure Date", param_type=None, data_type=Date, editable=True, show_on_form=True, values=None)
    plan_eol_mech_date = Parameter(display_name="Planned EOL Mech Date", param_type=None, data_type=Date, editable=True, show_on_form=True, values=None)
    plan_eol_ei_date = Parameter(display_name="Planned EOL EI Date", param_type=None, data_type=Date, editable=True, show_on_form=True, values=None)
    mfg_commitment_date = Parameter(display_name="MFG Commitment Date", param_type=None, data_type=Date, editable=True, show_on_form=True, values=None)
  
    oc_number = Parameter(display_name="OC Number", param_type=None, data_type=Integer, editable=True, show_on_form=True, values=None)

    remarks = Parameter(display_name="Remarks", param_type=None, data_type=String, editable=True, show_on_form=True, values=None)

    @classmethod
    def execute_action(cls):
        print("Executing Action ")
        print(f"sales_order_header_id          old - {cls.sales_order_header_id.old_value}        new - {cls.sales_order_header_id.new_value}")
        print(f"model_line_id          old - {cls.model_line_id.old_value}        new - {cls.model_line_id.new_value}")
        print(f"std_nstd   old - {cls.std_nstd.old_value} new - {cls.std_nstd.new_value}")
        print(f"mfg_organization_code         old - {cls.mfg_organization_code.old_value}       new - {cls.mfg_organization_code.new_value}")
        print("Completed Execution")
        return {}
