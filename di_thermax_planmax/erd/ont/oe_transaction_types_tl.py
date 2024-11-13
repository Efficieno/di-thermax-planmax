from typing import TYPE_CHECKING

from sqlalchemy import Date, Float, Integer, String
from sqlalchemy.orm import Mapped, mapped_column, relationship

from efficieno.components.erd_objects import ERDBase, ColumnMetadata

if TYPE_CHECKING:
    from ..ont.oe_order_headers_all import OeOrderHeadersAll


class OeTransactionTypesTl(ERDBase):
    __data_object_type__ = "data_object"
    __tablename__ = "oe_transaction_types_tl"
    __table_args__ = {"schema": "ont", "extend_existing": True}
    __table_properties__ = {"ui_x_pos": 1661.822265625, "ui_y_pos": -265.12799072265625, "colour": "#F2F3F5"}

    transaction_type_id: Mapped[str] = mapped_column('transaction_type_id', Integer, primary_key=True, info={"column_metadata": ColumnMetadata()})
    language: Mapped[str] = mapped_column('language', String, primary_key=False, info={"column_metadata": ColumnMetadata()})
    source_lang: Mapped[str] = mapped_column('source_lang', String, primary_key=False, info={"column_metadata": ColumnMetadata()})
    name: Mapped[str] = mapped_column('name', String, primary_key=False, info={"column_metadata": ColumnMetadata()})
    description: Mapped[str] = mapped_column('description', String, primary_key=False, info={"column_metadata": ColumnMetadata()})
    creation_date: Mapped[str] = mapped_column('creation_date', Date, primary_key=False, info={"column_metadata": ColumnMetadata()})
    created_by: Mapped[str] = mapped_column('created_by', Integer, primary_key=False, info={"column_metadata": ColumnMetadata()})
    last_update_date: Mapped[str] = mapped_column('last_update_date', Date, primary_key=False, info={"column_metadata": ColumnMetadata()})
    last_updated_by: Mapped[str] = mapped_column('last_updated_by', Integer, primary_key=False, info={"column_metadata": ColumnMetadata()})
    last_update_login: Mapped[str] = mapped_column('last_update_login', Integer, primary_key=False, info={"column_metadata": ColumnMetadata()})
    program_application_id: Mapped[str] = mapped_column('program_application_id', Integer, primary_key=False, info={"column_metadata": ColumnMetadata()})
    program_id: Mapped[str] = mapped_column('program_id', Integer, primary_key=False, info={"column_metadata": ColumnMetadata()})
    request_id: Mapped[str] = mapped_column('request_id', Integer, primary_key=False, info={"column_metadata": ColumnMetadata()})

        

    

    OeOrderHeadersAll_order_type_id: Mapped["OeOrderHeadersAll"] = relationship(back_populates="OeTransactionTypesTl_transaction_type_id", primaryjoin="OeOrderHeadersAll.order_type_id==OeTransactionTypesTl.transaction_type_id", foreign_keys="[OeTransactionTypesTl.transaction_type_id]", viewonly=True)



