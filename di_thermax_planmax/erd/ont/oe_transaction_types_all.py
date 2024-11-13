from typing import TYPE_CHECKING

from sqlalchemy import Date, Float, Integer, String
from sqlalchemy.orm import Mapped, mapped_column, relationship

from efficieno.components.erd_objects import ERDBase, ColumnMetadata

if TYPE_CHECKING:
    from ..ont.oe_order_headers_all import OeOrderHeadersAll


class OeTransactionTypesAll(ERDBase):
    __data_object_type__ = "data_object"
    __tablename__ = "oe_transaction_types_all"
    __table_args__ = {"schema": "ont", "extend_existing": True}
    __table_properties__ = {"ui_x_pos": 1354.2816162109375, "ui_y_pos": -312.3231964111328, "colour": "#F2F3F5"}

    transaction_type_id: Mapped[str] = mapped_column('transaction_type_id', Integer, primary_key=True, info={"column_metadata": ColumnMetadata()})
    transaction_type_code: Mapped[str] = mapped_column('transaction_type_code', String, primary_key=False, info={"column_metadata": ColumnMetadata()})
    order_category_code: Mapped[str] = mapped_column('order_category_code', String, primary_key=False, info={"column_metadata": ColumnMetadata()})
    start_date_active: Mapped[str] = mapped_column('start_date_active', Date, primary_key=False, info={"column_metadata": ColumnMetadata()})
    end_date_active: Mapped[str] = mapped_column('end_date_active', Date, primary_key=False, info={"column_metadata": ColumnMetadata()})
    creation_date: Mapped[str] = mapped_column('creation_date', Date, primary_key=False, info={"column_metadata": ColumnMetadata()})
    created_by: Mapped[str] = mapped_column('created_by', Integer, primary_key=False, info={"column_metadata": ColumnMetadata()})
    last_update_date: Mapped[str] = mapped_column('last_update_date', Date, primary_key=False, info={"column_metadata": ColumnMetadata()})
    last_updated_by: Mapped[str] = mapped_column('last_updated_by', Integer, primary_key=False, info={"column_metadata": ColumnMetadata()})
    last_update_login: Mapped[str] = mapped_column('last_update_login', Integer, primary_key=False, info={"column_metadata": ColumnMetadata()})
    program_application_id: Mapped[str] = mapped_column('program_application_id', Integer, primary_key=False, info={"column_metadata": ColumnMetadata()})
    program_id: Mapped[str] = mapped_column('program_id', Integer, primary_key=False, info={"column_metadata": ColumnMetadata()})
    request_id: Mapped[str] = mapped_column('request_id', Integer, primary_key=False, info={"column_metadata": ColumnMetadata()})
    currency_code: Mapped[str] = mapped_column('currency_code', String, primary_key=False, info={"column_metadata": ColumnMetadata()})
    conversion_type_code: Mapped[str] = mapped_column('conversion_type_code', String, primary_key=False, info={"column_metadata": ColumnMetadata()})
    cust_trx_type_id: Mapped[str] = mapped_column('cust_trx_type_id', Integer, primary_key=False, info={"column_metadata": ColumnMetadata()})
    cost_of_goods_sold_account: Mapped[str] = mapped_column('cost_of_goods_sold_account', Integer, primary_key=False, info={"column_metadata": ColumnMetadata()})
    entry_credit_check_rule_id: Mapped[str] = mapped_column('entry_credit_check_rule_id', Integer, primary_key=False, info={"column_metadata": ColumnMetadata()})
    shipping_credit_check_rule_id: Mapped[str] = mapped_column('shipping_credit_check_rule_id', Integer, primary_key=False, info={"column_metadata": ColumnMetadata()})
    price_list_id: Mapped[str] = mapped_column('price_list_id', Integer, primary_key=False, info={"column_metadata": ColumnMetadata()})
    enforce_line_prices_flag: Mapped[str] = mapped_column('enforce_line_prices_flag', String, primary_key=False, info={"column_metadata": ColumnMetadata()})
    warehouse_id: Mapped[str] = mapped_column('warehouse_id', Integer, primary_key=False, info={"column_metadata": ColumnMetadata()})
    demand_class_code: Mapped[str] = mapped_column('demand_class_code', String, primary_key=False, info={"column_metadata": ColumnMetadata()})
    shipment_priority_code: Mapped[str] = mapped_column('shipment_priority_code', String, primary_key=False, info={"column_metadata": ColumnMetadata()})
    shipping_method_code: Mapped[str] = mapped_column('shipping_method_code', String, primary_key=False, info={"column_metadata": ColumnMetadata()})
    freight_terms_code: Mapped[str] = mapped_column('freight_terms_code', String, primary_key=False, info={"column_metadata": ColumnMetadata()})
    fob_point_code: Mapped[str] = mapped_column('fob_point_code', String, primary_key=False, info={"column_metadata": ColumnMetadata()})
    ship_source_type_code: Mapped[str] = mapped_column('ship_source_type_code', String, primary_key=False, info={"column_metadata": ColumnMetadata()})
    agreement_type_code: Mapped[str] = mapped_column('agreement_type_code', String, primary_key=False, info={"column_metadata": ColumnMetadata()})
    agreement_required_flag: Mapped[str] = mapped_column('agreement_required_flag', String, primary_key=False, info={"column_metadata": ColumnMetadata()})
    po_required_flag: Mapped[str] = mapped_column('po_required_flag', String, primary_key=False, info={"column_metadata": ColumnMetadata()})
    invoicing_rule_id: Mapped[str] = mapped_column('invoicing_rule_id', Integer, primary_key=False, info={"column_metadata": ColumnMetadata()})
    invoicing_credit_method_code: Mapped[str] = mapped_column('invoicing_credit_method_code', String, primary_key=False, info={"column_metadata": ColumnMetadata()})
    accounting_rule_id: Mapped[str] = mapped_column('accounting_rule_id', Integer, primary_key=False, info={"column_metadata": ColumnMetadata()})
    accounting_credit_method_code: Mapped[str] = mapped_column('accounting_credit_method_code', String, primary_key=False, info={"column_metadata": ColumnMetadata()})
    invoice_source_id: Mapped[str] = mapped_column('invoice_source_id', Integer, primary_key=False, info={"column_metadata": ColumnMetadata()})
    non_delivery_invoice_source_id: Mapped[str] = mapped_column('non_delivery_invoice_source_id', Integer, primary_key=False, info={"column_metadata": ColumnMetadata()})
    inspection_required_flag: Mapped[str] = mapped_column('inspection_required_flag', String, primary_key=False, info={"column_metadata": ColumnMetadata()})
    depot_repair_code: Mapped[str] = mapped_column('depot_repair_code', String, primary_key=False, info={"column_metadata": ColumnMetadata()})
    org_id: Mapped[str] = mapped_column('org_id', Integer, primary_key=False, info={"column_metadata": ColumnMetadata()})
    auto_scheduling_flag: Mapped[str] = mapped_column('auto_scheduling_flag', String, primary_key=False, info={"column_metadata": ColumnMetadata()})
    scheduling_level_code: Mapped[str] = mapped_column('scheduling_level_code', String, primary_key=False, info={"column_metadata": ColumnMetadata()})
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
    default_inbound_line_type_id: Mapped[str] = mapped_column('default_inbound_line_type_id', Integer, primary_key=False, info={"column_metadata": ColumnMetadata()})
    default_outbound_line_type_id: Mapped[str] = mapped_column('default_outbound_line_type_id', Integer, primary_key=False, info={"column_metadata": ColumnMetadata()})
    tax_calculation_event_code: Mapped[str] = mapped_column('tax_calculation_event_code', String, primary_key=False, info={"column_metadata": ColumnMetadata()})
    picking_credit_check_rule_id: Mapped[str] = mapped_column('picking_credit_check_rule_id', Integer, primary_key=False, info={"column_metadata": ColumnMetadata()})
    packing_credit_check_rule_id: Mapped[str] = mapped_column('packing_credit_check_rule_id', Integer, primary_key=False, info={"column_metadata": ColumnMetadata()})
    min_margin_percent: Mapped[str] = mapped_column('min_margin_percent', Integer, primary_key=False, info={"column_metadata": ColumnMetadata()})
    sales_document_type_code: Mapped[str] = mapped_column('sales_document_type_code', String, primary_key=False, info={"column_metadata": ColumnMetadata()})
    default_line_set_code: Mapped[str] = mapped_column('default_line_set_code', String, primary_key=False, info={"column_metadata": ColumnMetadata()})
    default_fulfillment_set: Mapped[str] = mapped_column('default_fulfillment_set', String, primary_key=False, info={"column_metadata": ColumnMetadata()})
    def_transaction_phase_code: Mapped[str] = mapped_column('def_transaction_phase_code', String, primary_key=False, info={"column_metadata": ColumnMetadata()})
    quote_num_as_ord_num_flag: Mapped[str] = mapped_column('quote_num_as_ord_num_flag', String, primary_key=False, info={"column_metadata": ColumnMetadata()})
    layout_template_id: Mapped[str] = mapped_column('layout_template_id', Integer, primary_key=False, info={"column_metadata": ColumnMetadata()})
    contract_template_id: Mapped[str] = mapped_column('contract_template_id', Integer, primary_key=False, info={"column_metadata": ColumnMetadata()})
    credit_card_rev_reauth_code: Mapped[str] = mapped_column('credit_card_rev_reauth_code', String, primary_key=False, info={"column_metadata": ColumnMetadata()})
    use_ame_approval: Mapped[str] = mapped_column('use_ame_approval', String, primary_key=False, info={"column_metadata": ColumnMetadata()})
    bill_only: Mapped[str] = mapped_column('bill_only', String, primary_key=False, info={"column_metadata": ColumnMetadata()})

        

    

    OeOrderHeadersAll_order_type_id: Mapped["OeOrderHeadersAll"] = relationship(back_populates="OeTransactionTypesAll_transaction_type_id", primaryjoin="OeOrderHeadersAll.order_type_id==OeTransactionTypesAll.transaction_type_id", foreign_keys="[OeTransactionTypesAll.transaction_type_id]", viewonly=True)



