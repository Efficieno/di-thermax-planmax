from typing import TYPE_CHECKING

from sqlalchemy import Date, Float, Integer, String
from sqlalchemy.orm import Mapped, mapped_column, relationship

from efficieno.components.erd_objects import ERDBase, ColumnMetadata

if TYPE_CHECKING:
    from ..ar.ra_customer_trx_all import RaCustomerTrxAll


class RaTermsTl(ERDBase):
    __data_object_type__ = "data_object"
    __tablename__ = "ra_terms_tl"
    __table_args__ = {"schema": "ar", "extend_existing": True}
    __table_properties__ = {"ui_x_pos": 2342.1632690429688, "ui_y_pos": 1143.4335327148438, "colour": "#F2F3F5"}

    term_id: Mapped[str] = mapped_column('term_id', Integer, primary_key=True, info={"column_metadata": ColumnMetadata()})
    description: Mapped[str] = mapped_column('description', String, primary_key=False, info={"column_metadata": ColumnMetadata()})
    name: Mapped[str] = mapped_column('name', String, primary_key=False, info={"column_metadata": ColumnMetadata()})
    language: Mapped[str] = mapped_column('language', String, primary_key=False, info={"column_metadata": ColumnMetadata()})
    source_lang: Mapped[str] = mapped_column('source_lang', String, primary_key=False, info={"column_metadata": ColumnMetadata()})
    last_update_date: Mapped[str] = mapped_column('last_update_date', Date, primary_key=False, info={"column_metadata": ColumnMetadata()})
    creation_date: Mapped[str] = mapped_column('creation_date', Date, primary_key=False, info={"column_metadata": ColumnMetadata()})
    created_by: Mapped[str] = mapped_column('created_by', Integer, primary_key=False, info={"column_metadata": ColumnMetadata()})
    last_updated_by: Mapped[str] = mapped_column('last_updated_by', Integer, primary_key=False, info={"column_metadata": ColumnMetadata()})
    last_update_login: Mapped[str] = mapped_column('last_update_login', Integer, primary_key=False, info={"column_metadata": ColumnMetadata()})
    zd_edition_name: Mapped[str] = mapped_column('zd_edition_name', String, primary_key=False, info={"column_metadata": ColumnMetadata()})
    zd_sync: Mapped[str] = mapped_column('zd_sync', String, primary_key=False, info={"column_metadata": ColumnMetadata()})

        

    

    RaCustomerTrxAll_term_id: Mapped["RaCustomerTrxAll"] = relationship(back_populates="RaTermsTl_term_id", primaryjoin="RaCustomerTrxAll.term_id==RaTermsTl.term_id", foreign_keys="[RaTermsTl.term_id]", viewonly=True)



