from typing import TYPE_CHECKING

from sqlalchemy import Date, Float, Integer, String
from sqlalchemy.orm import Mapped, mapped_column, relationship

from efficieno.components.erd_objects import ERDBase, ColumnMetadata

if TYPE_CHECKING:
    from ..ar.ra_customer_trx_all import RaCustomerTrxAll


class RaCustTrxTypesAll(ERDBase):
    __data_object_type__ = "data_object"
    __tablename__ = "ra_cust_trx_types_all"
    __table_args__ = {"schema": "ar", "extend_existing": True}
    __table_properties__ = {"ui_x_pos": 2090.7808227539062, "ui_y_pos": 1041.747314453125, "colour": "#F2F3F5"}

    cust_trx_type_id: Mapped[str] = mapped_column('cust_trx_type_id', Integer, primary_key=True, info={"column_metadata": ColumnMetadata()})
    last_update_date: Mapped[str] = mapped_column('last_update_date', Date, primary_key=False, info={"column_metadata": ColumnMetadata()})
    last_updated_by: Mapped[str] = mapped_column('last_updated_by', Integer, primary_key=False, info={"column_metadata": ColumnMetadata()})
    creation_date: Mapped[str] = mapped_column('creation_date', Date, primary_key=False, info={"column_metadata": ColumnMetadata()})
    created_by: Mapped[str] = mapped_column('created_by', Integer, primary_key=False, info={"column_metadata": ColumnMetadata()})
    last_update_login: Mapped[str] = mapped_column('last_update_login', Integer, primary_key=False, info={"column_metadata": ColumnMetadata()})
    post_to_gl: Mapped[str] = mapped_column('post_to_gl', String, primary_key=False, info={"column_metadata": ColumnMetadata()})
    accounting_affect_flag: Mapped[str] = mapped_column('accounting_affect_flag', String, primary_key=False, info={"column_metadata": ColumnMetadata()})
    credit_memo_type_id: Mapped[str] = mapped_column('credit_memo_type_id', Integer, primary_key=False, info={"column_metadata": ColumnMetadata()})
    status: Mapped[str] = mapped_column('status', String, primary_key=False, info={"column_metadata": ColumnMetadata()})
    name: Mapped[str] = mapped_column('name', String, primary_key=False, info={"column_metadata": ColumnMetadata()})
    description: Mapped[str] = mapped_column('description', String, primary_key=False, info={"column_metadata": ColumnMetadata()})
    type: Mapped[str] = mapped_column('type', String, primary_key=False, info={"column_metadata": ColumnMetadata()})
    default_term: Mapped[str] = mapped_column('default_term', Integer, primary_key=False, info={"column_metadata": ColumnMetadata()})
    default_printing_option: Mapped[str] = mapped_column('default_printing_option', String, primary_key=False, info={"column_metadata": ColumnMetadata()})
    default_status: Mapped[str] = mapped_column('default_status', String, primary_key=False, info={"column_metadata": ColumnMetadata()})
    gl_id_rev: Mapped[str] = mapped_column('gl_id_rev', Integer, primary_key=False, info={"column_metadata": ColumnMetadata()})
    gl_id_freight: Mapped[str] = mapped_column('gl_id_freight', Integer, primary_key=False, info={"column_metadata": ColumnMetadata()})
    gl_id_rec: Mapped[str] = mapped_column('gl_id_rec', Integer, primary_key=False, info={"column_metadata": ColumnMetadata()})
    subsequent_trx_type_id: Mapped[str] = mapped_column('subsequent_trx_type_id', Integer, primary_key=False, info={"column_metadata": ColumnMetadata()})
    set_of_books_id: Mapped[str] = mapped_column('set_of_books_id', Integer, primary_key=False, info={"column_metadata": ColumnMetadata()})
    attribute_category: Mapped[str] = mapped_column('attribute_category', String, primary_key=False, info={"column_metadata": ColumnMetadata()})
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
    allow_freight_flag: Mapped[str] = mapped_column('allow_freight_flag', String, primary_key=False, info={"column_metadata": ColumnMetadata()})
    allow_overapplication_flag: Mapped[str] = mapped_column('allow_overapplication_flag', String, primary_key=False, info={"column_metadata": ColumnMetadata()})
    creation_sign: Mapped[str] = mapped_column('creation_sign', String, primary_key=False, info={"column_metadata": ColumnMetadata()})
    end_date: Mapped[str] = mapped_column('end_date', Date, primary_key=False, info={"column_metadata": ColumnMetadata()})
    gl_id_clearing: Mapped[str] = mapped_column('gl_id_clearing', Integer, primary_key=False, info={"column_metadata": ColumnMetadata()})
    gl_id_tax: Mapped[str] = mapped_column('gl_id_tax', Integer, primary_key=False, info={"column_metadata": ColumnMetadata()})
    gl_id_unbilled: Mapped[str] = mapped_column('gl_id_unbilled', Integer, primary_key=False, info={"column_metadata": ColumnMetadata()})
    gl_id_unearned: Mapped[str] = mapped_column('gl_id_unearned', Integer, primary_key=False, info={"column_metadata": ColumnMetadata()})
    start_date: Mapped[str] = mapped_column('start_date', Date, primary_key=False, info={"column_metadata": ColumnMetadata()})
    tax_calculation_flag: Mapped[str] = mapped_column('tax_calculation_flag', String, primary_key=False, info={"column_metadata": ColumnMetadata()})
    attribute11: Mapped[str] = mapped_column('attribute11', String, primary_key=False, info={"column_metadata": ColumnMetadata()})
    attribute12: Mapped[str] = mapped_column('attribute12', String, primary_key=False, info={"column_metadata": ColumnMetadata()})
    attribute13: Mapped[str] = mapped_column('attribute13', String, primary_key=False, info={"column_metadata": ColumnMetadata()})
    attribute14: Mapped[str] = mapped_column('attribute14', String, primary_key=False, info={"column_metadata": ColumnMetadata()})
    attribute15: Mapped[str] = mapped_column('attribute15', String, primary_key=False, info={"column_metadata": ColumnMetadata()})
    natural_application_only_flag: Mapped[str] = mapped_column('natural_application_only_flag', String, primary_key=False, info={"column_metadata": ColumnMetadata()})
    org_id: Mapped[str] = mapped_column('org_id', Integer, primary_key=False, info={"column_metadata": ColumnMetadata()})
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
    global_attribute_category: Mapped[str] = mapped_column('global_attribute_category', String, primary_key=False, info={"column_metadata": ColumnMetadata()})
    rule_set_id: Mapped[str] = mapped_column('rule_set_id', Integer, primary_key=False, info={"column_metadata": ColumnMetadata()})
    signed_flag: Mapped[str] = mapped_column('signed_flag', String, primary_key=False, info={"column_metadata": ColumnMetadata()})
    drawee_issued_flag: Mapped[str] = mapped_column('drawee_issued_flag', String, primary_key=False, info={"column_metadata": ColumnMetadata()})
    magnetic_format_code: Mapped[str] = mapped_column('magnetic_format_code', String, primary_key=False, info={"column_metadata": ColumnMetadata()})
    format_program_id: Mapped[str] = mapped_column('format_program_id', Integer, primary_key=False, info={"column_metadata": ColumnMetadata()})
    gl_id_unpaid_rec: Mapped[str] = mapped_column('gl_id_unpaid_rec', Integer, primary_key=False, info={"column_metadata": ColumnMetadata()})
    gl_id_remittance: Mapped[str] = mapped_column('gl_id_remittance', Integer, primary_key=False, info={"column_metadata": ColumnMetadata()})
    gl_id_factor: Mapped[str] = mapped_column('gl_id_factor', Integer, primary_key=False, info={"column_metadata": ColumnMetadata()})
    allocate_tax_freight: Mapped[str] = mapped_column('allocate_tax_freight', String, primary_key=False, info={"column_metadata": ColumnMetadata()})
    legal_entity_id: Mapped[str] = mapped_column('legal_entity_id', Integer, primary_key=False, info={"column_metadata": ColumnMetadata()})
    exclude_from_late_charges: Mapped[str] = mapped_column('exclude_from_late_charges', String, primary_key=False, info={"column_metadata": ColumnMetadata()})
    adj_post_to_gl: Mapped[str] = mapped_column('adj_post_to_gl', String, primary_key=False, info={"column_metadata": ColumnMetadata()})
    zd_edition_name: Mapped[str] = mapped_column('zd_edition_name', String, primary_key=False, info={"column_metadata": ColumnMetadata()})
    zd_sync: Mapped[str] = mapped_column('zd_sync', String, primary_key=False, info={"column_metadata": ColumnMetadata()})
    pa_organization_id: Mapped[str] = mapped_column('pa_organization_id', Integer, primary_key=False, info={"column_metadata": ColumnMetadata()})

        

    

    RaCustomerTrxAll_cust_trx_type_id: Mapped["RaCustomerTrxAll"] = relationship(back_populates="RaCustTrxTypesAll_cust_trx_type_id", primaryjoin="RaCustomerTrxAll.cust_trx_type_id==RaCustTrxTypesAll.cust_trx_type_id", foreign_keys="[RaCustTrxTypesAll.cust_trx_type_id]", viewonly=True)



