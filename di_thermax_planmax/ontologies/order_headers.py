from typing import TYPE_CHECKING

from sqlalchemy import Date, Float, Integer, String, Numeric, DateTime, join
from sqlalchemy.orm import Mapped, mapped_column, relationship, column_property
from efficieno.components.erd_objects import ERDBase, ColumnMetadata
from di_thermax_planmax.erd.ont.oe_order_headers_all import OeOrderHeadersAll
from di_thermax_planmax.erd.apps.org_organization_definitions import OrgOrganizationDefinitions


class OrderHeaders(ERDBase):
    __table__ = join(OeOrderHeadersAll, OrgOrganizationDefinitions, OeOrderHeadersAll.OrgOrganizationDefinitions_organization_id.expression)
    __table_properties__ = {"ui_x_pos": 503.13734483912555, "ui_y_pos": 891.5731584714746, "colour": "#F2F3F5"}

    header_id = column_property(OeOrderHeadersAll.header_id)
    organization_code = column_property(OrgOrganizationDefinitions.organization_code)
    org_id = column_property(OeOrderHeadersAll.org_id)
    order_type_id = column_property(OeOrderHeadersAll.order_type_id)
    order_number = column_property(OeOrderHeadersAll.order_number)
    version_number = column_property(OeOrderHeadersAll.version_number)
    ordered_date = column_property(OeOrderHeadersAll.ordered_date)
    request_date = column_property(OeOrderHeadersAll.request_date)
    pricing_date = column_property(OeOrderHeadersAll.pricing_date)
    shipment_priority_code = column_property(OeOrderHeadersAll.shipment_priority_code)
    demand_class_code = column_property(OeOrderHeadersAll.demand_class_code)
    price_list_id = column_property(OeOrderHeadersAll.price_list_id)
    tax_exempt_flag = column_property(OeOrderHeadersAll.tax_exempt_flag)
    tax_exempt_number = column_property(OeOrderHeadersAll.tax_exempt_number)
    tax_exempt_reason_code = column_property(OeOrderHeadersAll.tax_exempt_reason_code)
    conversion_rate = column_property(OeOrderHeadersAll.conversion_rate)
    conversion_type_code = column_property(OeOrderHeadersAll.conversion_type_code)
    conversion_rate_date = column_property(OeOrderHeadersAll.conversion_rate_date)
    partial_shipments_allowed = column_property(OeOrderHeadersAll.partial_shipments_allowed)
    ship_tolerance_above = column_property(OeOrderHeadersAll.ship_tolerance_above)
    ship_tolerance_below = column_property(OeOrderHeadersAll.ship_tolerance_below)
    transactional_curr_code = column_property(OeOrderHeadersAll.transactional_curr_code)
    agreement_id = column_property(OeOrderHeadersAll.agreement_id)
    tax_point_code = column_property(OeOrderHeadersAll.tax_point_code)
    cust_po_number = column_property(OeOrderHeadersAll.cust_po_number)
    shipping_method_code = column_property(OeOrderHeadersAll.shipping_method_code)
    freight_carrier_code = column_property(OeOrderHeadersAll.freight_carrier_code)
    fob_point_code = column_property(OeOrderHeadersAll.fob_point_code)
    freight_terms_code = column_property(OeOrderHeadersAll.freight_terms_code)
    cancelled_flag = column_property(OeOrderHeadersAll.cancelled_flag)
    open_flag = column_property(OeOrderHeadersAll.open_flag)
    booked_flag = column_property(OeOrderHeadersAll.booked_flag)
    transaction_phase_code = column_property(OeOrderHeadersAll.transaction_phase_code)
    ship_from_org_id = column_property(OeOrderHeadersAll.ship_from_org_id, OrgOrganizationDefinitions.organization_id)
    flow_status_code = column_property(OeOrderHeadersAll.flow_status_code)


