from typing import TYPE_CHECKING

from sqlalchemy import Date, Float, Integer, String, Numeric, DateTime
from sqlalchemy.orm import Mapped, mapped_column, relationship

from efficieno.components.erd_objects import ERDBase, ColumnMetadata

if TYPE_CHECKING:
    from ..xxtmx_planmax.xxplanmax_header_dtls import XxplanmaxHeaderDtls


class XxplanmaxCustDtls(ERDBase):
    __data_object_type__ = "data_object"
    __tablename__ = "xxplanmax_cust_dtls"
    __table_args__ = {"schema": "xxtmx_planmax", "extend_existing": True}
    __table_properties__ = {"ui_x_pos": -450.8699951171875, "ui_y_pos": 270.399658203125, "colour": "#F2F3F5"}

    account_number: Mapped[str] = mapped_column('account_number', String, primary_key=True, info={"column_metadata": ColumnMetadata()})
    cust_account_id: Mapped[str] = mapped_column('cust_account_id', Numeric, primary_key=False, info={"column_metadata": ColumnMetadata()})
    party_id: Mapped[str] = mapped_column('party_id', Numeric, primary_key=False, info={"column_metadata": ColumnMetadata()})
    party_number: Mapped[str] = mapped_column('party_number', String, primary_key=False, info={"column_metadata": ColumnMetadata()})
    party_name: Mapped[str] = mapped_column('party_name', String, primary_key=False, info={"column_metadata": ColumnMetadata()})
    creation_date: Mapped[str] = mapped_column('creation_date', DateTime, primary_key=False, info={"column_metadata": ColumnMetadata()})
    site_use_code: Mapped[str] = mapped_column('site_use_code', String, primary_key=False, info={"column_metadata": ColumnMetadata()})
    party_site_number: Mapped[str] = mapped_column('party_site_number', String, primary_key=False, info={"column_metadata": ColumnMetadata()})
    cust_acct_site_id: Mapped[str] = mapped_column('cust_acct_site_id', Numeric, primary_key=False, info={"column_metadata": ColumnMetadata()})
    site_use_id: Mapped[str] = mapped_column('site_use_id', Numeric, primary_key=False, info={"column_metadata": ColumnMetadata()})
    site_use_status: Mapped[str] = mapped_column('site_use_status', String, primary_key=False, info={"column_metadata": ColumnMetadata()})
    location_id: Mapped[str] = mapped_column('location_id', Numeric, primary_key=False, info={"column_metadata": ColumnMetadata()})
    address1: Mapped[str] = mapped_column('address1', String, primary_key=False, info={"column_metadata": ColumnMetadata()})
    address2: Mapped[str] = mapped_column('address2', String, primary_key=False, info={"column_metadata": ColumnMetadata()})
    address3: Mapped[str] = mapped_column('address3', String, primary_key=False, info={"column_metadata": ColumnMetadata()})
    address4: Mapped[str] = mapped_column('address4', String, primary_key=False, info={"column_metadata": ColumnMetadata()})
    city: Mapped[str] = mapped_column('city', String, primary_key=False, info={"column_metadata": ColumnMetadata()})
    postal_code: Mapped[str] = mapped_column('postal_code', String, primary_key=False, info={"column_metadata": ColumnMetadata()})
    state: Mapped[str] = mapped_column('state', String, primary_key=False, info={"column_metadata": ColumnMetadata()})
    province: Mapped[str] = mapped_column('province', String, primary_key=False, info={"column_metadata": ColumnMetadata()})
    country: Mapped[str] = mapped_column('country', String, primary_key=False, info={"column_metadata": ColumnMetadata()})

        

    

    XxplanmaxHeaderDtls_ship_site_use_id: Mapped["XxplanmaxHeaderDtls"] = relationship(back_populates="XxplanmaxCustDtls_site_use_id", primaryjoin="XxplanmaxHeaderDtls.ship_site_use_id==XxplanmaxCustDtls.site_use_id", foreign_keys="[XxplanmaxCustDtls.site_use_id]", viewonly=True)



