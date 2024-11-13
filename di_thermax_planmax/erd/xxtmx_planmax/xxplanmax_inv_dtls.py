from typing import TYPE_CHECKING

from sqlalchemy import Date, Float, Integer, String, Numeric, DateTime
from sqlalchemy.orm import Mapped, mapped_column, relationship

from efficieno.components.erd_objects import ERDBase, ColumnMetadata



class XxplanmaxInvDtls(ERDBase):
    __data_object_type__ = "data_object"
    __tablename__ = "xxplanmax_inv_dtls"
    __table_args__ = {"schema": "xxtmx_planmax", "extend_existing": True}
    __table_properties__ = {"ui_x_pos": -453.8673400878906, "ui_y_pos": 393.9957275390625, "colour": "#F2F3F5"}

    trx_number: Mapped[str] = mapped_column('trx_number', String, primary_key=True, info={"column_metadata": ColumnMetadata()})
    trx_date: Mapped[str] = mapped_column('trx_date', DateTime, primary_key=False, info={"column_metadata": ColumnMetadata()})
    invoice_currency_code: Mapped[str] = mapped_column('invoice_currency_code', String, primary_key=False, info={"column_metadata": ColumnMetadata()})
    complete_flag: Mapped[str] = mapped_column('complete_flag', String, primary_key=False, info={"column_metadata": ColumnMetadata()})
    batch_source_name: Mapped[str] = mapped_column('batch_source_name', String, primary_key=False, info={"column_metadata": ColumnMetadata()})
    trx_type_name: Mapped[str] = mapped_column('trx_type_name', String, primary_key=False, info={"column_metadata": ColumnMetadata()})
    trx_type_desc: Mapped[str] = mapped_column('trx_type_desc', String, primary_key=False, info={"column_metadata": ColumnMetadata()})
    invoice_type: Mapped[str] = mapped_column('invoice_type', String, primary_key=False, info={"column_metadata": ColumnMetadata()})
    gl_date: Mapped[str] = mapped_column('gl_date', DateTime, primary_key=False, info={"column_metadata": ColumnMetadata()})
    customer_trx_id: Mapped[str] = mapped_column('customer_trx_id', Numeric, primary_key=False, info={"column_metadata": ColumnMetadata()})
    invoice_amt: Mapped[str] = mapped_column('invoice_amt', Numeric, primary_key=False, info={"column_metadata": ColumnMetadata()})
    bill_to_site_use_id: Mapped[str] = mapped_column('bill_to_site_use_id', Numeric, primary_key=False, info={"column_metadata": ColumnMetadata()})




