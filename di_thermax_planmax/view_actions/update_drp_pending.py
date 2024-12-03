from sqlalchemy import Integer, Select, bindparam, String, Date, Update, and_, func
from efficieno.components.actions_object import Action, Parameter
from efficieno.data_sources.data_sources import DataSource

from di_thermax_planmax.erd.apps.org_organization_definitions import OrgOrganizationDefinitions
from di_thermax_planmax.erd.inv.mtl_system_items_b import MtlSystemItemsB
from di_thermax_planmax.erd.xxtmx_planmax.xxplanmax_header_dtls import XxplanmaxHeaderDtls


class UpdateDRPPendingStatus(Action):
    __action_name__ = "Update DRP Pending"
    __action_description__ = "Update DRP Pending Status"

    sales_order_header_id = Parameter(display_name="sales_order_header_id", param_type=None, data_type=Integer, editable=False, show_on_form=False, values=None)

    model_line_id = Parameter(display_name="model_line_id", param_type=None, data_type=Integer, editable=False, show_on_form=False, values=None)

    mat_planning_status = Parameter(display_name="DRP Pending", param_type=None, data_type=String, editable=True, show_on_form=True, values=[{"label": "Completed",
                                                                                                                                              "value": "C"}])

    @classmethod
    def execute_action(cls):
        print("Executing Action ")

        # subQuery = Select(OrgOrganizationDefinitions.organization_id).filter(OrgOrganizationDefinitions.organization_code == cls.mfg_organization_code.current_value).scalar_subquery()
        update_sql = (Update(XxplanmaxHeaderDtls)
                      .where(and_(XxplanmaxHeaderDtls.sales_order_header_id == cls.sales_order_header_id.current_value, XxplanmaxHeaderDtls.model_line_id == cls.model_line_id.current_value))
                      .values(mat_planning_status = cls.mat_planning_status.current_value))

        print(f"Executing Statement {update_sql}")
        data_source = DataSource()
        result = data_source.execute_update(update_sql)
        print(f"Completed Execution {result}")
        return {}
