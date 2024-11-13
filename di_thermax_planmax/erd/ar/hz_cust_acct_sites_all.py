from typing import TYPE_CHECKING

from sqlalchemy import Date, Float, Integer, String
from sqlalchemy.orm import Mapped, mapped_column, relationship

from efficieno.components.erd_objects import ERDBase, ColumnMetadata

if TYPE_CHECKING:
    from ..ar.hz_cust_site_uses_all import HzCustSiteUsesAll
    from ..ar.hz_party_sites import HzPartySites


class HzCustAcctSitesAll(ERDBase):
    __data_object_type__ = "data_object"
    __tablename__ = "hz_cust_acct_sites_all"
    __table_args__ = {"schema": "ar", "extend_existing": True}
    __table_properties__ = {"ui_x_pos": 1721.6031799316406, "ui_y_pos": 1597.0497436523438, "colour": "#F2F3F5"}

    cust_acct_site_id: Mapped[str] = mapped_column('cust_acct_site_id', Integer, primary_key=True, info={"column_metadata": ColumnMetadata()})
    cust_account_id: Mapped[str] = mapped_column('cust_account_id', Integer, primary_key=False, info={"column_metadata": ColumnMetadata()})
    party_site_id: Mapped[str] = mapped_column('party_site_id', Integer, primary_key=False, info={"column_metadata": ColumnMetadata()})
    last_update_date: Mapped[str] = mapped_column('last_update_date', Date, primary_key=False, info={"column_metadata": ColumnMetadata()})
    last_updated_by: Mapped[str] = mapped_column('last_updated_by', Integer, primary_key=False, info={"column_metadata": ColumnMetadata()})
    creation_date: Mapped[str] = mapped_column('creation_date', Date, primary_key=False, info={"column_metadata": ColumnMetadata()})
    created_by: Mapped[str] = mapped_column('created_by', Integer, primary_key=False, info={"column_metadata": ColumnMetadata()})
    last_update_login: Mapped[str] = mapped_column('last_update_login', Integer, primary_key=False, info={"column_metadata": ColumnMetadata()})
    request_id: Mapped[str] = mapped_column('request_id', Integer, primary_key=False, info={"column_metadata": ColumnMetadata()})
    program_application_id: Mapped[str] = mapped_column('program_application_id', Integer, primary_key=False, info={"column_metadata": ColumnMetadata()})
    program_id: Mapped[str] = mapped_column('program_id', Integer, primary_key=False, info={"column_metadata": ColumnMetadata()})
    program_update_date: Mapped[str] = mapped_column('program_update_date', Date, primary_key=False, info={"column_metadata": ColumnMetadata()})
    wh_update_date: Mapped[str] = mapped_column('wh_update_date', Date, primary_key=False, info={"column_metadata": ColumnMetadata()})
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
    attribute11: Mapped[str] = mapped_column('attribute11', String, primary_key=False, info={"column_metadata": ColumnMetadata()})
    attribute12: Mapped[str] = mapped_column('attribute12', String, primary_key=False, info={"column_metadata": ColumnMetadata()})
    attribute13: Mapped[str] = mapped_column('attribute13', String, primary_key=False, info={"column_metadata": ColumnMetadata()})
    attribute14: Mapped[str] = mapped_column('attribute14', String, primary_key=False, info={"column_metadata": ColumnMetadata()})
    attribute15: Mapped[str] = mapped_column('attribute15', String, primary_key=False, info={"column_metadata": ColumnMetadata()})
    attribute16: Mapped[str] = mapped_column('attribute16', String, primary_key=False, info={"column_metadata": ColumnMetadata()})
    attribute17: Mapped[str] = mapped_column('attribute17', String, primary_key=False, info={"column_metadata": ColumnMetadata()})
    attribute18: Mapped[str] = mapped_column('attribute18', String, primary_key=False, info={"column_metadata": ColumnMetadata()})
    attribute19: Mapped[str] = mapped_column('attribute19', String, primary_key=False, info={"column_metadata": ColumnMetadata()})
    attribute20: Mapped[str] = mapped_column('attribute20', String, primary_key=False, info={"column_metadata": ColumnMetadata()})
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
    orig_system_reference: Mapped[str] = mapped_column('orig_system_reference', String, primary_key=False, info={"column_metadata": ColumnMetadata()})
    status: Mapped[str] = mapped_column('status', String, primary_key=False, info={"column_metadata": ColumnMetadata()})
    org_id: Mapped[str] = mapped_column('org_id', Integer, primary_key=False, info={"column_metadata": ColumnMetadata()})
    bill_to_flag: Mapped[str] = mapped_column('bill_to_flag', String, primary_key=False, info={"column_metadata": ColumnMetadata()})
    market_flag: Mapped[str] = mapped_column('market_flag', String, primary_key=False, info={"column_metadata": ColumnMetadata()})
    ship_to_flag: Mapped[str] = mapped_column('ship_to_flag', String, primary_key=False, info={"column_metadata": ColumnMetadata()})
    customer_category_code: Mapped[str] = mapped_column('customer_category_code', String, primary_key=False, info={"column_metadata": ColumnMetadata()})
    language: Mapped[str] = mapped_column('language', String, primary_key=False, info={"column_metadata": ColumnMetadata()})
    key_account_flag: Mapped[str] = mapped_column('key_account_flag', String, primary_key=False, info={"column_metadata": ColumnMetadata()})
    tp_header_id: Mapped[str] = mapped_column('tp_header_id', Integer, primary_key=False, info={"column_metadata": ColumnMetadata()})
    ece_tp_location_code: Mapped[str] = mapped_column('ece_tp_location_code', String, primary_key=False, info={"column_metadata": ColumnMetadata()})
    service_territory_id: Mapped[str] = mapped_column('service_territory_id', Integer, primary_key=False, info={"column_metadata": ColumnMetadata()})
    primary_specialist_id: Mapped[str] = mapped_column('primary_specialist_id', Integer, primary_key=False, info={"column_metadata": ColumnMetadata()})
    secondary_specialist_id: Mapped[str] = mapped_column('secondary_specialist_id', Integer, primary_key=False, info={"column_metadata": ColumnMetadata()})
    territory_id: Mapped[str] = mapped_column('territory_id', Integer, primary_key=False, info={"column_metadata": ColumnMetadata()})
    address_text: Mapped[str] = mapped_column('address_text', String, primary_key=False, info={"column_metadata": ColumnMetadata()})
    territory: Mapped[str] = mapped_column('territory', String, primary_key=False, info={"column_metadata": ColumnMetadata()})
    translated_customer_name: Mapped[str] = mapped_column('translated_customer_name', String, primary_key=False, info={"column_metadata": ColumnMetadata()})
    object_version_number: Mapped[str] = mapped_column('object_version_number', Integer, primary_key=False, info={"column_metadata": ColumnMetadata()})
    created_by_module: Mapped[str] = mapped_column('created_by_module', String, primary_key=False, info={"column_metadata": ColumnMetadata()})
    application_id: Mapped[str] = mapped_column('application_id', Integer, primary_key=False, info={"column_metadata": ColumnMetadata()})

        

    

    HzCustSiteUsesAll_cust_acct_site_id: Mapped["HzCustSiteUsesAll"] = relationship(back_populates="HzCustAcctSitesAll_cust_acct_site_id", primaryjoin="HzCustSiteUsesAll.cust_acct_site_id==HzCustAcctSitesAll.cust_acct_site_id", foreign_keys="[HzCustSiteUsesAll.cust_acct_site_id]", viewonly=True)
        

    

    HzPartySites_party_site_id: Mapped["HzPartySites"] = relationship(back_populates="HzCustAcctSitesAll_party_site_id", primaryjoin="HzPartySites.party_site_id==HzCustAcctSitesAll.party_site_id", foreign_keys="[HzCustAcctSitesAll.party_site_id]", viewonly=True)



