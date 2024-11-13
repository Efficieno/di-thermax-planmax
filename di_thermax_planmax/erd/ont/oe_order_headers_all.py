from typing import TYPE_CHECKING

from sqlalchemy import Date, Float, Integer, String
from sqlalchemy.orm import Mapped, mapped_column, relationship

from efficieno.components.erd_objects import ERDBase, ColumnMetadata

if TYPE_CHECKING:
    from ..inv.mtl_system_items_b import MtlSystemItemsB
    from ..apps.org_organization_definitions import OrgOrganizationDefinitions
    from ..wsh.wsh_delivery_details import WshDeliveryDetails
    from ..wsh.wsh_new_deliveries import WshNewDeliveries
    from ..ont.oe_transaction_types_tl import OeTransactionTypesTl
    from ..ont.oe_transaction_types_all import OeTransactionTypesAll
    from ..ont.oe_order_lines_all import OeOrderLinesAll


class OeOrderHeadersAll(ERDBase):
    __data_object_type__ = "data_object"
    __tablename__ = "oe_order_headers_all"
    __table_args__ = {"schema": "ont", "extend_existing": True}
    __table_properties__ = {"ui_x_pos": 1332.42578125, "ui_y_pos": -55.78007888793945, "colour": "#F2F3F5"}

    header_id: Mapped[str] = mapped_column('header_id', Integer, primary_key=True, info={"column_metadata": ColumnMetadata()})
    org_id: Mapped[str] = mapped_column('org_id', Integer, primary_key=False, info={"column_metadata": ColumnMetadata()})
    order_type_id: Mapped[str] = mapped_column('order_type_id', Integer, primary_key=False, info={"column_metadata": ColumnMetadata()})
    order_number: Mapped[str] = mapped_column('order_number', Integer, primary_key=False, info={"column_metadata": ColumnMetadata()})
    version_number: Mapped[str] = mapped_column('version_number', Integer, primary_key=False, info={"column_metadata": ColumnMetadata()})
    expiration_date: Mapped[str] = mapped_column('expiration_date', Date, primary_key=False, info={"column_metadata": ColumnMetadata()})
    order_source_id: Mapped[str] = mapped_column('order_source_id', Integer, primary_key=False, info={"column_metadata": ColumnMetadata()})
    source_document_type_id: Mapped[str] = mapped_column('source_document_type_id', Integer, primary_key=False, info={"column_metadata": ColumnMetadata()})
    orig_sys_document_ref: Mapped[str] = mapped_column('orig_sys_document_ref', String, primary_key=False, info={"column_metadata": ColumnMetadata()})
    source_document_id: Mapped[str] = mapped_column('source_document_id', Integer, primary_key=False, info={"column_metadata": ColumnMetadata()})
    ordered_date: Mapped[str] = mapped_column('ordered_date', Date, primary_key=False, info={"column_metadata": ColumnMetadata()})
    request_date: Mapped[str] = mapped_column('request_date', Date, primary_key=False, info={"column_metadata": ColumnMetadata()})
    pricing_date: Mapped[str] = mapped_column('pricing_date', Date, primary_key=False, info={"column_metadata": ColumnMetadata()})
    shipment_priority_code: Mapped[str] = mapped_column('shipment_priority_code', String, primary_key=False, info={"column_metadata": ColumnMetadata()})
    demand_class_code: Mapped[str] = mapped_column('demand_class_code', String, primary_key=False, info={"column_metadata": ColumnMetadata()})
    price_list_id: Mapped[str] = mapped_column('price_list_id', Integer, primary_key=False, info={"column_metadata": ColumnMetadata()})
    tax_exempt_flag: Mapped[str] = mapped_column('tax_exempt_flag', String, primary_key=False, info={"column_metadata": ColumnMetadata()})
    tax_exempt_number: Mapped[str] = mapped_column('tax_exempt_number', String, primary_key=False, info={"column_metadata": ColumnMetadata()})
    tax_exempt_reason_code: Mapped[str] = mapped_column('tax_exempt_reason_code', String, primary_key=False, info={"column_metadata": ColumnMetadata()})
    conversion_rate: Mapped[str] = mapped_column('conversion_rate', Integer, primary_key=False, info={"column_metadata": ColumnMetadata()})
    conversion_type_code: Mapped[str] = mapped_column('conversion_type_code', String, primary_key=False, info={"column_metadata": ColumnMetadata()})
    conversion_rate_date: Mapped[str] = mapped_column('conversion_rate_date', Date, primary_key=False, info={"column_metadata": ColumnMetadata()})
    partial_shipments_allowed: Mapped[str] = mapped_column('partial_shipments_allowed', String, primary_key=False, info={"column_metadata": ColumnMetadata()})
    ship_tolerance_above: Mapped[str] = mapped_column('ship_tolerance_above', Integer, primary_key=False, info={"column_metadata": ColumnMetadata()})
    ship_tolerance_below: Mapped[str] = mapped_column('ship_tolerance_below', Integer, primary_key=False, info={"column_metadata": ColumnMetadata()})
    transactional_curr_code: Mapped[str] = mapped_column('transactional_curr_code', String, primary_key=False, info={"column_metadata": ColumnMetadata()})
    agreement_id: Mapped[str] = mapped_column('agreement_id', Integer, primary_key=False, info={"column_metadata": ColumnMetadata()})
    tax_point_code: Mapped[str] = mapped_column('tax_point_code', String, primary_key=False, info={"column_metadata": ColumnMetadata()})
    cust_po_number: Mapped[str] = mapped_column('cust_po_number', String, primary_key=False, info={"column_metadata": ColumnMetadata()})
    invoicing_rule_id: Mapped[str] = mapped_column('invoicing_rule_id', Integer, primary_key=False, info={"column_metadata": ColumnMetadata()})
    accounting_rule_id: Mapped[str] = mapped_column('accounting_rule_id', Integer, primary_key=False, info={"column_metadata": ColumnMetadata()})
    payment_term_id: Mapped[str] = mapped_column('payment_term_id', Integer, primary_key=False, info={"column_metadata": ColumnMetadata()})
    shipping_method_code: Mapped[str] = mapped_column('shipping_method_code', String, primary_key=False, info={"column_metadata": ColumnMetadata()})
    freight_carrier_code: Mapped[str] = mapped_column('freight_carrier_code', String, primary_key=False, info={"column_metadata": ColumnMetadata()})
    fob_point_code: Mapped[str] = mapped_column('fob_point_code', String, primary_key=False, info={"column_metadata": ColumnMetadata()})
    freight_terms_code: Mapped[str] = mapped_column('freight_terms_code', String, primary_key=False, info={"column_metadata": ColumnMetadata()})
    sold_from_org_id: Mapped[str] = mapped_column('sold_from_org_id', Integer, primary_key=False, info={"column_metadata": ColumnMetadata()})
    sold_to_org_id: Mapped[str] = mapped_column('sold_to_org_id', Integer, primary_key=False, info={"column_metadata": ColumnMetadata()})
    ship_from_org_id: Mapped[str] = mapped_column('ship_from_org_id', Integer, primary_key=False, info={"column_metadata": ColumnMetadata()})
    ship_to_org_id: Mapped[str] = mapped_column('ship_to_org_id', Integer, primary_key=False, info={"column_metadata": ColumnMetadata()})
    invoice_to_org_id: Mapped[str] = mapped_column('invoice_to_org_id', Integer, primary_key=False, info={"column_metadata": ColumnMetadata()})
    deliver_to_org_id: Mapped[str] = mapped_column('deliver_to_org_id', Integer, primary_key=False, info={"column_metadata": ColumnMetadata()})
    sold_to_contact_id: Mapped[str] = mapped_column('sold_to_contact_id', Integer, primary_key=False, info={"column_metadata": ColumnMetadata()})
    ship_to_contact_id: Mapped[str] = mapped_column('ship_to_contact_id', Integer, primary_key=False, info={"column_metadata": ColumnMetadata()})
    invoice_to_contact_id: Mapped[str] = mapped_column('invoice_to_contact_id', Integer, primary_key=False, info={"column_metadata": ColumnMetadata()})
    deliver_to_contact_id: Mapped[str] = mapped_column('deliver_to_contact_id', Integer, primary_key=False, info={"column_metadata": ColumnMetadata()})
    creation_date: Mapped[str] = mapped_column('creation_date', Date, primary_key=False, info={"column_metadata": ColumnMetadata()})
    created_by: Mapped[str] = mapped_column('created_by', Integer, primary_key=False, info={"column_metadata": ColumnMetadata()})
    last_updated_by: Mapped[str] = mapped_column('last_updated_by', Integer, primary_key=False, info={"column_metadata": ColumnMetadata()})
    last_update_date: Mapped[str] = mapped_column('last_update_date', Date, primary_key=False, info={"column_metadata": ColumnMetadata()})
    last_update_login: Mapped[str] = mapped_column('last_update_login', Integer, primary_key=False, info={"column_metadata": ColumnMetadata()})
    program_application_id: Mapped[str] = mapped_column('program_application_id', Integer, primary_key=False, info={"column_metadata": ColumnMetadata()})
    program_id: Mapped[str] = mapped_column('program_id', Integer, primary_key=False, info={"column_metadata": ColumnMetadata()})
    program_update_date: Mapped[str] = mapped_column('program_update_date', Date, primary_key=False, info={"column_metadata": ColumnMetadata()})
    request_id: Mapped[str] = mapped_column('request_id', Integer, primary_key=False, info={"column_metadata": ColumnMetadata()})
    context: Mapped[str] = mapped_column('context', String, primary_key=False, info={"column_metadata": ColumnMetadata()})
    attribute1: Mapped[str] = mapped_column('attribute1', String, primary_key=False, info={"column_metadata": ColumnMetadata()})
    attribute2: Mapped[str] = mapped_column('attribute2', String, primary_key=False, info={"column_metadata": ColumnMetadata()})
    attribute3: Mapped[str] = mapped_column('attribute3', String, primary_key=False, info={"column_metadata": ColumnMetadata()})
    attribute4: Mapped[str] = mapped_column('attribute4', String, primary_key=False, info={"column_metadata": ColumnMetadata()})
    attribute5: Mapped[str] = mapped_column('attribute5', String, primary_key=False, info={"column_metadata": ColumnMetadata()})
    attribute6: Mapped[str] = mapped_column('attribute6', String, primary_key=False, info={"column_metadata": ColumnMetadata()})
    attribute7: Mapped[str] = mapped_column('attribute7', String, primary_key=False, info={"column_metadata": ColumnMetadata()})
    attribute8: Mapped[str] = mapped_column('attribute8', String, primary_key=False, info={"column_metadata": ColumnMetadata()})
    attribute9: Mapped[str] = mapped_column('attribute9', String, primary_key=False, info={"column_metadata": ColumnMetadata()})
    attribute10: Mapped[str] = mapped_column('attribute10', String, primary_key=False, info={"column_metadata": ColumnMetadata()})
    attribute11: Mapped[str] = mapped_column('attribute11', String, primary_key=False, info={"column_metadata": ColumnMetadata()})
    attribute12: Mapped[str] = mapped_column('attribute12', String, primary_key=False, info={"column_metadata": ColumnMetadata()})
    attribute13: Mapped[str] = mapped_column('attribute13', String, primary_key=False, info={"column_metadata": ColumnMetadata()})
    attribute14: Mapped[str] = mapped_column('attribute14', String, primary_key=False, info={"column_metadata": ColumnMetadata()})
    attribute15: Mapped[str] = mapped_column('attribute15', String, primary_key=False, info={"column_metadata": ColumnMetadata()})
    global_attribute_category: Mapped[str] = mapped_column('global_attribute_category', String, primary_key=False, info={"column_metadata": ColumnMetadata()})
    global_attribute1: Mapped[str] = mapped_column('global_attribute1', String, primary_key=False, info={"column_metadata": ColumnMetadata()})
    global_attribute2: Mapped[str] = mapped_column('global_attribute2', String, primary_key=False, info={"column_metadata": ColumnMetadata()})
    global_attribute3: Mapped[str] = mapped_column('global_attribute3', String, primary_key=False, info={"column_metadata": ColumnMetadata()})
    global_attribute4: Mapped[str] = mapped_column('global_attribute4', String, primary_key=False, info={"column_metadata": ColumnMetadata()})
    global_attribute5: Mapped[str] = mapped_column('global_attribute5', String, primary_key=False, info={"column_metadata": ColumnMetadata()})
    global_attribute6: Mapped[str] = mapped_column('global_attribute6', String, primary_key=False, info={"column_metadata": ColumnMetadata()})
    global_attribute7: Mapped[str] = mapped_column('global_attribute7', String, primary_key=False, info={"column_metadata": ColumnMetadata()})
    global_attribute8: Mapped[str] = mapped_column('global_attribute8', String, primary_key=False, info={"column_metadata": ColumnMetadata()})
    global_attribute9: Mapped[str] = mapped_column('global_attribute9', String, primary_key=False, info={"column_metadata": ColumnMetadata()})
    global_attribute10: Mapped[str] = mapped_column('global_attribute10', String, primary_key=False, info={"column_metadata": ColumnMetadata()})
    global_attribute11: Mapped[str] = mapped_column('global_attribute11', String, primary_key=False, info={"column_metadata": ColumnMetadata()})
    global_attribute12: Mapped[str] = mapped_column('global_attribute12', String, primary_key=False, info={"column_metadata": ColumnMetadata()})
    global_attribute13: Mapped[str] = mapped_column('global_attribute13', String, primary_key=False, info={"column_metadata": ColumnMetadata()})
    global_attribute14: Mapped[str] = mapped_column('global_attribute14', String, primary_key=False, info={"column_metadata": ColumnMetadata()})
    global_attribute15: Mapped[str] = mapped_column('global_attribute15', String, primary_key=False, info={"column_metadata": ColumnMetadata()})
    global_attribute16: Mapped[str] = mapped_column('global_attribute16', String, primary_key=False, info={"column_metadata": ColumnMetadata()})
    global_attribute17: Mapped[str] = mapped_column('global_attribute17', String, primary_key=False, info={"column_metadata": ColumnMetadata()})
    global_attribute18: Mapped[str] = mapped_column('global_attribute18', String, primary_key=False, info={"column_metadata": ColumnMetadata()})
    global_attribute19: Mapped[str] = mapped_column('global_attribute19', String, primary_key=False, info={"column_metadata": ColumnMetadata()})
    global_attribute20: Mapped[str] = mapped_column('global_attribute20', String, primary_key=False, info={"column_metadata": ColumnMetadata()})
    cancelled_flag: Mapped[str] = mapped_column('cancelled_flag', String, primary_key=False, info={"column_metadata": ColumnMetadata()})
    open_flag: Mapped[str] = mapped_column('open_flag', String, primary_key=False, info={"column_metadata": ColumnMetadata()})
    booked_flag: Mapped[str] = mapped_column('booked_flag', String, primary_key=False, info={"column_metadata": ColumnMetadata()})
    salesrep_id: Mapped[str] = mapped_column('salesrep_id', Integer, primary_key=False, info={"column_metadata": ColumnMetadata()})
    return_reason_code: Mapped[str] = mapped_column('return_reason_code', String, primary_key=False, info={"column_metadata": ColumnMetadata()})
    order_date_type_code: Mapped[str] = mapped_column('order_date_type_code', String, primary_key=False, info={"column_metadata": ColumnMetadata()})
    earliest_schedule_limit: Mapped[str] = mapped_column('earliest_schedule_limit', Integer, primary_key=False, info={"column_metadata": ColumnMetadata()})
    latest_schedule_limit: Mapped[str] = mapped_column('latest_schedule_limit', Integer, primary_key=False, info={"column_metadata": ColumnMetadata()})
    payment_type_code: Mapped[str] = mapped_column('payment_type_code', String, primary_key=False, info={"column_metadata": ColumnMetadata()})
    payment_amount: Mapped[str] = mapped_column('payment_amount', Integer, primary_key=False, info={"column_metadata": ColumnMetadata()})
    check_number: Mapped[str] = mapped_column('check_number', String, primary_key=False, info={"column_metadata": ColumnMetadata()})
    credit_card_code: Mapped[str] = mapped_column('credit_card_code', String, primary_key=False, info={"column_metadata": ColumnMetadata()})
    credit_card_holder_name: Mapped[str] = mapped_column('credit_card_holder_name', String, primary_key=False, info={"column_metadata": ColumnMetadata()})
    credit_card_number: Mapped[str] = mapped_column('credit_card_number', String, primary_key=False, info={"column_metadata": ColumnMetadata()})
    credit_card_expiration_date: Mapped[str] = mapped_column('credit_card_expiration_date', Date, primary_key=False, info={"column_metadata": ColumnMetadata()})
    credit_card_approval_code: Mapped[str] = mapped_column('credit_card_approval_code', String, primary_key=False, info={"column_metadata": ColumnMetadata()})
    sales_channel_code: Mapped[str] = mapped_column('sales_channel_code', String, primary_key=False, info={"column_metadata": ColumnMetadata()})
    first_ack_code: Mapped[str] = mapped_column('first_ack_code', String, primary_key=False, info={"column_metadata": ColumnMetadata()})
    first_ack_date: Mapped[str] = mapped_column('first_ack_date', Date, primary_key=False, info={"column_metadata": ColumnMetadata()})
    last_ack_code: Mapped[str] = mapped_column('last_ack_code', String, primary_key=False, info={"column_metadata": ColumnMetadata()})
    last_ack_date: Mapped[str] = mapped_column('last_ack_date', Date, primary_key=False, info={"column_metadata": ColumnMetadata()})
    order_category_code: Mapped[str] = mapped_column('order_category_code', String, primary_key=False, info={"column_metadata": ColumnMetadata()})
    change_sequence: Mapped[str] = mapped_column('change_sequence', String, primary_key=False, info={"column_metadata": ColumnMetadata()})
    drop_ship_flag: Mapped[str] = mapped_column('drop_ship_flag', String, primary_key=False, info={"column_metadata": ColumnMetadata()})
    customer_payment_term_id: Mapped[str] = mapped_column('customer_payment_term_id', Integer, primary_key=False, info={"column_metadata": ColumnMetadata()})
    shipping_instructions: Mapped[str] = mapped_column('shipping_instructions', String, primary_key=False, info={"column_metadata": ColumnMetadata()})
    packing_instructions: Mapped[str] = mapped_column('packing_instructions', String, primary_key=False, info={"column_metadata": ColumnMetadata()})
    tp_context: Mapped[str] = mapped_column('tp_context', String, primary_key=False, info={"column_metadata": ColumnMetadata()})
    tp_attribute1: Mapped[str] = mapped_column('tp_attribute1', String, primary_key=False, info={"column_metadata": ColumnMetadata()})
    tp_attribute2: Mapped[str] = mapped_column('tp_attribute2', String, primary_key=False, info={"column_metadata": ColumnMetadata()})
    tp_attribute3: Mapped[str] = mapped_column('tp_attribute3', String, primary_key=False, info={"column_metadata": ColumnMetadata()})
    tp_attribute4: Mapped[str] = mapped_column('tp_attribute4', String, primary_key=False, info={"column_metadata": ColumnMetadata()})
    tp_attribute5: Mapped[str] = mapped_column('tp_attribute5', String, primary_key=False, info={"column_metadata": ColumnMetadata()})
    tp_attribute6: Mapped[str] = mapped_column('tp_attribute6', String, primary_key=False, info={"column_metadata": ColumnMetadata()})
    tp_attribute7: Mapped[str] = mapped_column('tp_attribute7', String, primary_key=False, info={"column_metadata": ColumnMetadata()})
    tp_attribute8: Mapped[str] = mapped_column('tp_attribute8', String, primary_key=False, info={"column_metadata": ColumnMetadata()})
    tp_attribute9: Mapped[str] = mapped_column('tp_attribute9', String, primary_key=False, info={"column_metadata": ColumnMetadata()})
    tp_attribute10: Mapped[str] = mapped_column('tp_attribute10', String, primary_key=False, info={"column_metadata": ColumnMetadata()})
    tp_attribute11: Mapped[str] = mapped_column('tp_attribute11', String, primary_key=False, info={"column_metadata": ColumnMetadata()})
    tp_attribute12: Mapped[str] = mapped_column('tp_attribute12', String, primary_key=False, info={"column_metadata": ColumnMetadata()})
    tp_attribute13: Mapped[str] = mapped_column('tp_attribute13', String, primary_key=False, info={"column_metadata": ColumnMetadata()})
    tp_attribute14: Mapped[str] = mapped_column('tp_attribute14', String, primary_key=False, info={"column_metadata": ColumnMetadata()})
    tp_attribute15: Mapped[str] = mapped_column('tp_attribute15', String, primary_key=False, info={"column_metadata": ColumnMetadata()})
    flow_status_code: Mapped[str] = mapped_column('flow_status_code', String, primary_key=False, info={"column_metadata": ColumnMetadata()})
    marketing_source_code_id: Mapped[str] = mapped_column('marketing_source_code_id', Integer, primary_key=False, info={"column_metadata": ColumnMetadata()})
    credit_card_approval_date: Mapped[str] = mapped_column('credit_card_approval_date', Date, primary_key=False, info={"column_metadata": ColumnMetadata()})
    upgraded_flag: Mapped[str] = mapped_column('upgraded_flag', String, primary_key=False, info={"column_metadata": ColumnMetadata()})
    customer_preference_set_code: Mapped[str] = mapped_column('customer_preference_set_code', String, primary_key=False, info={"column_metadata": ColumnMetadata()})
    booked_date: Mapped[str] = mapped_column('booked_date', Date, primary_key=False, info={"column_metadata": ColumnMetadata()})
    lock_control: Mapped[str] = mapped_column('lock_control', Integer, primary_key=False, info={"column_metadata": ColumnMetadata()})
    price_request_code: Mapped[str] = mapped_column('price_request_code', String, primary_key=False, info={"column_metadata": ColumnMetadata()})
    batch_id: Mapped[str] = mapped_column('batch_id', Integer, primary_key=False, info={"column_metadata": ColumnMetadata()})
    xml_message_id: Mapped[str] = mapped_column('xml_message_id', Integer, primary_key=False, info={"column_metadata": ColumnMetadata()})
    accounting_rule_duration: Mapped[str] = mapped_column('accounting_rule_duration', Integer, primary_key=False, info={"column_metadata": ColumnMetadata()})
    attribute16: Mapped[str] = mapped_column('attribute16', String, primary_key=False, info={"column_metadata": ColumnMetadata()})
    attribute17: Mapped[str] = mapped_column('attribute17', String, primary_key=False, info={"column_metadata": ColumnMetadata()})
    attribute18: Mapped[str] = mapped_column('attribute18', String, primary_key=False, info={"column_metadata": ColumnMetadata()})
    attribute19: Mapped[str] = mapped_column('attribute19', String, primary_key=False, info={"column_metadata": ColumnMetadata()})
    attribute20: Mapped[str] = mapped_column('attribute20', String, primary_key=False, info={"column_metadata": ColumnMetadata()})
    blanket_number: Mapped[str] = mapped_column('blanket_number', Integer, primary_key=False, info={"column_metadata": ColumnMetadata()})
    sales_document_type_code: Mapped[str] = mapped_column('sales_document_type_code', String, primary_key=False, info={"column_metadata": ColumnMetadata()})
    sold_to_phone_id: Mapped[str] = mapped_column('sold_to_phone_id', Integer, primary_key=False, info={"column_metadata": ColumnMetadata()})
    fulfillment_set_name: Mapped[str] = mapped_column('fulfillment_set_name', String, primary_key=False, info={"column_metadata": ColumnMetadata()})
    line_set_name: Mapped[str] = mapped_column('line_set_name', String, primary_key=False, info={"column_metadata": ColumnMetadata()})
    default_fulfillment_set: Mapped[str] = mapped_column('default_fulfillment_set', String, primary_key=False, info={"column_metadata": ColumnMetadata()})
    transaction_phase_code: Mapped[str] = mapped_column('transaction_phase_code', String, primary_key=False, info={"column_metadata": ColumnMetadata()})
    sales_document_name: Mapped[str] = mapped_column('sales_document_name', String, primary_key=False, info={"column_metadata": ColumnMetadata()})
    quote_number: Mapped[str] = mapped_column('quote_number', Integer, primary_key=False, info={"column_metadata": ColumnMetadata()})
    quote_date: Mapped[str] = mapped_column('quote_date', Date, primary_key=False, info={"column_metadata": ColumnMetadata()})
    user_status_code: Mapped[str] = mapped_column('user_status_code', String, primary_key=False, info={"column_metadata": ColumnMetadata()})
    draft_submitted_flag: Mapped[str] = mapped_column('draft_submitted_flag', String, primary_key=False, info={"column_metadata": ColumnMetadata()})
    source_document_version_number: Mapped[str] = mapped_column('source_document_version_number', Integer, primary_key=False, info={"column_metadata": ColumnMetadata()})
    sold_to_site_use_id: Mapped[str] = mapped_column('sold_to_site_use_id', Integer, primary_key=False, info={"column_metadata": ColumnMetadata()})
    supplier_signature: Mapped[str] = mapped_column('supplier_signature', String, primary_key=False, info={"column_metadata": ColumnMetadata()})
    supplier_signature_date: Mapped[str] = mapped_column('supplier_signature_date', Date, primary_key=False, info={"column_metadata": ColumnMetadata()})
    customer_signature: Mapped[str] = mapped_column('customer_signature', String, primary_key=False, info={"column_metadata": ColumnMetadata()})
    customer_signature_date: Mapped[str] = mapped_column('customer_signature_date', Date, primary_key=False, info={"column_metadata": ColumnMetadata()})
    minisite_id: Mapped[str] = mapped_column('minisite_id', Integer, primary_key=False, info={"column_metadata": ColumnMetadata()})
    end_customer_id: Mapped[str] = mapped_column('end_customer_id', Integer, primary_key=False, info={"column_metadata": ColumnMetadata()})
    end_customer_contact_id: Mapped[str] = mapped_column('end_customer_contact_id', Integer, primary_key=False, info={"column_metadata": ColumnMetadata()})
    end_customer_site_use_id: Mapped[str] = mapped_column('end_customer_site_use_id', Integer, primary_key=False, info={"column_metadata": ColumnMetadata()})
    ib_owner: Mapped[str] = mapped_column('ib_owner', String, primary_key=False, info={"column_metadata": ColumnMetadata()})
    order_firmed_date: Mapped[str] = mapped_column('order_firmed_date', Date, primary_key=False, info={"column_metadata": ColumnMetadata()})
    inst_id: Mapped[str] = mapped_column('inst_id', Integer, primary_key=False, info={"column_metadata": ColumnMetadata()})
    csr_user_id: Mapped[str] = mapped_column('csr_user_id', Integer, primary_key=False, info={"column_metadata": ColumnMetadata()})
    cancel_unshipped_lines: Mapped[str] = mapped_column('cancel_unshipped_lines', String, primary_key=False, info={"column_metadata": ColumnMetadata()})

        

    

    MtlSystemItemsB_organization_id: Mapped["MtlSystemItemsB"] = relationship(back_populates="OeOrderHeadersAll_ship_from_org_id", primaryjoin="MtlSystemItemsB.organization_id==OeOrderHeadersAll.ship_from_org_id", foreign_keys="[MtlSystemItemsB.organization_id]", viewonly=True)
        

    

    OrgOrganizationDefinitions_organization_id: Mapped["OrgOrganizationDefinitions"] = relationship(back_populates="OeOrderHeadersAll_ship_from_org_id", primaryjoin="OrgOrganizationDefinitions.organization_id==OeOrderHeadersAll.ship_from_org_id", foreign_keys="[OrgOrganizationDefinitions.organization_id]", viewonly=True)
        

    

    WshDeliveryDetails_source_header_id: Mapped["WshDeliveryDetails"] = relationship(back_populates="OeOrderHeadersAll_header_id", primaryjoin="WshDeliveryDetails.source_header_id==OeOrderHeadersAll.header_id", foreign_keys="[OeOrderHeadersAll.header_id]", viewonly=True)
        

    

    WshNewDeliveries_source_header_id: Mapped["WshNewDeliveries"] = relationship(back_populates="OeOrderHeadersAll_header_id", primaryjoin="WshNewDeliveries.source_header_id==OeOrderHeadersAll.header_id", foreign_keys="[OeOrderHeadersAll.header_id]", viewonly=True)
        

    

    OeTransactionTypesTl_transaction_type_id: Mapped["OeTransactionTypesTl"] = relationship(back_populates="OeOrderHeadersAll_order_type_id", primaryjoin="OeTransactionTypesTl.transaction_type_id==OeOrderHeadersAll.order_type_id", foreign_keys="[OeTransactionTypesTl.transaction_type_id]", viewonly=True)
        

    

    OeTransactionTypesAll_transaction_type_id: Mapped["OeTransactionTypesAll"] = relationship(back_populates="OeOrderHeadersAll_order_type_id", primaryjoin="OeTransactionTypesAll.transaction_type_id==OeOrderHeadersAll.order_type_id", foreign_keys="[OeTransactionTypesAll.transaction_type_id]", viewonly=True)
        

    

    OeOrderLinesAll_header_id: Mapped["OeOrderLinesAll"] = relationship(back_populates="OeOrderHeadersAll_header_id", primaryjoin="OeOrderLinesAll.header_id==OeOrderHeadersAll.header_id", foreign_keys="[OeOrderLinesAll.header_id]", viewonly=True)



